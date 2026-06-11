import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOOL_ENTRYPOINTS = ROOT / "templates" / "tool-entrypoints"
SKILLS = ROOT / "skills"


ENTRYPOINT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "COPILOT_INSTRUCTIONS.md",
    "CURSOR_RULES.md",
    "CLINE_RULES.md",
    "AIDER_NOTES.md",
    "OPENCODE.md",
    "COMMANDCODE_SKILL.md",
]

SKILL_FILES = {
    "repo-onboarding": [
        "Repository evidence",
        "Programmiersprachen",
        "docs/ai/",
        "localized knowledge base",
        "Human Review",
    ],
    "docs-ai-review": [
        "existing AI knowledge base",
        "Repository evidence",
        "TECH_STACK.md",
        "localized output",
        "Context Bloat",
    ],
    "docs-ai-update": [
        "approved repository changes",
        "TECH_STACK.md",
        "FRESHNESS.md",
        "localized equivalent",
        "Keine temporaeren Sitzungsnotizen",
    ],
}

BANNED_SUPPORT_CLAIMS = [
    "official support",
    "officially supported",
    "certified integration",
    "guaranteed support",
]


class Phase6ToolEntrypointsAndSkillsTests(unittest.TestCase):
    def test_tool_entrypoint_templates_exist(self):
        self.assertTrue(TOOL_ENTRYPOINTS.is_dir())
        for filename in ENTRYPOINT_FILES:
            with self.subTest(filename=filename):
                self.assertTrue((TOOL_ENTRYPOINTS / filename).is_file())

    def test_tool_entrypoints_are_short_references_to_knowledge_base(self):
        required_terms = [
            "docs/ai/CONTEXT_INDEX.md",
            "localized equivalent",
            "TECH_STACK.md",
            "BUILD_AND_TEST.md",
            "DEPENDENCIES.md",
            "RUNTIME_ENVIRONMENT.md",
            "SECURITY_RULES.md",
            "REVIEW_CHECKLIST.md",
            "PROJECT_MEMORY.md",
            "DECISIONS.md",
            "Repository evidence",
        ]
        for filename in ENTRYPOINT_FILES:
            if filename == "COMMANDCODE_SKILL.md":
                continue
            text = (TOOL_ENTRYPOINTS / filename).read_text(encoding="utf-8")
            with self.subTest(filename=filename):
                self.assertLessEqual(len(text.splitlines()), 80)
                for term in required_terms:
                    self.assertIn(term, text)
                lowered = text.lower()
                for claim in BANNED_SUPPORT_CLAIMS:
                    self.assertNotIn(claim, lowered)

    def test_commandcode_skill_template_has_portable_frontmatter(self):
        text = (TOOL_ENTRYPOINTS / "COMMANDCODE_SKILL.md").read_text(encoding="utf-8")

        self.assertTrue(text.startswith("---\n"))
        self.assertIn("name: repo-onboarding", text)
        self.assertIn(
            "description: Use the reviewed docs/ai knowledge base before planning, coding, testing or reviewing changes in this repository.",
            text,
        )
        self.assertIn("localized equivalent", text)
        self.assertIn("Repository evidence", text)

    def test_skill_packages_exist_with_frontmatter_and_required_guidance(self):
        for skill_name, required_terms in SKILL_FILES.items():
            path = SKILLS / skill_name / "SKILL.md"
            with self.subTest(skill_name=skill_name):
                self.assertTrue(path.is_file())
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"))
                self.assertIn(f"name: {skill_name}", text)
                self.assertIn("description:", text)
                self.assertLessEqual(len(text.splitlines()), 140)
                for term in required_terms:
                    self.assertIn(term, text)
                lowered = text.lower()
                for claim in BANNED_SUPPORT_CLAIMS:
                    self.assertNotIn(claim, lowered)

    def test_skill_packaging_is_documented_from_readme(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("templates/tool-entrypoints/", readme)
        self.assertIn("skills/repo-onboarding/SKILL.md", readme)


if __name__ == "__main__":
    unittest.main()
