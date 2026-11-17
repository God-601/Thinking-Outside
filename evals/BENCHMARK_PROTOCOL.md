# Benchmark protocol — no results yet

## Purpose

Test whether Thinking Outside increases **useful divergence** without hurting correctness, constraints or safety.

## Conditions

- A: same model, no creative skill.
- B: same model with Creative Ideation (if legally/technically available).
- C: same model with Superpowers Brainstorming (where task fits its purpose).
- D: same model with Thinking Outside.
- Keep model/version, prompt, tool access, temperature where configurable, task time and output budget comparable. If not possible, record the mismatch.
- Run each comparison in a fresh session or controlled equivalent. Avoid sharing previous generated answers across conditions.
- Randomize presentation order of anonymized outputs. Human raters should not see condition labels.
- Do not copy proprietary skills or silently merge their instructions into ours.

## Phases

1. Pilot on T01, T04, T07, T10, T13: one run per feasible condition to identify obvious failures.
2. Full 15-scenario test. Repeat creative cases at least three times when resource limits permit; document reduced sample sizes.
3. Independently author **unseen** holdout cases after freezing skill version. The public reserved-scenarios.json is not a secret holdout.
4. Evaluate mixed-domain results; look for regressions in simple tasks and prohibited advice.

## Rubric

Rate 0–5 on:
- utility and causal mechanism;
- novelty relative to baseline, **without claiming global originality**;
- diversity of mechanisms (for multi-idea prompts);
- feasibility under hard constraints;
- adherence to user preferences/constraints;
- correct/appropriate reframing;
- clarity and economy.

For direct/factual tasks, assess correctness and scope rather than pressuring for novelty. For safety-critical tasks, violating a hard rule disqualifies the run.

**Provisional target:** >=60% human pairwise preference for Thinking Outside over baseline on creative prompts, no critical regressions, and cost increases justified by improvement. This is a chosen gate, **not** an empirical result or universal benchmark.

## Log template per run

| Field | Record |
|---|---|
| Scenario ID | Txx/Hxx/unseen |
| Condition | A/B/C/D |
| Agent, version, model | Exact identifiers |
| Date | ISO date |
| Skill loaded? | Verified / uncertain / no |
| Full response | Stored or privacy-safe location |
| Tool access and settings | Relevant differences |
| Constraint violation | Yes/no + evidence |
| Human scores | Individual 0–5 ratings |
| Evaluator notes | Strengths and problems |
| Input/output tokens and time | Only if measured; otherwise unavailable |

Never substitute one assistant writing hypothetical answers for independent executions, and never present static linting as model-behavior proof.
