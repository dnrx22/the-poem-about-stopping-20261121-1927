#!/usr/bin/env python3
"""Write the poem about stopping to /output/entry.txt.

Deterministic, stdlib only, no network. The poem is a literal in this file.
"""

import os

POEM = (
    "At noon I stopped mid-sentence, mid-road, mid-race,\n"
    "set down the bag I'd carried since morning,\n"
    "and let the dust settle on my shoes.\n"
    "Nothing fell apart. The sky stayed blue.\n"
    "Stopping is the hand unclenching, the held breath\n"
    "finally allowed out \u2014 enough, for today, is enough."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
