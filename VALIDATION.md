# Validation status — v1.0.0-rc.1 (prerelease)

The installed `thinking-outside/SKILL.md` contains the exact benchmark-pinned revised D candidate. Structural checks validate Agent Skills metadata, references, canonical evaluation inputs, scoring scripts and repository consistency. GitHub Actions runs the tests on Windows and Ubuntu.

**Automated behavior:** Codex CLI 0.169.0 with GPT-6.1-Sol (medium) compared no skill, the earlier B version, and revised D across eight creative task families with two repetitions. The pooled tie-adjusted automated preference favored D in 84.4% of pairs against no skill and 78.1% against B. One anonymized automated judge assessed results; this is not an independent human evaluation. The 15 canonical D checks returned 13 passes, two noncritical concerns and zero automated critical failures.

**Outstanding for stable 1.0:** two independent blind human reviews on matched outputs, additional client and automatic activation evidence, and maintainer review of limitations. Explicit Codex loading was verified using an isolated skill. The archived Claude Code run was blocked by insufficient credits. A user-supplied Sonnet 5.5 Medium manual marker test gives evidence for explicit loading but is not independently reproduced by the repository.

These results do not guarantee unique ideas, token savings or superiority in every model. Synthetic test fixtures do not establish behavior quality. Read the [audit](docs/review-1.0.md) and [stable release requirements](docs/release-readiness.md).
