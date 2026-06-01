import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


class RepositoryValidationTests(unittest.TestCase):
    def write(self, root: Path, relative_path: str, content: str) -> None:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_validates_clean_mirrored_documentation_repo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n\nSee [docs](docs/README.md).\n")
            self.write(root, "docs/README.md", "# Docs\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", "# English\n")
            self.write(root, "ai/English/tools/README.md", "# Tools\n")
            self.write(root, "ai/German/README.md", "# German\n\n<!-- translation-status: ai-translated; ai-quality-pass -->\n")
            self.write(root, "ai/German/tools/README.md", "# Tools\n\n<!-- translation-status: ai-translated; ai-quality-pass -->\n")

            report = validate_repository(root)

            self.assertEqual(report.status, "PASS")
            self.assertEqual(report.summary["broken_local_markdown_links"], 0)
            self.assertEqual(report.summary["missing_mirrored_ai_files"], 0)
            self.assertEqual(report.summary["markdown_files_without_h1"], 0)
            self.assertEqual(report.summary["directories_without_readme"], 0)

    def test_reports_markdown_and_ai_structure_problems(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n\nSee [missing](missing.md).\n")
            self.write(root, "docs/page.md", "No heading\n")
            self.write(root, "ai/English/README.md", "# English\n")
            self.write(root, "ai/English/tools/README.md", "# Tools\n")
            self.write(root, "ai/German/README.md", "# German\n")

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["broken_local_markdown_links"], 1)
            self.assertEqual(report.summary["missing_mirrored_ai_files"], 1)
            self.assertEqual(report.summary["markdown_files_without_h1"], 1)
            self.assertGreaterEqual(report.summary["directories_without_readme"], 1)

    def test_separates_source_scaffolds_from_ai_translations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(
                root,
                "ai/English/agents/README.md",
                "# Agents\n\nThis file gives users a structured, practical reference for `agents/README.md`.\n",
            )
            self.write(
                root,
                "ai/French/agents/README.md",
                "# Agents\n\n<!-- translation-status: ai-translated; ai-quality-pass -->\n",
            )

            report = validate_repository(root)

            self.assertEqual(report.summary["english_source_scaffold_files"], 1)
            self.assertEqual(report.summary["ai_translated_files"], 1)
            self.assertEqual(report.summary["unreviewed_translation_files"], 0)
            self.assertEqual(report.summary["missing_ai_translation_marker_files"], 0)

    def test_counts_ai_translations_legacy_drafts_and_mirror_placeholders_separately(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "ai/English/agents/README.md", "# Agents\n")
            self.write(
                root,
                "ai/French/agents/README.md",
                "# Agents\n\n<!-- translation-status: ai-translated; ai-quality-pass -->\n",
            )
            self.write(
                root,
                "ai/Portuguese/agents/README.md",
                "# Agents\n\n<!-- translation-status: localized-draft; human-review-required -->\n",
            )
            self.write(
                root,
                "ai/Spanish/agents/README.md",
                "# Agents\n\n> Status da tradução: rascunho localizado em português, revisão humana necessária.\n",
            )
            self.write(
                root,
                "ai/Turkish/agents/README.md",
                "# Agents\n\nThis file mirrors `ai/English/agents/README.md` for the Spanish localization.\n",
            )

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["ai_translated_files"], 1)
            self.assertEqual(report.summary["unreviewed_translation_files"], 3)
            self.assertEqual(report.summary["translation_mirror_placeholder_files"], 1)
            self.assertEqual(report.summary["missing_ai_translation_marker_files"], 3)


if __name__ == "__main__":
    unittest.main()
