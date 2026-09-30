# Development modules

Organized first by language/tooling, then by runtime:

| Folder | Contents |
|---|---|
| [pawn/samp](pawn/samp) | SA-MP 0.3.7 / open.mp Pawn starter, gamemode and filterscript source archives, includes/dependencies and feature indexes |
| [lua/moonloader](lua/moonloader) | GTA SA client Lua modules |
| [lua/mta](lua/mta) | MTA client/server Lua resource modules |
| [cpp/asi](cpp/asi) | Native C++ ASI modules |
| [assets/blender](assets/blender) | Blender Python asset tooling |

SA-MP/open.mp are runtimes and Pawn is the language. The Pawn starter contains separate samp037/openmp gamemode and filterscript entrypoints. Bundled gamemode sources include DL-only code labeled as porting references.

Shared routing tools live here: REFERENCE_CATALOG.json, prepare_references.py and PREPARE_REFERENCES.md. Run from the checkout root:

```sh
python3 modules/prepare_references.py --all --starters
```

The command uses the folders above and prepares readable `.references` source trees. Sources remain ZIP snapshots in GitHub, preserving upstream paths, available includes and license files. Runtime starters contain actual Pawn, Lua, C++ and Blender source. Read pawn/samp/FEATURE_GUIDE.md before implementing a requested system. Three dependency declarations remain unresolved and no running-game build has been verified.

Older top-level archives and indexes are retained for compatibility with previous checkout links; the folders above and current catalog are canonical. New source packs must be added to the appropriate runtime folder.
