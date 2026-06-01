# Prompts

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> Kildespråk: engelsk
> Kildefil: ai/English/prompts/README.md
> Ved avvik gjelder den engelske filen.

Denne siden forklarer hvordan `prompts/README.md` passer inn i AI Agent Operating Manual. Den er skrevet for mennesker og AI-agenter som må planlegge, verifisere eller gjenta repositoryarbeid.

## Praktisk omfang

Bruk siden som operativ veiledning for temaet `prompts`. Den erstatter ikke repositorybevis eller prosjektspesifikke instruksjoner.

## Arbeidsretningslinjer

- Behandle repositorybevis som primær autoritet.
- Bevar filnavn, kommandoer, API-navn og modellnavn nøyaktig.
- Merk uverifiserte konklusjoner med `[ASSUMPTION: ...]` og ukjente fakta med `[UNKNOWN]`.
- Knytt verktøyspesifikk atferd til verktøyet eller runtime som faktisk eier den.
- Eskaler risiko rundt sikkerhet, tillatelser og produksjonsklarhet til menneskelig gjennomgang.

## Fokus

Definer omfang, nødvendig bevis, verifiserbare kommandoer og grenser for menneskelig godkjenning før siden brukes i en workflow.

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


## Kvalitetskontroll

- Formålet er tydelig for en ny bidragsyter.
- Veiledningen hjelper både AI-agenter og menneskelige maintainers.
- Ingen modellspesifikke kommandoer blir funnet opp.
- Grenser for sikkerhet og menneskelig godkjenning forblir synlige.
- Den engelske kilden forblir avgjørende ved lokaliseringskonflikter.
