#!/usr/bin/env python3
"""Inventory and optionally check external links in Markdown files."""

from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen


MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
HTML_LINK = re.compile(r"<(?:a|img)\b[^>]*\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
DEFAULT_ALLOWLIST = Path("config/external-link-allowlist.txt")
DEFAULT_EXCLUDED_DIRS = {".git", ".worktrees", "worktrees", "__pycache__", "ai"}
USER_AGENT = "AI-Smart-Superpowers-Link-Check/1.0"


@dataclass(frozen=True)
class ExternalLink:
    source: str
    line: int
    index: int
    url: str


def _is_http_candidate(target: str) -> bool:
    return target.startswith(("http://", "https://"))


def _is_valid_http_url(url: str) -> bool:
    if any(character.isspace() for character in url):
        return False
    parts = urlsplit(url)
    return parts.scheme in {"http", "https"} and bool(parts.netloc)


def _request_url(url: str, timeout: float) -> tuple[int | None, str | None]:
    parts = urlsplit(url)
    check_url = urlunsplit((parts.scheme, parts.netloc, parts.path or "/", parts.query, ""))
    last_error: str | None = None
    for method in ("HEAD", "GET"):
        request = Request(check_url, method=method, headers={"User-Agent": USER_AGENT})
        try:
            with urlopen(request, timeout=timeout) as response:  # nosec B310 - release link checker.
                return int(response.status), None
        except HTTPError as error:
            if method == "HEAD" and error.code in {403, 405, 406, 429}:
                last_error = f"HTTP {error.code}"
                continue
            return int(error.code), f"HTTP {error.code}"
        except (TimeoutError, URLError, OSError) as error:
            last_error = str(error)
            if method == "HEAD":
                continue
            return None, last_error
    return None, last_error


def _iter_markdown_files(root: Path, includes: Iterable[str] | None = None) -> list[Path]:
    if includes:
        paths: list[Path] = []
        for include in includes:
            path = root / include
            if path.is_file() and path.suffix.lower() == ".md":
                paths.append(path)
            elif path.is_dir():
                paths.extend(sorted(child for child in path.rglob("*.md") if _is_scannable(child, root)))
        return sorted(set(paths))
    return sorted(child for child in root.rglob("*.md") if _is_scannable(child, root))


def _is_scannable(path: Path, root: Path) -> bool:
    try:
        relative = path.relative_to(root)
    except ValueError:
        return False
    return not any(part in DEFAULT_EXCLUDED_DIRS for part in relative.parts)


def extract_external_links(markdown: str, source: str) -> list[ExternalLink]:
    links: list[ExternalLink] = []
    index = 0
    for line_number, line in enumerate(markdown.splitlines(), start=1):
        for pattern in (MARKDOWN_LINK, HTML_LINK):
            for match in pattern.finditer(line):
                target = match.group(1).strip()
                if not _is_http_candidate(target):
                    continue
                index += 1
                links.append(ExternalLink(source=source, line=line_number, index=index, url=target))
    return links


def load_allowlist(path: str | Path) -> list[str]:
    allowlist_path = Path(path)
    if not allowlist_path.exists():
        return []
    patterns: list[str] = []
    for raw_line in allowlist_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line and not line.startswith("#"):
            patterns.append(line)
    return patterns


def _is_allowlisted(url: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatchcase(url, pattern) for pattern in patterns)


def _check_network_link(url: str, timeout: float, retries: int) -> str | None:
    attempts = max(1, retries + 1)
    last_error: str | None = None
    for _ in range(attempts):
        status, error = _request_url(url, timeout)
        if status is not None and 200 <= status < 400:
            return None
        last_error = error or f"HTTP {status}"
    return last_error or "request failed"


def check_external_links(
    root: str | Path = ".",
    allowlist_path: str | Path | None = None,
    check_network: bool = False,
    timeout: float = 8.0,
    retries: int = 1,
    includes: Iterable[str] | None = None,
) -> dict:
    root_path = Path(root)
    allowlist = load_allowlist(allowlist_path or root_path / DEFAULT_ALLOWLIST)
    errors: list[dict[str, object]] = []
    warnings: list[str] = []
    all_links: list[ExternalLink] = []

    for path in _iter_markdown_files(root_path, includes):
        relative = path.relative_to(root_path).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        all_links.extend(extract_external_links(text, relative))

    allowlisted = [link for link in all_links if _is_allowlisted(link.url, allowlist)]
    candidates = [link for link in all_links if link not in allowlisted]
    malformed = [link for link in candidates if not _is_valid_http_url(link.url)]
    for link in malformed:
        errors.append({**asdict(link), "error": "malformed external URL"})

    network_checked = 0
    if check_network:
        seen: set[str] = set()
        for link in candidates:
            if link in malformed or link.url in seen:
                continue
            seen.add(link.url)
            network_checked += 1
            error = _check_network_link(link.url, timeout=timeout, retries=retries)
            if error:
                errors.append({**asdict(link), "error": error})
    else:
        warnings.append("network checks disabled; run with --check-network for release link validation")

    summary = {
        "markdown_files": len(_iter_markdown_files(root_path, includes)),
        "external_links": len(all_links),
        "allowlisted_links": len(allowlisted),
        "malformed_links": len(malformed),
        "network_checked_links": network_checked,
    }
    return {
        "name": "check_external_links",
        "status": "PASS" if not errors else "FAIL",
        "summary": summary,
        "allowlist": allowlist,
        "warnings": warnings,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventory and optionally check external Markdown links.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--allowlist", default=None, help="Optional allowlist path.")
    parser.add_argument("--include", action="append", default=None, help="File or directory to scan. May be repeated.")
    parser.add_argument("--check-network", action="store_true", help="Perform HTTP checks with timeout and retry.")
    parser.add_argument("--timeout", type=float, default=8.0, help="HTTP timeout in seconds.")
    parser.add_argument("--retries", type=int, default=1, help="HTTP retry count after the first attempt.")
    parser.add_argument("--json", default=None, help="Optional JSON report path.")
    args = parser.parse_args()

    result = check_external_links(
        root=args.root,
        allowlist_path=args.allowlist,
        check_network=args.check_network,
        timeout=args.timeout,
        retries=args.retries,
        includes=args.include,
    )
    output = json.dumps(result, indent=2)
    print(output)
    if args.json:
        Path(args.json).write_text(output + "\n", encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
