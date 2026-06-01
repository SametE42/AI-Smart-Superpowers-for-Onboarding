#!/usr/bin/env python3
"""Validate repository documentation structure for release readiness."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


LOCAL_MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"AIza[0-9A-Za-z_-]{35}"),
    re.compile(r"BEGIN (?:RSA |DSA |EC |OPENSSH )?PRIVATE KEY"),
]
SOURCE_SCAFFOLD_MARKERS = [
    "This file gives users a structured, practical reference",
    "## Recommended content",
    "English source kept authoritative",
]
AI_TRANSLATION_MARKERS = [
    "<!-- translation-status: ai-translated; ai-quality-pass -->",
]
UNREVIEWED_TRANSLATION_MARKERS = [
    "<!-- translation-status: localized-draft; human-review-required -->",
    "This file mirrors `ai/English/",
    "Translation status: pending review",
    "Translation status: structure prepared",
    "Translation status: localized draft, human review required",
    "Übersetzungsstatus: deutsch lokalisierter Entwurf, menschliches Review erforderlich",
    "Uebersetzungsstatus: deutsch lokalisierter Entwurf, menschliches Review erforderlich",
    "Statut de traduction : brouillon localisé en français, révision humaine requise",
    "Estado de traducción: borrador localizado en español, requiere revisión humana",
    "Çeviri durumu: Türkçe yerelleştirilmiş taslak, insan incelemesi gerekli",
    "حالة الترجمة: مسودة مترجمة إلى العربية، تتطلب مراجعة بشرية",
    "Stato della traduzione: bozza localizzata in italiano, revisione umana richiesta",
    "Status da tradução: rascunho localizado em português, revisão humana necessária",
    "Vertaalstatus: gelokaliseerd concept in het Nederlands, menselijke review vereist",
    "Status tłumaczenia: szkic zlokalizowany po polsku, wymagana weryfikacja człowieka",
]
TRANSLATION_MIRROR_PLACEHOLDER_MARKERS = [
    "This file mirrors `ai/English/",
]
LANGUAGE_README_REQUIRED_SECTIONS = [
    "# AI Agent Operating Manual",
    "## Purpose of this language folder",
    "## English source of truth",
    "## How to use this folder",
    "## Folder overview",
    "## Recommended reading order",
    "## Safety and human review rules",
    "## Localization notes",
    "## Quality checklist",
]
LANGUAGE_README_STANDARD_SUBFOLDERS = [
    "agents/",
    "commands/",
    "context-engineering/",
    "evals/",
    "examples/",
    "memory/",
    "models/",
    "optimization/",
    "prompts/",
    "providers/",
    "safety/",
    "skills/",
    "templates/",
    "tools/",
]
OLD_REPOSITORY_REFERENCE_TEXTS = sorted(
    {
        "".join(parts)
        for parts in (
            ("AI Repo ", "Onboarding Standard"),
            ("Ai-", "Repo-", "Onboarding"),
            ("ai-", "repo-", "onboarding"),
            ("Repo ", "Onboarding Standard"),
            ("repo ", "onboarding standard"),
            ("Repository ", "Onboarding Standard"),
            ("repository ", "onboarding standard"),
            ("SametE42/", "Ai-", "Repo-", "Onboarding"),
            ("https://github.com/", "SametE42/", "Ai-", "Repo-", "Onboarding"),
            ("https://github.com/", "SametE42/", "Ai-", "Repo-", "Onboarding", ".git"),
            ("git@github.com:", "SametE42/", "Ai-", "Repo-", "Onboarding", ".git"),
        )
    },
    key=len,
    reverse=True,
)
OLD_REPOSITORY_REFERENCE_PATTERN = re.compile(
    "|".join(re.escape(reference) for reference in OLD_REPOSITORY_REFERENCE_TEXTS),
    re.IGNORECASE,
)
OLD_REPOSITORY_REFERENCE_REPORTS = {
    "ai/VALIDATION_REPORT.json",
    "ai/VALIDATION_REPORT.md",
}
CHANGELOG_HISTORICAL_REFERENCE_HINTS = (
    "former",
    "historical",
    "legacy",
    "previous",
    "renamed from",
)


@dataclass(frozen=True)
class ValidationReport:
    status: str
    root: str
    summary: dict[str, int | bool]
    details: dict[str, list]

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "root": self.root,
            **self.summary,
            "details": self.details,
        }


def _git_files(root: Path) -> list[Path] | None:
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None

    files = []
    for line in result.stdout.splitlines():
        if line.strip():
            path = Path(line.strip())
            if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
                continue
            files.append(root / path)
    return files


def _repository_name(root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return root.name

    remote_url = result.stdout.strip().removesuffix(".git")
    if not remote_url:
        return root.name

    return remote_url.rstrip("/").rsplit("/", 1)[-1] or root.name


def _filesystem_files(root: Path) -> list[Path]:
    ignored_dirs = {
        ".git",
        ".worktrees",
        "node_modules",
        "dist",
        "build",
        ".next",
        "venv",
        ".venv",
        "__pycache__",
    }
    files: list[Path] = []
    for current_root, dirnames, filenames in os.walk(root):
        dirnames[:] = [dirname for dirname in dirnames if dirname not in ignored_dirs]
        current = Path(current_root)
        files.extend(current / filename for filename in filenames)
    return files


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _relative_sort_key(path: Path, root: Path) -> tuple[str, str]:
    relative = _relative(path, root)
    return relative.casefold(), relative


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.lstrip("\ufeff")
    return ""


def _is_external_or_anchor(target: str) -> bool:
    return bool(re.match(r"^(?:https?:|mailto:|#)", target))


def _normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if " " in target and not target.startswith("<"):
        target = target.split(" ", 1)[0]
    return target.strip("<>")


def _find_broken_local_links(
    markdown_files: Iterable[Path],
    all_files: set[str],
    root: Path,
    text_by_path: dict[Path, str],
) -> list[dict]:
    broken: list[dict] = []
    for markdown_file in markdown_files:
        text = text_by_path[markdown_file]
        base_dir = markdown_file.parent
        for match in LOCAL_MARKDOWN_LINK.finditer(text):
            target = _normalize_link_target(match.group(1))
            if not target or _is_external_or_anchor(target):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (base_dir / target_path).resolve()
            try:
                resolved_relative = resolved.relative_to(root.resolve()).as_posix()
            except ValueError:
                line_number = text.count("\n", 0, match.start()) + 1
                broken.append({"file": _relative(markdown_file, root), "line": line_number, "target": target})
                continue
            if resolved_relative not in all_files and not resolved.exists():
                line_number = text.count("\n", 0, match.start()) + 1
                broken.append({"file": _relative(markdown_file, root), "line": line_number, "target": target})
    return broken


def _find_missing_mirrors(root: Path) -> tuple[list[str], int, int, bool]:
    ai_dir = root / "ai"
    if not ai_dir.exists():
        return [], 0, 0, True

    language_dirs = sorted(path for path in ai_dir.iterdir() if path.is_dir())
    language_names = [path.name for path in language_dirs]
    languages_alphabetically_sorted = language_names == sorted(language_names)

    english_dir = ai_dir / "English"
    if not english_dir.exists():
        return ["ai/English"], len(language_dirs), 0, languages_alphabetically_sorted

    english_markdown_files = sorted(english_dir.rglob("*.md"))
    english_relatives = [path.relative_to(english_dir) for path in english_markdown_files]
    missing: list[str] = []
    for language_dir in language_dirs:
        if language_dir.name == "English":
            continue
        for relative_path in english_relatives:
            candidate = language_dir / relative_path
            if not candidate.exists():
                missing.append(f"{language_dir.name}/{relative_path.as_posix()}")

    return missing, len(language_dirs), len(english_markdown_files), languages_alphabetically_sorted


def _find_directories_without_readme(files: list[Path], root: Path) -> list[str]:
    directories = sorted({path.parent for path in files if path.parent != root})
    missing = []
    for directory in directories:
        if not (directory / "README.md").exists():
            missing.append(_relative(directory, root))
    return missing


def _find_secret_patterns(files: Iterable[Path], root: Path, text_by_path: dict[Path, str]) -> list[dict]:
    hits: list[dict] = []
    for path in files:
        text = text_by_path[path]
        for line_number, line in enumerate(text.splitlines(), start=1):
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                hits.append({"file": _relative(path, root), "line": line_number})
    return hits


def _find_files_with_markers(
    markdown_files: Iterable[Path],
    root: Path,
    markers: Iterable[str],
    text_by_path: dict[Path, str],
) -> list[str]:
    matched_files = []
    for path in sorted(markdown_files, key=lambda item: _relative_sort_key(item, root)):
        text = text_by_path[path]
        if any(marker in text for marker in markers):
            matched_files.append(_relative(path, root))
    return matched_files


def _localized_language_markdown_files(root: Path, markdown_files: Iterable[Path]) -> list[Path]:
    ai_dir = root / "ai"
    if not ai_dir.exists():
        return []

    language_names = {path.name for path in ai_dir.iterdir() if path.is_dir()}
    localized_files: list[Path] = []
    for path in markdown_files:
        relative_parts = path.relative_to(root).parts
        if (
            len(relative_parts) >= 3
            and relative_parts[0] == "ai"
            and relative_parts[1] in language_names
            and relative_parts[1] != "English"
        ):
            localized_files.append(path)
    return localized_files


def _language_readme_files(root: Path) -> list[Path]:
    ai_dir = root / "ai"
    if not ai_dir.exists():
        return []

    return sorted(path / "README.md" for path in ai_dir.iterdir() if path.is_dir() and (path / "README.md").exists())


def _find_language_readme_issues(
    language_readmes: Iterable[Path],
    root: Path,
    text_by_path: dict[Path, str],
) -> tuple[list[dict], list[dict], list[dict]]:
    missing_sections: list[dict] = []
    missing_subfolders: list[dict] = []
    missing_translation_markers: list[dict] = []

    for path in language_readmes:
        text = text_by_path[path]
        relative = _relative(path, root)
        language = path.parent.name
        section_gaps = [section for section in LANGUAGE_README_REQUIRED_SECTIONS if section not in text]
        subfolder_gaps = [subfolder for subfolder in LANGUAGE_README_STANDARD_SUBFOLDERS if subfolder not in text]
        if section_gaps:
            missing_sections.append({"file": relative, "missing_sections": section_gaps})
        if subfolder_gaps:
            missing_subfolders.append({"file": relative, "missing_subfolders": subfolder_gaps})
        if language != "English" and AI_TRANSLATION_MARKERS[0] not in text:
            missing_translation_markers.append({"file": relative})

    return missing_sections, missing_subfolders, missing_translation_markers


def _is_allowed_historical_old_repository_reference(relative_path: str, line: str) -> bool:
    if relative_path != "CHANGELOG.md":
        return False

    normalized = line.casefold()
    return any(hint in normalized for hint in CHANGELOG_HISTORICAL_REFERENCE_HINTS)


def _find_old_repository_reference_hits(
    files: Iterable[Path],
    root: Path,
    text_by_path: dict[Path, str],
) -> list[dict]:
    hits: list[dict] = []
    for path in files:
        relative = _relative(path, root)
        if relative in OLD_REPOSITORY_REFERENCE_REPORTS:
            continue

        text = text_by_path[path]
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in OLD_REPOSITORY_REFERENCE_PATTERN.finditer(line):
                if _is_allowed_historical_old_repository_reference(relative, line):
                    continue
                hits.append({"file": relative, "line": line_number, "match": match.group(0)})
    return hits


def validate_repository(root: str | Path = ".") -> ValidationReport:
    root_path = Path(root).resolve()
    files = _git_files(root_path) or _filesystem_files(root_path)
    files = sorted((path for path in files if path.exists() and path.is_file()), key=lambda item: _relative_sort_key(item, root_path))
    all_file_relatives = {_relative(path, root_path) for path in files}
    text_by_path = {path: _read_text(path) for path in files}
    markdown_files = [path for path in files if path.suffix.lower() == ".md"]

    missing_h1 = [
        _relative(path, root_path)
        for path in markdown_files
        if not _first_non_empty_line(text_by_path[path]).startswith("# ")
    ]
    empty_files = [_relative(path, root_path) for path in files if path.stat().st_size == 0]
    broken_links = _find_broken_local_links(markdown_files, all_file_relatives, root_path, text_by_path)
    missing_mirrors, language_count, english_count, languages_sorted = _find_missing_mirrors(root_path)
    directories_without_readme = _find_directories_without_readme(files, root_path)
    secret_hits = _find_secret_patterns(files, root_path, text_by_path)
    old_repository_reference_hits = _find_old_repository_reference_hits(files, root_path, text_by_path)
    english_markdown_files = [path for path in markdown_files if _relative(path, root_path).startswith("ai/English/")]
    localized_markdown_files = _localized_language_markdown_files(root_path, markdown_files)
    language_readmes = _language_readme_files(root_path)
    english_scaffold_files = _find_files_with_markers(
        english_markdown_files,
        root_path,
        SOURCE_SCAFFOLD_MARKERS,
        text_by_path,
    )
    ai_translated_files = _find_files_with_markers(
        localized_markdown_files,
        root_path,
        AI_TRANSLATION_MARKERS,
        text_by_path,
    )
    unreviewed_translation_files = _find_files_with_markers(
        localized_markdown_files,
        root_path,
        UNREVIEWED_TRANSLATION_MARKERS,
        text_by_path,
    )
    translation_mirror_placeholder_files = _find_files_with_markers(
        localized_markdown_files,
        root_path,
        TRANSLATION_MIRROR_PLACEHOLDER_MARKERS,
        text_by_path,
    )
    ai_translated_file_set = set(ai_translated_files)
    missing_ai_translation_marker_files = [
        _relative(path, root_path)
        for path in localized_markdown_files
        if _relative(path, root_path) not in ai_translated_file_set
    ]
    (
        language_readmes_missing_required_sections,
        language_readmes_missing_standard_subfolders,
        language_readmes_missing_translation_markers,
    ) = _find_language_readme_issues(language_readmes, root_path, text_by_path)
    incomplete_language_readmes = sorted(
        {
            item["file"]
            for item in (
                language_readmes_missing_required_sections
                + language_readmes_missing_standard_subfolders
                + language_readmes_missing_translation_markers
            )
        }
    )
    legacy_ai_links = [
        item
        for item in broken_links
        if str(item.get("target", "")).startswith("i18n/")
    ]

    summary: dict[str, int | bool] = {
        "total_files": len(files),
        "markdown_files": len(markdown_files),
        "language_folders": language_count,
        "languages_alphabetically_sorted": languages_sorted,
        "english_source_markdown_files": english_count,
        "missing_mirrored_ai_files": len(missing_mirrors),
        "broken_local_markdown_links": len(broken_links),
        "markdown_files_without_h1": len(missing_h1),
        "empty_files": len(empty_files),
        "directories_without_readme": len(directories_without_readme),
        "legacy_ai_links": len(legacy_ai_links),
        "secret_pattern_hits": len(secret_hits),
        "old_repository_reference_hits": len(old_repository_reference_hits),
        "english_source_scaffold_files": len(english_scaffold_files),
        "ai_translated_files": len(ai_translated_files),
        "missing_ai_translation_marker_files": len(missing_ai_translation_marker_files),
        "unreviewed_translation_files": len(unreviewed_translation_files),
        "translation_mirror_placeholder_files": len(translation_mirror_placeholder_files),
        "scaffold_or_unreviewed_translation_files": len(english_scaffold_files) + len(unreviewed_translation_files),
        "incomplete_language_readmes": len(incomplete_language_readmes),
        "language_readmes_missing_required_sections": len(language_readmes_missing_required_sections),
        "language_readmes_missing_standard_subfolders": len(language_readmes_missing_standard_subfolders),
    }
    details = {
        "missing_mirrors": missing_mirrors,
        "broken_links": broken_links,
        "missing_h1": missing_h1,
        "empty_files": empty_files,
        "dirs_without_readme": directories_without_readme,
        "legacy_links": legacy_ai_links,
        "secret_pattern_hits": secret_hits,
        "old_repository_reference_hits": old_repository_reference_hits[:200],
        "english_source_scaffold_files_sample": english_scaffold_files[:200],
        "ai_translated_files_sample": ai_translated_files[:200],
        "missing_ai_translation_marker_files_sample": missing_ai_translation_marker_files[:200],
        "unreviewed_translation_files_sample": unreviewed_translation_files[:200],
        "translation_mirror_placeholder_files_sample": translation_mirror_placeholder_files[:200],
        "incomplete_language_readmes": incomplete_language_readmes[:200],
        "language_readmes_missing_required_sections": language_readmes_missing_required_sections[:200],
        "language_readmes_missing_standard_subfolders": language_readmes_missing_standard_subfolders[:200],
        "language_readmes_missing_translation_marker": language_readmes_missing_translation_markers[:200],
    }
    blocking_keys = [
        "missing_mirrored_ai_files",
        "broken_local_markdown_links",
        "markdown_files_without_h1",
        "empty_files",
        "directories_without_readme",
        "legacy_ai_links",
        "secret_pattern_hits",
        "old_repository_reference_hits",
        "missing_ai_translation_marker_files",
        "unreviewed_translation_files",
        "incomplete_language_readmes",
        "language_readmes_missing_required_sections",
        "language_readmes_missing_standard_subfolders",
    ]
    status = "PASS" if all(summary[key] == 0 for key in blocking_keys) else "FAIL"
    return ValidationReport(status=status, root=_repository_name(root_path), summary=summary, details=details)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate release-readiness invariants for this repository.")
    parser.add_argument("--root", default=".", help="Repository root to validate.")
    parser.add_argument("--json", default=None, help="Optional path for JSON report output.")
    parser.add_argument("--markdown", default=None, help="Optional path for Markdown summary output.")
    parser.add_argument("--full", action="store_true", help="Print the full JSON report to stdout.")
    args = parser.parse_args()

    report = validate_repository(args.root)
    report_data = report.to_dict()
    json_text = json.dumps(report_data, ensure_ascii=False, indent=2) + "\n"
    if args.full:
        print(json_text, end="")
    else:
        print(json.dumps({"status": report.status, **report.summary}, ensure_ascii=False, indent=2))

    if args.json:
        Path(args.json).write_text(json_text, encoding="utf-8")

    if args.markdown:
        lines = [
            "# Validation Report",
            "",
            f"Status: **{report.status}**",
            "",
            "## Summary",
            "",
        ]
        for key, value in report.summary.items():
            lines.append(f"- {key}: {value}")
        lines.extend(["", "## Details", ""])
        for key, value in report.details.items():
            lines.append(f"- {key}: {len(value)}")
        Path(args.markdown).write_text("\n".join(lines) + "\n", encoding="utf-8")

    return 0 if report.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
