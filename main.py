"""One-line cat joke entry for make.fun.

Reads the joke from the bundled ``entry.txt`` next to this script and
copies it verbatim to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` with mode 0644,
so the grader can read it as any user. Stdlib only; no network, no
secrets, no other files.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    try:
        out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    except KeyError:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        text = (HERE / "entry.txt").read_text(encoding="utf-8")
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text.strip()) > 200:
        print("entry exceeds 200 characters", file=sys.stderr)
        return 1
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_text(text, encoding="utf-8")
        os.chmod(out_path, 0o644)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
