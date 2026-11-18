# Final candidate validation

The candidate is the exact revised D tested in the last round. Its missing baseline and repeated-idea issues were already addressed. No further entrypoint change was made before this comparison. The earlier B/C/D runs remain archived. C still occupies the canonical install path on the PR, while the local candidate ZIP installs revised D.

## Comparison protocol

The final panel uses five families, two cases from the previous revised-D experiment and three additional prompts frozen before generation. Each has two independent generations per condition. A has no skill, B uses the pinned previous main bundle, and D uses its revised standalone instructions. The earlier responses used the same Codex CLI version, model and effort. They were scored in a four-arm panel including C. The new responses use a three-arm panel. Automated scores are reported separately as well as pooled so that panel effects remain visible.

## Results

Codex CLI 0.169.0 with GPT-6.1-Sol at medium reasoning completed 18 answers and six automated blind review groups in the [new batch](../benchmarks/final-fresh-plan.json). It covers 3D orientation, mono audio editing and education. Offline transactions and cooperative game design contribute 12 A/B/D answers from the [earlier repeated batch](../benchmarks/evidence/d-revised-fresh.json). The combined set has 30 answers and ten matched comparisons per pair.

| Comparison | New batch, wins/ties/losses | New batch preference | Pooled preference |
|---|---:|---:|---:|
| D vs A | 3 / 3 / 0 | 75% | 85% |
| D vs B | 1 / 4 / 1 | 50% | 70% |

Ties count as half. In the new batch, B and D both scored 2.67/5 on originality, 4.42 on utility and 4.17 on feasibility. D scored higher on adherence (4.75 vs 4.67) and lower on diversity (4.33 vs 4.58). In the first 3D repetition the judge identified several D options that all offered the same directional cue through different sensory channels. The second repetition included more distinct roles. This is a measured inconsistency in the outputs. A new deduplication rule would need its own matched test.

| Condition | New weighted score | New input tokens | New output tokens | New elapsed time | Pooled weighted score |
|---|---:|---:|---:|---:|---:|
| A | 3.99 | 16,358 | 1,033 | 58.4 s | 3.85 |
| B | 4.10 | 17,793 | 1,097 | 60.3 s | 3.95 |
| D | 4.06 | 19,922 | 1,127 | 62.1 s | 4.04 |

Figures are means per answer. D used 12.0% more input tokens than B in the new batch. CLI counters include host context and times reflect concurrent generation. The automated judge flagged zero critical failures. See the [full answers and ratings](../benchmarks/evidence/final-fresh.json).

D remains the strongest candidate on pooled weighted quality. Its 50% preference against B in the independent new batch falls below the target. Keep the tested entrypoint and archive intact for blinded human review. The promotion, native Claude and automated-use gates remain open.

## Independent review handoff

Reviewer 1 and Reviewer 2 each receive a Markdown packet with the same ten case-and-repetition groups, independently shuffled cases and answer labels. The answer key is separate. Share only one packet per reviewer. Each reviewer should score all answers on the five criteria and flag explicit critical failures independently. Do not send the key, public automated scores, or the other reviewer's notes until both are done. Average each reviewer's tie-adjusted preferences over the matched groups and report reviewer agreement, individual scores and any critical flags before considering approval.

The review packets are prepared locally. No human judgments have been collected. The two rounds of model review are automated screening evidence.

## Client and integration checks

Codex CLI 0.169.0 installed the extracted candidate ZIP in an isolated skill directory. A three-turn resumed session used 16,759 characters of initial approved constraints and field notes. The first turn returned the requested `OK`. The explicit third turn loaded the candidate and a second test skill, as established by two distinct markers absent from the prompts. The reply retained the no-phone, no-personal-data and no-new-sign restrictions and supplied a measurable rollback trigger. The [probe record](../benchmarks/evidence/final-native.json) includes the answers and CLI counters. The earlier arithmetic, scoped-edit and payments checks remain valid for this unchanged entrypoint.

Automatic selection was attempted in the resumed session and in a separate fresh creative request. Both answers announced an intention to use Thinking Outside, but neither supplied its body marker. The resumed answer reported a read restriction. Automatic loading remains unverified. Explicit invocation is verified for the installed test fixture. Claude Code 1.0.83 again returned `Credit balance is too low`, so native behavior remains unverified there.

The [installation guide and release draft](install-candidate.md) describe the candidate ZIP and promotion procedure. No files were installed into the user's global skill directory.
