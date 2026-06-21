#!/usr/bin/env python3
"""Load and validate the standard docs contract."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path


EXPECTED_MODE_COUNTS = {
    "minimal": 7,
    "standard": 17,
    "enterprise": 21,
}


@dataclass(frozen=True)
class StandardDocsContract:
    schema_version: int
    conceptual_core: list[str]
    modes: dict[str, list[str]]
    descriptions: dict[str, str] = field(default_factory=dict)


def _contract_path(root_or_path: str | Path) -> Path:
    path = Path(root_or_path)
    if path.is_file():
        return path
    return path / "config" / "standard-docs.yml"


def _parse_scalar(value: str) -> str | int:
    value = value.strip()
    if value.isdigit():
        return int(value)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


def load_standard_docs_contract(root_or_path: str | Path = ".") -> StandardDocsContract:
    """Load config/standard-docs.yml without requiring a YAML dependency."""
    path = _contract_path(root_or_path)
    schema_version: int | None = None
    conceptual_core: list[str] = []
    modes: dict[str, list[str]] = {}
    descriptions: dict[str, str] = {}
    section: str | None = None
    active_mode: str | None = None
    active_list: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not line.startswith(" "):
            active_mode = None
            active_list = None
            if stripped == "conceptual_core:":
                section = "conceptual_core"
                continue
            if stripped == "modes:":
                section = "modes"
                continue
            section = None
            if ":" in stripped:
                key, value = stripped.split(":", 1)
                if key == "schema_version":
                    parsed = _parse_scalar(value)
                    if isinstance(parsed, int):
                        schema_version = parsed
            continue
        if section == "conceptual_core":
            if line.startswith("  description:"):
                _key, value = stripped.split(":", 1)
                descriptions["conceptual_core"] = str(_parse_scalar(value))
                continue
            if stripped == "files:":
                active_list = "conceptual_core"
                continue
            if active_list == "conceptual_core" and stripped.startswith("- "):
                conceptual_core.append(stripped[2:].strip())
            continue
        if section == "modes":
            if line.startswith("  ") and not line.startswith("    ") and stripped.endswith(":"):
                active_mode = stripped[:-1]
                modes[active_mode] = []
                active_list = None
                continue
            if active_mode and line.startswith("    description:"):
                _key, value = stripped.split(":", 1)
                descriptions[active_mode] = str(_parse_scalar(value))
                continue
            if active_mode and stripped == "docs:":
                active_list = active_mode
                continue
            if active_mode and active_list == active_mode and stripped.startswith("- "):
                modes[active_mode].append(stripped[2:].strip())

    if schema_version is None:
        raise ValueError(f"{path}: missing schema_version")
    return StandardDocsContract(
        schema_version=schema_version,
        conceptual_core=conceptual_core,
        modes=modes,
        descriptions=descriptions,
    )


def mode_docs(root_or_path: str | Path = ".") -> dict[str, list[str]]:
    """Return a copy of the installer mode document lists."""
    contract = load_standard_docs_contract(root_or_path)
    return {mode: list(files) for mode, files in contract.modes.items()}


def enterprise_docs(root_or_path: str | Path = ".") -> list[str]:
    """Return the enterprise document list used by language file maps."""
    return list(load_standard_docs_contract(root_or_path).modes["enterprise"])


def _duplicate_items(items: list[str]) -> list[str]:
    return sorted({item for item in items if items.count(item) > 1})


def validate_standard_docs_contract(root_or_path: str | Path = ".") -> list[str]:
    """Return validation errors for the docs contract and referenced templates."""
    root = Path(root_or_path)
    path = _contract_path(root)
    errors: list[str] = []
    if not path.exists():
        return [f"missing {path.as_posix()}"]
    try:
        contract = load_standard_docs_contract(path)
    except Exception as exc:  # pragma: no cover - defensive CLI path
        return [str(exc)]

    if contract.schema_version != 1:
        errors.append("schema_version must be 1")
    if len(contract.conceptual_core) != 10:
        errors.append("conceptual_core must contain exactly 10 files")
    if list(contract.modes) != ["minimal", "standard", "enterprise"]:
        errors.append("modes must be ordered as minimal, standard, enterprise")
    for mode, expected_count in EXPECTED_MODE_COUNTS.items():
        files = contract.modes.get(mode)
        if files is None:
            errors.append(f"missing mode: {mode}")
            continue
        if len(files) != expected_count:
            errors.append(f"{mode} must contain exactly {expected_count} docs")
        duplicates = _duplicate_items(files)
        if duplicates:
            errors.append(f"{mode} contains duplicate docs: {', '.join(duplicates)}")

    minimal = set(contract.modes.get("minimal", []))
    standard = set(contract.modes.get("standard", []))
    enterprise = set(contract.modes.get("enterprise", []))
    if not minimal.issubset(standard):
        errors.append("minimal docs must be a subset of standard docs")
    if not standard.issubset(enterprise):
        errors.append("standard docs must be a subset of enterprise docs")

    docs_root = root / "templates" / "docs-ai"
    for filename in sorted(set(contract.conceptual_core) | set().union(*[set(v) for v in contract.modes.values()])):
        if not (docs_root / filename).exists():
            errors.append(f"missing docs template: templates/docs-ai/{filename}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate config/standard-docs.yml.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--json", default=None, help="Optional JSON report path.")
    args = parser.parse_args(argv)

    errors = validate_standard_docs_contract(args.root)
    contract = load_standard_docs_contract(args.root) if not errors else None
    data = {
        "status": "PASS" if not errors else "FAIL",
        "conceptual_core_files": len(contract.conceptual_core) if contract else 0,
        "modes": {mode: len(files) for mode, files in contract.modes.items()} if contract else {},
        "errors": errors,
    }
    output = json.dumps(data, ensure_ascii=False, indent=2)
    print(output)
    if args.json:
        Path(args.json).write_text(output + "\n", encoding="utf-8")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
