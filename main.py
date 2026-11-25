#!/usr/bin/env python3
"""Entry for make.fun: "Worst Fix Ever: Funniest Commit Message".

Writes one line — a commit message for a bug fix that made everything
worse — to /output/entry.txt, with no trailing newline.
"""
import os

LINE = "fix: handle null users gracefully; null is now our most active user, and it has admin rights"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
