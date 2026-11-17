# Thinking Outside — Functional specification

**Version:** 0.1.0 experimental. **Owner:** project maintainers. **Phase:** first implementation; behavior not yet benchmarked.

## Goal

Guide an AI agent to explore feasible, unconventional solutions and challenge a problem's framing **when doing so improves the user's actual goal**. Work across domains without assuming that every task requires brainstorming.

## Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| BB-01 | Support multiple domains | Must |
| BB-02 | Adapt creative effort and methods to task | Must |
| BB-03 | Explore meaningfully non-obvious mechanisms | Must |
| BB-04 | Use established creative techniques selectively | Must |
| BB-05 | Filter generic or duplicate mechanisms | Must |
| BB-06 | Respect all hard user constraints and earlier decisions | Must |
| BB-07 | Challenge assumptions when there is a concrete benefit | Must |
| BB-08 | Preserve original goal; ask before material reframing | Must |
| BB-09 | Select feasible options or label experimental ones clearly | Must |
| BB-10 | Ask clarifying questions only if consequential | Must |
| BB-11 | Complement other installed skills | Must |
| BB-12 | Avoid extra complexity on direct/factual requests | Must |
| BB-13 | Research precedents when novelty matters and sources exist | Should |
| BB-14 | Explain mechanisms and benefits instead of branding | Must |
| BB-15 | Be economical with agent context and output | Should |
| BB-16 | Avoid retrying previously rejected proposals | Must when context available |
| BB-17 | Identify next practical validation step when helpful | Should |

## Operating contract

1. Detect intent: direct / improve / explore / reframe.
2. Identify goal, non-negotiable constraints and prior rejected ideas.
3. Select a minimal creative method mix. No fixed five-level score or long mandatory questionnaire.
4. Generate alternative **mechanisms** and test them against constraints.
5. Reframe only if its benefit is explainable. Keep the original request visible.
6. Deliver appropriately sized results; no padding or unsupported uniqueness.

## Nonfunctional requirements

- Runs as text skill in Agent Skills style; **no mandatory server, API, model or paid dependency**.
- Portability is a goal, not an assertion of verified compatibility with every client.
- Must never override system safety, user approvals or domain expertise.
- No persistent personal memory is implied; only context actually available may be used.
- Do not represent intent as implementation, tests as passed or opinions as market facts.
- Do not promise creativity gains without A/B evidence.

## Non-goals for v0.1

Build a custom model; autonomous market research in absence of tools; memory service; Windows app; MCP infrastructure; hidden code execution; automatic modification of the user's project; ranking all ideas using rigid universal scores.

## Acceptance

- Structure checks pass.
- 15 documented test scenarios + 5 reserved open scenarios exist.
- Behavioral A/B compares agent baseline to skill on identical prompts, then competitors where available.
- Human evaluators prefer the skill sufficiently often **without regressions** on safety, constraints or direct tasks. Thresholds are hypotheses in benchmark protocol.
