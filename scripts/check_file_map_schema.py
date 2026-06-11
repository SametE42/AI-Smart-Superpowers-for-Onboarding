#!/usr/bin/env python3
"""Validate file-map schema details for all supported languages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from scripts.check_language_support import validate_language_support
except ModuleNotFoundError:
    from check_language_support import validate_language_support  # type: ignore[no-redef]


def check_file_map_schema(root: str | Path = ".") -> dict:
    result = validate_language_support(root)
    errors = list(result.errors)
    warnings = list(result.warnings)
    for code, file_map in sorted(result.file_maps.items()):
        if file_map.get("schema_version") != 1:
            errors.append(f"{code}: schema_version must be 1")
        for required in ["language", "language_name", "docs_directory", "agents_filename", "translation_review_status", "files"]:
            if required not in file_map:
                errors.append(f"{code}: missing {required}")
    return {"name": "check_file_map_schema", "status": "PASS" if not errors else "FAIL", "warnings": warnings, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate file-map schema.")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    result = check_file_map_schema(args.root)
    print(json.dumps(result, indent=2))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
