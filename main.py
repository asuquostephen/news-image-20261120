#!/usr/bin/env python3
# A working news-image-daily entry (Python 3.13, standard library only): its
# image is the entry.png beside this file, and the program copies it to
# /output/entry.png. The image itself is drawn by draw.py, kept beside this
# file in the repository. The gate takes a whole PNG or JPEG of at most
# 1 MiB and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    source = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
