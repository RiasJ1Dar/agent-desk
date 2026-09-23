#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from agent_desk.view import render_file


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="agent-desk")
    sub = p.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("view", help="Render NOW.md to HTML")
    v.add_argument("now_md", type=Path)
    v.add_argument("-o", "--output", type=Path, default=None)
    args = p.parse_args(argv)
    if args.cmd == "view":
        html_out = render_file(args.now_md)
        if args.output:
            args.output.write_text(html_out, encoding="utf-8")
            print(args.output)
        else:
            print(html_out)
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
