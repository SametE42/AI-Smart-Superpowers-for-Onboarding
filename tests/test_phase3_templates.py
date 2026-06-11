import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates" / "docs-ai"


REQUIRED_TEMPLATES = {
    "CONTEXT_INDEX.md": [
        "Task type",
        "Read first",
        "Bug fix",
        "Architecture review",
    ],
    "MASTER_SYSTEM.md": [
        "Evidence-first behavior",
        "Use `CONTEXT_INDEX.md` first",
        "Do not assume project language or stack without evidence",
    ],
    "ONBOARDING.md": [
        "Repository scan checklist",
        "Language and stack discovery",
        "Unknowns",
    ],
    "ARCHITECTURE.md": [
        "System overview",
        "Boundaries",
        "Data flow",
    ],
    "TECH_STACK.md": [
        "Detected programming languages",
        "Package managers",
        "Configuration files",
    ],
    "BUILD_AND_TEST.md": [
        "Install commands",
        "Build commands",
        "Test commands",
        "Known limitations",
    ],
    "DEPENDENCIES.md": [
        "Package managers",
        "Lockfiles",
        "Human review for dependency updates",
    ],
    "RUNTIME_ENVIRONMENT.md": [
        "Runtime",
        "Environment variables",
        "Unknown operating assumptions",
    ],
    "EVIDENCE_MAP.md": [
        "Claim",
        "Evidence source",
        "Confidence",
        "High",
        "Unknown",
    ],
    "PROJECT_MEMORY.md": [
        "Do not store temporary chat notes",
        "Long-lived project knowledge",
    ],
    "DECISIONS.md": [
        "Date",
        "Decision",
        "Review trigger",
        "Accepted",
    ],
    "STYLE_GUIDE.md": [
        "Naming",
        "Formatting",
        "Test style",
    ],
    "SECURITY_RULES.md": [
        "Secrets",
        "Credentials",
        "Human review requirements",
    ],
    "RISK_REGISTER.md": [
        "Risk",
        "Severity",
        "Critical",
        "Human review required",
    ],
    "REVIEW_CHECKLIST.md": [
        "Evidence checked",
        "Tests considered",
        "Human review gates checked",
    ],
    "ERROR_PATTERNS.md": [
        "Pattern",
        "Symptom",
        "Safe response",
    ],
    "TASK_SCOPING.md": [
        "Task type",
        "Affected areas",
        "Files not to touch",
    ],
    "FRESHNESS.md": [
        "Last reviewed",
        "Review trigger",
        "Needs review",
        "Stale",
    ],
    "AGENT_ROLES.md": [
        "Repository Researcher",
        "Security Reviewer",
        "Human Reviewer",
        "Allowed actions",
    ],
    "SAFETY_BOUNDARIES.md": [
        "Destructive commands",
        "Generated translations",
        "Compliance claims",
    ],
    "HUMAN_REVIEW_GATES.md": [
        "Authentication",
        "Authorization",
        "Deployment",
        "Major dependency upgrades",
    ],
}


class Phase3TemplateTests(unittest.TestCase):
    def read_template(self, filename: str) -> str:
        return (TEMPLATE_DIR / filename).read_text(encoding="utf-8")

    def test_required_templates_exist_and_cover_required_topics(self):
        for filename, phrases in REQUIRED_TEMPLATES.items():
            with self.subTest(filename=filename):
                path = TEMPLATE_DIR / filename
                self.assertTrue(path.exists(), f"{filename} should exist")
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("# "), f"{filename} should start with an H1")
                for phrase in phrases:
                    self.assertIn(phrase, text)

    def test_status_values_are_consistent(self):
        checks = {
            "EVIDENCE_MAP.md": ["High", "Medium", "Low", "Unknown"],
            "DECISIONS.md": ["Proposed", "Accepted", "Deprecated", "Replaced"],
            "RISK_REGISTER.md": ["Low", "Medium", "High", "Critical"],
            "FRESHNESS.md": ["Current", "Needs review", "Stale", "Unknown"],
        }
        for filename, values in checks.items():
            text = self.read_template(filename)
            for value in values:
                with self.subTest(filename=filename, value=value):
                    self.assertIn(value, text)

    def test_templates_are_technology_neutral(self):
        stack_text = self.read_template("TECH_STACK.md")
        onboarding_text = self.read_template("ONBOARDING.md")
        combined = stack_text + "\n" + onboarding_text
        for phrase in [
            "Python",
            "JavaScript",
            "TypeScript",
            "Java",
            "C#",
            "Go",
            "Rust",
            "Infrastructure-as-Code",
            "[UNKNOWN]",
            "[ASSUMPTION:",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, combined)


if __name__ == "__main__":
    unittest.main()
