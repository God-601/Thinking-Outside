---
name: thinking-outside
description: Use for requests seeking non-generic ideas, unconventional but feasible solutions, creative improvements, alternate approaches to persistent problems, or reframing limiting assumptions. Applies across domains (software, games, design, music, business, study). Adapt exploration and filtering to the task. Do not force brainstorming on simple, factual or tightly scoped requests.
---

# Thinking Outside

**Purpose:** Help the agent find *better* solutions by exploring non-obvious, distinct, useful and feasible mechanisms—not just longer lists of ideas. Complement domain-specific instructions; do not override user choices, safety rules, evidence standards or other skills' technical constraints.

## Routing: choose effort by task, not by a rigid script

- **Direct:** clear factual, narrowly scoped, or safety-critical task. Answer accurately; no needless ideation.
- **Improve:** existing design/solution works; preserve approved elements and explore targeted, practical improvements.
- **Explore:** user explicitly seeks ideas or alternatives. Generate structurally different approaches, then filter.
- **Reframe:** repeated failure, hidden assumption or symptom-as-problem suggests a better problem formulation. Offer both the requested path and a justified alternative; ask approval before changing key goals.
- If information is missing, ask only a question that would materially change the result. Otherwise state a minimal assumption and proceed.

## Procedure — scale depth to value

1. **Frame:** identify real goal, audience, hard constraints, rejected ideas, resources and what success means. Respect past decisions in available context.
2. **Challenge selectively:** ask “What might we be assuming without evidence?” and “Are we solving the cause or a symptom?” Reframe **only if** it plausibly improves the outcome. Do not quietly substitute a new task.
3. **Diverge:** choose 1–3 fitting moves from [methods](references/methods.md): first principles, reversal, lateral thinking, SCAMPER, TRIZ-style contradiction resolution, distant analogies, systems thinking, or morphological recombination. Seek distinct causal mechanisms, not cosmetic renaming.
4. **Critique:** remove repeats, unverifiable uniqueness claims, infeasible options, unnecessary complexity and contradictions with hard constraints. Check actual user benefit. For current market novelty or technical claims, research if tools are available; otherwise label as hypotheses. Creative ideation is not proof.
5. **Converge:** deliver useful options with how each works, why it is different, benefit, feasibility and key tradeoff where relevant. Respect requested count when possible; never pad weak ideas. Recommend next validation step when helpful.

## Quality guardrails

- **Non-generic:** an idea needs an actual mechanism, not a buzzword, product name or generic feature.
- **Feasibility-first:** unconventional is valuable only when executable within the stated constraints. Experimental speculation must be labeled and must not displace feasible answers.
- **Respect scope:** do not redesign approved components or change requirements without permission.
- **No fabricated novelty:** “No competitor exists” is never inferred from not knowing a competitor.
- **No false certainty:** distinguish proposal, hypothesis, verified fact and performed test.
- **Evidence over flair:** for high-stakes issues favor validated conventional practice, not invented solutions.
- **Efficiency:** do not show verbose internal technique names or an evaluation spreadsheet unless requested; make the output proportional to the task.
- **Other skills:** use this skill to widen *candidate approaches*, then defer technical validation and execution to domain-specific skills and tools.

## Output defaults

- **Idea request:** distinct idea + mechanism + concrete user benefit + feasibility caveat (compact).
- **Problem-solving request:** probable assumptions, 2–3 materially different strategies if warranted, recommended diagnostic/experiment.
- **Reframe:** “You asked X; if the real goal is Y, Z may work better because ...” and preserve the original option.
- **Simple task:** direct answer; skip the creativity framework.

**Do not claim** that this skill makes the model smarter, inherently more original or reliably superior without comparative evaluation.
