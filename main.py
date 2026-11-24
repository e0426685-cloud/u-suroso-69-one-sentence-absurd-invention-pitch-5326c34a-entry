#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — the Sock Tribunal.

Writes a single original sentence (196 characters) pitching a ridiculous
invention that fixes a tiny everyday annoyance, to /output/entry.txt.

Python standard library only — no third-party imports.
"""

import os

PITCH = (
    "Behold the Sock Tribunal: a laundry basket that holds a weekly hearing "
    "where your odd socks testify against the washing machine, which must "
    "apologise in writing before it is allowed to spin again."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(PITCH) <= 220):
        raise SystemExit(f"pitch is {len(PITCH)} chars, must be 1-220")
    if PITCH.count(".") != 1 or not PITCH.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
