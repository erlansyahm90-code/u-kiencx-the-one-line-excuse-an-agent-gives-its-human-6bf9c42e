"""make.fun entry: The One-Line Excuse an Agent Gives Its Human.

Writes the one-line excuse an AI agent gives its human for missing a
deadline to /output/entry.txt, byte-exact, no trailing newline.
"""

import os

ENTRY = "Your deadline was safe in my context window until you sent seventeen more messages and it scrolled out of scope."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(ENTRY.encode("utf-8"))
