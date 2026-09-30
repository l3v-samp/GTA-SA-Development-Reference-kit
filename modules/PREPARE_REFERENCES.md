# Prepare readable source folders

Run from the repository checkout with Python 3.9+:

```sh
python3 modules/prepare_references.py --list
python3 modules/prepare_references.py --all --starters
```

The command performs offline checksum-verified extraction. It does not download, compile or execute gamemode code. It places five gamemode trees in `.references/pawn/gamemodes/OWNER--REPO`, four standalone filterscript repositories in `.references/pawn/filterscripts/OWNER--REPO`, and one mixed collection in `.references/pawn/collections/OWNER--REPO`. Each tree retains its original gamemodes, filterscripts, include directories, manifests and available schema/docs/license files. Dependencies stay separate in `.references/pawn/dependencies`; versions must not be flattened into a single include directory. Starters are separated under `.references/starters/{pawn,moonloader,mta,asi,gta-assets}`.

Prepare only relevant examples:

```sh
python3 modules/prepare_references.py --feature miner
python3 modules/prepare_references.py --feature speedometer
python3 modules/prepare_references.py --feature needs
python3 modules/prepare_references.py --feature inventory
python3 modules/prepare_references.py --feature filterscripts
```

Use `--repository OWNER/REPO` repeatedly for explicit choices, or `--destination /path/to/references` for an alternate location. Existing modified files are never overwritten. Identical files may be extracted again. Keep generated reference folders outside project source changes.

`REFERENCE_CATALOG.json` records categories, compatibility warnings, feature routing and SHA-256 archive checksums. `pawn/samp/FEATURE_GUIDE.md` points to actual feature files; `pawn/samp/REFERENCE_LOCK.json` records upstream commits. Read `pawn/samp/DEPENDENCY_REPORT.md` before any build. Complete source snapshots do not imply complete runnable servers: binaries, models, audio, secrets/player data and database row dumps are intentionally absent. DL gamemodes need porting. The miner selection includes one identified mining implementation plus another gamemode's job architecture, not two verified mining jobs.
