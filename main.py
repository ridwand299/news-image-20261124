"""Entry point for the make.fun news-image-20261124 bounty.
Copies the pre-rendered entry.png (built by build_image.py) to
/output/entry.png, as required by the competition harness.
Deterministic: byte-identical output on every run.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")

def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"copied {SRC} -> {DST} ({DST.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
