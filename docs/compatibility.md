# Compatibility status

This is an **Agent Skills-style** repository. SKILL.md uses YAML frontmatter with a lowercase hyphenated name and a plain description.

| Agent | Goal | Status |
|---|---|---|
| Codex | Discover and follow skill | Not tested |
| Claude Code | Discover and follow skill | Not tested |
| OpenCode | Discover and follow skill | Not tested |
| Cursor | Discover and follow skill | Not tested |
| Other Agent Skills-compatible hosts | Best-effort | Not tested |

## Test each host separately

1. Install the same directory according to the host's **current official** skill-loading documentation.
2. Record version, model, skill-loading path, flags and whether skill activation is explicit or automatic.
3. Verify that a creative request activates the intended behavior, and a narrow factual request does not create unsolicited brainstorming.
4. Run at least two samples from evals/evals.json; compare to no-skill runs.
5. Record omissions and incompatibilities rather than implying identical support.

**Important:** Installation path, activation and behavior vary by host. A markdown file alone does not grant new model capabilities, tools or private cross-session memory.
