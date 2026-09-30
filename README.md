# GTA SA Development Reference kit

Small cloud-first reference hub for Pawn, SA-MP/open.mp, MoonLoader, ASI C++, MTA Lua, Blender, INU Tools, Ariane and GTA formats.

## Storage strategy
Keep only this hub and your project source in GitHub. Fetch individual upstream repositories in the cloud when a task needs them. Never commit downloaded references, game files, build caches or credentials. This repository does not install software or launch a paid cloud machine.

## Reference catalog
These are upstream links collected for research, not vendored dependencies. Check availability, README, license, supported versions and actual source before use. Some are historical or community-maintained. Inclusion does not certify compatibility or current maintenance.

| Area | Sources | Consult for |
|---|---|---|
| Pawn | [compiler](https://github.com/pawn-lang/compiler), [YSI](https://github.com/pawn-lang/YSI-Includes), [omp-stdlib](https://github.com/openmultiplayer/omp-stdlib), [sscanf](https://github.com/Y-Less/sscanf) | Compiler, includes, native signatures, parsing |
| SA-MP/open.mp | [open.mp](https://github.com/openmultiplayer/open.mp), [plugin SDK archive](https://github.com/samp-forks/samp-plugin-sdk), [sampgdk](https://github.com/samp-forks/sampgdk), [additional SDK](https://github.com/guil2k7/samp-plugin-sdk) | Server behavior and legacy AMX/plugin interfaces |
| MoonLoader | [SAMP.Lua](https://github.com/THE-FYP/SAMP.Lua), [community Lua docs](https://github.com/MST-Community/samp-lua-docs), [examples](https://github.com/ins1x/moonloader-scripts), [mimgui](https://github.com/THE-FYP/mimgui) | Event definitions, Lua APIs, UI and examples |
| GTA engine / ASI | [plugin-sdk](https://github.com/DK22Pac/plugin-sdk), [gta-reversed](https://github.com/gta-reversed/gta-reversed), [SAEncyclopedia](https://github.com/TsyVM/SAEncyclopedia), [sa-sdk](https://github.com/TsyVM/sa-sdk) | Game classes, addresses, layouts and engine behavior |
| Networking | [RakSAMP](https://github.com/YashasSamaga/RakSAMP), [RakSAMP-cli](https://github.com/pavetr1337/RakSAMP-cli), [sampraknet](https://github.com/mishpro-programm/sampraknet), [RakNet](https://github.com/facebookarchive/RakNet) | Historical protocol and serialization research; verify exact SA-MP revision |
| MTA | [engine](https://github.com/multitheftauto/mtasa-blue), [resources](https://github.com/multitheftauto/mtasa-resources), [official wiki](https://wiki.multitheftauto.com/) | Client/server Lua, resources, synchronization and native implementations |
| Blender / mapping | [INU Tools](https://github.com/INU-ez/INU_Tools-GTA-Blender), [Ariane](https://github.com/Dryxio/ariane), [DragonFF](https://github.com/Parik27/DragonFF) | Asset export, map placement; check installed INU/Ariane bridge versions |
| RenderWare | [librw](https://github.com/aap/librw), [Magic.TXD source candidate](https://github.com/FrannDzs/Magic.TXD), [rwfury](https://github.com/Hancapo/rwfury), [Go parser](https://github.com/go-theft-auto/renderware) | Independent DFF/TXD/COL/IMG/IFP implementations |
| Animation | [ifp-reader](https://github.com/tmfksoft/ifp-reader), DragonFF, INU Tools, SAEncyclopedia above | IFP variants, bone IDs, HAnim/Skin and animation workflows |
| CLEO / opcodes | [CLEO5](https://github.com/cleolibrary/CLEO5), [CLEO4](https://github.com/cleolibrary/CLEO4), [Redux](https://github.com/cleolibrary/CLEO-Redux), [Sanny library](https://github.com/sannybuilder/library), [Sanny docs](https://github.com/sannybuilder/docs) | Opcode signatures and scripting runtimes |
| Loading / limits | [Mod Loader](https://github.com/thelink2012/modloader), [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader), [Silent loader mirror](https://github.com/GTAmodding/ASI-Loader), [fastman92](https://github.com/fastman92/fastman92_limit_adjuster) | Loading and patching reference; inspect licenses before reuse |
| Discovery / debugging | [community index](https://github.com/GTAmodding/Community-Plugins), [CLEO organization](https://github.com/cleolibrary), [x64dbg](https://github.com/x64dbg/x64dbg), [Ghidra](https://github.com/NationalSecurityAgency/ghidra), [Dependencies](https://github.com/lucasg/Dependencies) | Discover CrashInfo, SilentPatch, SkyGfx, Project2DFX, VehFuncs; inspect crashes and DLL dependencies |

SAMPFUNCS SDK, SAMemory, vanilla skeletons and game asset references must be matched to your actual installed versions. No unverified download or redistributed vanilla game assets are bundled here.

## Cloud workflow
1. Grant your Codex GitHub connection access to this private repository and select it in your development environment.
2. Read AGENTS.md. State the project category, exact game/client/tool versions and desired output.
3. Use scripts/fetch_reference.py with one owner/repository at a time. References go to an ignored folder. Internet access must be available in the cloud environment.
4. Add your own source under projects/<category>/<project>. Keep build and export commands documented in the project README.
5. Download only final artifacts for local runtime testing.

GitHub stores files; it does not itself run Blender, GTA SA or Codex. Cloud task availability and limits depend on your account. No Codespace, billing setting or live Ariane bridge has been configured by this hub.

## Validation by project type
- Pawn: compile with matching includes/plugins; test callbacks on the intended server.
- MoonLoader: LuaJIT-compatible syntax; verify APIs in installed libraries; test in GTA/SA-MP.
- ASI: record GTA executable revision, architecture, compiler and SDK; verify pointers and build for the target.
- MTA: validate meta.xml and test client/server events in MTA.
- Assets: inspect scale, normals, UVs, prelighting, materials, collision and skin weights; re-import exports and test in-game.
- INU/Ariane: confirm bridge documentation and compatible versions before linking running applications.

## Project starter brief
Copy this into projects/<category>/<name>/README.md:

- Goal:
- Target game and revision:
- SA-MP/open.mp/MTA version:
- Installed libraries and tool versions:
- Inputs and expected outputs:
- Build/export command:
- Runtime verification:
- References and pinned commits:

Never label an AMX/ASI/DFF/TXD/COL ready for the game until its relevant build/export and runtime checks have actually passed.
