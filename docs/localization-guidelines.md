# Localization Guidelines

Localization in this repository has two separate concerns: functional output support and language quality. Functional support means a language can be selected, mapped, generated and validated. Language quality is tracked through `translation_review_status`.

## Status Values

Use these values for `translation_review_status`:

- `reviewed`: a qualified human reviewer has checked the translation.
- `needs_review`: the translation is usable as a draft but requires human review.
- automated draft: public reports should render this as `pending linguistic review`.
- `unknown`: review provenance is not known.

Do not mark a language as `reviewed` without documented human review.

## Terminology Rules

Keep technical terms consistent across README, templates, file maps and generated output. Terms such as AI, agent, review, runtime, dependency, build, test, evidence, context, repository, onboarding and human review should be handled consistently.

When a technical term is commonly used in English by local developers, keep the English term or show it next to a localized phrase. Commands, paths, filenames, API names, package names and configuration keys should remain unchanged unless a file map explicitly localizes a generated Markdown filename.

## File Maps

Localized filenames must come from file maps. Do not infer localized filenames from free-form translation. File maps should explain any ASCII-safe filename decisions for RTL scripts or complex writing systems.

The current Phase 4 file maps provide functional localized structure for all 75 detected languages. English uses canonical filenames, German uses a localized ASCII-safe example mapping, and the remaining non-English languages use stable language-code-prefixed ASCII-safe filenames until linguistic filename review is available. This is functional support, not a claim of human-reviewed localization.

## Human Review

A language may be marked `reviewed` only when a qualified human review records:

- reviewer role or qualification, without private personal data;
- reviewed language;
- reviewed files or mapping scope;
- date or release reference;
- whether filenames, terminology and Markdown rendering were checked.

At minimum, review evidence must cover the language README, standard output filenames, core terminology, commands, paths, model/provider names and Markdown rendering. Automated checks can support this process, but they do not replace the human review decision.

## Pending Linguistic Review

Automated or draft localizations must be marked honestly. They can still be functionally complete, but their language quality is not the same as human-reviewed content.

Use `i18n/glossary.yml` for terminology. It includes entries for every supported language code so gaps are explicit instead of hidden. Non-English glossary values are review targets unless a documented human review says otherwise.

## RTL And Unicode Guidance

Markdown paths, code blocks and commands should remain left-to-right. RTL content should be valid Markdown and should avoid filename choices that common tooling cannot handle. If ASCII-safe filenames are used, document the decision in the file map or language-support report.

## Validation

Run `python scripts/check_language_support.py --root .` after changing language metadata, file maps or glossary structure. Regenerate `docs/language-support-report.md` with `python scripts/generate_language_support_report.py --root .`.
