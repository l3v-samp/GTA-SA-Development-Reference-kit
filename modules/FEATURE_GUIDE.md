# Feature reference routing

Read source snapshots in their original folders. Compare at least two implementations when available. Follow callback ownership, data enums, persistence, include versions and initialization/cleanup before adapting a feature.

| Requested feature | Primary implementation | Comparison / supporting implementation |
|---|---|---|
| Miner job | Wild-West-Roleplay: gamemodes/func/jobs/mining/core.pwn | gta-open: gamemodes/core/systems/jobs (other job architecture); AdvancedRP Minerext.pwn is mapping only, not a mining job |
| Speedometer | Xeon-SpeedoMeter: filterscripts/xspeedo.pwn with pawno/include/foreach.inc | AdvancedRP: gamemodes/modules/player/visual/speedometer.pwn |
| Hunger/thirst HUD | Wild-West-Roleplay: gamemodes/data/account/core.pwn and gamemodes/utils/gui/core.pwn | ScavengeSurvive: gamemodes/sss/core/char/food.pwn; SP-RP: gamemodes/hunger |
| Inventory | ScavengeSurvive: gamemodes/sss/core/char/inventory.pwn and external inventory/item/container packages | Wild-West-Roleplay: gamemodes/data/inv, gamemodes/utils/inv; AdvancedRP: gamemodes/modules/player/visual/inventory.pwn with bundled SIF includes |
| Filterscript tools | samp-animbrowse and samp-texture-workshop | ST4NSB samp-filterscripts and ins1x useful-samp-stuff |

## Retrieval

1. Select the archive from REFERENCE_LOCK.json. Extract with `python3 -m zipfile -e modules/OWNER--REPO-source.zip .references`.
2. Extract `modules/pawn-reference-dependencies.zip` into `.references`; read its DEPENDENCY_LOCK.json and the original pawn.json. Preserve distinct versions in separate directories.
3. Open the feature file, its includes, associated data/core/GUI/persistence modules and schema. FEATURE_INDEX.json is a keyword discovery index, not a guarantee of a complete feature.
4. Choose SA-MP 0.3.7 or open.mp explicitly. DL repositories require porting and are algorithm references, not compatibility-tested 0.3.7 builds.
5. Implement in your own feature directory with config/data/service/UI/persistence boundaries. Route callbacks through the project callback owner or its existing hook framework. Register cleanup for timers, TextDraws, pickups, objects and player data.
6. Report upstream commit, adapted paths, dependencies, license and validation result. Missing includes and plugin binaries must be explicit.

Source archives retain available includes and source dependencies. Runtime binaries, model/audio assets, secrets, player data and database row dumps are excluded. Three dependency declarations remain unresolved (see DEPENDENCY_REPORT.md); no source pack has been certified as build complete.
