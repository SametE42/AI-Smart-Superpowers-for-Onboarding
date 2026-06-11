#!/usr/bin/env python3
"""Validate compact tool entrypoint templates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ENTRYPOINTS = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "COPILOT_INSTRUCTIONS.md",
    "CURSOR_RULES.md",
    "CLINE_RULES.md",
    "AIDER_NOTES.md",
    "OPENCODE.md",
    "COMMANDCODE_SKILL.md",
]


def check_tool_entrypoints(root: str | Path = ".", max_lines: int = 90) -> dict:
    root_path = Path(root)
    base = root_path / "templates" / "tool-entrypoints"
    errors: list[str] = []
    warnings: list[str] = []
    for filename in ENTRYPOINTS:
        path = base / filename
        if not path.exists():
            errors.append(f"missing entrypoint: {path.relative_to(root_path).as_posix()}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text.splitlines()) > max_lines:
            errors.append(f"{filename}: too long")
        if "docs/ai/CONTEXT_INDEX.md" not in text and "localized equivalent" not in text:
            errors.append(f"{filename}: missing knowledge-base reference")
        for required in ["SECURITY_RULES.md", "REVIEW_CHECKLIST.md"]:
            if required not in text:
                errors.append(f"{filename}: missing {required}")
    return {"name": "check_tool_entrypoints", "status": "PASS" if not errors else "FAIL", "warnings": warnings, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate tool entrypoint templates.")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    result = check_tool_entrypoints(args.root)
    print(json.dumps(result, indent=2))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
