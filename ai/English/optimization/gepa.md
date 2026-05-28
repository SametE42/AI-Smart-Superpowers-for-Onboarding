# GEPA Optimization

GEPA means Genetic-Pareto Prompt Evolution. In an agent repository, GEPA-style optimization can be used to improve prompts, skills, tool descriptions, command instructions, agent policies and evaluation rubrics.

## What to optimize

- Prompt instructions
- Skill instructions
- Tool descriptions
- Model routing rules
- Agent role definitions
- Evaluation rubrics
- Repository documentation workflows

## Optimization loop

1. Define a measurable task.
2. Run baseline attempts.
3. Score outputs with an evaluation rubric.
4. Reflect on failures in natural language.
5. Mutate the textual artifact.
6. Keep Pareto-useful variants.
7. Re-test against regression cases.
8. Promote only reviewed improvements.

## Repository rule

Do not optimize blindly. Every optimization run must record input task, baseline, metric, changed artifact, score delta, known regressions and human approval status.
