#!/usr/bin/env python3
"""Fetch one public reference. Requires Python 3 and Git.
Usage: python3 scripts/fetch_reference.py THE-FYP/SAMP.Lua
Downloads source only; does not build, install, execute or update it.
"""
import argparse
import pathlib
import re
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repository', help='GitHub owner/repository')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*', args.repository):
        parser.error('Expected owner/repository, not a URL or local path')
    root = pathlib.Path(__file__).resolve().parent.parent
    owner, repo = args.repository.split('/')
    destination = root / 'references-cache' / owner / repo
    if destination.exists():
        parser.error('Destination exists; inspect it manually. No overwrite or automatic update.')
    destination.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'clone', '--depth', '1', '--single-branch',
                    '--', 'https://github.com/' + args.repository + '.git',
                    str(destination)], check=True)
    commit = subprocess.check_output(['git', '-C', str(destination), 'rev-parse', 'HEAD'], text=True).strip()
    print('Saved:', destination)
    print('Reference commit:', commit)
    print('Review README and LICENSE before using. Submodules and LFS assets are not provisioned.')


if __name__ == '__main__':
    main()
