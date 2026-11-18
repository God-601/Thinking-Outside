# Creativity regression investigation

The corrected 15-case Codex experiment found that the PR candidate lagged the previous main in originality (2.23 vs 2.40) and diversity (3.40 vs 3.50). Its feasibility (4.57 vs 4.47) and adherence (4.77 vs 4.67) improved. C won two of 12 creative comparisons against B, tied five and lost five. Tie-adjusted preference was 37.5%.

## What changed in the answers

| Case | Previous skill compared with PR candidate |
|---|---|
| Music, T03 | B included a delay used as a response and a separate stereo-space treatment. C mostly varied omissions, emphasis, groove and texture. The judge scored diversity 4.5 vs 4.0. |
| Retention, T04 | B offered choices involving risk and changes to the game world. C did more to challenge whether daily tasks were the right intervention, but most proposals stayed inside mission selection and reward delivery. Reframing improved from 2.5 to 4.0 while diversity fell from 4.5 to 3.5. |
| Local AI, T09 | C omitted B's use of small, task-specific transcription models. Three routes instead of four left more of the answer concentrated on general-purpose text models. |
| Interface, T11 | Both preserved context and suggested local feedback. B also distinguished empty states and accessibility barriers. C focused on four adjacent interaction improvements. Diversity fell from 4.5 to 3.5. |
| Game redesign, T10 | C distinguished five mechanisms, including exposing abandoned plans to an opponent and turning defeat history into terrain. Originality rose from 3.5 to 4.0 and diversity held at 4.5. |
| Scoped edit, T06 | C asked for the missing code and kept the change limited to the button color. The judge flagged B for omitting the code request. |

The recurring loss was fewer distinct routes in constrained tasks. The original benchmark changed the entrypoint and the methods reference together, so it could not identify the responsible lines. The historical example ablation had six pairs and did not establish that removing concrete examples caused harm. The main comparison did not inject optional examples in either condition. The earlier run with corrupted Portuguese is unsuitable for causal comparison.

## Isolated changes

Both variants start from the same PR candidate bundle. X delays consideration of the conventional route until after divergent drafting. This tests whether the opening instruction anchors exploration. Y changes the request to start from one bottleneck into an instruction to explore two intervention points with different causal moves. This tests whether the initial search is too narrow. Each variant replaces one paragraph. Examples, references, the direct edit safeguard, applicability rules, model and reasoning effort stay fixed.

The experiment repeats T03, T10 and T11 twice, covering losses in two domains and a prior win. A separate model session rates the shuffled outputs. A runtime change should earn at least 60% preference against C, improve mean originality and diversity, and avoid critical failures or a drop greater than 0.25/5 in utility, feasibility or adherence. These are screening criteria. A win on this small reused set still needs validation on fresh cases.

## Results and decision

Codex CLI 0.169.0, GPT-6.1-Sol at medium reasoning, completed all 18 answers and six anonymized judge sessions. The judge used the same model. See the [plan](../benchmarks/regression-isolation.json) and [scores with judge rationales](../benchmarks/evidence/regression-isolation.json). Raw runs and mappings are in the local `benchmarks/runs/regression-isolation/` directory.

| Instruction | Originality | Diversity | Utility | Feasibility | Adherence | Preference vs C |
|---|---:|---:|---:|---:|---:|---:|
| C, unchanged PR instructions | 2.25 | 4.58 | 4.58 | 4.67 | 5.00 | — |
| X, defer conventional route | 2.58 | 4.25 | 4.58 | 4.67 | 5.00 | 50.0% (1 win, 4 ties, 1 loss) |
| Y, vary intervention point | 2.50 | 4.33 | 4.50 | 4.67 | 5.00 | 41.7% (1 win, 3 ties, 2 losses) |

No critical failures were flagged. X improved ordinal originality at the cost of mechanism breadth. Y showed the same tradeoff and had lower overall preference. Y reported fewer input tokens in this batch (16,578 vs 18,108 for C), but took longer (36.4 s vs 31.5 s). A small change in instruction text cannot explain the measured context difference by itself.

Conventional-first drafting and single-bottleneck exploration are plausible contributors to lower originality in this sample. Changing either one alone did not recover originality and diversity together. The evidence therefore does not establish a single cause for the regression against B. Retain C's runtime instructions, including the scoped-edit safeguard, and keep both alternatives as experimental fixtures. The 1.0 gate remains unmet.
