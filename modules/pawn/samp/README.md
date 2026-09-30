# Pawn — SA-MP and open.mp

Pawn is the language; SA-MP and open.mp are the server runtimes. Both belong here. The modular starter has separate samp037 and openmp entrypoints. Source snapshots keep their original paths and bundled includes; dependencies retain separate versions. DL gamemodes are porting references only.

Read FEATURE_GUIDE.md, REFERENCE_LOCK.json and DEPENDENCY_REPORT.md. From the repository root, run `python3 modules/prepare_references.py --all --starters`.

Shared library sources: pawn-libraries-source.zip contains the standard library pack and separate samp037/openmp profiles. PAWN_LIBRARIES.md and PAWN_SOURCE_LOCK.json document its libraries; PAWN_FUNCTION_INDEX.tsv lists declarations. This shared pack complements the gamemode-specific dependency pack; preserve the original versions.
