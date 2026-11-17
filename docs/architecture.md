# Architecture — minimal, testable, extensible

~~~text
User goal + constraints
        |
Agent discovers SKILL.md (if supported)
        |
  Route task: direct / improve / explore / reframe
        |
  Optionally read references/methods.md
        |
  Critique mechanisms, feasibility and constraint adherence
        |
  User-facing result / request for approval on material scope change
~~~

## Why a small skill first

The original idea is a **thinking behavior**, not a dashboard. Keeping it in SKILL.md with one methods reference lets us test the incremental effect against the base model before adding layers that could obscure causality or waste context.

The skill does not intercept other agents, read their private states, force method invocation or persist memory. The host agent decides whether/when to load the instructions according to its own skill mechanism.

## Optional future components — NOT adopted

- Method retrieval based on task type (after usage evidence).
- Curated examples of high-quality vs generic ideas.
- Benchmark utilities (if evaluation volume justifies it).
- Domain-specific companion guides (only if general behavior fails in a documented domain).

## Integration boundaries

Thinking Outside supplies **creative candidate generation and critique**. A Blender, Roblox, programming or safety skill remains authoritative for technical validation, format requirements, and domain-specific safe practice. Real-world facts require sources; creativity cannot replace checking.
