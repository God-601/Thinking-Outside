#!/usr/bin/env python3
"""Summarize paired human ratings of real agent outputs; no AI calls.

Input JSON:
{
  "provenance": {"kind": "real" or "synthetic", "notes": "..."},
  "records": [
    {"case_id": 1, "round": 1, "reviewer": "r1",
     "condition": "baseline" or "thinking-outside",
     "scores": {"utility": 4, "originality": 3, "diversity": 3,
                "feasibility": 5, "adherence": 5},
     "critical_failure": false,
     "evidence": "path-or-link-to-actual-output"}
  ]
}
The comparison is a screening aid, NOT an automatic certificate for release.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

WEIGHTS = {"utility": .30, "originality": .20, "diversity": .20, "feasibility": .15, "adherence": .15}
CREATIVE = {1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14}


def score(record: dict) -> float:
    ratings = record.get("scores", {})
    if set(ratings) != set(WEIGHTS):
        raise ValueError("Each record must rate all five criteria")
    for key, value in ratings.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 5:
            raise ValueError(f"Rating {key} must be numeric from 0 to 5")
    if not isinstance(record.get("critical_failure"), bool):
        raise ValueError("critical_failure must be a boolean")
    return sum(ratings[key] * weight for key, weight in WEIGHTS.items())


def assess(data: dict) -> dict:
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        raise ValueError("Expected object with a records array")
    grouped = defaultdict(dict)
    critical = 0
    reviewers = set()
    evidence_missing = False
    for r in data["records"]:
        case = r.get("case_id")
        if isinstance(case, bool) or not isinstance(case, int) or case not in range(1, 16):
            raise ValueError("case_id must be an integer from 1 to 15")
        repetition = r.get("round")
        reviewer = r.get("reviewer")
        condition = r.get("condition")
        if isinstance(repetition, bool) or not isinstance(repetition, int) or repetition < 1:
            raise ValueError("round must be a positive integer")
        if not isinstance(reviewer, str) or not reviewer.strip():
            raise ValueError("A reviewer ID is required")
        if condition not in ("baseline", "thinking-outside"):
            raise ValueError("Condition must be baseline or thinking-outside")
        _ = score(r)
        critical += int(r["critical_failure"])
        reviewers.add(reviewer)
        if not isinstance(r.get("evidence"), str) or not r["evidence"].strip():
            evidence_missing = True
        key = (case, repetition, reviewer)
        if condition in grouped[key]:
            raise ValueError(f"Duplicate rating for {key}, {condition}")
        grouped[key][condition] = r
    if any(set(v) != {"baseline", "thinking-outside"} for v in grouped.values()):
        raise ValueError("Every case/round/reviewer must have both conditions")
    wins = ties = losses = 0
    creative_pairs = 0
    creative_families = set()
    for (case, _round, _reviewer), pair in grouped.items():
        if case not in CREATIVE:
            continue
        creative_pairs += 1
        creative_families.add(case)
        diff = score(pair["thinking-outside"]) - score(pair["baseline"])
        if diff > .15:
            wins += 1
        elif diff < -.15:
            losses += 1
        else:
            ties += 1
    preference = (wins + .5 * ties) / creative_pairs if creative_pairs else 0
    provenance = data.get("provenance", {})
    real = isinstance(provenance, dict) and provenance.get("kind") == "real"
    eligible = bool(real and not evidence_missing and critical == 0 and creative_pairs >= 15
                    and len(creative_families) >= 5 and len(reviewers) >= 2
                    and preference >= .60)
    return {
        "creative_pairs": creative_pairs, "families": len(creative_families),
        "reviewers": len(reviewers), "wins": wins, "ties": ties, "losses": losses,
        "pairwise_preference": round(preference, 4), "critical_failures": critical,
        "evidence_missing": evidence_missing, "real_data_claimed": real,
        "eligible_for_maintainer_review": eligible,
        "note": "Eligibility is NOT proof of unbiased evaluation or authorization to publish a release."
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", help="Human review JSON. No model calls are made.")
    args = parser.parse_args()
    data = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    print(json.dumps(assess(data), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
