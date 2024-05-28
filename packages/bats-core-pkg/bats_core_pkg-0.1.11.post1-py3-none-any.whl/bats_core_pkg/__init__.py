#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
from os import environ


def main():
    curfile = Path(__file__)
    bats_installation = curfile.absolute().parent / "dist"
    bats_path = bats_installation / "bin/bats"
    environ["BATS_LIB_PATH"] = str(bats_installation / "test_helper")
    proc = subprocess.run([bats_path] + sys.argv[1:], check=False, env=environ)
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
