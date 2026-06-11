#!/usr/bin/env python3
"""Validate language mappings for canonical and localized output."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from scripts.check_language_support import REQUIRED_FILES, validate_language_support
except ModuleNotFoundError:
    from check_language_support import REQUIRED_FILES, validate_language_support  # type: ignore[no-redef]


def check_localized_output(root: str | Path = ".") -> dict:
    result = validate_language_support(root)
    errors = list(result.errors)
    warnings = list(result.warnings)
    for code, info in sorted(result.language_support.items()):
        if info.get("agents_filename") != "AGENTS.md":
            errors.append(f"{code}: AGENTS.md filename is not preserved")
        if info.get("canonical_structure") is not True:
            errors.append(f"{code}: canonical mode disabled")
        if info.get("localized_structure") is not True:
            errors.append(f"{code}: localized mode disabled")
        file_map = result.file_maps.get(code)
        if not file_map:
            errors.append(f"{code}: missing file map")
            continue
        if file_map.get("docs_directory") != info.get("docs_directory"):
            errors.append(f"{code}: docs_directory mismatch")
        files = file_map.get("files", {})
        missing = sorted(set(REQUIRED_FILES) - set(files))
        if missing:
            errors.append(f"{code}: missing mappings: {', '.join(missing)}")
        targets = list(files.values())
        duplicates = sorted({target for target in targets if targets.count(target) > 1})
        if duplicates:
            errors.append(f"{code}: duplicate localized targets: {', '.join(duplicates)}")
    return {"name": "check_localized_output", "status": "PASS" if not errors else "FAIL", "warnings": warnings, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate localized output mappings.")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    result = check_localized_output(args.root)
    print(json.dumps(result, indent=2))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
