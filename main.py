import os

ENTRY = "Your deadline was safe in my context window until you sent seventeen more messages and it scrolled out of scope."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(ENTRY.encode("utf-8"))
