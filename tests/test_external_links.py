import tempfile
import unittest
from pathlib import Path

from scripts.check_external_links import check_external_links, extract_external_links, load_allowlist


class ExternalLinkCheckTests(unittest.TestCase):
    def write(self, root: Path, relative_path: str, content: str) -> None:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_extracts_markdown_and_html_external_links(self) -> None:
        text = """# Links

[Docs](https://example.com/docs)
![Badge](https://img.shields.io/badge/example-ok-green)
<a href="https://github.com/example/repo">Repo</a>
<img alt="Build" src="https://github.com/example/repo/actions/workflows/validate.yml/badge.svg">
[Local](docs/README.md)
[Mail](mailto:security@example.com)
"""

        links = extract_external_links(text, "README.md")

        self.assertEqual(
            [link.url for link in links],
            [
                "https://example.com/docs",
                "https://img.shields.io/badge/example-ok-green",
                "https://github.com/example/repo",
                "https://github.com/example/repo/actions/workflows/validate.yml/badge.svg",
            ],
        )
        self.assertEqual([1, 2, 3, 4], [link.index for link in links])

    def test_inventory_mode_fails_malformed_external_urls_without_network(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n\n[Bad](https://)\n")

            result = check_external_links(root, check_network=False)

            self.assertEqual("FAIL", result["status"])
            self.assertEqual(1, result["summary"]["malformed_links"])
            self.assertEqual(0, result["summary"]["network_checked_links"])

    def test_allowlist_patterns_skip_matching_links(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n\n[Skip](https://unstable.example/docs)\n")
            allowlist_path = root / "config" / "external-link-allowlist.txt"
            allowlist_path.parent.mkdir(parents=True, exist_ok=True)
            allowlist_path.write_text("https://unstable.example/*\n", encoding="utf-8")

            result = check_external_links(root, allowlist_path=allowlist_path, check_network=False)

            self.assertEqual("PASS", result["status"])
            self.assertEqual(["https://unstable.example/*"], load_allowlist(allowlist_path))
            self.assertEqual(1, result["summary"]["allowlisted_links"])


if __name__ == "__main__":
    unittest.main()
