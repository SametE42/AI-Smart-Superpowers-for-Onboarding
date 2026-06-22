import tempfile
import unittest
from pathlib import Path

from scripts.check_language_review_evidence import validate_language_review_evidence


class LanguageReviewEvidenceTests(unittest.TestCase):
    def write(self, root: Path, relative_path: str, content: str) -> None:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_reviewed_language(self, root: Path, evidence: bool = True) -> None:
        self.write(
            root,
            "i18n/language-support.yml",
            """languages:
  en:
    name: English
    source_folder: English
    output_support: complete
    translation_review_status: reviewed
    canonical_structure: true
    localized_structure: true
    file_map: i18n/file-map.en.yml
    docs_directory: docs/ai
    agents_filename: AGENTS.md
    notes: Canonical source language.
""",
        )
        self.write(
            root,
            "i18n/file-map.en.yml",
            """schema_version: 1
language: en
language_name: English
source_folder: ai/English
docs_directory: docs/ai
agents_filename: AGENTS.md
translation_review_status: reviewed
files:
  MASTER_SYSTEM.md: MASTER_SYSTEM.md
review_notes:
  - Canonical English reference mapping.
""",
        )
        self.write(root, "ai/English/README.md", "# English\n")
        self.write(root, "i18n/file-map.en.yml.marker", "present\n")
        if evidence:
            self.write(
                root,
                "i18n/review-evidence.en.yml",
                """schema_version: 1
language: en
language_name: English
review_status: reviewed
review_date: 2026-06-21
reviewer_role: maintainer
review_scope:
  - canonical source manual
  - canonical file map
checked_artifacts:
  - ai/English/README.md
  - i18n/file-map.en.yml
notes:
  - English is the canonical source language.
""",
            )

    def test_reviewed_language_requires_valid_evidence_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_reviewed_language(root)

            result = validate_language_review_evidence(root)

            self.assertEqual("PASS", result["status"])
            self.assertEqual(1, result["summary"]["reviewed_languages"])
            self.assertEqual(1, result["summary"]["evidence_files"])

    def test_missing_review_evidence_fails_for_reviewed_language(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_reviewed_language(root, evidence=False)

            result = validate_language_review_evidence(root)

            self.assertEqual("FAIL", result["status"])
            self.assertIn("en: missing review evidence file", result["errors"][0])

    def test_file_map_and_language_support_review_status_must_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_reviewed_language(root)
            (root / "i18n" / "file-map.en.yml").write_text(
                (root / "i18n" / "file-map.en.yml")
                .read_text(encoding="utf-8")
                .replace("translation_review_status: reviewed", "translation_review_status: machine_generated"),
                encoding="utf-8",
            )

            result = validate_language_review_evidence(root)

            self.assertEqual("FAIL", result["status"])
            self.assertTrue(any("review status mismatch" in error for error in result["errors"]))

    def test_checked_artifacts_must_exist(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_reviewed_language(root)
            (root / "i18n" / "review-evidence.en.yml").write_text(
                (root / "i18n" / "review-evidence.en.yml")
                .read_text(encoding="utf-8")
                .replace("ai/English/README.md", "ai/English/MISSING.md"),
                encoding="utf-8",
            )

            result = validate_language_review_evidence(root)

            self.assertEqual("FAIL", result["status"])
            self.assertTrue(any("checked artifact does not exist" in error for error in result["errors"]))

    def test_schema_file_is_not_reported_as_orphaned_review_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_reviewed_language(root)
            self.write(root, "i18n/review-evidence.schema.yml", "schema_version: 1\n")

            result = validate_language_review_evidence(root)

            self.assertEqual("PASS", result["status"])
            self.assertEqual([], result["warnings"])


if __name__ == "__main__":
    unittest.main()
