import click

from os import getcwd
from os.path import abspath, join

from clar_cloc.count import process_directory


@click.command()
@click.option('--exclude-dirs', default="", help='Comma-separated list of directories to exclude.')
@click.option('--markdown', help='Markdown file to export the scope. (relative)')
@click.option('--include-breakdowns', is_flag=True, help='Include line breakdowns in the markdown export.')
def main(exclude_dirs: str, markdown: str, include_breakdowns: bool) -> None:
    cwd: str = getcwd()
    process_directory(
        cwd,
        [abspath(join(cwd, d.strip())) for d in exclude_dirs.split(',')],
        abspath(join(cwd, markdown)) if markdown else None,
        include_breakdowns
    )

if __name__ == "__main__":
    main()
