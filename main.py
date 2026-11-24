#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.
The word: ASAP. The boss is pure ASAP — everything is urgent, everything
was due yesterday, and the word needs no caption to land.
"""

import os

WORD = "ASAP"


def validate(word):
    """Mirror the bounty gate: UTF-8 text, 1 to 30 characters, not only
    whitespace, and exactly one word (no spaces, no newlines)."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")
    return True


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    with open("/output/entry.txt", encoding="utf-8") as f:
        validate(f.read())


if __name__ == "__main__":
    main()
