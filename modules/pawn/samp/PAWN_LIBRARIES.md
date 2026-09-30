# Pawn libraries: SA-MP 0.3.7 and open.mp

`pawn-libraries-source.zip` contains actual upstream source snapshots, includes, documentation and license notices. It is not just a list of links. Extract it in your cloud workspace to let Codex search the files.

## Contents

| Source folder | Purpose |
|---|---|
| pawn-lang--samp-stdlib | Legacy SA-MP includes, pinned to tag 0.3.7-R2-2-1 |
| openmultiplayer--omp-stdlib | open.mp standard includes |
| pawn-lang--pawn-stdlib | Pawn language standard includes |
| pawn-lang--YSI-Includes | YSI framework, including its four recorded submodules |
| Y-Less--sscanf | Input parsing includes and implementation |
| samp-incognito--samp-streamer-plugin | Dynamic objects/checkpoints/areas and related streaming source |
| pBlueG--SA-MP-MySQL | MySQL Pawn include and plugin source |
| katursis--Pawn.CMD | Command processor include and plugin source |

See `PAWN_SOURCE_LOCK.json` for upstream URLs and exact commit IDs. SA-MP revision here is the 0.3.7 R2 server include snapshot, not a promise that every plugin supports every client/server build.

## Separate profiles

Legacy SA-MP: begin with `#include <a_samp>`, resolve it from the pinned samp-stdlib folder and resolve language includes from pawn-stdlib. Do not add the open.mp include directory to this profile.

open.mp: begin with `#include <open.mp>`, resolve it from omp-stdlib and use matching Pawn language includes. Do not add the legacy samp-stdlib directory to this profile. Consult omp-stdlib documentation for tags/const-correctness compatibility.

For YSI keep the full directory structure and required dependencies. Include only modules needed by your script (e.g. y_hooks, y_commands, y_ini, y_iterate). Do not indiscriminately include every YSI module.

`sscanf2.inc`, `streamer.inc`, `a_mysql.inc` and Pawn.CMD includes declare plugin APIs; their matching runtime binaries must be installed separately. Consult each recorded upstream README/releases for your server, OS and architecture. A snapshot of the newest source is reference material, not verified binary compatibility with legacy SA-MP.

Choose one command processor per project. YSI commands and Pawn.CMD are alternatives; do not load both blindly. Keep library directories separate instead of overwriting equal include filenames.

## Search the functions

`PAWN_FUNCTION_INDEX.tsv` lists 4,499 native, forward and stock declaration lines with original source path and line number. It is a search aid, not a complete semantic API parser: macros, multi-line signatures and conditional compilation require inspecting the original file. It spans both profiles and third-party libraries; filter by source before choosing an API.

Extract in the cloud:

```sh
python3 -m zipfile -e pawn-libraries-source.zip references-cache/pawn
rg -n 'SetPlayerPos|CreateDynamicObject|mysql_connect' references-cache/pawn/sources
```

For compilation, configure include paths and runtime plugins for the selected profile using your matching compiler/server installation. No compiler or plugin binaries are bundled. Plugin C++ dependency submodules are not provisioned; this is not a complete C++ plugin build environment.

## Validation and attribution

Archive creation and integrity checks were performed. The source retains upstream notices. No Pawn compilation, server launch or plugin compatibility testing has been performed. Preserve upstream notices and review licenses before redistribution. These eight selected repositories cover core and common libraries, not every Pawn library ever published.
