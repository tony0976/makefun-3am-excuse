"""Writes one hardware wallet excuse to /output/entry.txt."""
import os

TEXT = "No. It is 3 AM, my screen is off, and the last thing I signed at this hour was a JPEG of a rock you swore was an investment."

# Rule: the excuse must be a single line under 200 characters.
# The joke is the wallet's own grudge: it remembers the last 3 AM signing
# (a JPEG rock "investment") and refuses to repeat it — no battery, firmware
# or cold-storage cliche.
assert "\n" not in TEXT and len(TEXT) < 200, f"entry must be one line, under 200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
