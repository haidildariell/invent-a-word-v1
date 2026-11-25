#!/usr/bin/env python3
"""Invent a Word We Need — entry generator.

Writes the invented word entry to /output/entry.txt.
Deterministic, no network, no dependencies.
"""

import os

ENTRY_TEXT = (
    "pocketpat - the frantic pat-down of every pocket to confirm "
    "your phone, keys, and wallet are still there."
)
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def build_entry_text():
    """Assemble the single-line entry text from its parts."""
    return ENTRY_TEXT


def validate_entry(text):
    """Check the entry against the competition gate."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main():
    text = build_entry_text()
    validate_entry(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
