# Prompts

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> Pinagmulan na wika: Ingles
> Pinagmulan na file: ai/English/prompts/README.md
> Kapag may pagkakaiba, ang English file ang susundin.

Ipinapaliwanag ng pahinang ito kung paano umaangkop ang `prompts/README.md` sa AI Agent Operating Manual. Para ito sa mga tao at AI agents na kailangang magplano, magberipika o umulit ng repository work.

## Praktikal na saklaw

Gamitin ang pahinang ito bilang operational na gabay para sa paksang `prompts`. Hindi nito pinapalitan ang repository evidence o project-specific instructions.

## Mga gabay sa trabaho

- Ituring ang repository evidence bilang pangunahing awtoridad.
- Panatilihing eksakto ang file names, commands, API names at model names.
- Markahan ang hindi pa nabeberipikang konklusyon ng `[ASSUMPTION: ...]` at hindi alam na facts ng `[UNKNOWN]`.
- Ikabit ang tool-specific behavior sa tool o runtime na tunay na nagmamay-ari nito.
- I-escalate ang security, permissions at production-readiness risks sa pagsusuri ng tao.

## Pokus

Bago gamitin ang pahinang ito sa workflow, tukuyin ang saklaw, kinakailangang evidence, verifiable commands at hangganan ng human approval.

## Manual Pages

- [Accuracy Clause](accuracy-clause.md)
- [Code Review](code-review.md)
- [Documentation Update](documentation-update.md)
- [Magical Prompt Improver](magical-prompt-improver.md)
- [Master Prompt](master-prompt.md)
- [Prompt Refinement](prompt-refinement.md)
- [Prompt Structure](prompt-structure.md)
- [Security Review](security-review.md)
- [Translation](translation.md)


## Quality check

- Malinaw ang layunin para sa bagong contributor.
- Nakatutulong ang gabay sa AI agents at human maintainers.
- Hindi iniimbento ang model-specific commands.
- Nakikita pa rin ang boundaries ng security at human approval.
- Ang English source pa rin ang masusunod sa localization conflicts.
