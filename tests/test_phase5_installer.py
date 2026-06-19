import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts.check_language_support import validate_language_support
from scripts.install_ai_onboarding import (
    MODES,
    detect_stack,
    install_ai_onboarding,
    load_language_support,
    main,
)


ROOT = Path(__file__).resolve().parents[1]


class Phase5InstallerTests(unittest.TestCase):
    def write_minimal_framework(self, root: Path, missing_template: str | None = None) -> None:
        (root / "templates" / "docs-ai").mkdir(parents=True)
        (root / "templates" / "AGENTS.md").write_text("# AGENTS\n", encoding="utf-8")
        (root / "i18n").mkdir()
        (root / "i18n" / "language-support.yml").write_text(
            "languages:\n"
            "  en:\n"
            "    name: English\n"
            "    source_folder: English\n"
            "    output_support: complete\n"
            "    translation_review_status: reviewed\n"
            "    canonical_structure: true\n"
            "    localized_structure: true\n"
            "    file_map: i18n/file-map.en.yml\n"
            "    docs_directory: docs/ai\n"
            "    agents_filename: AGENTS.md\n",
            encoding="utf-8",
        )
        (root / "i18n" / "file-map.en.yml").write_text(
            "schema_version: 1\n"
            "language: en\n"
            "language_name: English\n"
            "docs_directory: docs/ai\n"
            "agents_filename: AGENTS.md\n"
            "translation_review_status: reviewed\n"
            "files:\n"
            + "".join(f"  {filename}: {filename}\n" for filename in MODES["minimal"]),
            encoding="utf-8",
        )
        for filename in MODES["minimal"]:
            if filename == missing_template:
                continue
            (root / "templates" / "docs-ai" / filename).write_text(f"# {filename}\n", encoding="utf-8")

    def test_list_languages_includes_all_supported_languages(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            exit_code = main(["--root", str(ROOT), "--list-languages"])

        self.assertEqual(0, exit_code)
        output = buffer.getvalue()
        support = validate_language_support(ROOT)
        for code in support.language_support:
            with self.subTest(code=code):
                self.assertIn(f"| {code} |", output)

    def test_every_supported_language_allows_canonical_and_localized_dry_run(self):
        support = validate_language_support(ROOT)

        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            for code in support.language_support:
                for structure in ["canonical", "localized"]:
                    with self.subTest(code=code, structure=structure):
                        result = install_ai_onboarding(
                            root=ROOT,
                            target=target,
                            mode="minimal",
                            language=code,
                            structure=structure,
                            stack="generic",
                            dry_run=True,
                            manifest=True,
                        )
                        self.assertEqual([], result.errors)
                        self.assertTrue(result.actions)
            self.assertEqual([], list(target.rglob("*")), "dry-run must not write files")

    def test_language_metadata_is_complete_for_installer(self):
        support, file_maps = load_language_support(ROOT)

        for code, info in support.items():
            with self.subTest(code=code):
                self.assertEqual("complete", info["output_support"])
                self.assertTrue(info["translation_review_status"])
                self.assertIs(info["canonical_structure"], True)
                self.assertIs(info["localized_structure"], True)
                self.assertIn(code, file_maps)
                self.assertEqual("AGENTS.md", file_maps[code]["agents_filename"])

    def test_canonical_mode_writes_english_filenames_and_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="standard",
                language="de",
                structure="canonical",
                stack="typescript",
                dry_run=False,
                manifest=True,
            )

            self.assertEqual([], result.errors)
            self.assertTrue((target / "AGENTS.md").exists())
            self.assertTrue((target / "docs" / "ai" / "CONTEXT_INDEX.md").exists())
            self.assertTrue((target / "docs" / "ai" / "TECH_STACK.md").exists())
            self.assertTrue((target / "docs" / "ai" / "AI_ONBOARDING_MANIFEST.yml").exists())
            text = (target / "docs" / "ai" / "TECH_STACK.md").read_text(encoding="utf-8")
            self.assertIn("Selected language: de", text)
            self.assertIn("Stack hint: typescript", text)
            self.assertIn("Translation review status: machine_generated", text)

    def test_standard_mode_generates_manifest_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="standard",
                language="en",
                structure="canonical",
                stack="generic",
            )

            self.assertEqual([], result.errors)
            manifest = target / "docs" / "ai" / "AI_ONBOARDING_MANIFEST.yml"
            self.assertTrue(manifest.exists())
            text = manifest.read_text(encoding="utf-8")
            self.assertIn("mode: standard", text)
            self.assertIn("agents_filename: AGENTS.md", text)

    def test_localized_mode_writes_german_directory_and_filenames(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="standard",
                language="de",
                structure="localized",
                stack="generic",
                dry_run=False,
                manifest=True,
            )

            self.assertEqual([], result.errors)
            self.assertTrue((target / "AGENTS.md").exists())
            self.assertTrue((target / "docs" / "ki" / "KONTEXT_INDEX.md").exists())
            self.assertTrue((target / "docs" / "ki" / "SYSTEMREGELN.md").exists())
            self.assertTrue((target / "docs" / "ki" / "KI_ONBOARDING_MANIFEST.yml").exists())

    def test_no_localized_filenames_keeps_localized_directory_but_canonical_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            result = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="minimal",
                language="de",
                structure="localized",
                stack="generic",
                no_localized_filenames=True,
                manifest=True,
            )

            self.assertEqual([], result.errors)
            self.assertTrue((target / "docs" / "ki" / "CONTEXT_INDEX.md").exists())
            self.assertFalse((target / "docs" / "ki" / "KONTEXT_INDEX.md").exists())

    def test_missing_required_template_aborts_instead_of_generating_unknown_document(self):
        with tempfile.TemporaryDirectory() as framework_tmp, tempfile.TemporaryDirectory() as target_tmp:
            framework = Path(framework_tmp)
            target = Path(target_tmp)
            self.write_minimal_framework(framework, missing_template="BUILD_AND_TEST.md")

            result = install_ai_onboarding(
                root=framework,
                target=target,
                mode="minimal",
                language="en",
                structure="canonical",
                stack="generic",
            )

            self.assertIn("Missing required template", "\n".join(result.errors))
            self.assertEqual([], list(target.rglob("*")))

    def test_dry_run_reports_existing_files_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            existing = target / "AGENTS.md"
            existing.write_text("original\n", encoding="utf-8")

            result = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="minimal",
                language="en",
                structure="canonical",
                stack="generic",
                dry_run=True,
            )

            self.assertEqual([], result.errors)
            self.assertEqual("original\n", existing.read_text(encoding="utf-8"))
            self.assertIn("would overwrite", {action.action for action in result.actions})

    def test_force_and_backup_existing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            existing = target / "AGENTS.md"
            existing.write_text("original\n", encoding="utf-8")

            blocked = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="minimal",
                language="en",
                structure="canonical",
                stack="generic",
            )
            self.assertTrue(blocked.errors)
            self.assertEqual("original\n", existing.read_text(encoding="utf-8"))

            forced = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="minimal",
                language="en",
                structure="canonical",
                stack="generic",
                force=True,
                backup_existing=True,
            )
            self.assertEqual([], forced.errors)
            self.assertNotEqual("original\n", existing.read_text(encoding="utf-8"))
            backups = list(target.glob("AGENTS.md.bak-*"))
            self.assertEqual(1, len(backups))

    def test_interactive_can_cancel_without_writing(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            with patch("builtins.input", return_value="n"):
                result = install_ai_onboarding(
                    root=ROOT,
                    target=target,
                    mode="minimal",
                    language="en",
                    structure="canonical",
                    stack="generic",
                    interactive=True,
                )

            self.assertIn("cancelled", "\n".join(result.errors).lower())
            self.assertEqual([], list(target.rglob("*")))

    def test_unknown_language_and_structure_are_clear_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            unknown_language = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="minimal",
                language="xx",
                structure="canonical",
                stack="generic",
                dry_run=True,
            )
            self.assertIn("Unsupported language", "\n".join(unknown_language.errors))

            unknown_structure = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="minimal",
                language="en",
                structure="sideways",
                stack="generic",
                dry_run=True,
            )
            self.assertIn("Unsupported structure", "\n".join(unknown_structure.errors))

    def test_detect_stack_returns_hints_without_overclaiming(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "package.json").write_text("{}", encoding="utf-8")
            (target / "tsconfig.json").write_text("{}", encoding="utf-8")
            hint = detect_stack(target)
            self.assertEqual("typescript", hint.stack)
            self.assertIn("tsconfig.json", hint.evidence)

            result = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="standard",
                language="en",
                structure="canonical",
                detect_stack_flag=True,
                dry_run=False,
                manifest=True,
            )
            self.assertEqual([], result.errors)
            evidence = (target / "docs" / "ai" / "EVIDENCE_MAP.md").read_text(encoding="utf-8")
            self.assertIn("Stack hint: typescript", evidence)
            self.assertIn("Evidence source:", evidence)

    def test_detect_stack_covers_supported_marker_files(self):
        cases = [
            ("package.json", "javascript"),
            ("tsconfig.json", "typescript"),
            ("pyproject.toml", "python"),
            ("requirements.txt", "python"),
            ("setup.py", "python"),
            ("pom.xml", "java"),
            ("build.gradle", "java"),
            ("build.gradle.kts", "kotlin"),
            ("app.csproj", "csharp"),
            ("app.sln", "csharp"),
            ("go.mod", "go"),
            ("Cargo.toml", "rust"),
            ("composer.json", "php"),
            ("Gemfile", "ruby"),
            ("Package.swift", "swift"),
            ("CMakeLists.txt", "cpp"),
            ("Makefile", "cpp"),
            ("main.tf", "iac"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            for marker, expected_stack in cases:
                target = base / marker.replace(".", "_")
                target.mkdir()
                (target / marker).write_text("", encoding="utf-8")
                with self.subTest(marker=marker):
                    hint = detect_stack(target)
                    self.assertEqual(expected_stack, hint.stack)
                    self.assertIn(marker, hint.evidence)

            terraform_target = base / "terraform_directory"
            (terraform_target / "terraform").mkdir(parents=True)
            hint = detect_stack(terraform_target)
            self.assertEqual("iac", hint.stack)
            self.assertIn("terraform/", hint.evidence)

    def test_detected_stack_is_written_to_localized_evidence_map(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "go.mod").write_text("module example\n", encoding="utf-8")

            result = install_ai_onboarding(
                root=ROOT,
                target=target,
                mode="standard",
                language="de",
                structure="localized",
                detect_stack_flag=True,
            )

            self.assertEqual([], result.errors)
            evidence = (target / "docs" / "ki" / "NACHWEISUEBERSICHT.md").read_text(encoding="utf-8")
            self.assertIn("Stack hint: go", evidence)
            self.assertIn("go.mod", evidence)


if __name__ == "__main__":
    unittest.main()
