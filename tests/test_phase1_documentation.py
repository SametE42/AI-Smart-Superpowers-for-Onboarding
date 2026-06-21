import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Phase1DocumentationTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_readme_positions_project_as_modular_preflight_framework(self):
        readme = self.read("README.md")

        required_phrases = [
            "Ein modulares Repository-Preflight-Framework fuer KI-Coding-Agenten.",
            "Bereite Repositories vor, bevor KI-Coding-Agenten Code veraendern.",
            "AGENTS.md -> AI Smart Superpowers for Onboarding -> docs/ai/ or localized knowledge base -> Skills/Workflows -> Coding Agent -> Human Review",
            "This project is not a coding agent, SDK or runtime package, and it does not replace human review.",
            "Python is only an internal automation option for installer, validation and tests.",
            "All existing languages are intended to reach the same functional output support level.",
            "AGENTS.md stays unchanged by default because many tools expect that entrypoint filename.",
            "## Choose Your Path",
            "schnell testen",
            "review-ready",
            "## Why So Many Files?",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, readme)
        self.assertNotIn("reviewed AI knowledge base", readme)
        self.assertNotIn("reviewed `docs/ai/` folder", readme)

    def test_phase1_documentation_files_exist_and_have_expected_focus(self):
        expected_files = {
            "docs/architecture-of-this-project.md": [
                "Core Onboarding",
                "Localized Output",
                "Language Support Matrix",
                "Tool Entrypoints",
                "Validation & CI",
            ],
            "docs/roadmap.md": [
                "Phase 1: Framework Clarity",
                "Phase 3: Complete Multilingual Support",
                "Phase 10: Release Readiness",
            ],
            "RELEASE_NOTES.md": [
                "v0.1.0 - 2026-06-21",
                "experimental but functional",
            ],
            "docs/language-support.md": [
                "75 language folders",
                "canonical structure",
                "localized structure",
                "translation_review_status",
            ],
            "docs/localization-guidelines.md": [
                "translation_review_status",
                "pending linguistic review",
                "human review",
            ],
            "docs/file-map-schema.md": [
                "schema_version",
                "agents_filename",
                "reserved Windows filenames",
            ],
            "docs/migration-guide.md": [
                "canonical to localized",
                "localized to canonical",
                "Output Manifest",
            ],
            "docs/release-checklist.md": [
                "Release Checklist",
                "python scripts/check_standard_docs.py --root .",
                "git diff --check",
            ],
            "docs/demo-5-minute-onboarding.md": [
                "5-Minute Repository Onboarding Demo",
                "python scripts/install_ai_onboarding.py",
                "Human review",
            ],
            "docs/german-localized-output-demo.md": [
                "German Localized Output Demo",
                "docs/ki/",
                "pending linguistic review",
            ],
        }

        for relative_path, required_phrases in expected_files.items():
            with self.subTest(relative_path=relative_path):
                path = ROOT / relative_path
                self.assertTrue(path.exists(), f"{relative_path} should exist")
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("# "), f"{relative_path} should start with an H1")
                for phrase in required_phrases:
                    self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
