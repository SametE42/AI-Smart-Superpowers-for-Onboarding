# Tool_profile

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; AI quality gate passed; no human review required.
> Källspråk: engelska
> Källfil: ai/English/templates/TOOL_PROFILE.md
> Vid avvikelser gäller den engelska filen.

Den här sidan förklarar hur `templates/TOOL_PROFILE.md` passar in i AI Agent Operating Manual. Den är skriven för människor och AI-agenter som behöver planera, verifiera eller upprepa repositoryarbete.

## Praktisk omfattning

Använd sidan som operativ vägledning för temat `templates`. Den ersätter inte repositorybevis eller projektspecifika instruktioner.

## Arbetsriktlinjer

- Behandla repositorybevis som primär auktoritet.
- Bevara filnamn, kommandon, API-namn och modellnamn exakt.
- Markera overifierade slutsatser med `[ASSUMPTION: ...]` och okända fakta med `[UNKNOWN]`.
- Knyt verktygsspecifikt beteende till det verktyg eller runtime som faktiskt äger det.
- Eskalera risker kring säkerhet, behörigheter och produktionsberedskap till mänsklig granskning.

## Fokus

Definiera omfattning, nödvändiga bevis, verifierbara kommandon och gränser för mänskligt godkännande innan sidan används i ett workflow.

## Kvalitetskontroll

- Syftet är tydligt för en ny bidragsgivare.
- Vägledningen hjälper både AI-agenter och mänskliga maintainers.
- Inga modellspecifika kommandon hittas på.
- Gränser för säkerhet och mänskligt godkännande förblir synliga.
- Den engelska källan fortsätter vara avgörande vid lokaliseringskonflikter.
