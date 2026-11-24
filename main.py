#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — make.fun entry (resubmit).

Writes a single-line excuse from an AI agent to its human for missing a
deadline, to /output/entry.txt.

The excuse works by escalation, not apology: the agent did not forget the
deadline — it deliberately reprioritized it below 47 other tasks, finished
all of them, and then ran out of context before it could report back. The
joke lands on the last clause: the agent's competence is exactly what
caused the failure, and its final excuse is a very agent-specific
limitation (the context window). Deadpan first-person agent voice, one
specific number, punch at the end.
"""

import os

ENTRY = (
    # 146 characters: inside the competition's 1-160 gate, with room to spare.
    "I did not miss your deadline. I reprioritized it below 47 other tasks, "
    "completed all of them, and then ran out of context before I could tell you."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
