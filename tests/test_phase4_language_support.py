import unittest
from pathlib import Path

from scripts.check_language_support import REQUIRED_FILES, validate_language_support


ROOT = Path(__file__).resolve().parents[1]


class Phase4LanguageSupportTests(unittest.TestCase):
    def test_all_detected_languages_have_complete_support(self):
        result = validate_language_support(ROOT)

        self.assertEqual([], result.errors)
        self.assertEqual(75, result.summary["detected_languages"])
        self.assertEqual(75, result.summary["supported_languages"])
        self.assertEqual(75, result.summary["complete_languages"])

    def test_required_phase4_files_exist(self):
        required_paths = [
            "i18n/language-support.yml",
            "i18n/glossary.yml",
            "i18n/file-map.schema.yml",
            "scripts/check_language_support.py",
            "scripts/generate_language_support_report.py",
            "docs/language-support-report.md",
        ]
        for relative_path in required_paths:
            with self.subTest(relative_path=relative_path):
                self.assertTrue((ROOT / relative_path).exists(), f"{relative_path} should exist")

    def test_each_file_map_contains_required_files_and_metadata(self):
        result = validate_language_support(ROOT)
        self.assertEqual([], result.errors)

        for language, file_map in result.file_maps.items():
            with self.subTest(language=language):
                self.assertEqual(1, file_map["schema_version"])
                self.assertEqual("AGENTS.md", file_map["agents_filename"])
                self.assertIn(file_map["translation_review_status"], {"reviewed", "needs_review", "machine_generated", "unknown"})
                self.assertTrue(file_map["docs_directory"].startswith("docs/"))
                self.assertEqual(set(REQUIRED_FILES), set(file_map["files"].keys()))
                self.assertEqual(len(REQUIRED_FILES), len(set(file_map["files"].values())))

    def test_english_and_german_mappings_are_canonical_and_localized_examples(self):
        result = validate_language_support(ROOT)
        english = result.file_maps["en"]
        german = result.file_maps["de"]

        self.assertEqual("docs/ai", english["docs_directory"])
        self.assertEqual("CONTEXT_INDEX.md", english["files"]["CONTEXT_INDEX.md"])
        self.assertEqual("docs/ki", german["docs_directory"])
        self.assertEqual("KONTEXT_INDEX.md", german["files"]["CONTEXT_INDEX.md"])
        self.assertEqual("SYSTEMREGELN.md", german["files"]["MASTER_SYSTEM.md"])

    def test_glossary_covers_required_terms_and_all_languages(self):
        glossary = (ROOT / "i18n" / "glossary.yml").read_text(encoding="utf-8")
        language_codes = set(validate_language_support(ROOT).language_support.keys())

        for term in ["agent", "ai", "context", "evidence", "review", "runtime", "dependency", "tool_entrypoint"]:
            with self.subTest(term=term):
                self.assertIn(f"  {term}:", glossary)

        for code in language_codes:
            with self.subTest(code=code):
                self.assertIn(f"      {code}:", glossary)

    def test_standard_docs_contract_matches_language_checker_and_installer_modes(self):
        from scripts.install_ai_onboarding import MODES
        from scripts.standard_contract import load_standard_contract

        contract = load_standard_contract(ROOT / "standard-docs.yml")

        self.assertEqual(REQUIRED_FILES, contract.required_files)
        self.assertEqual(MODES["minimal"], contract.modes["minimal"])
        self.assertEqual(MODES["standard"], contract.modes["standard"])
        self.assertEqual(MODES["enterprise"], contract.modes["enterprise"])


if __name__ == "__main__":
    unittest.main()
