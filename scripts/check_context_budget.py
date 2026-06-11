#!/usr/bin/env python3
"""Warn about oversized or repetitive AI documentation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


GENERIC_PHRASES = [
    "do not invent",
    "mark assumptions",
    "human review",
    "repository evidence",
]


def check_context_budget(root: str | Path = ".", max_lines: int = 220) -> dict:
    root_path = Path(root)
    warnings: list[str] = []
    errors: list[str] = []
    markdown_files = [
        path
        for base in [root_path / "templates" / "docs-ai", root_path / "docs"]
        if base.exists()
        for path in base.rglob("*.md")
    ]

    headings_seen: dict[str, Path] = {}
    for path in markdown_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        if len(lines) > max_lines:
            warnings.append(f"{path.relative_to(root_path).as_posix()}: {len(lines)} lines exceeds {max_lines}")
        lowered = text.lower()
        repeated = [phrase for phrase in GENERIC_PHRASES if lowered.count(phrase) > 4]
        if repeated:
            warnings.append(f"{path.relative_to(root_path).as_posix()}: repeated generic phrases: {', '.join(repeated)}")
        for line in lines:
            if line.startswith("## "):
                heading = line.strip().casefold()
                previous = headings_seen.get(heading)
                if previous and previous != path:
                    warnings.append(
                        f"duplicate section heading {line.strip()!r} in "
                        f"{previous.relative_to(root_path).as_posix()} and {path.relative_to(root_path).as_posix()}"
                    )
                    break
                headings_seen[heading] = path

    return {"name": "check_context_budget", "status": "PASS", "warnings": warnings, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Warn about oversized or repetitive AI docs.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--max-lines", type=int, default=220, help="Line-count warning threshold.")
    args = parser.parse_args()
    print(json.dumps(check_context_budget(args.root, args.max_lines), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
