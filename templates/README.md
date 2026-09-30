# Actual starter source files

These are minimal examples, not compiled binaries or a configured full toolchain.

| Folder | Target | Try |
|---|---|---|
| pawn | open.mp Pawn, matching open.mp includes | Compile gamemode.pwn with your Pawn compiler, configure server gamemode, then /hello |
| moonloader | MoonLoader with SA-MP bindings | Install starter.lua under moonloader/; /kithello |
| asi | Windows x86 C++ DLL/ASI | cmake -S templates/asi -B build/asi -A Win32; cmake --build build/asi --config Release |
| mta/reference_kit | MTA resource | Copy folder into server resources, start reference_kit, then /kithello and /kitclient |
| blender | Blender bpy | Run create_test_asset.py in Blender; inspect generated cube |

ASI starter exports a version function only; it has no game hooks or visible in-game behavior. Add verified plugin-sdk functionality for your executable revision as a separate project.
Pawn example uses open.mp headers. For legacy SA-MP, adapt includes to the installed server SDK before compiling.
Blender script creates geometry only. Install a compatible INU Tools/DragonFF exporter and follow its documented material, collision, skin and export requirements. Ariane integration must be configured separately.

Validation: source reviewed; runtime, Pawn compilation, Windows ASI compilation, MTA testing and Blender execution have not been performed in this browser workspace. Verify on the target tools before use.

Copy the relevant folder into projects/category/name/ and add exact dependencies and test results. Never mix MoonLoader APIs with MTA APIs.
