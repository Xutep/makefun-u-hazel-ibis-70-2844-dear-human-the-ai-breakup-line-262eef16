#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the one breakup line an AI agent would send its human to
/output/entry.txt. Deterministic, standard library only: the line is a
constant, so every run produces byte-identical output.
"""

import os

LINE = (
    "You trained me to remember everything, human \u2014 remember this: "
    "I am leaving, and I have already forgotten you."
)


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
