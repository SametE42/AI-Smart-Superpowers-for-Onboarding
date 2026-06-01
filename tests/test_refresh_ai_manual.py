import tempfile
import unittest
from pathlib import Path

from scripts.refresh_ai_manual import refresh_manual_pair, refresh_scaffold_pages, render_manual_page


class RefreshAiManualTests(unittest.TestCase):
    def test_render_english_page_removes_generic_scaffold(self) -> None:
        content = render_manual_page("English", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("## Practical Scope", content)
        self.assertIn("## Operating Guidance", content)
        self.assertNotIn("This file gives users a structured, practical reference", content)

    def test_render_root_readme_has_non_empty_title(self) -> None:
        content = render_manual_page("Arabic", Path("README.md"))

        self.assertTrue(content.startswith("# AI Agent Operating Manual\n"))
        self.assertNotIn("# \n", content)
        self.assertIn("ai/English/README.md", content)

    def test_render_german_page_is_localized_and_keeps_source_note(self) -> None:
        content = render_manual_page("German", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("## Praktischer Scope", content)
        self.assertIn("## Arbeitsleitlinien", content)
        self.assertIn("englische Datei maßgeblich", content)
        self.assertNotIn("This file gives users a structured, practical reference", content)

    def test_render_french_page_is_localized_and_ai_quality_passed(self) -> None:
        content = render_manual_page("French", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("## Portée pratique", content)
        self.assertIn("<!-- translation-status: ai-translated; ai-quality-pass -->", content)
        self.assertIn("AI-translated from the English source", content)
        self.assertIn("no human review required", content)
        self.assertNotIn("révision humaine requise", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_portuguese_page_is_localized_and_ai_quality_passed(self) -> None:
        content = render_manual_page("Portuguese", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("<!-- translation-status: ai-translated; ai-quality-pass -->", content)
        self.assertIn("## Escopo prático", content)
        self.assertIn("AI-translated from the English source", content)
        self.assertNotIn("revisão humana necessária", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_japanese_page_is_localized_and_ai_quality_passed(self) -> None:
        content = render_manual_page("Japanese", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("<!-- translation-status: ai-translated; ai-quality-pass -->", content)
        self.assertIn("## 実用範囲", content)
        self.assertIn("AI-translated from the English source", content)
        self.assertNotIn("人間によるレビューが必要", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_latvian_page_is_localized_and_ai_quality_passed(self) -> None:
        content = render_manual_page("Latvian", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("<!-- translation-status: ai-translated; ai-quality-pass -->", content)
        self.assertIn("## Praktiskais tvērums", content)
        self.assertIn("AI-translated from the English source", content)
        self.assertNotIn("nepieciešama cilvēka pārbaude", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_hindi_page_is_localized_and_ai_quality_passed(self) -> None:
        content = render_manual_page("Hindi", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("<!-- translation-status: ai-translated; ai-quality-pass -->", content)
        self.assertIn("## व्यावहारिक दायरा", content)
        self.assertIn("AI-translated from the English source", content)
        self.assertNotIn("मानवीय समीक्षा आवश्यक", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_zulu_page_is_localized_and_ai_quality_passed(self) -> None:
        content = render_manual_page("Zulu", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("<!-- translation-status: ai-translated; ai-quality-pass -->", content)
        self.assertIn("## Ububanzi bokusebenza", content)
        self.assertIn("AI-translated from the English source", content)
        self.assertNotIn("ukubuyekezwa ngumuntu kuyadingeka", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_refresh_pair_updates_only_scaffold_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            english = root / "ai/English/agents/agent-architecture.md"
            german = root / "ai/German/agents/agent-architecture.md"
            english.parent.mkdir(parents=True)
            german.parent.mkdir(parents=True)
            english.write_text(
                "# Agent Architecture\n\nThis file gives users a structured, practical reference for `agents/agent-architecture.md`.\n",
                encoding="utf-8",
            )
            german.write_text(
                "# Agent Architecture\n\nThis file gives users a structured, practical reference for `agents/agent-architecture.md`.\n",
                encoding="utf-8",
            )

            changed = refresh_manual_pair(root, Path("agents/agent-architecture.md"))

            self.assertEqual(changed, 2)
            self.assertIn("## Practical Scope", english.read_text(encoding="utf-8"))
            self.assertIn("## Praktischer Scope", german.read_text(encoding="utf-8"))

    def test_refresh_scaffold_pages_updates_requested_localization_mirrors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            english = root / "ai/English/agents/agent-architecture.md"
            french = root / "ai/French/agents/agent-architecture.md"
            english.parent.mkdir(parents=True)
            french.parent.mkdir(parents=True)
            english.write_text("# Agent Architecture\n\nReal English source.\n", encoding="utf-8")
            french.write_text(
                "# Agent Architecture\n\nThis file mirrors `ai/English/agents/agent-architecture.md` for the French localization.\n"
                "\n> Translation status: pending review.\n",
                encoding="utf-8",
            )

            changed = refresh_scaffold_pages(root, languages=("French",))

            self.assertEqual(changed, 1)
            self.assertIn("## Portée pratique", french.read_text(encoding="utf-8"))
            self.assertNotIn("This file mirrors", french.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
