# Magical Prompt Improver

<!-- localization-status: localized-mirror; review-status: tracked-in-language-support -->

> Language status: localized mirror of the English reference. Review status is tracked in the language support metadata.
> Langue source : anglais
> Fichier source: ai/English/prompts/magical-prompt-improver.md
> En cas de divergence, le fichier anglais fait autorité.

Utilise cette page lorsqu'une demande, un prompt réutilisable ou un transfert d'agent doit être clarifié avant un travail de dépôt. Source protocol: [`templates/optional/MAGICAL_PROMPT_IMPROVER.md`](../../../templates/optional/MAGICAL_PROMPT_IMPROVER.md).

## Portée pratique

Le Magical Prompt Improver réduit l'ambiguïté, rend le contexte manquant visible, fixe les limites de sécurité et définit les preuves nécessaires pour terminer.

## Consignes de travail

- Choisis toujours le mode le plus léger qui couvre correctement le risque de la demande.
- Conserve exactement les chemins, commandes, noms de modèles, noms d'API et contraintes utilisateur.
- Marque les faits inconnus avec `[UNKNOWN]` et les hypothèses non vérifiées avec `[ASSUMPTION: ...]`.
- Exige des preuves concrètes avant toute affirmation sur les tests, la livraison, le commit, le push ou la production.

## Règles d'activation

| Mode | Quand l'utiliser | Sortie |
|---|---|---|
| Intake Mode | Demande ambiguë ou incomplète. | Objectif clarifié, risques, contexte manquant et hypothèses sûres. |
| Full Rewrite Mode | Travail de dépôt substantiel. | Rôle, périmètre, workflow, vérification et règles de rapport final. |
| Verification Mode | Affirmation de réussite ou de préparation. | Preuves concrètes requises avant de déclarer l'achèvement. |
| Commit/Push Readiness Mode | Action Git, release ou PR. | Confirmation du périmètre, revue du diff, contrôles et liste d'actions Git finale. |

## Arbre de décision

1. Statut, liste ou courte explication -> répondre directement sauf si la demande est floue.
2. Objectif, périmètre ou critère de réussite flou -> Intake Mode.
3. Modification de fichiers, documentation, tests, scripts, CI ou structure -> définir périmètre et vérification avant édition.
4. Sécurité, confidentialité, secrets, production, release, commit, push ou PR -> Full Rewrite Mode plus Verification Mode.
5. Prompt réutilisable ou transfert d'agent -> Full Rewrite Mode.

## Ordre de workflow recommandé

1. Conserver la demande d'origine et les contraintes explicites.
2. Choisir le mode d'activation sûr le plus léger.
3. Définir objectif, périmètre, exclusions, risques et contexte manquant.
4. Réécrire complètement seulement pour un travail large, risqué ou réutilisable.
5. Définir les preuves de vérification avant l'exécution.
6. Aligner le rapport final sur le diff et la sortie des commandes.

## Sortie d'intake

```text
Objective:
[Concrete end state]

Risks and ambiguities:
- [Risk or missing detail]

Safe assumptions:
- [Assumption with reason]

Verification:
[Command, check or evidence required]
```

## Sortie Full Rewrite

```text
Role:
[Who the agent should be]

Objective:
[Concrete end state]

Repository context:
[Files, directories, docs or commands to inspect first]

Scope:
[What is in scope]

Out of scope:
[What must not be changed or claimed]

Workflow:
1. [First action]
2. [Next action]

Verification:
[Commands, manual checks or evidence required]

Final report:
[What to summarize]
```

## Règles anti-hallucination

- Utilise les fichiers, sorties de commande, textes d'issue ou sources citées comme preuves.
- Marque les faits inconnus avec `[UNKNOWN]`.
- Marque les conclusions non vérifiées avec `[ASSUMPTION: ...]`.
- N'invente pas de capacités d'outil, de modèle, d'API, de règles métier ou d'URL de dépôt.
- N'affirme pas que les tests passent sans sortie de commande exacte.
- N'ajoute pas de secrets, données réelles, URL internes ou logs de production.
- Préserve les chemins, commandes, noms de modèles et noms d'API sauf demande contraire.

## Critères de vérification

| Exigence | Preuve |
|---|---|
| Modifications intentionnelles | `git diff --name-only` relu |
| Tests réussis | Commande exacte et code de sortie |
| Liens de documentation valides | Sortie du validateur ou d'un link checker |
| Aucun secret ajouté | Sortie d'un scan de secrets ou du validateur |
| Réponse finale exacte | Résumé cohérent avec le diff et les sorties de commandes |

Si un contrôle n'est pas disponible, le rapport final doit le dire.

## Point d'attention

Avant l'exécution, l'objectif, le périmètre, les exclusions, les risques et les contrôles vérifiables doivent être explicites.

## Exemples

### Petite demande de statut

- Mode : réponse directe ou Intake Mode.
- Sortie : réponse courte, preuves et aucune modification de fichier.

### Demande de modification du dépôt

- Mode : Intake Mode, puis Full Rewrite Mode si le périmètre reste large.
- Sortie : workflow cadré, fichiers à inspecter, commandes de vérification et règles de rapport final.

## Contrôle qualité

- L'intention d'origine est conservée.
- Les critères de réussite sont mesurables.
- Les risques, hypothèses et faits inconnus sont visibles.
- Le mode choisi correspond à la demande.
- La réponse finale ne contient pas d'affirmation de réussite non vérifiée.
