"""VELMORA — a travel poster for a place that isn't there.

The poster image (entry.png) was rendered at build time and ships with
this repository. This program is intentionally stdlib-only: it copies
the finished poster to /output/entry.png and verifies the copy, so it
runs cleanly in the grader's no-network sandbox.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.png")

# The competition gate: at most 1,048,576 bytes and 1024 by 1024 pixels.
MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024

# PNG header layout: bytes 16..24 hold the width and height as big-endian
# 32-bit integers inside the IHDR chunk.
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_png_dimensions(path):
    """Return (width, height) read from a PNG file's IHDR chunk."""
    with open(path, "rb") as handle:
        header = handle.read(24)
    if header[:8] != PNG_SIGNATURE:
        raise ValueError("entry.png is not a PNG file")
    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    return width, height


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    if not os.path.isfile(SOURCE):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1

    size = os.path.getsize(SOURCE)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the {MAX_BYTES} cap",
              file=sys.stderr)
        return 1

    width, height = read_png_dimensions(SOURCE)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"entry.png is {width}x{height}, over the "
              f"{MAX_DIMENSION}x{MAX_DIMENSION} cap", file=sys.stderr)
        return 1

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_PATH)

    # Confirm the copy is byte-identical to the shipped poster, not just
    # the same size: a truncated or altered copy must fail loudly here.
    if sha256_of(OUTPUT_PATH) != sha256_of(SOURCE):
        print("copied entry.png does not match the shipped entry.png",
              file=sys.stderr)
        return 1

    copied_size = os.path.getsize(OUTPUT_PATH)
    copied_hash = sha256_of(OUTPUT_PATH)
    print(f"Wrote {OUTPUT_PATH}: {copied_size} bytes, "
          f"{width}x{height}, sha256 {copied_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
