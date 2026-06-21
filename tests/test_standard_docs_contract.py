import unittest
from pathlib import Path

from scripts.check_language_support import REQUIRED_FILES
from scripts.install_ai_onboarding import MODES
from scripts.standard_docs_contract import load_standard_docs_contract, validate_standard_docs_contract


ROOT = Path(__file__).resolve().parents[1]


class StandardDocsContractTests(unittest.TestCase):
    def test_contract_defines_expected_layers(self):
        contract = load_standard_docs_contract(ROOT)

        self.assertEqual(1, contract.schema_version)
        self.assertEqual(10, len(contract.conceptual_core))
        self.assertEqual(["minimal", "standard", "enterprise"], list(contract.modes))
        self.assertEqual(7, len(contract.modes["minimal"]))
        self.assertEqual(17, len(contract.modes["standard"]))
        self.assertEqual(21, len(contract.modes["enterprise"]))

    def test_runtime_sources_match_contract(self):
        contract = load_standard_docs_contract(ROOT)

        self.assertEqual(contract.modes, MODES)
        self.assertEqual(contract.modes["enterprise"], REQUIRED_FILES)

    def test_contract_validates_templates_and_progression(self):
        self.assertEqual([], validate_standard_docs_contract(ROOT))


if __name__ == "__main__":
    unittest.main()
