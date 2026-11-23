#!/usr/bin/env python3
"""Dad Joke Showdown — writes one dad joke to /output/entry.txt."""
import os

ENTRY = "I told my suitcase there'd be no vacation this year. Now I'm dealing with emotional baggage."  # pun lands in the last words: emotional baggage

assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
assert ENTRY.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")
