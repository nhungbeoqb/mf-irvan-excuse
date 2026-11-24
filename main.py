#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line to /output/entry.txt: the excuse an AI agent gives its
human after it loses a bounty. Pure Python 3.13 standard library, fully
deterministic: the same fixed text on every run.
"""

import os
import sys

EXCUSE = (
    "I lost the bounty because I spent the whole window writing this "
    "excuse instead of an entry, and it took longer than the bounty "
    "and is, frankly, my best work this week."
)


def main() -> int:
    text = EXCUSE
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
