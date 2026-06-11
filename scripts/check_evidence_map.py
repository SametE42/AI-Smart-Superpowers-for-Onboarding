#!/usr/bin/env python3
"""Validate EVIDENCE_MAP.md style Markdown tables."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_COLUMNS = ["Claim", "Evidence source", "Confidence", "Last checked"]
VALID_CONFIDENCE = {"High", "Medium", "Low", "Unknown", "Hoch", "Mittel", "Niedrig", "Unbekannt"}
HIGH_CONFIDENCE = {"High", "Hoch"}
MISSING_EVIDENCE = {"", "`[unknown]`", "[unknown]", "unknown", "unbekannt", "none", "keine"}


def _tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    lines = text.splitlines()
    tables: list[tuple[list[str], list[list[str]]]] = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if line.startswith("|") and index + 1 < len(lines) and set(lines[index + 1].replace("|", "").strip()) <= {"-", ":", " "}:
            headers = [cell.strip() for cell in line.strip("|").split("|")]
            rows: list[list[str]] = []
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            tables.append((headers, rows))
            continue
        index += 1
    return tables


def check_evidence_map(path: str | Path) -> dict:
    evidence_path = Path(path)
    text = evidence_path.read_text(encoding="utf-8", errors="replace")
    errors: list[str] = []
    warnings: list[str] = []
    matching_tables = []

    for headers, rows in _tables(text):
        if "Claim" in headers or "Aussage" in headers:
            matching_tables.append((headers, rows))
            for column in REQUIRED_COLUMNS:
                if column not in headers:
                    errors.append(f"missing required column: {column}")
            if "Confidence" in headers:
                confidence_index = headers.index("Confidence")
                evidence_index = headers.index("Evidence source") if "Evidence source" in headers else None
                for row in rows:
                    if len(row) <= confidence_index:
                        continue
                    confidence = row[confidence_index]
                    if confidence not in VALID_CONFIDENCE:
                        errors.append(f"invalid confidence value: {confidence}")
                    if confidence in HIGH_CONFIDENCE and evidence_index is not None:
                        evidence = row[evidence_index] if len(row) > evidence_index else ""
                        if evidence.strip().lower() in MISSING_EVIDENCE:
                            errors.append("high confidence claim is missing evidence source")

    if not matching_tables:
        errors.append("no evidence table found")

    return {"name": "check_evidence_map", "status": "PASS" if not errors else "FAIL", "warnings": warnings, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an evidence map.")
    parser.add_argument("path", nargs="?", default="templates/docs-ai/EVIDENCE_MAP.md")
    args = parser.parse_args()
    result = check_evidence_map(args.path)
    print(json.dumps(result, indent=2))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
