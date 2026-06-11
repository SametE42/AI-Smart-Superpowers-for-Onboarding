#!/usr/bin/env python3
"""Generate templates/docs-ai/INDEX.md."""

from __future__ import annotations

import argparse
from pathlib import Path


def _title_for(path: Path) -> str:
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def generate_index(root: str | Path = ".") -> str:
    root_path = Path(root)
    docs_ai = root_path / "templates" / "docs-ai"
    files = sorted(path for path in docs_ai.glob("*.md") if path.name not in {"README.md", "INDEX.md"})
    lines = [
        "# Docs AI Template Index",
        "",
        "This index is generated from `templates/docs-ai/`.",
        "",
        "| File | Purpose |",
        "|---|---|",
    ]
    for path in files:
        lines.append(f"| `{path.name}` | {_title_for(path)} |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate docs-ai template index.")
    parser.add_argument("--root", default=".")
    parser.add_argument("--output", default="templates/docs-ai/INDEX.md")
    args = parser.parse_args()
    root = Path(args.root)
    output = root / args.output
    output.write_text(generate_index(root), encoding="utf-8")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
