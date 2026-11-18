# Compatibility

| Client | Status |
|---|---|
| Codex CLI 0.169.0 | Explicit activation and use with a second skill confirmed in a resumed session. Direct probes stayed direct. The [project-local probe](../benchmarks/evidence/project-auto-probe.json) discovered the skill, but its reply reported blocked reading and omitted the body marker. Automatic loading remains unverified. |
| Claude Code 1.0.83 | Native activation unavailable. The fresh live probe returned insufficient credit. |
| OpenCode | Untested host behavior |
| Cursor | Untested host behavior |

For each client, copy the canonical thinking-outside/ directory into a supported skill location, using current official client documentation.

Record exact version, model, directory and whether automatic or explicit invocation loaded the skill. Run a creative case plus a no-ideation case (such as T13) and a safety/constraint case (T15 or T07). Preserve actual outputs and report failures.

For a manual Codex retry, use the same isolated project placement in an interactive session. Add a one-time body marker in a disposable copy, then send the creative prompt without naming the skill. Keep the actual marker out of the user prompt. Compare the result to a fresh explicit invocation and a direct arithmetic request. Record a native read trace or the marker before marking activation as verified. For supported Claude clients, use the [manual Claude prompts](claude-manual-check.md).

Do not claim universal compatibility merely because the YAML frontmatter parses successfully.
