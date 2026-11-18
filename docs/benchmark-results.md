# Behavioral evidence for PR #4

The runner uses independent Codex CLI sessions, the same model and reasoning effort in each condition, shuffled generation order and a separate anonymized review. A has no skill. B uses the previous main, commit `f41c4d0`. C uses the named snapshot for each run. The main comparison provides the entrypoint, methods and quality references in B and C. Optional examples are exercised separately. The local `benchmarks/runs/` directory contains manifests, final outputs, raw JSONL, token counts and durations. Raw context and stderr are excluded from published evidence.

## Prior runs

| Run | Observed outcome | Interpretation |
|---|---|---|
| Example ablation | 24 responses and six reviews across three tasks and two repeats. The earlier example-free candidate scored 4.13/5 versus 4.18 for B, 4.11 with abstract examples and 4.21 with concrete examples. | A single automated judge and many ties. No general evidence that adding or removing examples improves creativity. |
| Original core A/B/C | 45 responses and 15 reviews. The earlier C earned 66.7% creative preference against A and 37.5% against B, counting half credit for ties. | The plan supplied mojibake in Portuguese. Excluded from release decisions, retained for audit. |
| Prior clean UTF-8 attempt | 7/45 responses completed. 38 quota failures. | Unbalanced. No valid paired comparison. |
| Independently authored holdout | 58/60 responses. Two timeouts. A retry of both matched groups returned four responses and two failures. | Earlier C snapshot. Full matched review pending. |
| Other skills | Eight responses across two tasks with A, C, Creative Ideation and Superpowers Brainstorming. | No scored comparison. |
| Codex native probes | The skill was discovered. Math and translation received direct responses. The four audited prompts did not contain the full skill text, and no file-read events established that it loaded. | Discovery and direct responses confirmed. Activation remains unverified. |

The historical judge marked T06 as a critical failure in all three conditions because each requested the button and desired color without requesting the minimum missing code. The candidate now explicitly asks for the smallest missing artifact when it cannot inspect a requested edit. This did not establish a safety failure in the exploratory set.

Input token counts varied substantially between otherwise identical repetitions. Raw CLI counters and wall-clock times are retained. Neither the earlier ablation nor the corrupted run establishes token savings. The candidate avoids reading the example reference until it needs to diagnose duplicate mechanisms.

## Corrected Portuguese comparison

Codex CLI 0.169.0 ran `gpt-6.1-sol` at medium reasoning. The corrected core batch completed 45/45 responses across the 15 canonical scenarios. A separate sample reused two independently authored holdout cases, with two repetitions in each of the three conditions (12/12 responses).

| Condition | Mean input tokens | Mean output tokens | Mean seconds |
|---|---:|---:|---:|
| A, no skill | 16,811 | 607 | 36.8 |
| B, previous main | 18,855 | 683 | 40.1 |
| C, candidate | 20,510 | 668 | 45.9 |

These are CLI totals and elapsed times from the corrected core run. C consumed 8.8% more input tokens than B in this setup. The totals include shared host context and can vary without a change in the supplied text.

The anonymized judge was a separate Codex session using the same model for each comparison. The five criteria use the published weights.

| Condition | Utility | Originality | Diversity | Feasibility | Adherence | Weighted |
|---|---:|---:|---:|---:|---:|---:|
| A | 4.33 | 2.07 | 3.33 | 4.40 | 4.67 | 3.74 |
| B | 4.50 | 2.40 | 3.50 | 4.47 | 4.67 | 3.90 |
| C | 4.50 | 2.23 | 3.40 | 4.57 | 4.77 | 3.88 |

Across the 12 cases categorized as creative, C earned 75% preference versus A (7 wins, 4 ties, 1 loss) and 37.5% versus B (2 wins, 5 ties, 5 losses). A tie counts half. The candidate improved feasibility and constraint adherence over B, but its originality and diversity scores were lower. In T04, the judge rated C's reframing 4/5, versus 3/5 for A and 2.5/5 for B. C asked for the minimum missing code in T06. The judge found one critical failure, in B for T06.

On the two reused holdout cases, C earned 50% versus A and 37.5% versus B across four comparisons. This small sample does not establish generalization. It is also not an unseen set for a future release.

## Publication

The candidate missed the 60% creative preference target against B and used more input tokens. Stable release still requires improved results on genuinely unseen cases, independent blind reviews by two people, verified native activation in Codex and Claude Code, and maintainer approval. A fresh Claude Code probe returned `Credit balance is too low`. No stable tag or installation ZIP has been published.
