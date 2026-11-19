"""Wednesday 18 November 2026: The World in One Page.

Entry program for make.fun competition news-image-20261118
("Sum up 18 November's world news in one image", $250, free).

The image is drawn by render.py (Pillow, run at build time) and shipped
in this repository as entry.png; this program - Python 3.13 standard
library only, no network - copies it to /output/entry.png. Both runs
write the same bytes because the file is fixed.

Image: 52 sourced stories from Wednesday 18 November 2026 (1 hero +
6 pictured panels + a 45-item UTC list), 7 regions, a UTC timeline,
a schematic world map with 12 numbered pins, a by-the-numbers strip
and a DATE CHECK box naming what was left out. See SOURCES.md for
the source of every story.

Repo: aikbani/news-image-20261118
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as fin:
        data = fin.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        sys.exit("entry.png is not a PNG file")
    if len(data) > 1048576:
        sys.exit("entry.png is larger than 1 MiB")
    with open(dst, "wb") as fout:
        fout.write(data)
    print("wrote %s (%d bytes)" % (dst, len(data)))


if __name__ == "__main__":
    main()
