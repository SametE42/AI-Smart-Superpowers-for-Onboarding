#!/usr/bin/env python3
"""Generate a Markdown report for language-support metadata."""

from __future__ import annotations

import argparse
from pathlib import Path

from check_language_support import validate_language_support


RTL_LANGUAGES = {"ar", "fa", "he", "ps", "ur"}


def render_report(root: str | Path = ".") -> str:
    result = validate_language_support(root)
    status_counts = result.summary.get("translation_review_status", {})
    lines = [
        "# Language Support Report",
        "",
        "This report is generated from `i18n/language-support.yml` and `i18n/file-map.*.yml`.",
        "",
        "## Summary",
        "",
        f"- Validation status: {'PASS' if result.ok else 'FAIL'}",
        f"- Detected existing languages: {result.summary.get('detected_languages', 0)}",
        f"- Functionally complete languages: {result.summary.get('complete_languages', 0)}",
        f"- File maps: {result.summary.get('file_maps', 0)}",
        "",
        "## Translation Review Status",
        "",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"- {status}: {count}")

    lines.extend(["", "## Languages", "", "| Code | Name | Output support | Review status | File map | Notes |", "|---|---|---|---|---|---|"])
    for code, info in sorted(result.language_support.items()):
        notes = str(info.get("notes", ""))
        lines.append(
            f"| {code} | {info.get('name', '')} | {info.get('output_support', '')} | "
            f"{info.get('translation_review_status', '')} | `{info.get('file_map', '')}` | {notes} |"
        )

    missing_file_maps = [
        code for code, info in sorted(result.language_support.items()) if code not in result.file_maps
    ]
    lines.extend(["", "## File-Map Issues", ""])
    if missing_file_maps:
        lines.append(f"- Missing file maps: {', '.join(missing_file_maps)}")
    else:
        lines.append("- Missing file maps: none")
    if result.errors:
        lines.append(f"- Validation errors: {len(result.errors)}")
        for error in result.errors:
            lines.append(f"  - {error}")
    else:
        lines.append("- Validation errors: none")

    lines.extend(["", "## RTL And Unicode Notes", ""])
    for code in sorted(RTL_LANGUAGES & set(result.language_support)):
        info = result.language_support[code]
        lines.append(
            f"- {code} ({info.get('name')}): uses documented ASCII-safe filenames in its file map; "
            "Markdown content may still be RTL."
        )

    lines.extend(["", "## ASCII-Safe Filename Decisions", ""])
    lines.append(
        "All non-English file maps use stable ASCII-safe target filenames unless a reviewed localized mapping exists. "
        "This keeps generated structures parseable while translation review remains separate from functional support."
    )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate language support report.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--output", default="docs/language-support-report.md", help="Markdown report path.")
    args = parser.parse_args()

    root = Path(args.root)
    output_path = root / args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_report(root), encoding="utf-8")
    print(f"wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
