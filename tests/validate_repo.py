"""Structure and evaluation-case validation for Thinking Outside; stdlib only."""
from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_skill() -> None:
    skill = ROOT / "SKILL.md"
    require(skill.is_file(), "missing SKILL.md")
    content = skill.read_text(encoding="utf-8")
    require(content.startswith("---\n"), "missing YAML frontmatter")
    parts = content.split("---\n", 2)
    require(len(parts) == 3, "incomplete YAML frontmatter")
    frontmatter = parts[1]
    require(re.search(r"^name:\s*thinking-outside\s*$", frontmatter, re.M) is not None, "invalid skill name")
    match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
    require(match is not None, "missing skill description")
    require(len(match.group(1)) <= 1024, "description too long")
    require("references/methods.md" in content, "methods reference not linked")
    require((ROOT / "references/methods.md").is_file(), "missing methods reference")


def validate_cases(path: str, expected: int, prefix: str) -> None:
    data = json.loads((ROOT / path).read_text(encoding="utf-8"))
    require(data["schema_version"] == 1, "wrong eval schema version")
    cases = data["cases"]
    require(len(cases) == expected, f"wrong count in {path}: {len(cases)}")
    require(len({item["id"] for item in cases}) == expected, "duplicate test ids")
    for i, item in enumerate(cases, 1):
        require(item["id"] == f"{prefix}{i:02d}", f"unexpected id {item['id']}")
        require(isinstance(item["prompt"], str) and len(item["prompt"]) >= 20, f"empty prompt in {item['id']}")
        for key in ("pass_criteria", "fail_examples"):
            value = item.get(key)
            require(isinstance(value, list) and len(value) > 0, f"missing {key} in {item['id']}")
            require(all(isinstance(s, str) and s.strip() for s in value), f"empty criteria in {item['id']}")


def validate_docs() -> None:
    required = [
        "README.md", "LICENSE", "CHANGELOG.md", "VALIDATION.md",
        "docs/specification.md", "docs/architecture.md",
        "docs/creative-methods.md", "docs/roadmap.md",
        "docs/compatibility.md", "evals/ACCEPTANCE_CASES.md",
        "evals/BENCHMARK_PROTOCOL.md",
    ]
    for name in required:
        require((ROOT / name).is_file(), f"missing {name}")
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for term in ("reframe", "feasib", "constraints", "generic"):
        require(term in text.lower(), f"skill missing essential guardrail {term}")


if __name__ == "__main__":
    validate_skill()
    validate_cases("evals/evals.json", 15, "T")
    validate_cases("evals/reserved-scenarios.json", 5, "H")
    validate_docs()
    print("PASS: skill structure, reference links, docs, 15 acceptance cases and 5 reserved cases.")
