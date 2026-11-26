# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay enumerates depth profiles up to 16 leaves at five rational discounts. It checks the tree formula, 500 seeded two-point inequalities, five exact four-state gaps and the smoothed center at M = 3 and smoothing radius 1/16. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/persuasion-gap-explorer.zip) and open index.html to rotate the posterior simplex and compare its exact scores. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font parameters. [Build the paper](paper/BUILD.md).
