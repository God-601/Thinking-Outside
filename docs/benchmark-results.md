# Behavioral evidence for PR #4

The runner uses independent Codex CLI sessions, the same model and reasoning effort in each condition, shuffled generation order and a separate anonymized review. A has no skill. B uses the previous main. C uses the named snapshot for each run. The local `benchmarks/runs/` directory contains manifests, final outputs, raw JSONL, token counts and durations. Avoid publishing raw context or stderr without review.

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

## Publication

The 1.0 decision remains open pending review of the corrected A/B/C run, repeated results on unseen cases, the quality threshold, independent human reviews and verified native activation in Codex and Claude Code. Claude Code reported insufficient credits during the previous attempt. No stable tag or installation ZIP has been published.
