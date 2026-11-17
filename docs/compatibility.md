# Compatibility

| Client | Status |
|---|---|
| Codex CLI 0.169.0 | Skill catalog discovery observed. Native full-instruction loading and automatic activation remain unverified. Controlled comparisons explicitly supply the instructions. |
| Claude Code 1.0.83 | Behavioral test unavailable. The CLI reported insufficient credits in the prior attempt. |
| OpenCode | Untested host behavior |
| Cursor | Untested host behavior |

For each client, copy the canonical thinking-outside/ directory into a supported skill location, using current official client documentation.

Record exact version, model, directory and whether automatic or explicit invocation loaded the skill. Run a creative case plus a no-ideation case (such as T13) and a safety/constraint case (T15 or T07). Preserve actual outputs and report failures.

Do not claim universal compatibility merely because the YAML frontmatter parses successfully.
