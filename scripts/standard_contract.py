#!/usr/bin/env python3
"""Load the shared AI onboarding document contract."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class StandardContract:
    schema_version: int
    required_files: list[str]
    modes: dict[str, list[str]]
    purposes: dict[str, str]


def _scalar(value: str) -> str | int:
    value = value.strip().strip('"').strip("'")
    if value.isdigit():
        return int(value)
    return value


def load_standard_contract(path: str | Path) -> StandardContract:
    """Parse the repository's deliberately simple standard-docs YAML file."""
    contract_path = Path(path)
    schema_version = 0
    purposes: dict[str, str] = {}
    modes: dict[str, list[str]] = {}
    section: str | None = None
    current_document: str | None = None
    current_mode: str | None = None

    for raw_line in contract_path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        line = raw_line.rstrip()
        stripped = line.strip()

        if not line.startswith(" "):
            if stripped == "documents:":
                section = "documents"
                current_document = None
                current_mode = None
                continue
            if stripped == "modes:":
                section = "modes"
                current_document = None
                current_mode = None
                continue
            if ":" in stripped:
                key, value = stripped.split(":", 1)
                if key == "schema_version":
                    schema_version = int(_scalar(value))
                continue

        if section == "documents":
            if line.startswith("  ") and not line.startswith("    ") and stripped.endswith(":"):
                current_document = stripped[:-1]
                purposes[current_document] = ""
                continue
            if current_document and line.startswith("    ") and stripped.startswith("purpose:"):
                purposes[current_document] = str(_scalar(stripped.split(":", 1)[1]))
                continue

        if section == "modes":
            if line.startswith("  ") and not line.startswith("    ") and stripped.endswith(":"):
                current_mode = stripped[:-1]
                modes[current_mode] = []
                continue
            if current_mode and line.startswith("    - "):
                modes[current_mode].append(stripped[2:].strip())

    required_files = list(purposes)
    missing_modes = sorted({"minimal", "standard", "enterprise"} - set(modes))
    if schema_version != 1:
        raise ValueError(f"{contract_path}: schema_version must be 1")
    if missing_modes:
        raise ValueError(f"{contract_path}: missing modes: {', '.join(missing_modes)}")
    if modes["enterprise"] != required_files:
        raise ValueError(f"{contract_path}: enterprise mode must match documents order")

    return StandardContract(
        schema_version=schema_version,
        required_files=required_files,
        modes=modes,
        purposes=purposes,
    )
