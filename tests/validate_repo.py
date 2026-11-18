"""Validate the installable Thinking Outside skill and eval data (stdlib only)."""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "thinking-outside"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def validate_frontmatter() -> None:
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    require(text.startswith("---\n"), "SKILL.md must begin with YAML frontmatter")
    chunks = text.split("---\n", 2)
    require(len(chunks) == 3, "frontmatter not terminated")
    fm = chunks[1]
    require(re.search(r"(?m)^name:\s*thinking-outside\s*$", fm) is not None, "incorrect name")
    require(SKILL.name == "thinking-outside", "name must equal containing directory")
    m = re.search(r"(?m)^description:\s*(.+)$", fm)
    require(m is not None and 1 <= len(m.group(1)) <= 1024, "invalid description")
    require("license: MIT" in fm, "expected MIT frontmatter")
    require(len(text.splitlines()) < 500, "SKILL.md exceeds 500 lines")
    references = re.findall(r"\]\((references/[^)#]+)\)", chunks[2])
    require(references, "missing references")
    for rel in references:
        require((SKILL / rel).is_file(), f"broken skill link: {rel}")
    for marker in ("reframe", "feasib", "constraints", "approved"):
        require(marker in text.lower(), f"missing guardrail: {marker}")
    require("generic" in text.lower() or "non-obvious" in text.lower(),
            "skill must guard against generic solutions")


def validate_evals() -> None:
    data = load_json("thinking-outside/evals/evals.json")
    require(data.get("skill_name") == "thinking-outside", "skill creator name mismatch")
    evals = data.get("evals")
    require(isinstance(evals, list) and len(evals) == 15, "expected 15 evals")
    ids = [e.get("id") for e in evals]
    require(ids == list(range(1, 16)), "eval ids must be 1..15")
    prompts = []
    for e in evals:
        require(isinstance(e.get("prompt"), str) and len(e["prompt"]) > 20, f"bad prompt {e['id']}")
        require(isinstance(e.get("expected_output"), str) and e["expected_output"], "missing expected_output")
        require(isinstance(e.get("expectations"), list) and len(e["expectations"]) > 0, "missing expectations")
        prompts.append(e["prompt"].strip().casefold())
    require(len(set(prompts)) == 15, "duplicate eval prompts")

    criteria = load_json("thinking-outside/evals/criteria.json")["cases"]
    require(len(criteria) == 15, "criteria count mismatch")
    require([c["id"] for c in criteria] == ids, "criteria ids do not match evals")
    for c in criteria:
        for key in ("pass_criteria", "fail_examples"):
            require(isinstance(c.get(key), list) and len(c[key]) >= 1, f"missing {key}")
    reserved = load_json("thinking-outside/evals/reserved-scenarios.json")["cases"]
    require(len(reserved) == 5, "expected five extra examples")
    require(len({c["id"] for c in reserved}) == 5, "duplicate extras")

    trigger = load_json("thinking-outside/evals/trigger-cases.json")
    yes, no = trigger["should_trigger"], trigger["should_not_trigger"]
    require(len(yes) >= 8 and len(no) >= 8, "insufficient trigger or negative tests")
    require(len(set(yes + no)) == len(yes + no), "duplicate trigger prompts")
    require(all(len(p) > 12 for p in yes + no), "trigger prompt too short")


def validate_docs() -> None:
    required = [
        "README.md", "LICENSE", "CHANGELOG.md", "VALIDATION.md",
        "docs/specification.md", "docs/architecture.md", "docs/creative-methods.md",
        "docs/roadmap.md", "docs/compatibility.md", "docs/benchmark.md",
        "docs/release-readiness.md", "scripts/score_reviews.py",
        "thinking-outside/evals/ACCEPTANCE_CASES.md",
        "thinking-outside/evals/BENCHMARK_PROTOCOL.md",
        "thinking-outside/references/methods.md",
        "thinking-outside/references/quality.md",
        "thinking-outside/references/examples.md",
    ]
    for filename in required:
        require((ROOT / filename).is_file(), f"missing required file: {filename}")
    require(not (ROOT / "SKILL.md").exists(), "skill at repo root is noncanonical")
    require(not (ROOT / "evals/evals.json").exists(), "old evals.json conflicts with canonical one")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "benchmarks" in path.relative_to(ROOT).parts:
            continue
        for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "#", "mailto:")):
                continue
            local = target.split("#", 1)[0]
            require((path.parent / local).exists(), f"broken local link in {path.relative_to(ROOT)}: {target}")


def validate() -> None:
    validate_frontmatter()
    validate_evals()
    validate_docs()


if __name__ == "__main__":
    validate()
    print("PASS: Agent Skills layout, links, docs, Skill Creator schema, 15 cases, 5 extras and 22+ trigger cases")
