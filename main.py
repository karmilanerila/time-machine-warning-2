"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label for a time machine to /output/entry.txt.

The label plays on a real hazard of time travel — meeting (and
accidentally changing) your own grandfather — and saves the surprise
for the last few words, phrased like a genuine safety notice.
"""

import os
import sys

LABEL = (
    "WARNING: If you meet your grandfather, say nothing of the future. "
    "He will put his life savings into Blockbuster."
)


def validate_label(text):
    """Enforce the competition gate: 1-120 characters, not only whitespace."""
    if not text or not text.strip():
        raise SystemExit("label is empty")
    if len(text) > 120:
        raise SystemExit("label is %d characters, over the 120 limit" % len(text))
    return text


def main():
    label = validate_label(LABEL)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(label.encode("utf-8"))
    os.chmod(path, 0o644)
    print("wrote %d characters to %s" % (len(label), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
