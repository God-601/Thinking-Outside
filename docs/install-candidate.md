# Install Thinking Outside v1.0.0-rc.1

This is a **prerelease**, not the final stable 1.0. Its canonical `thinking-outside/SKILL.md` is the exact revised D used in the benchmark. Previous A/B/C/D fixtures stay in `benchmarks/instructions/`.

1. Download `thinking-outside-v1.0.0-rc.1.zip` and the matching `.sha256` file from the [GitHub prerelease](https://github.com/God-601/Thinking-Outside/releases/tag/v1.0.0-rc.1).
2. Verify integrity with PowerShell: `Get-FileHash -Algorithm SHA256 .\\thinking-outside-v1.0.0-rc.1.zip` and compare its value against the checksum file.
3. Extract the archive, preserving the single `thinking-outside/` folder and its `SKILL.md`, `references/`, and `LICENSE`.
4. For **Codex**, copy the folder to `.agents/skills/` in your project. Start a fresh session and explicitly invoke `$thinking-outside`.
5. For **Claude Code**, copy the folder to `.claude/skills/` in your project (or `~/.claude/skills/`). Start a fresh session and invoke `/thinking-outside`. See the [manual activation protocol](claude-manual-check.md).
6. In a separate fresh session, run a simple arithmetic request without invoking the skill to confirm the direct-answer route.

**Client limitations:** explicit Codex loading was verified; automatic loading remained unverified in the logged experiments. The logged Claude Code client was blocked by credits; a subsequent user-supplied Sonnet 5.5 Medium marker test supports manual explicit invocation. OpenCode and Cursor are unverified.

## Verification from source

```bash
python tests/validate_repo.py
python -m unittest discover -s tests -p "test_*.py" -v
# after installing skills-ref:
agentskills validate ./thinking-outside
```

## Release channel

The prerelease enables installation and broader evaluation while the [stable-release criteria](release-readiness.md) are still being satisfied. Two independent blind human reviews, more automatic-loading evidence and maintainer assessment of limitations remain outstanding.

For published measured evidence, read [review-1.0](review-1.0.md). The original evaluation artifacts and hashes are intentionally left unchanged.
