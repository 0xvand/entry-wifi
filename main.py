#!/usr/bin/env python3
"""One Word for Your Wi-Fi - a make.fun entry.

Writes a single word describing Wi-Fi to /output/entry.txt
(or to the path given by the ENTRY_OUTPUT env var, for local testing).
The word is written with no trailing newline.
"""

import os

WORD = "Ghosted"

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    # The gate only judges a single token of 1-20 characters; fail loudly
    # rather than ever write an entry the scorer would refuse.
    assert WORD == WORD.strip() and " " not in WORD and 1 <= len(WORD) <= 20
    out_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
