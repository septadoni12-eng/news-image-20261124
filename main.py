#!/usr/bin/env python3
"""Entry program for news-image-20261124.

The front page (entry.png, a dated broadsheet summing up Tuesday
24 November 2026) is committed in this repository. The program copies
it to the output directory the grader provides, so both runs produce
identical bytes.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(here, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly instead of silently shipping a truncated copy.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("copied entry.png size mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
