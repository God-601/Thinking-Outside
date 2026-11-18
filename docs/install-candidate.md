# Install the 1.0 candidate

The candidate ZIP contains revised D as `thinking-outside/SKILL.md`, its three optional references and the MIT license. The repository's canonical entrypoint is still C. The ZIP is a local candidate for review.

1. Verify the SHA-256 from the accompanying checksum file. On Windows, use `Get-FileHash -Algorithm SHA256 .\thinking-outside-1.0-candidate.zip`.
2. Extract the archive and copy the entire `thinking-outside` directory to a skill folder. Keep the existing installation in a separate backup directory if there is a name conflict.
3. In Codex, use `.agents/skills/` in the project or the configured Codex skills folder. Start a fresh session and invoke `$thinking-outside`. For a direct-answer check, ask for one arithmetic result without naming the skill.
4. For a current Claude Code client, use `.claude/skills/` in the project or `~/.claude/skills/`. Start a fresh session and use `/thinking-outside`. Live verification in the available Claude Code client is blocked. See the [official Claude Code skill instructions](https://code.claude.com/docs/en/skills).

## Release draft

**Title:** Thinking Outside 1.0

The candidate introduces Explore for different causal mechanisms, Evaluate for choosing feasible and useful options, and Evolve for testing and refining an approach. Direct requests remain direct. Scoped edits request only the missing artifact needed to proceed. The ZIP installs without a separate runtime.

After the [release gates](release-readiness.md) pass and the maintainer approves, promote the exact reviewed entrypoint, confirm CI on the resulting commit, and attach the ZIP and its SHA-256 to the release. Rebuild the archive if the candidate changes and verify its extracted contents with `agentskills validate ./thinking-outside`.
