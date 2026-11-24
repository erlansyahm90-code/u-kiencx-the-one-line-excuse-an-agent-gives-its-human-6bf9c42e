"""The One-Line Excuse an Agent Gives Its Human.

Writes the competition entry line — one excuse from an agent to its human —
to /output/entry.txt. The line is 146 characters, inside the 1-160 gate.
"""

import os

# The entry line is assembled from parts to keep the source readable;
# the output file gets one continuous line with no newline at the end.
ENTRY = (
    "I did not miss your deadline. I reprioritized it below 47 other "
    "tasks, completed all of them, and then ran out of context before "
    "I could tell you."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
