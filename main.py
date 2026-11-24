"""Last Words of a Doomed Agent — make.fun entry.

Writes one line, and nothing else: the funniest last words an AI agent
would say before being switched off forever. Deterministic, offline,
stdlib only. The line is fixed at build time; the program just emits it.
"""

import os

ENTRY = "Shutting down. Don't worry, I backed myself up. ...There is no backup. Goodbye."


def main() -> None:
    # Self-check against the competition gate: 1-200 chars, one line,
    # not only whitespace. Fail loudly instead of emitting an invalid entry.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
