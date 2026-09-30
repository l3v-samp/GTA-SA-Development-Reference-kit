#!/usr/bin/env python3
"""Prepare bundled reference sources without downloading or executing upstream code."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile


def extract(archive, destination, digest):
    if hashlib.sha256(archive.read_bytes()).hexdigest() != digest:
        raise ValueError(f"Archive checksum mismatch: {archive.name}")
    root = destination.resolve()
    with zipfile.ZipFile(archive) as source:
        plans = []
        for item in source.infolist():
            path = PurePosixPath(item.filename)
            if path.is_absolute() or '..' in path.parts or '\\' in item.filename:
                raise ValueError(f"Unsafe archive path: {item.filename}")
            if stat.S_ISLNK(item.external_attr >> 16):
                raise ValueError(f"Archive symlink: {item.filename}")
            parts = path.parts[2:] if len(path.parts) > 2 and path.parts[0] == 'sources' else path.parts
            target = root.joinpath(*parts)
            if not target.resolve().is_relative_to(root):
                raise ValueError(f"Path escapes destination: {item.filename}")
            if item.is_dir():
                continue
            data = source.read(item)
            if target.exists() and (not target.is_file() or target.read_bytes() != data):
                raise ValueError(f"Refusing to overwrite modified file: {target}")
            plans.append((target, data))
        for target, data in plans:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    return len(plans)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--all', action='store_true', help='Prepare all Pawn snapshots and dependencies')
    parser.add_argument('--repository', action='append', default=[], help='Exact owner/repository from catalog')
    parser.add_argument('--feature', choices=['miner', 'speedometer', 'needs', 'inventory', 'filterscripts'])
    parser.add_argument('--starters', action='store_true', help='Prepare modular runtime scaffolds')
    parser.add_argument('--destination', type=Path, default=Path('.references'))
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    catalog = json.loads((base / 'REFERENCE_CATALOG.json').read_text())
    if args.list:
        for repo, entry in catalog['repositories'].items():
            print(f"{repo}: {entry['kind']}; {entry['compatibility']}")
        return
    selected = set(args.repository)
    if args.all:
        selected.update(catalog['repositories'])
    if args.feature:
        selected.update(catalog['features'][args.feature])
    unknown = selected - catalog['repositories'].keys()
    if unknown:
        parser.error('Unknown repositories: ' + ', '.join(sorted(unknown)))
    if not selected and not args.starters:
        parser.error('Choose --all, --repository, --feature or --starters')
    work = []
    for repo in sorted(selected):
        entry = catalog['repositories'][repo]
        work.append((entry['archive'], args.destination / 'pawn' / entry['kind'] / repo.replace('/', '--')))
    if selected:
        work.append(('pawn/samp/pawn-reference-dependencies.zip', args.destination / 'pawn'))
    if args.starters:
        for runtime, archive in catalog['starters'].items():
            work.append((archive, args.destination / 'starters' / runtime))
    # Fail before writing if any selected archive is absent or has been changed.
    for name, destination in work:
        path = base / name
        if hashlib.sha256(path.read_bytes()).hexdigest() != catalog['sha256'][name]:
            raise ValueError(f'Archive checksum mismatch: {name}')
    for name, destination in work:
        count = extract(base / name, destination, catalog['sha256'][name])
        print(f'{name}: {count} files -> {destination}')
    print('Reference extraction complete. See pawn/samp/DEPENDENCY_REPORT.md for unresolved packages; builds are not verified.')


if __name__ == '__main__':
    main()
