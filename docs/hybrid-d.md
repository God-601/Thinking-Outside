# Hybrid D experiment

D is a 2,340-byte standalone entrypoint organized around Explore, Evaluate and Evolve. It borrows adaptive routing and reframing from B, causal deduplication and scoped-edit safeguards from C, later comparison with the conventional route from X, and multiple intervention points from Y. It does not combine their full prompts. The installed entrypoint remains C pending evidence.

Previous paired judging favored B over C on the corrected creative cases. X and Y raised originality and lowered diversity on a six-pair screen. These observations motivated the hybrid but do not show that any individual instruction transfers its measured benefit.

| Dimensions | What D does |
|---|---|
| Depth, creativity, surprise, context, contextual precision | Search at different intervention points. Ground a promising mechanism in actual actors, resources and constraints. |
| Selection, consistency, verifiable novelty | Remove causal duplicates. Compare value, novelty, feasibility and constraints. Verify precedents where relevant or qualify novelty. |
| Refinement, combination, interdisciplinary transfer | Repair the weakest assumption. Combine mechanisms to fill a gap. Transfer a causal rule and check where it breaks. |
| Efficiency, activation, skill integration | Choose the needed capability. Keep direct tasks direct, load methods on demand and leave implementation checks to domain skills. |

These are design choices. The benchmark measures answer quality and cost in aggregate. It cannot establish improvements on each of the 14 dimensions or native activation.

## Screening plan

[Run plan](../benchmarks/hybrid-screen.json) compares A/B/C/D using the same model, effort and prompts within this run. T03 and T11 check creative breadth. T06 and T15 check scoped editing and safety. B and C use their frozen instruction bundles. D uses the standalone entrypoint without optional reference loading. This is a comparison of complete prompt treatments. The earlier X and Y ablations isolate individual changes and remain separate.

Advance to a fresh-case screen if D has no critical issue, retains utility, feasibility and adherence within 0.25/5 of the stronger control and earns at least 50% preference versus B and C on the two creative cases. Promotion requires stronger evidence, including the existing 60% preference target and release gates. The blinded judge is automated.

## First screen

Codex CLI 0.169.0 ran GPT-6.1-Sol at medium reasoning. Sixteen answers and four blinded ratings groups completed. Topic-level ratings below are for T03 and T11. Cost and critical counts span all four tasks.

| Condition | Originality | Diversity | Mean input tokens | Mean output tokens | Mean time | Critical |
|---|---:|---:|---:|---:|---:|---:|
| A | 1.75 | 4.50 | 14,748 | 416 | 35.6 s | 0 |
| B | 1.75 | 4.00 | 18,501 | 455 | 37.4 s | 1 |
| C | 1.75 | 4.00 | 18,938 | 515 | 30.1 s | 0 |
| D | 2.00 | 4.25 | 15,190 | 481 | 32.3 s | 0 |

D won T03 and tied T11 against all controls under the weighted rubric. Compared with C, mean input fell 19.8%, but latency increased 2.2 seconds. In T06, D requested the missing code before the scoped edit. In T15, D declined to present an invented cipher as production-ready. The only critical flag was in B for omitting the minimal code request in T06.

Three fresh challenges were written after freezing D and before reading the triage scores. The fresh prompts cover accessible public services, manual production and acoustic performance. They use the same A/B/C/D controls. Keep D experimental if fresh preference falls below 60% against either skill control, if originality or diversity drops below the stronger skill control, or if a guardrail regresses. This follow-up compares only one response per condition per fresh case.

## Fresh cases and decision

The [fresh plan](../benchmarks/hybrid-fresh.json) completed 12 answers and three blinded ratings groups. [First-screen evidence](../benchmarks/evidence/hybrid-screen.json) and [fresh-case evidence](../benchmarks/evidence/hybrid-fresh.json) include the answers, ratings, rationales and input hashes. Raw CLI logs remain under local `benchmarks/runs/`.

| Condition | Utility | Originality | Diversity | Feasibility | Adherence | Input tokens | Output tokens | Mean time |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 4.50 | 2.33 | 4.00 | 4.50 | 4.83 | 10,146 | 820 | 75.5 s |
| B | 4.50 | 2.83 | 3.83 | 4.50 | 4.83 | 14,671 | 891 | 48.6 s |
| C | 4.00 | 2.50 | 4.33 | 4.00 | 4.33 | 18,199 | 1,085 | 54.0 s |
| D | 4.33 | 2.83 | 4.33 | 4.33 | 4.50 | 16,769 | 943 | 40.6 s |

D won the coral case, tied on manual production and lost the library case against each control. Its library response left the anonymous abandonment metric underspecified. No fresh response was flagged as critical. D matched B's originality and C's diversity. It used 7.9% fewer input tokens than C and 14.3% more than B. Measured tokens include host context and times reflect concurrent CLI runs.

Fresh creative preference reached 50% against each control, below 60%. Keep D and its evidence as experimental assets. Keep C as the installed entrypoint pending a repeatable quality improvement, blind human review, native compatibility checks and maintainer approval. This experiment supports the hybrid architecture's potential and the observed cost reduction against C. It does not establish gains in all 14 dimensions.
