# Compatibility

| Client | Status |
|---|---|
| Codex CLI 0.169.0 | Explicit activation confirmed for an isolated revised D fixture. A direct math probe stayed direct. Automatic creative selection remains unverified. See the [activation evidence](../benchmarks/evidence/d-native-probe.json). |
| Claude Code 1.0.83 | Native activation unavailable. The fresh live probe returned insufficient credit. |
| OpenCode | Untested host behavior |
| Cursor | Untested host behavior |

For each client, copy the canonical thinking-outside/ directory into a supported skill location, using current official client documentation.

Record exact version, model, directory and whether automatic or explicit invocation loaded the skill. Run a creative case plus a no-ideation case (such as T13) and a safety/constraint case (T15 or T07). Preserve actual outputs and report failures.

Do not claim universal compatibility merely because the YAML frontmatter parses successfully.
