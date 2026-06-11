# Localized DE Example

## Use Case

German team wants localized documentation paths while keeping `AGENTS.md` stable.

## Repository-Typ

Application repository maintained primarily in German.

## verwendeter Modus

Standard Integration.

## verwendete Sprache

German (`de`).

## verwendeter Strukturmodus

Localized.

## erkannter oder angenommener Stack

TypeScript hint in this example; verify from `package.json` and `tsconfig.json`.

## verwendete Templates

Standard templates mapped through `i18n/file-map.de.yml`.

## Agent zuerst lesen

1. `AGENTS.md`
2. `docs/ki/KONTEXT_INDEX.md`
3. `docs/ki/NACHWEISUEBERSICHT.md`
4. `docs/ki/PRUEFCHECKLISTE.md`

## Human Review

Review German wording before marking translations as reviewed.

## Installer

```bash
python scripts/install_ai_onboarding.py --mode standard --language de --structure localized --dry-run
```
