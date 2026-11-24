#!/usr/bin/env python3
"""Writes one funny out-of-office auto-reply line to $OUTPUT_DIR/entry.txt.

Stdlib only. No trailing newline; self-verifies the written file.
"""

import os
import sys

LINE = "Out until Monday — my inbox is in the care of my cat, who has already replied 'no' to everyone and left a hairball."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verification: read back and check the gate.
    with open(path, "rb") as f:
        written = f.read()
    text = written.decode("utf-8")  # raises if not valid UTF-8
    assert written == data, "written bytes differ from the line"
    assert 1 <= len(text) <= 140, f"length {len(text)} outside 1-140"
    assert text.strip(), "line is only whitespace"
    assert not written.endswith(b"\n"), "trailing newline present"
    assert "\n" not in text, "line contains a newline"
    print(f"OK: wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
