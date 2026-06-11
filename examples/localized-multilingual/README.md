# Localized Multilingual Example

## Use Case

Show several localized output structures without limiting the full language support list.

## Repository-Typ

Documentation-heavy or multi-region repository.

## verwendeter Modus

Standard Integration.

## verwendete Sprache

Examples: `de`, `fr`, `ar`, `zh`. All supported languages remain equal through the language inventory and File-Maps.

## verwendeter Strukturmodus

Localized.

## erkannter oder angenommener Stack

Documentation repository; use `--stack docs` unless repository evidence suggests otherwise.

## verwendete Templates

Standard templates mapped through each selected `i18n/file-map.<code>.yml`.

## Agent zuerst lesen

1. `AGENTS.md`
2. The selected localized `CONTEXT_INDEX` equivalent.
3. The selected localized review checklist equivalent.

## Human Review

Human language review is required before marking non-English output as reviewed.

## Example Dry Runs

```bash
python scripts/install_ai_onboarding.py --mode standard --language de --structure localized --dry-run
python scripts/install_ai_onboarding.py --mode standard --language fr --structure localized --dry-run
python scripts/install_ai_onboarding.py --mode standard --language ar --structure localized --dry-run
python scripts/install_ai_onboarding.py --mode standard --language zh --structure localized --dry-run
```
