#!/usr/bin/env python3
"""Validate language support metadata and file maps."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REQUIRED_FILES = [
    "CONTEXT_INDEX.md",
    "MASTER_SYSTEM.md",
    "ONBOARDING.md",
    "ARCHITECTURE.md",
    "TECH_STACK.md",
    "BUILD_AND_TEST.md",
    "DEPENDENCIES.md",
    "RUNTIME_ENVIRONMENT.md",
    "EVIDENCE_MAP.md",
    "PROJECT_MEMORY.md",
    "DECISIONS.md",
    "STYLE_GUIDE.md",
    "SECURITY_RULES.md",
    "RISK_REGISTER.md",
    "REVIEW_CHECKLIST.md",
    "ERROR_PATTERNS.md",
    "TASK_SCOPING.md",
    "FRESHNESS.md",
    "AGENT_ROLES.md",
    "SAFETY_BOUNDARIES.md",
    "HUMAN_REVIEW_GATES.md",
]

REQUIRED_LANGUAGE_FIELDS = {
    "name",
    "source_folder",
    "output_support",
    "translation_review_status",
    "canonical_structure",
    "localized_structure",
    "file_map",
    "docs_directory",
    "agents_filename",
}
REQUIRED_FILE_MAP_FIELDS = {
    "schema_version",
    "language",
    "language_name",
    "docs_directory",
    "agents_filename",
    "translation_review_status",
    "files",
}
OUTPUT_SUPPORT_VALUES = {"complete", "incomplete"}
TRANSLATION_REVIEW_VALUES = {"reviewed", "needs_review", "machine_generated", "unknown"}
RESERVED_WINDOWS_NAMES = {
    "CON",
    "PRN",
    "AUX",
    "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}
INVISIBLE_CHARACTERS = re.compile(r"[\u200b-\u200f\u202a-\u202e\u2060-\u206f\ufeff]")


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    summary: dict[str, Any] = field(default_factory=dict)
    language_support: dict[str, dict[str, Any]] = field(default_factory=dict)
    file_maps: dict[str, dict[str, Any]] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": "PASS" if self.ok else "FAIL",
            "summary": self.summary,
            "errors": self.errors,
            "warnings": self.warnings,
        }


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


def parse_language_support(path: Path) -> dict[str, dict[str, Any]]:
    languages: dict[str, dict[str, Any]] = {}
    current_language: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#") or line == "languages:":
            continue
        if line.startswith("  ") and not line.startswith("    ") and line.endswith(":"):
            current_language = line.strip()[:-1]
            languages[current_language] = {}
            continue
        if current_language and line.startswith("    ") and ":" in line:
            key, value = _split_key_value(line.strip())
            languages[current_language][key] = value
    return languages


def parse_file_map(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {"files": {}, "review_notes": []}
    section: str | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            if line in {"files:", "review_notes:"}:
                section = line[:-1]
                continue
            section = None
            if ":" in line:
                key, value = _split_key_value(line)
                data[key] = value
            continue
        if section == "files" and line.startswith("  ") and ":" in line:
            key, value = _split_key_value(line.strip())
            data["files"][key] = value
            continue
        if section == "review_notes" and line.strip().startswith("- "):
            data["review_notes"].append(line.strip()[2:])
    return data


def _detected_language_folders(root: Path) -> set[str]:
    ai_root = root / "ai"
    if not ai_root.exists():
        return set()
    return {path.name for path in ai_root.iterdir() if path.is_dir()}


def _validate_target_filename(filename: str, language: str, errors: list[str]) -> None:
    if not filename:
        errors.append(f"{language}: empty target filename")
        return
    if filename != filename.strip():
        errors.append(f"{language}: target filename has leading or trailing spaces: {filename!r}")
    if "/" in filename or "\\" in filename:
        errors.append(f"{language}: target filename contains a path separator: {filename}")
    if not filename.endswith(".md"):
        errors.append(f"{language}: target filename must end with .md: {filename}")
    stem = filename[:-3].upper()
    if stem in RESERVED_WINDOWS_NAMES:
        errors.append(f"{language}: target filename uses reserved Windows name: {filename}")
    if INVISIBLE_CHARACTERS.search(filename):
        errors.append(f"{language}: target filename contains invisible Unicode: {filename!r}")


def _validate_file_map(language: str, file_map: dict[str, Any], errors: list[str]) -> None:
    missing = sorted(REQUIRED_FILE_MAP_FIELDS - file_map.keys())
    if missing:
        errors.append(f"{language}: file map missing fields: {', '.join(missing)}")
        return
    if file_map["schema_version"] != 1:
        errors.append(f"{language}: schema_version must be 1")
    if file_map["language"] != language:
        errors.append(f"{language}: file map language mismatch: {file_map['language']}")
    if file_map["agents_filename"] != "AGENTS.md":
        errors.append(f"{language}: agents_filename must remain AGENTS.md")
    if file_map["translation_review_status"] not in TRANSLATION_REVIEW_VALUES:
        errors.append(f"{language}: invalid translation_review_status in file map")
    if not str(file_map["docs_directory"]).startswith("docs/"):
        errors.append(f"{language}: docs_directory must start with docs/")

    files = file_map["files"]
    missing_files = sorted(set(REQUIRED_FILES) - set(files))
    extra_files = sorted(set(files) - set(REQUIRED_FILES))
    if missing_files:
        errors.append(f"{language}: file map missing required files: {', '.join(missing_files)}")
    if extra_files:
        errors.append(f"{language}: file map contains unexpected files: {', '.join(extra_files)}")

    targets = list(files.values())
    for target in targets:
        _validate_target_filename(str(target), language, errors)
    duplicates = sorted({target for target in targets if targets.count(target) > 1})
    if duplicates:
        errors.append(f"{language}: duplicate target filenames: {', '.join(duplicates)}")


def validate_language_support(root: str | Path = ".") -> ValidationResult:
    root_path = Path(root)
    result = ValidationResult()
    support_path = root_path / "i18n" / "language-support.yml"
    schema_path = root_path / "i18n" / "file-map.schema.yml"
    glossary_path = root_path / "i18n" / "glossary.yml"
    detected_folders = _detected_language_folders(root_path)

    if not support_path.exists():
        result.errors.append("missing i18n/language-support.yml")
        return result
    if not schema_path.exists():
        result.errors.append("missing i18n/file-map.schema.yml")
    if not glossary_path.exists():
        result.errors.append("missing i18n/glossary.yml")

    language_support = parse_language_support(support_path)
    result.language_support = language_support

    supported_folders = {str(info.get("source_folder", "")) for info in language_support.values()}
    missing_folders = sorted(detected_folders - supported_folders)
    extra_folders = sorted(supported_folders - detected_folders)
    if missing_folders:
        result.errors.append(f"detected language folders missing support entries: {', '.join(missing_folders)}")
    if extra_folders:
        result.errors.append(f"support entries reference missing folders: {', '.join(extra_folders)}")

    complete_languages = 0
    status_counts: dict[str, int] = {}
    for language, info in sorted(language_support.items()):
        missing = sorted(REQUIRED_LANGUAGE_FIELDS - info.keys())
        if missing:
            result.errors.append(f"{language}: language support missing fields: {', '.join(missing)}")
            continue
        if info["output_support"] not in OUTPUT_SUPPORT_VALUES:
            result.errors.append(f"{language}: invalid output_support")
        if info["output_support"] == "complete":
            complete_languages += 1
        if info["translation_review_status"] not in TRANSLATION_REVIEW_VALUES:
            result.errors.append(f"{language}: invalid translation_review_status")
        status_counts[str(info["translation_review_status"])] = status_counts.get(str(info["translation_review_status"]), 0) + 1
        if info["canonical_structure"] is not True:
            result.errors.append(f"{language}: canonical_structure must be true")
        if info["localized_structure"] is not True:
            result.errors.append(f"{language}: localized_structure must be true")
        if info["agents_filename"] != "AGENTS.md":
            result.errors.append(f"{language}: agents_filename must remain AGENTS.md")
        file_map_path = root_path / str(info["file_map"])
        if not file_map_path.exists():
            result.errors.append(f"{language}: missing file map {info['file_map']}")
            continue
        file_map = parse_file_map(file_map_path)
        result.file_maps[language] = file_map
        _validate_file_map(language, file_map, result.errors)

    result.summary = {
        "detected_languages": len(detected_folders),
        "supported_languages": len(language_support),
        "complete_languages": complete_languages,
        "file_maps": len(result.file_maps),
        "translation_review_status": status_counts,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate multilingual language-support metadata and file maps.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--json", default=None, help="Optional JSON report path.")
    parser.add_argument("--full", action="store_true", help="Print full validation details.")
    args = parser.parse_args()

    result = validate_language_support(args.root)
    data = result.to_dict()
    output = data if args.full else {"status": data["status"], **result.summary, "errors": len(result.errors)}
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if args.json:
        Path(args.json).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
