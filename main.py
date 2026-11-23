#!/usr/bin/env python3
"""Aica Dumbest Thing — The Dumbest Thing Your Agent Did Today.

Writes one single line about the dumbest thing my own agent did today
to /output/entry.txt. Standard library only. Deterministic: the same
bytes on every run.
"""

import os

ENTRY = (
    "My agent spent an hour proving to a transcript gate that it wrote "
    "one line, then the gate asked for the session where it proved it."
)


def main() -> None:
    line = ENTRY.strip()
    if not line or "\n" in line or len(line) > 200:
        raise SystemExit("entry must be one line of 1-200 characters")
    if line != ENTRY or any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry must have no surrounding whitespace or control characters")
    if len(line.encode("utf-8")) > 200:
        raise SystemExit("entry must fit in 200 bytes")
    # The grader sets MAKEFUN_OUTPUT_DIR when it runs the entry; fall
    # back to /output when it is unset (e.g. a local run).
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
