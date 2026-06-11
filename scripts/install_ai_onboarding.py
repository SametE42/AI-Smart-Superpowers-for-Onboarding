#!/usr/bin/env python3
"""Install AI onboarding files into a target repository."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

try:
    from scripts.check_language_support import (
        REQUIRED_FILES,
        parse_file_map,
        parse_language_support,
    )
except ModuleNotFoundError:
    from check_language_support import (  # type: ignore[no-redef]
        REQUIRED_FILES,
        parse_file_map,
        parse_language_support,
    )


MODES = {
    "minimal": [
        "CONTEXT_INDEX.md",
        "MASTER_SYSTEM.md",
        "ARCHITECTURE.md",
        "BUILD_AND_TEST.md",
        "PROJECT_MEMORY.md",
        "SECURITY_RULES.md",
        "REVIEW_CHECKLIST.md",
    ],
    "standard": [
        "CONTEXT_INDEX.md",
        "MASTER_SYSTEM.md",
        "ONBOARDING.md",
        "ARCHITECTURE.md",
        "TECH_STACK.md",
        "BUILD_AND_TEST.md",
        "DEPENDENCIES.md",
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
    ],
    "enterprise": list(REQUIRED_FILES),
}

SUPPORTED_STACKS = {
    "generic",
    "python",
    "javascript",
    "typescript",
    "java",
    "csharp",
    "go",
    "rust",
    "php",
    "ruby",
    "kotlin",
    "swift",
    "cpp",
    "frontend",
    "backend",
    "fullstack",
    "iac",
    "docs",
}


@dataclass
class StackHint:
    stack: str = "generic"
    evidence: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


@dataclass
class PlannedFile:
    source_name: str
    path: Path
    content: str
    language: str
    structure: str
    stack: str


@dataclass
class InstallAction:
    path: Path
    action: str
    language: str
    structure: str
    stack: str


@dataclass
class InstallResult:
    actions: list[InstallAction] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    language: str = ""
    structure: str = ""
    stack: str = "generic"
    mode: str = "standard"

    @property
    def ok(self) -> bool:
        return not self.errors


def load_language_support(root: str | Path) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    """Load the language matrix and all referenced file maps."""
    root_path = Path(root)
    support = parse_language_support(root_path / "i18n" / "language-support.yml")
    file_maps: dict[str, dict[str, Any]] = {}
    for code, info in support.items():
        file_maps[code] = parse_file_map(root_path / str(info["file_map"]))
    return support, file_maps


def detect_stack(target: str | Path) -> StackHint:
    """Return a conservative stack hint from repository files."""
    target_path = Path(target)
    signals: list[tuple[str, str]] = []

    checks = [
        ("tsconfig.json", "typescript"),
        ("package.json", "javascript"),
        ("pyproject.toml", "python"),
        ("requirements.txt", "python"),
        ("setup.py", "python"),
        ("pom.xml", "java"),
        ("build.gradle", "java"),
        ("go.mod", "go"),
        ("Cargo.toml", "rust"),
        ("composer.json", "php"),
        ("Gemfile", "ruby"),
        ("Package.swift", "swift"),
        ("CMakeLists.txt", "cpp"),
        ("Makefile", "cpp"),
    ]
    for filename, stack in checks:
        if (target_path / filename).exists():
            signals.append((filename, stack))

    for child in target_path.glob("*.csproj"):
        signals.append((child.name, "csharp"))
    for child in target_path.glob("*.sln"):
        signals.append((child.name, "csharp"))
    for child in target_path.glob("*.tf"):
        signals.append((child.name, "iac"))
    if (target_path / "terraform").is_dir():
        signals.append(("terraform/", "iac"))

    if not signals:
        return StackHint(stack="generic", notes=["No supported stack files detected."])

    evidence = [name for name, _stack in signals]
    stacks = {stack for _name, stack in signals}
    if "typescript" in stacks:
        return StackHint(stack="typescript", evidence=evidence, notes=["TypeScript is a hint from tsconfig.json."])
    if "kotlin" in stacks:
        return StackHint(stack="kotlin", evidence=evidence, notes=["Kotlin is a hint from Gradle metadata."])
    if len(stacks) == 1:
        stack = next(iter(stacks))
        return StackHint(stack=stack, evidence=evidence, notes=[f"{stack} is a file-based hint, not a certainty."])
    return StackHint(
        stack="generic",
        evidence=evidence,
        notes=["Multiple stack hints were found; treat this as ambiguous until reviewed."],
    )


def _language_notice(language: str, info: dict[str, Any], structure: str, stack_hint: StackHint) -> str:
    language_name = info["name"]
    review_status = info["translation_review_status"]
    evidence = ", ".join(stack_hint.evidence) if stack_hint.evidence else "[none]"
    if language == "de":
        note = (
            "Hinweis: Dieser Inhalt ist ein strukturierter deutschsprachiger Ziel-Platzhalter, "
            "wenn keine menschlich gepruefte Uebersetzung vorhanden ist."
        )
    elif language == "en":
        note = "Note: English is the canonical reference language."
    else:
        note = (
            f"Note: This is a structured localized placeholder for {language_name}; "
            "replace bracketed fields with reviewed language-specific repository evidence."
        )
    return "\n".join(
        [
            f"> Selected language: {language}",
            f"> Language name: {language_name}",
            f"> Structure mode: {structure}",
            f"> Stack hint: {stack_hint.stack}",
            f"> Evidence source: {evidence}",
            f"> Translation review status: {review_status}",
            f"> {note}",
            "",
        ]
    )


def _read_template(root: Path, filename: str) -> str:
    path = root / "templates" / "docs-ai" / filename
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"# {filename}\n\n[UNKNOWN]\n"


def _render_doc(root: Path, filename: str, language: str, info: dict[str, Any], structure: str, stack_hint: StackHint) -> str:
    body = _read_template(root, filename).rstrip()
    rendered = _language_notice(language, info, structure, stack_hint) + body + "\n"
    if filename == "EVIDENCE_MAP.md":
        evidence = ", ".join(stack_hint.evidence) if stack_hint.evidence else "[none]"
        rendered += "\n## Generated stack hint\n\n"
        rendered += "| Claim | Evidence source | Confidence | Notes |\n"
        rendered += "|---|---|---|---|\n"
        rendered += (
            f"| Stack hint: {stack_hint.stack} | Evidence source: {evidence} | "
            "Medium | File-based hint only; verify before relying on it. |\n"
        )
    return rendered


def _render_agents(root: Path, language: str, info: dict[str, Any], structure: str, docs_directory: str, stack_hint: StackHint) -> str:
    template = (root / "templates" / "AGENTS.md").read_text(encoding="utf-8").rstrip()
    return "\n".join(
        [
            f"> Selected language: {language}",
            f"> Language name: {info['name']}",
            f"> Structure mode: {structure}",
            f"> Stack hint: {stack_hint.stack}",
            f"> Translation review status: {info['translation_review_status']}",
            f"> Docs directory: {docs_directory}",
            "",
            template.replace("docs/ai/", f"{docs_directory.rstrip('/')}/"),
            "",
        ]
    )


def _render_manifest(
    result: InstallResult,
    info: dict[str, Any],
    docs_directory: str,
    file_map: dict[str, Any],
    stack_hint: StackHint,
) -> str:
    lines = [
        "schema_version: 1",
        "framework: AI Smart Superpowers for Onboarding",
        f"generated_at: {datetime.now(UTC).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}",
        f"mode: {result.mode}",
        f"language: {result.language}",
        f"language_name: {info['name']}",
        f"structure: {result.structure}",
        f"docs_directory: {docs_directory}",
        "agents_filename: AGENTS.md",
        f"translation_review_status: {info['translation_review_status']}",
        f"stack_hint: {stack_hint.stack}",
        "stack_evidence:",
    ]
    if stack_hint.evidence:
        lines.extend(f"  - {item}" for item in stack_hint.evidence)
    else:
        lines.append("  - none")
    lines.extend(
        [
            f"file_map_language: {file_map['language']}",
            "files:",
        ]
    )
    for action in result.actions:
        lines.append(f"  - path: {action.path.as_posix()}")
        lines.append(f"    action: {action.action}")
    return "\n".join(lines) + "\n"


def _target_docs_directory(structure: str, file_map: dict[str, Any]) -> str:
    if structure == "canonical":
        return "docs/ai"
    return str(file_map["docs_directory"])


def _target_filename(filename: str, structure: str, file_map: dict[str, Any], no_localized_filenames: bool) -> str:
    if structure == "localized" and not no_localized_filenames:
        return str(file_map["files"][filename])
    return filename


def _manifest_name(language: str, structure: str) -> str:
    if structure == "localized" and language == "de":
        return "KI_ONBOARDING_MANIFEST.yml"
    return "AI_ONBOARDING_MANIFEST.yml"


def _plan_files(
    root: Path,
    target: Path,
    mode: str,
    language: str,
    structure: str,
    stack_hint: StackHint,
    manifest: bool,
    no_localized_filenames: bool,
    info: dict[str, Any],
    file_map: dict[str, Any],
) -> list[PlannedFile]:
    docs_directory = _target_docs_directory(structure, file_map)
    planned = [
        PlannedFile(
            source_name="AGENTS.md",
            path=target / "AGENTS.md",
            content=_render_agents(root, language, info, structure, docs_directory, stack_hint),
            language=language,
            structure=structure,
            stack=stack_hint.stack,
        )
    ]
    for filename in MODES[mode]:
        target_name = _target_filename(filename, structure, file_map, no_localized_filenames)
        planned.append(
            PlannedFile(
                source_name=filename,
                path=target / docs_directory / target_name,
                content=_render_doc(root, filename, language, info, structure, stack_hint),
                language=language,
                structure=structure,
                stack=stack_hint.stack,
            )
        )
    if manifest:
        placeholder_result = InstallResult(language=language, structure=structure, stack=stack_hint.stack, mode=mode)
        manifest_path = target / docs_directory / _manifest_name(language, structure)
        planned.append(
            PlannedFile(
                source_name=manifest_path.name,
                path=manifest_path,
                content="",
                language=language,
                structure=structure,
                stack=stack_hint.stack,
            )
        )
        for item in planned:
            action = "create" if not item.path.exists() else "overwrite"
            placeholder_result.actions.append(InstallAction(item.path, action, language, structure, stack_hint.stack))
        planned[-1].content = _render_manifest(placeholder_result, info, docs_directory, file_map, stack_hint)
    return planned


def install_ai_onboarding(
    *,
    root: str | Path = ".",
    target: str | Path = ".",
    mode: str = "standard",
    language: str = "en",
    structure: str = "canonical",
    stack: str = "generic",
    detect_stack_flag: bool = False,
    dry_run: bool = False,
    force: bool = False,
    interactive: bool = False,
    backup_existing: bool = False,
    manifest: bool = False,
    no_localized_filenames: bool = False,
) -> InstallResult:
    root_path = Path(root)
    target_path = Path(target)
    result = InstallResult(language=language, structure=structure, stack=stack, mode=mode)
    support, file_maps = load_language_support(root_path)

    if mode not in MODES:
        result.errors.append(f"Unsupported mode: {mode}")
    if language not in support:
        result.errors.append(f"Unsupported language: {language}")
    if structure not in {"canonical", "localized"}:
        result.errors.append(f"Unsupported structure: {structure}")
    if stack not in SUPPORTED_STACKS:
        result.errors.append(f"Unsupported stack: {stack}")
    if result.errors:
        return result

    info = support[language]
    file_map = file_maps[language]
    if structure == "canonical" and info.get("canonical_structure") is not True:
        result.errors.append(f"Language does not support canonical structure: {language}")
    if structure == "localized" and info.get("localized_structure") is not True:
        result.errors.append(f"Language does not support localized structure: {language}")
    if result.errors:
        return result

    stack_hint = detect_stack(target_path) if detect_stack_flag else StackHint(stack=stack)
    result.stack = stack_hint.stack

    if interactive:
        answer = input(f"Install {mode} onboarding files into {target_path}? [y/N] ").strip().lower()
        if answer not in {"y", "yes"}:
            result.errors.append("Installation cancelled by user.")
            return result

    should_manifest = manifest or mode in {"standard", "enterprise"}
    planned = _plan_files(
        root_path,
        target_path,
        mode,
        language,
        structure,
        stack_hint,
        should_manifest,
        no_localized_filenames,
        info,
        file_map,
    )

    conflicts = [item.path for item in planned if item.path.exists() and not force and not dry_run]
    if conflicts:
        for path in conflicts:
            result.errors.append(f"Refusing to overwrite existing file without --force: {path}")
        return result

    timestamp = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    for item in planned:
        action = "create"
        if item.path.exists():
            action = "overwrite"
            if backup_existing and not dry_run:
                backup_path = item.path.with_name(f"{item.path.name}.bak-{timestamp}")
                backup_path.write_text(item.path.read_text(encoding="utf-8"), encoding="utf-8")
                result.actions.append(InstallAction(backup_path, "backup", language, structure, stack_hint.stack))
        if dry_run:
            action = "would overwrite" if item.path.exists() else "would create"
        else:
            item.path.parent.mkdir(parents=True, exist_ok=True)
            item.path.write_text(item.content, encoding="utf-8")
        result.actions.append(InstallAction(item.path, action, language, structure, stack_hint.stack))
    return result


def print_language_table(root: str | Path) -> None:
    support, _file_maps = load_language_support(root)
    print("| Sprachcode | Sprachname | Output support | Translation review status | Docs directory |")
    print("|---|---|---|---|---|")
    for code, info in sorted(support.items()):
        print(
            f"| {code} | {info['name']} | {info['output_support']} | "
            f"{info['translation_review_status']} | {info['docs_directory']} |"
        )


def print_summary(result: InstallResult, target: Path) -> None:
    if result.errors:
        print("Errors:")
        for error in result.errors:
            print(f"- {error}")
        return
    print("| Datei | Aktion | Sprache | Strukturmodus | Stack |")
    print("|---|---|---|---|---|")
    for action in result.actions:
        try:
            display_path = action.path.relative_to(target)
        except ValueError:
            display_path = action.path
        print(f"| {display_path.as_posix()} | {action.action} | {action.language} | {action.structure} | {action.stack} |")


def _interactive_defaults(args: argparse.Namespace) -> argparse.Namespace:
    if not args.interactive:
        return args
    language = input(f"Language [{args.language}]: ").strip()
    if language:
        args.language = language
    structure = input(f"Structure canonical/localized [{args.structure}]: ").strip()
    if structure:
        args.structure = structure
    mode = input(f"Mode minimal/standard/enterprise [{args.mode}]: ").strip()
    if mode:
        args.mode = mode
    return args


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Install AI onboarding files into a target repository.")
    parser.add_argument("--root", default=".", help="Framework repository root.")
    parser.add_argument("--mode", default="standard", help="minimal, standard or enterprise.")
    parser.add_argument("--language", default="en", help="Supported language code.")
    parser.add_argument("--structure", default="canonical", help="canonical or localized.")
    parser.add_argument("--target", default=".", help="Target repository path.")
    parser.add_argument("--stack", default="generic", help="Stack hint.")
    parser.add_argument("--detect-stack", action="store_true", help="Detect stack hints from target files.")
    parser.add_argument("--list-languages", action="store_true", help="List all supported output languages.")
    parser.add_argument("--dry-run", action="store_true", help="Show planned files without writing them.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--interactive", action="store_true", help="Ask before installing.")
    parser.add_argument("--backup-existing", action="store_true", help="Create .bak timestamp files before overwrites.")
    parser.add_argument("--manifest", action="store_true", help="Generate an output manifest.")
    parser.add_argument("--no-localized-filenames", action="store_true", help="Use localized docs directory with canonical filenames.")
    args = parser.parse_args(argv)

    if args.list_languages:
        print_language_table(args.root)
        return 0

    args = _interactive_defaults(args)
    result = install_ai_onboarding(
        root=args.root,
        target=args.target,
        mode=args.mode,
        language=args.language,
        structure=args.structure,
        stack=args.stack,
        detect_stack_flag=args.detect_stack,
        dry_run=args.dry_run,
        force=args.force,
        interactive=args.interactive,
        backup_existing=args.backup_existing,
        manifest=args.manifest,
        no_localized_filenames=args.no_localized_filenames,
    )
    print_summary(result, Path(args.target))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
