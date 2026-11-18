# Benchmark quick start

See the complete instructions at ../../docs/benchmark.md.

- A: baseline agent without creative skill.
- B: same model with Thinking Outside from the previous main.
- C: same model with the candidate. Compare other skills separately where their purposes overlap.
- Run comparable prompts in separate clean sessions.
- Keep agent/model/version, tool access, budget and temperature consistent when possible.
- Record actual outputs and review blind with at least two human raters.
- Do not claim that CI structural validation proves creative improvement.

Use `python scripts/benchmark.py benchmarks/core-plan.json` from the repository root with an authenticated Codex CLI. Human judgments can be summarized with `scripts/score_reviews.py`. See the [benchmark results](../../docs/benchmark-results.md).
