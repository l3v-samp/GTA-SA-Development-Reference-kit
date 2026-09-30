# GTA SA Development Reference kit

Actual source references and modular runtime starters for GTA SA development. Start with [modules](modules/README.md) and [source preparation](modules/PREPARE_REFERENCES.md).

| Folder | Contents |
|---|---|
| [modules/pawn/samp](modules/pawn/samp) | Pawn for SA-MP 0.3.7/open.mp: ten upstream gamemode/filterscript repositories, includes, dependencies and function/feature indexes |
| [modules/lua/moonloader](modules/lua/moonloader) | MoonLoader Lua client modules |
| [modules/lua/mta](modules/lua/mta) | MTA Lua client/server resource modules |
| [modules/cpp/asi](modules/cpp/asi) | Native x86 C++ ASI modules |
| [modules/assets/blender](modules/assets/blender) | Blender asset tooling |

Prepare readable source trees from the checkout root with Python 3.9+:

```sh
python3 modules/prepare_references.py --all --starters
```

Use `--feature miner`, `--feature speedometer`, `--feature needs` or `--feature inventory` for focused preparation. Read [FEATURE_GUIDE.md](modules/pawn/samp/FEATURE_GUIDE.md) and associated includes, lifecycle and persistence code before adapting a feature. `scripts/fetch_reference.py` remains an optional utility for fetching additional upstream references.

Only canonical runtime folders contain source ZIPs. Archives preserve upstream paths, available includes, manifests and license files. Player data, secrets, binaries and game/model/audio assets are excluded. Three dependency declarations remain unresolved; no game build or runtime compatibility is certified. DL examples require porting to the selected 0.3.7/open.mp target.

Keep new work under `projects/<runtime>/<project>/`, document compiler/tool versions and validate on the intended runtime. GitHub stores source; it does not run GTA SA, Blender or Codex. Preserve upstream licenses and attribution.
