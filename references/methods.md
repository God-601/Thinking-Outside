# Creative method selection (reference)

Use **only** methods that materially help the task. Avoid mechanical checklists and name-dropping methods.

| Method | Best for | Agent move | Common failure |
|---|---|---|---|
| First principles | Complexity inherited from conventions | Separate immutable requirements from assumptions; rebuild minimal mechanism | Rebuilding well-tested safety standards |
| Reversal / inversion | Stuck approaches | Ask what causes failure; reverse incentives or sequence | Treating inversion as useful automatically |
| Lateral thinking | Idea diversity | Change relationship, role, medium or scarce resource | Weird names with unchanged mechanics |
| SCAMPER | Improving existing systems | Substitute/combine/adapt/modify/repurpose/eliminate/rearrange | Random novelty that violates constraints |
| TRIZ-inspired contradictions | Two objectives in tension | State conflict explicitly; consider separation in time, space, condition or scale | Pretending to have formally solved engineering constraints |
| Distant analogy | Crossing disciplines | Map source mechanism to target; test transfer limits | Metaphor without executable mechanism |
| Systems thinking | Feedback and unintended consequences | Map incentives, bottlenecks and loops; check second-order effects | Massive systems with no viable MVP |
| Morphological combination | Multiple design dimensions | Combine independent axes to reveal alternatives | Combinatorial noise |
| Problem reframing | Persistent failure or misguided metric | Distinguish surface request from actual desired outcome | Ignoring user's stated objective |
| Constraint-driven design | Budget/time/performance limits | Treat a hard limit as a design input; simplify mechanism | Quietly removing the hard limit |

## Adaptive selection examples

- User asks for eight original game mechanics -> lateral thinking + reversal + incentive/feedback analysis; reject ideas whose only difference is theme.
- User asks for a small UI change -> no method needed. Make exact change.
- User asks to improve appearance of low-poly asset -> first principles of perception + constraint-driven design; preserve poly budget.
- User repeatedly fails to fix a bug -> look for assumptions about root cause; generate competing diagnostics, not speculative rewrites.
- User asks for profitable “unique” product -> research competitors if possible; distinguish unmet job from branding; validate willingness to pay.

## Novelty check

For each candidate, ask: (1) What physically/algorithmically happens? (2) What decision or experience changes for a real user? (3) How does this mechanism differ from the others? (4) What is cheapest safe test? (5) Which constraints might invalidate it?

A strong answer may offer fewer options than the internal brainstorm. Do not present hidden exploration as factual research or performed testing.
