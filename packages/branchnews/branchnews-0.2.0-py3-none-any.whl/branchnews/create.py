import pathlib
import subprocess

import click

from .util import get_frag_dir_and_config, percent_encode


TEMPLATE = """\
# Please replace this comment with a release note.
# - Your note may span multiple lines.
# - You do NOT need to put a bullet symbol at the start.
"""

@click.command(name='create')
def main():
    """
    Create a news fragment.

    Enter an issue number, or let the filename be based on your GitHub username and
    the current branch name.
    """
    fragments_directory, config = get_frag_dir_and_config()

    filename_parts = []

    issue_num = input("Issue number (leave blank to use branch name instead): ")

    if issue_num:
        filename_parts.append(issue_num)
    else:
        username = input("GitHub username: ")
        branch = subprocess.check_output(["git", "branch", "--show-current"]).decode().strip()

        if branch in ['main', 'master']:
            print(f'\n*** Branch name "{branch}" does not sound like a topic branch! ***')
            click.confirm(f'Are you sure you want to proceed?', abort=True)

        print("Branch name is", branch)
        pct_enc_branch = percent_encode(branch)
        filename_parts.extend([username, pct_enc_branch, 'branchnews'])

    news_types = [(k, d['name']) for k, d in config.types.items()]
    print('What type of news is it?')
    for i, t in enumerate(news_types):
        print(f'({i}): {t[1]}')
    type_index = input("Type: ")
    try:
        i = int(type_index)
        news_type = news_types[i][0]
    except (ValueError, KeyError):
        raise click.UsageError('Invalid choice!')

    filename_parts.append(news_type)
    filename_parts.append('txt')

    filename = '.'.join(filename_parts)
    filepath = fragments_directory / filename
    if not fragments_directory.exists():
        fragments_directory.mkdir(parents=True)
    with open(filepath, "w") as f:
        f.write(TEMPLATE)

    try:
        cwd = pathlib.Path('.').absolute()
        home = fragments_directory.relative_to(cwd)
    except ValueError:
        home = fragments_directory

    print()
    print(f"Created file:\n  {filename}")
    print(f"in directory:\n  {home}")
    print()
    print("Please edit the file to provide a release note.")
    print("  - Your note may span multiple lines.")
    print("  - You do NOT need to put a bullet symbol at the start.")
    print()


if __name__ == '__main__':
    main()
