# Prompts

<!-- translation-status: ai-translated; ai-quality-pass -->

> Translation status: AI-translated from the English source; structural quality gate passed; human linguistic review still required unless translation_review_status is reviewed.
> Kildesprog: engelsk
> Kildefil: ai/English/models/cohere/prompts.md
> Ved afvigelser er den engelske fil gældende.

Denne side forklarer, hvordan `models/cohere/prompts.md` passer ind i AI Agent Operating Manual. Den er skrevet til mennesker og AI-agenter, der skal planlægge, verificere eller gentage repository-arbejde.

## Praktisk omfang

Brug siden som operationel vejledning for temaet `models`. Den erstatter ikke repository-evidens eller projektspecifikke instruktioner.

## Arbejdsretningslinjer

- Behandl repository-evidens som primær autoritet.
- Bevar filnavne, kommandoer, API-navne og modelnavne nøjagtigt.
- Marker ikke-verificerede konklusioner med `[ASSUMPTION: ...]` og ukendte fakta med `[UNKNOWN]`.
- Knyt værktøjsspecifik adfærd til det værktøj eller runtime, der faktisk ejer den.
- Eskalér sikkerheds-, tilladelses- og produktionsrisici til menneskelig gennemgang.

## Fokus

Definér omfang, nødvendig evidens, verificerbare kommandoer og grænser for menneskelig godkendelse, før siden bruges i et workflow.


## Kvalitetskontrol

- Formålet er tydeligt for en ny bidragyder.
- Vejledningen hjælper både AI-agenter og menneskelige maintainers.
- Der opfindes ingen modelspecifikke kommandoer.
- Grænser for sikkerhed og menneskelig godkendelse forbliver synlige.
- Den engelske kilde forbliver afgørende ved lokaliseringskonflikter.
