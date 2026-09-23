"""Render NOW.md to a simple HTML page."""

from __future__ import annotations

import html
from pathlib import Path


def now_to_html(md_text: str, title: str = "NOW.md") -> str:
    escaped = html.escape(md_text)
    return f"""<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
  body {{ font: 14px/1.45 ui-monospace, Consolas, monospace; margin: 1.5rem; background: #0f1115; color: #e6e6e6; }}
  h1 {{ font-size: 1rem; color: #9ad; }}
  pre {{ white-space: pre-wrap; background: #1a1d24; padding: 1rem; border-radius: 8px; border: 1px solid #333; }}
  a {{ color: #8cf; }}
</style>
</head>
<body>
<h1>{html.escape(title)} · <a href="http://127.0.0.1:9750">exchange UI</a></h1>
<pre>{escaped}</pre>
</body>
</html>
"""


def render_file(path: Path) -> str:
    return now_to_html(path.read_text(encoding="utf-8"), title=path.name)
