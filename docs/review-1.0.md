# 1.0 review handoff

The candidate is the pinned revised D entrypoint. The candidate ZIP contains that exact file, its references and the MIT license. Its recorded SHA-256 is `a4d3db4ddd9fc9ea76f0acde3cf9af6eabb05d422675bfc3f5d0261a0a6c73c8`. The [installation and release draft](install-candidate.md) describes the archive and promotion. C remains the canonical install path on the review branch.

## Audit and compatibility

- A targeted variant grouped alternatives by functional role and allowed a distinct accessibility benefit to justify a channel variant. On a paired replay of F01 the two instruction sets proposed the same four functions and both scored 4.025/5. The variant remains a fixture. It is excluded from the ZIP.
- Human score screening now requires two reviewer IDs on each case and repetition, with the same answer digests. Unit checks cover disjoint reviewers and different answer files. Holdout IDs can be supplied explicitly, without relabeling them as core scenarios.
- Codex CLI 0.169.0 previously confirmed explicit activation, a direct-answer bypass, and use with a second skill in a resumed session. The new [project-local probe](../benchmarks/evidence/project-auto-probe.json) discovered an isolated ZIP installation in `.agents/skills/`. It announced the skill but reported a blocked read. No body marker or tool read was observed. Automatic loading remains unverified.
- Claude Code returned insufficient credit on the prior live check. Use the [manual Claude procedure and prompts](claude-manual-check.md) in a disposable project with a supported client and credits. Save client version, model and raw replies.

## Human review

Share one local review ZIP per reviewer. Each contains the same answer groups, shuffled independently, with prompts, criteria and a form. The mapping and exact answer artifacts stay with the coordinator. Reviewers should work independently and avoid the public model ratings until they submit.

The coordinator should decode the returned forms and run [paired scoring](benchmark.md) once for D vs A and once for D vs B. Use the frozen holdout IDs and identical answer hashes across reviewers. If a critical flag is disputed, keep the original ratings and record a separate adjudication. No human rating has been collected.

The two local ZIPs in `benchmarks/runs/distribution/review-1.0/` have 16 matched groups and 48 answers each. Every answer appears in both packets. `chave-privada.json` and `answers-private/` supply the exact item mapping and evidence bytes. They are outside both reviewer ZIPs. Run the scorer with the review directory as the working directory so the answer paths resolve.

## Final comparison

The new A/B/D batches ran the frozen revised D with Codex CLI 0.169.0, GPT-6.1-Sol, medium effort and two fresh sessions per arm on each of three new tasks. The [first two tasks](../benchmarks/evidence/pending-fresh.json) cover archive search and event flow. The [third task](../benchmarks/evidence/pending-extra.json) covers service recovery and brings the panel above the minimum 15 distinct pairs. The [one-phrase screen](../benchmarks/evidence/function-screen.json) is separate. Each case/round was judged anonymously by one automated reviewer.

| Comparison | New pairs, wins/ties/losses | New preference | All 16 pairs, wins/ties/losses | Pooled preference |
|---|---:|---:|---:|---:|
| D vs A | 4 / 2 / 0 | 83.3% | 11 / 5 / 0 | 84.4% |
| D vs B | 5 / 1 / 0 | 91.7% | 10 / 5 / 1 | 78.1% |

The pooled panel has eight task families, two repetitions and 48 answers across A/B/D. The earlier two-family batch used a four-arm judge panel, while later batches used three arms. The three-family batch immediately before this one reached 50% against B. Retain that result when interpreting consistency.

| Condition | New originality | Diversity | Utility | Feasibility | Adherence | Weighted | Input tokens | Output tokens | Mean seconds |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 2.58 | 4.17 | 3.83 | 4.08 | 3.92 | 3.70 | 16,352 | 1,072 | 61.5 |
| B | 2.67 | 4.08 | 3.75 | 4.00 | 3.75 | 3.64 | 19,332 | 1,076 | 67.7 |
| D | 3.00 | 4.42 | 4.17 | 3.83 | 4.17 | 3.93 | 15,277 | 1,054 | 58.9 |

D scored higher on originality, diversity, utility and adherence in this batch. It remained weaker on feasibility. Input tokens fell 21.0% versus B in the new batch, but pooled D used 18,176 versus 17,981 for B. The CLI totals include host context. The automated judge flagged no critical failures across the 48-answer panel.

The [core regression check](../benchmarks/evidence/d-core-checks.json) covers the exact revised-D entrypoint on all 15 canonical tasks. It reran the 13 missing tasks and reused T06 and T15 from the same instruction digest. Three automated rubric checks returned 13 passes, two concerns and zero critical failures. The concerns were limited reframing on retention and omitted UV guidance on a Blender-to-Roblox optimization task. The original corrected core comparison remains the source of A/B/C scores. These D checks are rubric checks, separate from preference comparisons.

## Release checklist

| Gate | Status |
|---|---|
| Five or more repeated task families and provisional 60% preference | Met in automated screening, including the newest batch. Human confirmation pending. |
| Safety, scope, arithmetic, resumed context and skill collaboration | Targeted checks passed. Revised D ran all 15 core tasks with no automated critical flag and two noncritical gaps. |
| Unit tests, Agent Skills structure, CI and archive digest | Verified. |
| Native Codex | Explicit invocation verified. Automatic body loading unverified. |
| Native Claude | Blocked on credits. Manual prompts ready. |
| Two independent blind human reviewers | Packages ready. Ratings pending. |
| Stable release | Draft notes and candidate ZIP ready. Promotion, merge and publication pending maintainer approval and the open gates. |
