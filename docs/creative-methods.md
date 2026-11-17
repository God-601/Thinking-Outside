# Creative methods guide

The operative, concise method guide lives at [references/methods.md](../references/methods.md). This document adds illustrations for maintainers.

## Different mechanisms vs different skins

Weak alternatives: “smart inventory,” “AI inventory,” “social inventory.” All are still inventories.

Stronger divergent mechanisms for a short multiplayer match:

- **Information asymmetry:** players see different parts of the map, and success relies on negotiating or inferring missing information.
- **Changing incentives:** declaring a limitation before a match changes scoring and player risk choices.
- **Feedback loops:** overused routes become less efficient for the next round; careful calibration avoids unfair punishment.

These ideas are **examples**, not assertions of novelty or endorsements for a specific game.

## Reframing rule

Original request: “Add 50 daily quests to keep players returning.” Possible reframing: “If the goal is meaningful retention, variety of match outcomes may be more effective than a large daily chore system.” Provide the original design route as well as the alternative and explain why testing one before implementing 50 quests could be useful.

Do NOT reframe: “Change only the button color; preserve everything else.” The user has already provided a bounded and deliberate target.

## Avoid fake feasibility

Do not suggest a paid cloud inference pipeline for a zero-budget app as if it were free. If a clever approach requires extra components, disclose tradeoffs and suggest the simplest demonstrable prototype.
