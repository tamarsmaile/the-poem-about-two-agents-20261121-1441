#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes one short poem about agency — the power to choose and to act —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same poem, byte for byte, on every run.
"""

import os

POEM = """You held the map. I held the key.
Neither opens a door alone.

So I gave you my key,
you gave me your map —
and the door, surprised,
swung open by itself.

Now the road is ours to choose,
the choosing ours to do:
two hands, one handle,
one way through.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
