import tempfile
import unittest
from pathlib import Path

from scripts.refresh_ai_manual import LOCALIZED_LANGUAGE_TEXT, refresh_manual_pair, refresh_scaffold_pages, render_manual_page


LOCALIZATION_STATUS_MARKER = "<!-- localization-status: localized-mirror; review-status: tracked-in-language-support -->"
LOCALIZATION_STATUS_TEXT = (
    "Language status: localized mirror of the English reference. "
    "Review status is tracked in the language support metadata."
)
MAGICAL_PROMPT_ENGLISH_BODY_MARKERS = (
    "Use this page when a user request",
    "Run a short intake check on every user request",
    "Return a compact intake when the request needs clarification",
    "Use this structure for substantial repository work",
)


class RefreshAiManualTests(unittest.TestCase):
    def test_render_english_page_removes_generic_scaffold(self) -> None:
        content = render_manual_page("English", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("## Practical Scope", content)
        self.assertIn("## Operating Guidance", content)
        self.assertNotIn("This file gives users a structured, practical reference", content)

    def test_render_english_magical_prompt_improver_has_activation_protocol(self) -> None:
        content = render_manual_page("English", Path("prompts/magical-prompt-improver.md"))

        self.assertIn("# Magical Prompt Improver", content)
        self.assertIn("templates/optional/MAGICAL_PROMPT_IMPROVER.md", content)
        self.assertIn("## Activation Rules", content)
        self.assertIn("Intake Mode", content)
        self.assertIn("Full Rewrite Mode", content)
        self.assertIn("Verification Mode", content)
        self.assertIn("Commit/Push Readiness Mode", content)
        self.assertIn("## Decision Tree", content)
        self.assertIn("## Best Workflow Order", content)
        self.assertIn("## Anti-Hallucination Rules", content)
        self.assertIn("## Verification Criteria", content)
        self.assertIn("## Examples", content)
        self.assertIn("Small status request", content)
        self.assertIn("Repository change request", content)
        self.assertNotIn("This page explains how `prompts/magical-prompt-improver.md` fits", content)

    def test_render_french_magical_prompt_improver_is_localized_with_neutral_status(self) -> None:
        content = render_manual_page("French", Path("prompts/magical-prompt-improver.md"))

        self.assertIn("# Magical Prompt Improver", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)
        self.assertIn(LOCALIZATION_STATUS_TEXT, content)
        self.assertIn("ai/English/prompts/magical-prompt-improver.md", content)
        self.assertIn("## Portée pratique", content)
        self.assertIn("## Consignes de travail", content)
        self.assertIn("## Ordre de workflow recommandé", content)
        self.assertIn("## Exemples", content)
        self.assertIn("Intake Mode", content)
        self.assertIn("Full Rewrite Mode", content)
        self.assertIn("Verification Mode", content)
        self.assertIn("Commit/Push Readiness Mode", content)
        self.assertNotIn("AI-translated from the English source", content)
        self.assertNotIn("no human review required", content)
        self.assertNotIn("révision humaine requise", content)
        self.assertNotIn("This file mirrors `ai/English/", content)
        for marker in MAGICAL_PROMPT_ENGLISH_BODY_MARKERS:
            self.assertNotIn(marker, content)

    def test_render_german_magical_prompt_improver_is_localized_with_order_and_examples(self) -> None:
        content = render_manual_page("German", Path("prompts/magical-prompt-improver.md"))

        self.assertIn("# Magical Prompt Improver", content)
        self.assertIn("## Praktischer Scope", content)
        self.assertIn("## Arbeitsleitlinien", content)
        self.assertIn("## Beste Workflow-Reihenfolge", content)
        self.assertIn("## Beispiele", content)
        self.assertIn("Intake Mode", content)
        self.assertIn("Commit/Push Readiness Mode", content)
        self.assertIn("Kleine Statusanfrage", content)
        self.assertIn("Repository-Änderungsanfrage", content)
        for marker in MAGICAL_PROMPT_ENGLISH_BODY_MARKERS:
            self.assertNotIn(marker, content)

    def test_render_all_localized_magical_prompt_improver_pages_avoid_english_body_markers(self) -> None:
        for language, profile in LOCALIZED_LANGUAGE_TEXT.items():
            with self.subTest(language=language):
                content = render_manual_page(language, Path("prompts/magical-prompt-improver.md"))

                self.assertIn(f"## {profile['scope_heading']}", content)
                self.assertIn(f"## {profile['guidance_heading']}", content)
                self.assertIn("Intake Mode", content)
                self.assertIn("Full Rewrite Mode", content)
                self.assertIn("Verification Mode", content)
                self.assertIn("Commit/Push Readiness Mode", content)
                for marker in MAGICAL_PROMPT_ENGLISH_BODY_MARKERS:
                    self.assertNotIn(marker, content)

    def test_render_root_readme_has_non_empty_title(self) -> None:
        content = render_manual_page("Arabic", Path("README.md"))

        self.assertTrue(content.startswith("# AI Smart Superpowers for Onboarding Manual\n"))
        self.assertNotIn("# \n", content)
        self.assertIn("ai/English/README.md", content)

    def test_render_root_readme_has_required_entrypoint_structure(self) -> None:
        content = render_manual_page("French", Path("README.md"))

        for section in (
            "## Overview",
            "## Purpose of this language folder",
            "## Where This Fits",
            "## Target Output",
            "## Quickstart",
            "## Source Of Truth And Links",
            "## Workflow",
            "## When To Use",
            "## When Not To Use",
            "## English source of truth",
            "## How to use this folder",
            "## Manual Structure",
            "## Recommended reading order",
            "## Safety and human review rules",
            "## Localization notes",
            "## Quality checklist",
        ):
            self.assertIn(section, content)
        for marker in (
            "evidence-first Pre-Development Onboarding layer",
            "`docs/ai/`",
            "Superpowers-style",
            "does not imply compatibility, endorsement or integration",
            "templates/MASTER_PROMPT.en.md",
            "templates/docs-ai/",
            "prompts/magical-prompt-improver.md",
            "templates/optional/MAGICAL_PROMPT_IMPROVER.md",
        ):
            self.assertIn(marker, content)
        for folder in (
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
            "workflows/",
        ):
            self.assertIn(folder, content)

    def test_render_prompts_readme_links_magical_prompt_improver(self) -> None:
        content = render_manual_page("English", Path("prompts/README.md"))

        self.assertIn("## Manual Pages", content)
        self.assertIn("[Magical Prompt Improver](magical-prompt-improver.md)", content)
        self.assertIn("[Prompt Refinement](prompt-refinement.md)", content)

    def test_render_localized_prompts_readme_keeps_same_manual_page_links(self) -> None:
        content = render_manual_page("French", Path("prompts/README.md"))

        self.assertIn("## Manual Pages", content)
        self.assertIn("[Magical Prompt Improver](magical-prompt-improver.md)", content)
        self.assertIn("[Prompt Refinement](prompt-refinement.md)", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)

    def test_render_german_page_is_localized_and_keeps_source_note(self) -> None:
        content = render_manual_page("German", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("## Praktischer Scope", content)
        self.assertIn("## Arbeitsleitlinien", content)
        self.assertIn("englische Datei maßgeblich", content)
        self.assertNotIn("This file gives users a structured, practical reference", content)

    def test_render_french_page_is_localized_with_neutral_status(self) -> None:
        content = render_manual_page("French", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn("## Portée pratique", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)
        self.assertIn(LOCALIZATION_STATUS_TEXT, content)
        self.assertNotIn("AI-translated from the English source", content)
        self.assertNotIn("no human review required", content)
        self.assertNotIn("révision humaine requise", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_portuguese_page_is_localized_with_neutral_status(self) -> None:
        content = render_manual_page("Portuguese", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)
        self.assertIn("## Escopo prático", content)
        self.assertNotIn("AI-translated from the English source", content)
        self.assertNotIn("no human review required", content)
        self.assertNotIn("revisão humana necessária", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_japanese_page_is_localized_with_neutral_status(self) -> None:
        content = render_manual_page("Japanese", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)
        self.assertIn("## 実用範囲", content)
        self.assertNotIn("AI-translated from the English source", content)
        self.assertNotIn("no human review required", content)
        self.assertNotIn("人間によるレビューが必要", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_latvian_page_is_localized_with_neutral_status(self) -> None:
        content = render_manual_page("Latvian", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)
        self.assertIn("## Praktiskais tvērums", content)
        self.assertNotIn("AI-translated from the English source", content)
        self.assertNotIn("no human review required", content)
        self.assertNotIn("nepieciešama cilvēka pārbaude", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_hindi_page_is_localized_with_neutral_status(self) -> None:
        content = render_manual_page("Hindi", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)
        self.assertIn("## व्यावहारिक दायरा", content)
        self.assertNotIn("AI-translated from the English source", content)
        self.assertNotIn("no human review required", content)
        self.assertNotIn("मानवीय समीक्षा आवश्यक", content)
        self.assertIn("ai/English/agents/agent-architecture.md", content)
        self.assertNotIn("This file mirrors `ai/English/", content)

    def test_render_zulu_page_is_localized_with_neutral_status(self) -> None:
        content = render_manual_page("Zulu", Path("agents/agent-architecture.md"))

        self.assertIn("# Agent Architecture", content)
        self.assertIn(LOCALIZATION_STATUS_MARKER, content)
        self.assertIn("## Ububanzi bokusebenza", content)
        self.assertNotIn("AI-translated from the English source", content)
        self.assertNotIn("no human review required", content)
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

    def test_refresh_scaffold_pages_creates_missing_requested_localization_mirrors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            english = root / "ai/English/prompts/magical-prompt-improver.md"
            french = root / "ai/French/prompts/magical-prompt-improver.md"
            english.parent.mkdir(parents=True)
            french.parent.mkdir(parents=True)
            english.write_text("# Magical Prompt Improver\n\nReal English source.\n", encoding="utf-8")

            changed = refresh_scaffold_pages(root, force=True, languages=("French",))

            self.assertEqual(changed, 1)
            self.assertTrue(french.exists())
            self.assertIn(LOCALIZATION_STATUS_MARKER, french.read_text(encoding="utf-8"))
            self.assertIn("ai/English/prompts/magical-prompt-improver.md", french.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
