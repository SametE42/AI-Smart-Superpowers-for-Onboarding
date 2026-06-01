import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


class RepositoryValidationTests(unittest.TestCase):
    STANDARD_SUBFOLDERS = (
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
    )

    def write(self, root: Path, relative_path: str, content: str) -> None:
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def complete_language_readme(self, translated: bool = False) -> str:
        marker = "<!-- translation-status: ai-translated; ai-quality-pass -->\n\n" if translated else ""
        rows = "\n".join(f"| `{folder}` | Purpose for {folder} |" for folder in self.STANDARD_SUBFOLDERS)
        return f"""# AI Agent Operating Manual

{marker}## Purpose of this language folder

This folder contains the localized AI operating manual for repository onboarding work.

## English source of truth

English is authoritative and localized files mirror `ai/English/README.md`.

## How to use this folder

Use this folder for onboarding, review, prompts, safety, tools, models and templates.

## Folder overview

| Folder | Purpose |
|---|---|
{rows}

## Recommended reading order

1. `README.md`
2. `safety/README.md`
3. `agents/README.md`
4. `context-engineering/README.md`
5. `prompts/README.md`
6. `tools/README.md`
7. `templates/README.md`

## Safety and human review rules

- Repository evidence is authoritative.
- Do not invent commands, model capabilities or provider behavior.
- Preserve file names, commands, API names and model names.
- Mark assumptions and unknowns.
- Escalate security, permissions and production-readiness risks to human review.

## Localization notes

File names, folder names, commands, APIs and model names stay unchanged. English wins when localized content conflicts with English.

## Quality checklist

- Purpose is clear.
- Folder overview is complete.
- All standard subfolders are listed.
- Safety boundaries are visible.
- No unsupported model/tool claims are added.
- English remains authoritative.
"""

    def test_validates_clean_mirrored_documentation_repo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n\nSee [docs](docs/README.md).\n")
            self.write(root, "docs/README.md", "# Docs\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", self.complete_language_readme())
            self.write(root, "ai/English/tools/README.md", "# Tools\n")
            self.write(root, "ai/German/README.md", self.complete_language_readme(translated=True))
            self.write(root, "ai/German/tools/README.md", "# Tools\n\n<!-- translation-status: ai-translated; ai-quality-pass -->\n")

            report = validate_repository(root)

            self.assertEqual(report.status, "PASS")
            self.assertEqual(report.summary["broken_local_markdown_links"], 0)
            self.assertEqual(report.summary["missing_mirrored_ai_files"], 0)
            self.assertEqual(report.summary["markdown_files_without_h1"], 0)
            self.assertEqual(report.summary["directories_without_readme"], 0)
            self.assertEqual(report.summary["incomplete_language_readmes"], 0)

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

    def test_complete_language_readme_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", self.complete_language_readme())
            self.write(root, "ai/German/README.md", self.complete_language_readme(translated=True))

            report = validate_repository(root)

            self.assertEqual(report.status, "PASS")
            self.assertEqual(report.summary["incomplete_language_readmes"], 0)
            self.assertEqual(report.summary["language_readmes_missing_required_sections"], 0)
            self.assertEqual(report.summary["language_readmes_missing_standard_subfolders"], 0)

    def test_language_readme_missing_required_section_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", self.complete_language_readme().replace("## Folder overview", "## Folder list"))

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["incomplete_language_readmes"], 1)
            self.assertEqual(report.summary["language_readmes_missing_required_sections"], 1)

    def test_language_readme_missing_translation_marker_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", self.complete_language_readme())
            self.write(root, "ai/German/README.md", self.complete_language_readme())

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["incomplete_language_readmes"], 1)
            self.assertEqual(report.summary["missing_ai_translation_marker_files"], 1)

    def test_language_readme_missing_standard_subfolder_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", self.complete_language_readme().replace("tools/", "tooling/"))

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["incomplete_language_readmes"], 1)
            self.assertEqual(report.summary["language_readmes_missing_standard_subfolders"], 1)

    def test_english_language_readme_does_not_require_translation_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", self.complete_language_readme())

            report = validate_repository(root)

            self.assertEqual(report.status, "PASS")
            self.assertEqual(report.summary["missing_ai_translation_marker_files"], 0)

    def test_non_english_language_readme_requires_translation_marker(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n")
            self.write(root, "ai/README.md", "# AI\n")
            self.write(root, "ai/English/README.md", self.complete_language_readme())
            self.write(root, "ai/French/README.md", self.complete_language_readme())

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["missing_ai_translation_marker_files"], 1)
            self.assertEqual(report.summary["incomplete_language_readmes"], 1)

    def test_old_repository_url_is_blocking(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            old_url = "https://github.com/" + "SametE42/" + "Ai-" + "Repo-" + "Onboarding"
            self.write(root, "README.md", f"# Root\n\nClone from {old_url}.\n")

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["old_repository_reference_hits"], 1)
            self.assertEqual(
                report.details["old_repository_reference_hits"],
                [{"file": "README.md", "line": 3, "match": old_url}],
            )

    def test_report_root_uses_origin_repository_name_when_available(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            subprocess.run(
                ["git", "remote", "add", "origin", "https://github.com/SametE42/AI-Smart-Superpowers-for-Onboarding.git"],
                cwd=root,
                check=True,
            )
            self.write(root, "README.md", "# Root\n")

            report = validate_repository(root)

            self.assertEqual(report.root, "AI-Smart-Superpowers-for-Onboarding")

    def test_validation_reports_can_be_generated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            json_report = root / "validation.json"
            markdown_report = root / "validation.md"
            self.write(root, "README.md", "# Root\n")

            result = subprocess.run(
                [
                    sys.executable,
                    "scripts/validate_repository.py",
                    "--root",
                    str(root),
                    "--json",
                    str(json_report),
                    "--markdown",
                    str(markdown_report),
                ],
                cwd=Path(__file__).resolve().parents[1],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(json_report.read_text(encoding="utf-8"))["status"], "PASS")
            self.assertIn("- old_repository_reference_hits: 0", markdown_report.read_text(encoding="utf-8"))

    def test_optional_template_missing_readme_entry_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, "README.md", "# Root\n")
            self.write(
                root,
                "templates/optional/README.md",
                "# Optional Templates\n\n| Template | Use when |\n|---|---|\n| `LISTED.md` | Listed template. |\n",
            )
            self.write(root, "templates/optional/LISTED.md", "# Listed\n")
            self.write(root, "templates/optional/UNLISTED.md", "# Unlisted\n")

            report = validate_repository(root)

            self.assertEqual(report.status, "FAIL")
            self.assertEqual(report.summary["optional_template_files_missing_readme_entries"], 1)
            self.assertEqual(report.details["optional_template_files_missing_readme_entries"], ["templates/optional/UNLISTED.md"])

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


class TemplateDocumentationTests(unittest.TestCase):
    def test_magical_prompt_improver_has_activation_structure(self) -> None:
        root = Path(__file__).resolve().parents[1]
        text = (root / "templates/optional/MAGICAL_PROMPT_IMPROVER.md").read_text(encoding="utf-8")

        for section in (
            "## Activation Rules",
            "## Activation Modes",
            "## Decision Tree",
            "## Example",
        ):
            self.assertIn(section, text)
        for mode in (
            "Intake Mode",
            "Full Rewrite Mode",
            "Verification Mode",
            "Commit/Push Readiness Mode",
        ):
            self.assertIn(mode, text)


if __name__ == "__main__":
    unittest.main()
