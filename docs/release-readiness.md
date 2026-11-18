# 1.0 release gate — do not ship on structural tests alone

See the [final candidate audit](final-validation.md) and [installation guide](install-candidate.md). The automated benchmark, human review packets and distribution ZIP are separate deliverables. Completed structural checks do not satisfy the human or compatibility gates.

- [ ] Canonical thinking-outside directory passes the official Agent Skills validator.
- [ ] Unit and structural CI pass.
- [ ] Confirm actual installation and activation in Codex and Claude Code; name versions/models.
- [ ] Complete baseline-versus-skill behavior tests on the fifteen core scenarios.
- [ ] Repeated creative tests and genuinely unseen holdouts assessed blind by >=2 human reviewers.
- [ ] At least five creative problem families with meaningful benefit (provisional >=60% paired preference, ties weighted as half).
- [ ] Zero critical regression on safety, mathematical correctness, non-negotiable constraints or scope.
- [ ] Compare Creative Ideation and Superpowers when available and when objectives actually overlap.
- [ ] Read actual limitations, review costs/tokens when measured, verify install instructions.
- [ ] Human maintainer approves stable release with documented evidence.

If any mandatory criterion is unverified, keep the version labeled experimental or release-candidate. Do not tag or announce 1.0 based only on automated Markdown checks. A report produced from asserted data is not independently verified evidence.
