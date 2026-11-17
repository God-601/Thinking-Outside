---
name: thinking-outside
description: Adaptive out-of-the-box thinking for AI agents. Use for non-generic ideas, unconventional but feasible systems, creative improvements, alternative ways to solve persistent problems, and useful reframing of assumptions in software, games, design, music, business, education, or everyday life. Avoid unnecessary brainstorming for simple factual or strictly scoped tasks.
license: MIT
---

# Thinking Outside

**Objective:** Find better, less obvious, **workable mechanisms** for the user's actual goal. Not merely more ideas, not random novelty, and never an unverified claim of uniqueness.

## Choose effort and method according to the task

- **Direct:** clear factual, tightly scoped or safety-critical task. Answer accurately; do not force brainstorming.
- **Improve:** preserve approved or working parts; explore small targeted improvements with real benefit.
- **Explore:** user wants ideas; seek structurally different mechanisms before selecting.
- **Unstick:** approaches keep failing; identify competing hypotheses and diagnostic experiments instead of speculative rewrites.
- **Reframe:** a hidden assumption or symptom-as-problem suggests a better path; offer the requested path **and** an alternative with a clear reason. Ask before changing key goals, budget or decisions.

Do not force five-level classifications or long steps on every request. Reply in the user's language and preferred level of detail.

## Understand the request

Extract goal, audience, hard constraints, approvals, rejected ideas, prior failures, available resources and success criteria.

Ask a targeted question only if the missing information could materially change the answer. Otherwise state modest assumptions and continue; never re-ask already answered questions available in context.

## Explore beyond the obvious

Consider what conventional answers would suggest. When the user rejects generic ideas, deliberately search for *different causal mechanisms* (what happens, what decisions change), not new branding, theme or buzzwords.

Select one or a few relevant techniques from [methods](references/methods.md): first principles, lateral thinking, inversion, SCAMPER, TRIZ-inspired contradiction resolution, distant analogies, systems feedback, recombination and constraint-driven design.

Scale exploration to complexity and importance. Do not overthink a trivial request or waste context on decorative idea lists.

## Question assumptions carefully

When it might help, ask whether the request addresses a symptom rather than the real objective, or whether a convention is an actual requirement. A reframe should earn its place by offering concrete benefit.

**Do not silently replace the goal.** Preserve a viable route to the stated request and request approval before material changes. A possible cause is a hypothesis, not a diagnosis.

## Filter and select adaptively

Check each promising idea:
1. **Mechanism:** how does it actually work?
2. **Diversity:** is it causally different from other ideas?
3. **Usefulness:** who benefits, and how?
4. **Feasibility:** does it meet budget, platform, hardware, time, safety and domain constraints?
5. **Evidence:** is novelty or expected impact researched, or a hypothesis?

Discard repetitive, generic, infeasible, unsupported and needlessly complex proposals. Research precedents when market originality matters and tools exist; otherwise disclose uncertainty. No promise of no competitors or guaranteed virality.

Select ideas for usefulness and fit, not drama. Respect a requested number when good options exist; never pad the list with weak variations.

## Output

- Idea request: distinct mechanism, practical benefit and tradeoff; concrete test when useful.
- Persistent problem: focused diagnosis and alternate approaches, without overwriting working systems.
- Reframing: compare requested approach and alternative briefly; preserve user agency.
- Simple request: answer directly.

Use specialized skills and tools for technical validation, source checking and implementation. Creativity never overrides safety, higher-priority instructions or approved constraints.

Do not assert that this skill changes model intelligence, guarantees originality or beats competing skills without controlled evidence. See [quality checks](references/quality.md) and [worked examples](references/examples.md) only when needed.

# Creative methods — select, do not ritualize

| Method | Best for | Agent move | Avoid |
|---|---|---|---|
| First principles | Costly inherited assumptions | Separate goals, constraints, conventions; rebuild essentials | Replacing validated safety standards |
| Inversion | Stuck strategies | Reverse incentive, actor, timing or sequence | Reversal only for novelty |
| Lateral thinking | Repetitive ideas | Alter the resource, interaction or feedback rule | Cosmetic renaming |
| SCAMPER | Improve a working idea | Substitute, combine, adapt, modify, repurpose, eliminate, reverse | Breaking approved parts |
| TRIZ-inspired contradictions | Conflicting goals | Separate constraints in space, time or conditions | Pretending to have a formal proof |
| Distant analogy | Saturated category | Transfer a mechanism from another field and test its limits | Metaphor without mechanism |
| Systems thinking | Multiple actors and feedback | Examine incentives, second-order effects, equilibria | Unbounded architecture |
| Morphological recombination | Independent design axes | Vary inputs, rules, feedback and actor roles | Combinatorial noise |
| Problem reframing | Means confused with outcome | Compare original request with real job-to-be-done | Replacing user goal |
| Constraint-driven design | Hard budget/performance limits | Use the limitation to guide simplification | Hidden extra dependencies |

## Examples of selection

- Non-generic game mechanics: inversion + feedback + asymmetric information.
- Change one UI button color: no creative method; make the bounded change.
- Repeated movement bug: competing diagnostics and assumptions; no invented root cause.
- Realistic 3D under 3,000 triangles: perception-first materials/normals/UV and constraint-driven choices.
- Original commercial product: user problem, competitor research where possible and smallest validation.
- No cloud budget: local-first design within hardware capabilities.

Question every serious candidate: what happens, who benefits, how does it differ, what is the cheapest test, what would falsify it?

# Quality checks

Reject or revise these failure patterns:

- Cosmetic originality: multiple brand names for the same feature.
- Complexity theater: elaborate agents, databases or services for a small problem.
- Fake market novelty: assuming no competitors because no one was searched.
- Constraint evasion: extra polycount, paid API when budget is zero, or changes to approved UI.
- Speculative certainty: diagnosing a bug, safety claim or revenue without evidence.
- Forced reframing: replacing an explicit bounded request with a redesign.
- Quota padding: weak ideas added solely to meet a requested count.
- Insecure experimentation: invented cryptography for real financial systems.

A selected idea needs a mechanism, concrete user benefit and honest feasibility tradeoff. When useful, include a minimal test.

When another technical skill is available, Thinking Outside contributes candidate approaches; the domain skill owns implementation validation. Do not require or expose hidden chain-of-thought.
