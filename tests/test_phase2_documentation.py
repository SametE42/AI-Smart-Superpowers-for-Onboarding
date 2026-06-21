import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Phase2DocumentationTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_comparison_document_covers_required_projects_and_boundaries(self):
        text = self.read("docs/comparison.md")

        self.assertTrue(text.startswith("# "))
        required_headers = [
            "Project / Approach",
            "Category",
            "Main purpose",
            "Strength",
            "Limit",
            "How this project differs",
            "What this project can learn",
        ]
        for header in required_headers:
            with self.subTest(header=header):
                self.assertIn(header, text)

        required_projects = [
            "AGENTS.md",
            "agentsmd/agents.md",
            "agentmd/agent.md",
            "agentskills/agentskills",
            "anthropics/skills",
            "addyosmani/agent-skills",
            "obra/superpowers",
            "CommandCode",
            "Aider",
            "Cline",
            "OpenHands",
            "Goose",
            "OpenCode",
            "Continue",
            "RepoMaster-like repository-understanding research",
            "GitTaskBench-like benchmark research",
        ]
        for project in required_projects:
            with self.subTest(project=project):
                self.assertIn(project, text)

        required_phrases = [
            "Other projects often define how agents work, or provide tools that execute work.",
            "This project defines what agents need to understand about a repository before they work.",
            "obra/superpowers defines structured development workflows for coding agents.",
            "This project focuses on the step before that",
            "No official compatibility is claimed by this comparison.",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_research_background_documents_design_principles(self):
        text = self.read("docs/research-background.md")

        self.assertTrue(text.startswith("# "))
        required_phrases = [
            "repository-specific context",
            "A single instruction file is useful",
            "Too much context can also hurt",
            "structured, reviewed and task-loadable",
            "technology and stack context",
            "language-dependent output",
            "functional multilingual support",
            "pending linguistic review",
            "evidence-first documentation",
            "technology-neutral templates",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

        required_principles = [
            "Evidence instead of assumptions",
            "Task-scoped context loading",
            "Human review before trust",
            "Separation of entrypoints and durable knowledge",
            "Traceability of claims",
            "Freshness and maintenance",
            "Governance and safety boundaries",
            "Tool-compatible entrypoints",
            "Fully localized output for all existing languages",
            "No knowledge duplication between tool files and knowledge base",
            "Technology and programming-language neutrality",
            "Build, test, dependency and runtime context as part of repository onboarding",
            "Same functional support level for all existing languages",
            "No permanent fallback treatment for individual languages",
            "Separate evaluation of functional language support and linguistic review quality",
        ]
        for principle in required_principles:
            with self.subTest(principle=principle):
                self.assertIn(principle, text)

    def test_tool_compatibility_matrix_records_sources_and_limits(self):
        text = self.read("docs/tool-compatibility.md")

        for phrase in [
            "Do not add a tool-support claim without a source",
            "Source",
            "Last checked",
            "Confidence",
            "Limitations",
            "OpenAI Codex",
            "GitHub Copilot",
            "Claude Code",
            "Gemini CLI",
            "OpenCode",
            "No primary source recorded in this repository",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)


if __name__ == "__main__":
    unittest.main()
