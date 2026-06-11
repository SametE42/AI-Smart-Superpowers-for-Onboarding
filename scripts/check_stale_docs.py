#!/usr/bin/env python3
"""Validate FRESHNESS.md review tables."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_COLUMNS = ["File", "Last reviewed", "Review trigger", "Owner", "Status"]
VALID_STATUS = {"Current", "Needs review", "Stale", "Unknown", "Aktuell", "Pruefung noetig", "Veraltet", "Unbekannt"}
STALE_STATUS = {"Needs review", "Stale", "Pruefung noetig", "Veraltet"}


def _table_rows(text: str) -> tuple[list[str], list[list[str]]] | None:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip().startswith("|") and "Status" in line:
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            rows: list[list[str]] = []
            row_index = index + 2
            while row_index < len(lines) and lines[row_index].strip().startswith("|"):
                rows.append([cell.strip() for cell in lines[row_index].strip().strip("|").split("|")])
                row_index += 1
            return headers, rows
    return None


def check_stale_docs(path: str | Path) -> dict:
    freshness_path = Path(path)
    text = freshness_path.read_text(encoding="utf-8", errors="replace")
    errors: list[str] = []
    warnings: list[str] = []
    table = _table_rows(text)
    if not table:
        return {"name": "check_stale_docs", "status": "FAIL", "warnings": warnings, "errors": ["no freshness table found"]}

    headers, rows = table
    for column in REQUIRED_COLUMNS:
        if column not in headers:
            errors.append(f"missing required column: {column}")
    if "Status" not in headers:
        return {"name": "check_stale_docs", "status": "FAIL", "warnings": warnings, "errors": errors}
    status_index = headers.index("Status")
    reviewed_index = headers.index("Last reviewed") if "Last reviewed" in headers else None
    file_index = headers.index("File") if "File" in headers else 0
    for row in rows:
        status = row[status_index] if len(row) > status_index else ""
        filename = row[file_index] if len(row) > file_index else "[unknown]"
        if status not in VALID_STATUS:
            errors.append(f"invalid status for {filename}: {status}")
        if status in STALE_STATUS:
            warnings.append(f"{filename}: {status}")
        if reviewed_index is not None and (len(row) <= reviewed_index or not row[reviewed_index].strip()):
            errors.append(f"{filename}: missing last reviewed value")
    return {"name": "check_stale_docs", "status": "PASS" if not errors else "FAIL", "warnings": warnings, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate freshness metadata.")
    parser.add_argument("path", nargs="?", default="templates/docs-ai/FRESHNESS.md")
    args = parser.parse_args()
    result = check_stale_docs(args.path)
    print(json.dumps(result, indent=2))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
