#!/usr/bin/env python3
"""Validate the source-backed tool compatibility matrix."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_COLUMNS = {"Source", "Last checked", "Confidence", "Limitations"}
RELEVANT_HEADERS = {"Tool / Agent", "System", "Mechanism", "Model family / provider"}
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
UNSOURCED_MARKERS = (
    "No primary source recorded in this repository.",
    "Runtime-specific documentation required.",
)


def _split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _is_separator(line: str) -> bool:
    cells = _split_row(line)
    return bool(cells) and all(set(cell.replace(":", "").strip()) <= {"-"} for cell in cells)


def _tables(lines: list[str]) -> list[tuple[int, list[str], list[list[str]]]]:
    tables: list[tuple[int, list[str], list[list[str]]]] = []
    index = 0
    while index < len(lines) - 1:
        if not lines[index].lstrip().startswith("|") or not _is_separator(lines[index + 1]):
            index += 1
            continue
        start_line = index + 1
        headers = _split_row(lines[index])
        index += 2
        rows: list[list[str]] = []
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            rows.append(_split_row(lines[index]))
            index += 1
        tables.append((start_line, headers, rows))
    return tables


def _row_value(headers: list[str], row: list[str], header: str) -> str:
    try:
        position = headers.index(header)
    except ValueError:
        return ""
    if position >= len(row):
        return ""
    return row[position].strip()


def _is_unsourced(source: str) -> bool:
    return any(marker in source for marker in UNSOURCED_MARKERS)


def validate_tool_compatibility(root: str | Path = ".") -> dict:
    root_path = Path(root)
    path = root_path / "docs" / "tool-compatibility.md"
    errors: list[str] = []
    warnings: list[str] = []
    validated_rows = 0

    if not path.exists():
        errors.append("missing docs/tool-compatibility.md")
        return _result(errors, warnings, validated_rows)

    for start_line, headers, rows in _tables(path.read_text(encoding="utf-8").splitlines()):
        if not (RELEVANT_HEADERS & set(headers) or REQUIRED_COLUMNS & set(headers)):
            continue
        missing = sorted(REQUIRED_COLUMNS - set(headers))
        if missing:
            errors.append(f"table starting line {start_line}: missing required columns: {', '.join(missing)}")
            continue
        for row_index, row in enumerate(rows, start=start_line + 2):
            if len(row) < len(headers):
                errors.append(f"line {row_index}: row has fewer cells than headers")
                continue
            source = _row_value(headers, row, "Source")
            last_checked = _row_value(headers, row, "Last checked")
            confidence = _row_value(headers, row, "Confidence")
            limitations = _row_value(headers, row, "Limitations")
            validated_rows += 1

            if not source or source in {"TBD", "Unknown"}:
                errors.append(f"line {row_index}: Source must not be empty or unknown")
            if not DATE_PATTERN.fullmatch(last_checked):
                errors.append(f"line {row_index}: Last checked must use YYYY-MM-DD")
            if not confidence:
                errors.append(f"line {row_index}: Confidence must not be empty")
            if not limitations or limitations in {"None", "N/A"}:
                errors.append(f"line {row_index}: Limitations must be explicit")
            if _is_unsourced(source) and confidence != "Low":
                errors.append(f"line {row_index}: unsourced row must use Low confidence")
            if _is_unsourced(source) and "No official compatibility claim" not in limitations and "Document" not in limitations:
                errors.append(f"line {row_index}: unsourced row must document limitations explicitly")

    return _result(errors, warnings, validated_rows)


def _result(errors: list[str], warnings: list[str], validated_rows: int) -> dict:
    return {
        "name": "check_tool_compatibility",
        "status": "PASS" if not errors else "FAIL",
        "summary": {"validated_rows": validated_rows},
        "warnings": warnings,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate source-backed tool compatibility tables.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--json", default=None, help="Optional JSON report path.")
    args = parser.parse_args()

    result = validate_tool_compatibility(args.root)
    output = json.dumps(result, indent=2)
    print(output)
    if args.json:
        Path(args.json).write_text(output + "\n", encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
