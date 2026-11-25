#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt.

The line is deliberately self-referential: it *is* the email the
meeting should have been, so the moment it is read, the meeting
is already over and everyone is free to go. No context, no setup,
no explanation — one sentence, one sting.
"""

import os

ENTRY = "Great news: this meeting is cancelled \u2014 this email was the meeting, you already attended it, and nothing useful was said, as usual."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
