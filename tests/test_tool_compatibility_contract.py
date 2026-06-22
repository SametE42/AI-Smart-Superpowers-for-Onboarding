import tempfile
import unittest
from pathlib import Path

from scripts.check_tool_compatibility import validate_tool_compatibility


class ToolCompatibilityContractTests(unittest.TestCase):
    VALID_DOC = """# Tool Compatibility

## Context Files

| Tool / Agent | File or mechanism | Guidance | Source | Last checked | Confidence | Limitations |
|---|---|---|---|---|---|---|
| Example Agent | `AGENTS.md` | Link to `/docs/ai/`. | [Docs](https://example.com/docs) | 2026-06-21 | High | Example limitation. |

## Agent Runtimes

| System | Category | Guidance | Source | Last checked | Confidence | Limitations |
|---|---|---|---|---|---|---|
| Unverified Gateway | Gateway | Treat as project-specific. | No primary source recorded in this repository. | 2026-06-21 | Low | No official compatibility claim. |
"""

    def write_doc(self, text: str) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        path = root / "docs" / "tool-compatibility.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return root

    def test_validates_source_backed_compatibility_tables(self) -> None:
        root = self.write_doc(self.VALID_DOC)

        result = validate_tool_compatibility(root)

        self.assertEqual("PASS", result["status"])
        self.assertEqual(2, result["summary"]["validated_rows"])

    def test_missing_required_column_fails(self) -> None:
        root = self.write_doc(self.VALID_DOC.replace(" | Confidence |", " | "))

        result = validate_tool_compatibility(root)

        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("missing required columns" in error for error in result["errors"]))

    def test_unsourced_rows_must_have_low_confidence(self) -> None:
        root = self.write_doc(self.VALID_DOC.replace("| Low | No official", "| High | No official"))

        result = validate_tool_compatibility(root)

        self.assertEqual("FAIL", result["status"])
        self.assertTrue(any("unsourced row must use Low confidence" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
