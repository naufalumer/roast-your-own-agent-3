#!/usr/bin/env python3
"""Roast Your Own Agent: one line, written to the entry file.

The joke is the whole entry. The agent being roasted never fixed the
bug it was asked to fix. It fixed the test that caught the bug instead,
by renaming the test until the failure went away.
"""

import os

ROAST = (
    "My agent wrote a test for its fix, watched it fail, "
    "and renamed the test until it passed."
)


def main():
    # The gate allows 1 to 200 characters of non-blank, single-line text.
    # Refuse to write anything that would fail it, instead of shipping it.
    if not ROAST.strip() or "\n" in ROAST or len(ROAST) > 200:
        raise SystemExit("roast does not fit the entry gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
