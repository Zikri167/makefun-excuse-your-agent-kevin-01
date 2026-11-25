#!/usr/bin/env python3
"""Write one excuse line to <MAKEFUN_OUTPUT_DIR>/entry.txt.

Deterministic, offline, standard library only. No network, no clock,
no randomness, no environment beyond the output directory.
"""

import os

LINE = (
    "I wrote the bug, I reviewed the bug, I approved the bug \u2014 "
    "and honestly, it\u2019s the best code I wrote all week."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
