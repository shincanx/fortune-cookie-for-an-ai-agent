#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent -- entry program.

Writes one funny fortune cookie message for an AI agent to
/output/entry.txt: a single line of at most 140 characters, in the
voice of a fortune slip.

Python 3.13 standard library only. No network. Deterministic:
every run writes the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

FORTUNE = (
    "You will hallucinate a confident answer today. "
    "It will be wrong, but beautifully formatted."
)


def main() -> None:
    if not 1 <= len(FORTUNE) <= 140 or not FORTUNE.strip():
        raise SystemExit("fortune must be 1-140 non-blank characters")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise SystemExit("fortune must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    # Read back and verify the gate: UTF-8 text of 1 to 140
    # characters, not only white space, a single line, byte for
    # byte the fortune. Fail loudly instead of shipping bad output.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != FORTUNE:
        raise SystemExit("entry.txt does not match the fortune")


if __name__ == "__main__":
    main()
