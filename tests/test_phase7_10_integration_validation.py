import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from scripts.check_context_budget import check_context_budget
from scripts.check_evidence_map import check_evidence_map
from scripts.check_file_map_schema import check_file_map_schema
from scripts.check_localized_output import check_localized_output
from scripts.check_stack_context import check_stack_context
from scripts.check_stale_docs import check_stale_docs
from scripts.check_tool_entrypoints import check_tool_entrypoints
from scripts.generate_docs_ai_index import generate_index
from scripts.install_ai_onboarding import install_ai_onboarding, main as installer_main


ROOT = Path(__file__).resolve().parents[1]


class Phase7To10IntegrationValidationTests(unittest.TestCase):
    def test_phase7_integration_docs_define_modes_and_language_behavior(self):
        how_to = (ROOT / "docs" / "how-to-integrate.md").read_text(encoding="utf-8")
        modes = (ROOT / "docs" / "integration-modes.md").read_text(encoding="utf-8")

        for term in [
            "manual integration",
            "installer",
            "Minimal",
            "Standard",
            "Enterprise",
            "--language",
            "canonical",
            "localized",
            "--detect-stack",
            "Tool entrypoints",
            "--backup-existing",
            "AI_ONBOARDING_MANIFEST.yml",
            "all supported languages",
        ]:
            self.assertIn(term, how_to)

        for term in [
            "| Modus | Fuer wen | Dateien | Aufwand | Empfehlung |",
            "Minimal Integration",
            "Standard Integration",
            "Enterprise Integration",
            "AGENTS.md",
            "docs/ai/",
            "docs/ki/",
            "File-Map",
            "TECH_STACK.md",
            "RUNTIME_ENVIRONMENT.md",
        ]:
            self.assertIn(term, modes)

    def test_phase8_examples_exist_with_required_metadata(self):
        examples = [
            "before-after",
            "minimal",
            "standard",
            "enterprise",
            "monorepo",
            "security-sensitive",
            "legacy-codebase",
            "localized-de",
            "localized-multilingual",
            "stacks",
        ]
        required = [
            "Use Case",
            "Repository-Typ",
            "verwendeter Modus",
            "verwendete Sprache",
            "verwendeter Strukturmodus",
            "erkannter oder angenommener Stack",
            "verwendete Templates",
            "Agent zuerst lesen",
            "Human Review",
        ]
        for name in examples:
            readme = ROOT / "examples" / name / "README.md"
            with self.subTest(example=name):
                self.assertTrue(readme.is_file())
                text = readme.read_text(encoding="utf-8")
                for term in required:
                    self.assertIn(term, text)

        self.assertIn("Risk Register", (ROOT / "examples" / "enterprise" / "README.md").read_text(encoding="utf-8"))
        self.assertIn("packages/", (ROOT / "examples" / "monorepo" / "README.md").read_text(encoding="utf-8"))
        self.assertIn("docs/ki/", (ROOT / "examples" / "localized-de" / "README.md").read_text(encoding="utf-8"))
        stacks = (ROOT / "examples" / "stacks" / "README.md").read_text(encoding="utf-8")
        for stack in ["Python", "TypeScript", "Java", "C#", "Go", "Rust", "Infrastructure-as-Code"]:
            self.assertIn(stack, stacks)

    def test_phase9_validation_scripts_cover_key_error_cases(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            evidence = root / "EVIDENCE_MAP.md"
            evidence.write_text(
                "# EVIDENCE_MAP.md\n\n"
                "| Claim | Evidence source | Confidence | Last checked | Notes |\n"
                "|---|---|---|---|---|\n"
                "| Uses TypeScript | `[UNKNOWN]` | High | 2026-06-11 | missing evidence |\n"
                "| Uses Java | `pom.xml` | Certain | 2026-06-11 | invalid confidence |\n",
                encoding="utf-8",
            )
            evidence_result = check_evidence_map(evidence)
            self.assertGreaterEqual(len(evidence_result["errors"]), 2)

            freshness = root / "FRESHNESS.md"
            freshness.write_text(
                "# FRESHNESS.md\n\n"
                "| File | Last reviewed | Review trigger | Owner | Status |\n"
                "|---|---|---|---|---|\n"
                "| `ARCHITECTURE.md` |  | Architecture changed | team | Needs review |\n",
                encoding="utf-8",
            )
            freshness_result = check_stale_docs(freshness)
            self.assertTrue(freshness_result["warnings"])
            self.assertTrue(freshness_result["errors"])

            docs_ai = root / "docs" / "ai"
            docs_ai.mkdir(parents=True)
            long_doc = docs_ai / "LONG.md"
            long_doc.write_text("# Long\n\n" + "\n".join("Repeat this generic instruction." for _ in range(20)), encoding="utf-8")
            budget_result = check_context_budget(root, max_lines=10)
            self.assertTrue(budget_result["warnings"])

    def test_phase9_repository_validators_pass_current_repo(self):
        checks = [
            check_tool_entrypoints(ROOT),
            check_localized_output(ROOT),
            check_file_map_schema(ROOT),
            check_stack_context(ROOT),
        ]
        for result in checks:
            with self.subTest(script=result["name"]):
                self.assertEqual([], result["errors"])

    def test_docs_ai_index_generator_creates_canonical_index(self):
        text = generate_index(ROOT)
        self.assertIn("# Docs AI Template Index", text)
        self.assertIn("CONTEXT_INDEX.md", text)
        self.assertIn("RUNTIME_ENVIRONMENT.md", text)
        self.assertIn("HUMAN_REVIEW_GATES.md", text)

    def test_phase10_representative_installer_dry_runs(self):
        representative = [
            ("minimal", "en", "canonical"),
            ("standard", "de", "canonical"),
            ("standard", "de", "localized"),
            ("enterprise", "de", "localized"),
            ("standard", "fr", "localized"),
            ("standard", "ja", "localized"),
            ("standard", "ar", "localized"),
            ("standard", "tr", "localized"),
            ("standard", "zh", "localized"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            for mode, language, structure in representative:
                with self.subTest(mode=mode, language=language, structure=structure):
                    result = install_ai_onboarding(
                        root=ROOT,
                        target=target,
                        mode=mode,
                        language=language,
                        structure=structure,
                        dry_run=True,
                        manifest=True,
                    )
                    self.assertEqual([], result.errors)
                    self.assertTrue(result.actions)
            self.assertEqual([], list(target.rglob("*")))

    def test_installer_list_languages_cli_covers_all_supported_languages(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = installer_main(["--root", str(ROOT), "--list-languages"])

        self.assertEqual(0, exit_code)
        output = buffer.getvalue()
        self.assertIn("| en |", output)
        self.assertIn("| de |", output)
        self.assertIn("| ar |", output)
        self.assertIn("| zh |", output)

    def test_phase10_summary_exists_with_required_status_fields(self):
        summary = (ROOT / "docs" / "release-readiness-summary.md").read_text(encoding="utf-8")
        for term in [
            "| Bereich | Erstellte Dateien | Aktualisierte Dateien | Zweck | Status |",
            "geschaetzte Reife vor den Aenderungen",
            "geschaetzte Reife nach den Aenderungen",
            "75",
            "pending linguistic review: 74",
            "reviewed: 1",
            "verbleibende Luecken",
            "empfohlene naechste Commits",
            "Phasen abgeschlossen",
            "Phasen noch offen",
        ]:
            self.assertIn(term, summary)

    def test_validation_workflow_checks_generated_language_report(self):
        workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(encoding="utf-8")

        self.assertIn("python scripts/generate_language_support_report.py --root . --output docs/language-support-report.md", workflow)
        self.assertIn("git diff --exit-code docs/language-support-report.md", workflow)

    def test_dependabot_covers_github_actions(self):
        dependabot = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")

        self.assertIn("package-ecosystem: \"github-actions\"", dependabot)
        self.assertIn("directory: \"/\"", dependabot)


if __name__ == "__main__":
    unittest.main()
