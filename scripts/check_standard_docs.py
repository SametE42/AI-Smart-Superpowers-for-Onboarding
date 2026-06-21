#!/usr/bin/env python3
"""CLI wrapper for standard docs contract validation."""

from __future__ import annotations

try:
    from scripts.standard_docs_contract import main
except ModuleNotFoundError:
    from standard_docs_contract import main  # type: ignore[no-redef]


if __name__ == "__main__":
    raise SystemExit(main())
