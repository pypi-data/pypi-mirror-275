from os import walk
from os.path import join, relpath

from tabulate import tabulate

from typing import List, Tuple, Optional

# Types:
Total = Tuple[int, int, int] # source, blank, comment
Totals = Tuple[int, int, int, int]  # source, blank, comment, count
Results = List[List] # relative path, source, blank, comment
ResultTables = Tuple[str, str]

# Constants:
#  -> Clarity:
BLANK: str = ""
COMMENT: str = ";;"
FILE_EXTENSION: str = ".clar"

#  -> Output:
TABLE_HEADERS: List[str] = ["File", "Source", "Blank", "Comment"]
TABLE_FORMAT: str = "rounded_grid"
MD_TABLE_FORMAT: str = "github"

# -> Errors:
ERROR_DIRECTORY_NOT_FOUND: str = "Directory not found"
ERROR_FILE_NOT_FOUND: str = "File not found"
ERROR_READING_DIRECTORY: str = "An error occurred while reading directory"
ERROR_READING_FILE: str = "An error occurred while reading file"
ERROR_WRITING_FILE: str = "An error occurred while writing to file"
ERROR_NO_FILES_FOUND: str = f"No {FILE_EXTENSION} files found"


def error(message: str, var: Optional[str] = None) -> None:
    """
        Raise an exception with a formatted error message.
    """
    raise Exception(f"ERROR: {message}{f': {var}' if var else ''}.")

def _count_lines(path: str) -> Total:
    """
        Count the number of source, blank, and comment lines in a file.
    """
    source, blank, comment = tuple(0 for _ in range(3))

    def _count_line(line: str) -> None:
        """
            Clojure function to identify the line type and increment the corresponding counter.
        """
        nonlocal source, blank, comment
        if line == BLANK: blank += 1
        elif line.startswith(COMMENT): comment += 1
        else: source += 1

    for line in open(path, "r"): _count_line(line.strip())

    return source, blank, comment

def count_lines(path: str) -> Total:
    """
        Wrapper function to return the file's data or raise an appropriate error.
    """
    try: return _count_lines(path)
    
    except FileNotFoundError: error(ERROR_FILE_NOT_FOUND, path)
    except IOError: error(ERROR_READING_FILE, path)

def generate_tables(results: Results, totals: Totals, format: str) -> ResultTables:
    """
        Generate the tables for the console output.
    """
    file_results: str = tabulate(results, headers=TABLE_HEADERS, tablefmt=format)
    totals_row = [["Total", totals[0], totals[1], totals[2]]]
    totals_results: str = tabulate(totals_row, headers=TABLE_HEADERS, tablefmt=format)
    
    return file_results, totals_results

def log(results: Results, totals: Totals) -> None:
    """
        Function to output the directory's metrics, or raise an error if no files were found.
    """
    
    if not results: error(ERROR_NO_FILES_FOUND)
    
    file_results, totals_results = generate_tables(results, totals, TABLE_FORMAT)
    
    # Log to console
    print(file_results, totals_results, f"Total files processed: {totals[3]}", sep="\n\n")
    
def log_scope(files: List[str], tables: ResultTables, markdown: str, include_breakdowns: bool) -> None:
    """
        Log the scope of the project to a markdown file.
    """
    
    # Log to markdown file
    try:
        md = open(markdown, "w")
        md.write(f"clar-cloc Report\n\n")
        if include_breakdowns:
            md.write(f"Files\n\n{tables[0]}\n\n")
            md.write(f"Totals\n\n{tables[1]}\n\n")
        else:
            plain_table: str = tabulate([files], [TABLE_HEADERS[0]], tablefmt=MD_TABLE_FORMAT)
            md.write(f"Files\n\n{plain_table}\n\n")
            
        md.write(f"Total files processed: {len(files)}\n")
        
    except IOError: error(ERROR_WRITING_FILE, markdown)
    
def process_directory(path: str, exclude: List[str], markdown: str, include_breakdowns: bool) -> None:
    """
        Process the directory and its subdirectories, counting the lines of each file.
    """
    
    totals: Totals = (0, 0, 0, 0)
    results: Results = []
    _files: List[str] = []

    try:
        for root, dirs, files in walk(path):
            # Skip directories that are in the exclude list
            dirs[:] = [d for d in dirs if join(root, d) not in exclude]

            for file in files:
                if not file.endswith(FILE_EXTENSION): continue

                abs_path = join(root, file)
                relative = relpath(abs_path, path)
                counts = count_lines(abs_path)
                
                totals = (
                    totals[0] + counts[0],
                    totals[1] + counts[1],
                    totals[2] + counts[2],
                    totals[3] + 1
                )
                
                results.append([relative, *counts])
                _files.append(relative)
                
        log(results, totals)
        
        if not markdown: return None
        
        log_scope(
            _files,
            generate_tables(results, totals, MD_TABLE_FORMAT),
            markdown,
            include_breakdowns
        )
        
    except FileNotFoundError: error(ERROR_DIRECTORY_NOT_FOUND, path)
    except IOError: error(ERROR_READING_DIRECTORY, path)
