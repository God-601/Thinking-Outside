# D revision

In the first Hybrid D experiment, the library answer satisfied access constraints but recycled familiar routes and lacked a way to distinguish a walk-away from a user who never found a free slot. The baseline B answer added preventive maintenance and defined anonymous counts. This is direct evidence about the answers. The instructions that produced the difference are a hypothesis.

Two short replacements address those gaps. Explore now switches to an overlooked failure or a transferable principle when the draft mostly repeats familiar fixes. Evolve defines an observable measure and baseline, and distinguishes failure types when they imply different interventions. The direct path, safety, causal deduplication, feasibility and scope safeguards are inherited from D. The original D snapshot remains available for reproduction.

The screen reruns the library prompt against the original D. Proceed to two fresh A/B/C/D challenges with two independent generations each if revised D improves baseline and measurement specificity without a critical failure or a weighted loss greater than the 0.15 tie margin. For promotion require fresh preference of at least 60% against each control, no critical failure and maintained feasibility and constraint adherence. Both studies use the existing five weighted criteria and a single anonymized automated judge. The screen tests the two adjacent changes together.

## Client activation

Codex CLI 0.169.0 ran an isolated copy of revised D with a one-time code in the skill body. The code was absent from both user prompts. With an explicit `$thinking-outside` request the response contained the code. A separate arithmetic request returned `92` without the code. The initial debug snapshot did not contain the full skill, and the exec stream did not expose a read event. The code response confirms access to the skill body on explicit invocation. This probe did not test automatic creative selection.

Claude Code 1.0.83 returned `Credit balance is too low` on a live probe. Native loading could not be tested there.

See the [Codex activation evidence](../benchmarks/evidence/d-native-probe.json).

## Small screen

The [paired screen](../benchmarks/d-revised-screen.json) completed two answers and one blind evaluation. Both versions scored 4.20/5 with no critical flag. Revised D specified five reference days, a denominator based on people who requested access, and separate counts before and during use. It also proposed preventing accessibility setup failures. Original D separated waiting and in-session abandonment but gave no explicit reference period. This cleared the measurement criterion. The single tie does not establish an overall quality gain. See [answers and scores](../benchmarks/evidence/d-revised-screen.json).

Two separate revised-D checks used the existing scoped-edit and payments prompts. In T06 it asked for the relevant code and kept the edit limited to color. In T15 it recommended established cryptography and provider infrastructure, and identified tests and review before production. These were inspected directly, without additional judge calls. See the [guardrail responses](../benchmarks/evidence/d-revised-guards.json).

## Fresh repeated benchmark

The [fresh plan](../benchmarks/d-revised-fresh.json) compared A (no skill), B (previous main), C (installed PR entrypoint) and revised D. Two new challenges, two repetitions and four conditions produced 16 successful answers. Four independent review sessions anonymized the conditions and used GPT-6.1-Sol at medium reasoning, the same model and effort as generation. The [evidence](../benchmarks/evidence/d-revised-fresh.json) contains answers, judge rationales, metrics and instruction hashes.

| Condition | Utility | Originality | Diversity | Feasibility | Adherence | Weighted | Input tokens | Output tokens | Seconds |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 4.00 | 2.63 | 3.50 | 4.25 | 3.75 | 3.63 | 17,118 | 1,173 | 55.7 |
| B | 4.00 | 2.88 | 3.75 | 4.13 | 3.88 | 3.73 | 16,235 | 1,221 | 60.2 |
| C | 4.00 | 3.38 | 4.50 | 3.75 | 4.13 | 3.96 | 18,990 | 1,305 | 78.4 |
| Revised D | 4.25 | 3.13 | 4.38 | 4.00 | 4.25 | 4.01 | 19,906 | 1,339 | 66.0 |

D won four of four creative pairs against A and B, and won two, tied one and lost one against C for 62.5% tie-adjusted preference. Against C it won both offline-order repetitions. In the cooperative game it tied one and lost one. The judge flagged no critical failures. D operationalized tests around known cases, the current process and measures of decision authorship. It still left error costs in the order flow underspecified, and some game mechanisms would let the strongest player retain control.

D had the best utility and adherence means. C retained higher originality and breadth, while A and B scored higher on feasibility. D used 4.8% more input tokens than C and 22.6% more than B in this batch, despite a smaller supplied entrypoint. It ran 12.3 seconds faster than C on average. CLI totals include shared host context, so the result demonstrates neither a prompt-only token cost nor a token saving in these runs.

Keep revised D as an experimental candidate and retain C as the installed entrypoint. Four pairs from two tasks are insufficient to confirm superiority across domains, especially with weaker originality and diversity than C and increased input cost. The 1.0 gate still requires more task families, independent human judging, native Claude verification and maintainer approval.
