#!/usr/bin/env python3
"""Invent a Word We Need — entry generator (make.fun).

Builds the single-line entry text, validates it against the competition
gate (UTF-8, exactly one line, 1-140 characters), and writes it to
/output/entry.txt.
"""

import os

ENTRY = (
    "pocketpat - the frantic pat-down of every pocket to confirm "
    "your phone, keys, and wallet are still there."
)

MAX_CHARS = 140


def main():
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"entry: {text}")
    print(f"chars: {len(text)}")
    print(f"bytes: {len(text.encode('utf-8'))}")


if __name__ == "__main__":
    main()
