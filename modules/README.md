# Runtime modules and reference sources

This is the canonical module entry point. Source archives preserve the original repository paths, bundled includes, manifests, documentation and licenses. Read FEATURE_GUIDE.md before implementing requested systems.

| Runtime | Modular scaffold | Boundaries |
|---|---|---|
| Pawn SA-MP 0.3.7 / open.mp | pawn-modular-starter.zip | Separate entrypoints, core config, feature modules, one callback owner |
| MoonLoader Lua | moonloader-modular-starter.zip | Bootstrap, config, features, MoonLoader API adapters |
| MTA Lua | mta-modular-starter.zip | Separate client/server core, features and lifecycle |
| ASI C++ | asi-modular-starter.zip | Entry point, core, headers, x86 CMake target |
| GTA assets / Blender | gta-assets-modular-starter.zip | Config, geometry, materials, entrypoint |

Extract the selected scaffold into your project; its README describes deployment. Keep runtime APIs separate. These scaffolds have not been compiled or tested in a running game.

## Pawn references

Ten source snapshots cover roleplay, survival, open.mp and standalone filterscripts. REFERENCE_LOCK.json records upstream repositories, exact commits and dependencies. FEATURE_INDEX.json maps feature keywords to original source paths and lines. INCLUDE_AUDIT.json records include candidates; it is not a compiler check.

Extract selected source archives into a working reference directory and extract pawn-reference-dependencies.zip alongside them. Use their original pawn.json and matching includes; never flatten conflicting versions into one include directory. Shared standard libraries are also available in ../pawn-libraries-source.zip.

SOURCE archives exclude binaries, custom model/audio assets, player data, secrets and database row dumps; pure schema files remain. They are reference snapshots, not ready-to-run complete servers. Wild-West-Roleplay, SP-RP and AdvancedRP contain 0.3.DL code: reuse algorithms only after porting DL APIs/assets to the selected 0.3.7 or open.mp target. PatrickGTR/gta-open is the open.mp gamemode reference; inspect its pinned manifest before use.

DEPENDENCY_REPORT.md explicitly lists four unresolved declarations, including missing crashdetect tags, a malformed logger name and a commit-style YSI spec. Do not assume dependency closure or silently replace versions. Preserve upstream licenses and attribution; unlicensed code requires permission before redistribution as your own implementation.
