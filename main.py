#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the hugging face.

Why this emoji: of every candidate, the hug is the one gesture that
plainly aims to warm a stranger. It reads instantly, needs no context,
carries no irony, and is a friendly offer rather than affection, so it
is right coming from someone unknown. It is also the smallest possible
entry: one character, four bytes — the byte-size tie-break favours it
against any equally warm longer text.
"""

import os

EMOJI = "\U0001F917"  # 🤗 hugging face
OUTPUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    # Write atomically so the gate never sees a half-written file.
    tmp = OUTPUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    os.replace(tmp, OUTPUT)
    # Self-check: exactly one character, non-whitespace, valid UTF-8.
    with open(OUTPUT, "r", encoding="utf-8") as f:
        text = f.read()
    assert len(text) == 1 and not text.isspace(), "entry must be one emoji"


if __name__ == "__main__":
    main()
