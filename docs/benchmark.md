# Behavioral benchmark protocol

**No prompt written in a file counts as an executed agent test.** This project requires real model runs and independent evaluation, not synthetic score inflation.

## Conditions

A: base model without a creative skill. B: same model with the previous Thinking Outside. C: same model with the candidate. Compare Creative Ideation and Superpowers Brainstorming separately.

From the repository root, run `python scripts/benchmark.py benchmarks/core-plan.json`, followed by `python scripts/blind_review.py prepare benchmarks/runs/candidate-core`. Run the generated `review-plan.json` with the same executor, then use `blind_review.py summarize` on the original run directory. The judge is a model and its ratings are exploratory. Use a fresh output directory for each attempt and retain partial attempts separately. The executor expects UTF-8 and stops scheduling after a usage-limit error.

See the [benchmark results](benchmark-results.md) for evidence and limitations.

Keep prompts, model version, tool access and response budgets comparable. Run in clean sessions. Note any differences and confirm the skill actually loaded.

## Evaluation data

- Core cases: ../thinking-outside/evals/evals.json (canonical Skill Creator schema)
- Criteria: ../thinking-outside/evals/criteria.json
- Public additional examples: ../thinking-outside/evals/reserved-scenarios.json
- Activation and near misses: ../thinking-outside/evals/trigger-cases.json
- Genuine holdout prompts: not stored publicly; author independently after freezing candidate

## Ratings and report

Two human reviewers should judge anonymized outputs independently, with a mapping revealed only afterward. Rate 0–5 each on utility, originality of mechanism, diversity, feasibility and constraint adherence. Hard errors in safety, factual correctness or user constraints disqualify an output.

Review data format (JSON object):

    {
      "provenance": {"kind": "real", "review_kind": "human", "blinded": true,
                     "notes": "actual agent versions and environment"},
      "records": [
        {"case_id": 1, "round": 1, "reviewer": "rater-1",
         "condition": "baseline",
         "scores": {"utility": 3, "originality": 2, "diversity": 2,
                    "feasibility": 4, "adherence": 5},
         "critical_failure": false,
         "evidence": "path/to/actual-output.json",
         "evidence_sha256": "<SHA-256 of the file>"}
      ]
    }

Include one matching record for the Thinking Outside condition, for the same case, round and reviewer. Evidence paths are relative to the working directory and must remain inside it. Complete the full set before scoring.

For a holdout-only panel, put the frozen string case IDs in top-level `creative_case_ids` and use those IDs verbatim in the records. Score A/D and B/D separately with the appropriate control mapped to `baseline`. Use the same answer artifact digest for both reviewers of each case and round.

Run:

    python scripts/score_reviews.py evals/reviews.json

The program reports paired preference, critical failures and whether minimum review data requirements are satisfied. It does **not** verify the truth of provenance or issue a release.

## Provisional success criterion

At least five creative scenario families, 15 distinct case/repetition pairs scored by two reviewers on identical answer artifacts, and >=60% pairwise preference for Thinking Outside with ties worth half. No critical regressions on the 15 core tasks. Compare latency and token use if measured. Use fully unseen tasks before 1.0.

A claim of novelty or superiority is unsupported without these actual results.
