#!/usr/bin/env python3
"""Validate stack-context coverage in modes, templates and file maps."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from scripts.check_language_support import validate_language_support
    from scripts.install_ai_onboarding import MODES
except ModuleNotFoundError:
    from check_language_support import validate_language_support  # type: ignore[no-redef]
    from install_ai_onboarding import MODES  # type: ignore[no-redef]


def check_stack_context(root: str | Path = ".") -> dict:
    root_path = Path(root)
    errors: list[str] = []
    warnings: list[str] = []

    expected_mode_files = {
        "minimal": {"BUILD_AND_TEST.md"},
        "standard": {"TECH_STACK.md", "BUILD_AND_TEST.md", "DEPENDENCIES.md"},
        "enterprise": {"TECH_STACK.md", "BUILD_AND_TEST.md", "DEPENDENCIES.md", "RUNTIME_ENVIRONMENT.md"},
    }
    for mode, files in expected_mode_files.items():
        missing = sorted(files - set(MODES.get(mode, [])))
        if missing:
            errors.append(f"{mode}: missing stack context files: {', '.join(missing)}")

    for filename in ["TECH_STACK.md", "BUILD_AND_TEST.md", "DEPENDENCIES.md", "RUNTIME_ENVIRONMENT.md"]:
        if not (root_path / "templates" / "docs-ai" / filename).exists():
            errors.append(f"missing template: {filename}")

    language_result = validate_language_support(root_path)
    errors.extend(language_result.errors)
    for code, file_map in sorted(language_result.file_maps.items()):
        files = file_map.get("files", {})
        for filename in ["TECH_STACK.md", "BUILD_AND_TEST.md", "DEPENDENCIES.md", "RUNTIME_ENVIRONMENT.md"]:
            if filename not in files:
                errors.append(f"{code}: missing localized stack mapping for {filename}")

    evidence_text = (root_path / "templates" / "docs-ai" / "EVIDENCE_MAP.md").read_text(encoding="utf-8", errors="replace")
    if "Stack detection must be recorded here before it is treated as context." not in evidence_text:
        errors.append("EVIDENCE_MAP.md does not require stack detection evidence")
    if "Project appears to use" not in evidence_text:
        warnings.append("EVIDENCE_MAP.md should phrase stack claims as evidence-backed hints")

    return {"name": "check_stack_context", "status": "PASS" if not errors else "FAIL", "warnings": warnings, "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate stack-context coverage.")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    result = check_stack_context(args.root)
    print(json.dumps(result, indent=2))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
