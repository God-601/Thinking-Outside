# Compatibility targets (not verified)

| Client | Status |
|---|---|
| Codex | Untested host behavior |
| Claude Code | Untested host behavior |
| OpenCode | Untested host behavior |
| Cursor | Untested host behavior |

For each client, copy the canonical thinking-outside/ directory into a supported skill location, using current official client documentation.

Record exact version, model, directory and whether automatic or explicit invocation loaded the skill. Run a creative case plus a no-ideation case (such as T13) and a safety/constraint case (T15 or T07). Preserve actual outputs and report failures.

Do not claim universal compatibility merely because the YAML frontmatter parses successfully.
