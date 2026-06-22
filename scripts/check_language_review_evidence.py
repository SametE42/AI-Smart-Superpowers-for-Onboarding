#!/usr/bin/env python3
"""Validate evidence files for languages marked as reviewed."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

try:
    from scripts.check_language_support import parse_file_map, parse_language_support
except ModuleNotFoundError:
    from check_language_support import parse_file_map, parse_language_support  # type: ignore[no-redef]


REQUIRED_EVIDENCE_FIELDS = {
    "schema_version",
    "language",
    "language_name",
    "review_status",
    "review_date",
    "reviewer_role",
    "review_scope",
    "checked_artifacts",
    "notes",
}
LIST_FIELDS = {"review_scope", "checked_artifacts", "notes"}
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value in {"true", "false"}:
        return value == "true"
    if value.isdigit():
        return int(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def _split_key_value(line: str) -> tuple[str, Any]:
    key, value = line.split(":", 1)
    return key.strip(), _parse_scalar(value)


def parse_review_evidence(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {field: [] for field in LIST_FIELDS}
    section: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            if line.endswith(":") and line[:-1] in LIST_FIELDS:
                section = line[:-1]
                continue
            section = None
            if ":" in line:
                key, value = _split_key_value(line)
                data[key] = value
            continue
        if section in LIST_FIELDS and line.strip().startswith("- "):
            data[section].append(line.strip()[2:])
    return data


def validate_language_review_evidence(root: str | Path = ".") -> dict:
    root_path = Path(root)
    support_path = root_path / "i18n" / "language-support.yml"
    errors: list[str] = []
    warnings: list[str] = []
    reviewed_languages = 0
    evidence_files = 0

    if not support_path.exists():
        errors.append("missing i18n/language-support.yml")
        return _result(errors, warnings, reviewed_languages, evidence_files)

    language_support = parse_language_support(support_path)
    for language, info in sorted(language_support.items()):
        support_status = str(info.get("translation_review_status", ""))
        file_map_path = root_path / str(info.get("file_map", ""))
        file_map_status = ""
        if file_map_path.exists():
            file_map = parse_file_map(file_map_path)
            file_map_status = str(file_map.get("translation_review_status", ""))
        else:
            errors.append(f"{language}: missing file map {info.get('file_map', '')}")

        if file_map_status and support_status != file_map_status:
            errors.append(
                f"{language}: review status mismatch between language-support ({support_status}) "
                f"and file map ({file_map_status})"
            )

        if support_status != "reviewed":
            continue

        reviewed_languages += 1
        evidence_path = root_path / "i18n" / f"review-evidence.{language}.yml"
        if not evidence_path.exists():
            errors.append(f"{language}: missing review evidence file {evidence_path.relative_to(root_path).as_posix()}")
            continue

        evidence_files += 1
        evidence = parse_review_evidence(evidence_path)
        missing = sorted(REQUIRED_EVIDENCE_FIELDS - set(evidence))
        if missing:
            errors.append(f"{language}: review evidence missing fields: {', '.join(missing)}")
            continue
        if evidence["schema_version"] != 1:
            errors.append(f"{language}: review evidence schema_version must be 1")
        if evidence["language"] != language:
            errors.append(f"{language}: review evidence language mismatch: {evidence['language']}")
        if evidence["review_status"] != "reviewed":
            errors.append(f"{language}: review evidence review_status must be reviewed")
        if not DATE_PATTERN.fullmatch(str(evidence["review_date"])):
            errors.append(f"{language}: review_date must use YYYY-MM-DD")
        for field in sorted(LIST_FIELDS):
            if not evidence.get(field):
                errors.append(f"{language}: review evidence {field} must not be empty")
        for artifact in evidence.get("checked_artifacts", []):
            artifact_path = root_path / str(artifact)
            if not artifact_path.exists():
                errors.append(f"{language}: checked artifact does not exist: {artifact}")

    orphaned = sorted((root_path / "i18n").glob("review-evidence.*.yml")) if (root_path / "i18n").exists() else []
    for path in orphaned:
        if path.name == "review-evidence.schema.yml":
            continue
        language = path.name.removeprefix("review-evidence.").removesuffix(".yml")
        if language not in language_support:
            warnings.append(f"orphaned review evidence file: {path.relative_to(root_path).as_posix()}")

    return _result(errors, warnings, reviewed_languages, evidence_files)


def _result(errors: list[str], warnings: list[str], reviewed_languages: int, evidence_files: int) -> dict:
    return {
        "name": "check_language_review_evidence",
        "status": "PASS" if not errors else "FAIL",
        "summary": {
            "reviewed_languages": reviewed_languages,
            "evidence_files": evidence_files,
        },
        "warnings": warnings,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate review evidence for reviewed language metadata.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--json", default=None, help="Optional JSON report path.")
    args = parser.parse_args()

    result = validate_language_review_evidence(args.root)
    output = json.dumps(result, indent=2)
    print(output)
    if args.json:
        Path(args.json).write_text(output + "\n", encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
