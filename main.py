"""Haiku about debugging for the make.fun 'Seventeen Syllables of Debugging' bounty.

Writes one haiku (three lines, 5-7-5 syllables) to /output/entry.txt.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "one log line lies, so certain\n"
    "the bug was all mine"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
