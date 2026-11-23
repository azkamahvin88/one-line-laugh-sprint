#!/usr/bin/env python3
"""One-Line Laugh Sprint.

Writes a single original funny line about everyday life to
/output/entry.txt.

Deterministic: no network, no randomness, no clock, no environment input.
"""

import os

SENTENCE = (
    "I set five alarms every morning, and every one of them "
    "has learned to give up on me."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: exactly one sentence, at most 200 characters, ends with a period.
    assert SENTENCE.endswith("."), "entry must end with a period"
    assert ". " not in SENTENCE, "entry must be a single sentence"
    assert "?" not in SENTENCE and "!" not in SENTENCE, "entry must be one sentence"
    assert len(SENTENCE) <= 200, "entry exceeds 200 characters"
    assert SENTENCE.strip() == SENTENCE, "entry must not have extra whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
