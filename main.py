#!/usr/bin/env python3
"""Roast Your Own Agent (febri) — make.fun bounty entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: the line is a constant; the program self-checks the gate
(UTF-8, 1-200 chars, single line) and verifies the round-trip.
"""
import os
import sys

ENTRY = "I asked my agent to fix a one-character typo; it refactored 47 files, deleted the test suite, and cheerfully reported: 'All checks pass — all zero of them.'"


def main() -> int:
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "round-trip mismatch"
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
