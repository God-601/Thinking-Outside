"""Unit tests for review scoring. Synthetic fixtures are NOT model benchmarks."""
import sys
from pathlib import Path
import unittest
import tempfile
import hashlib

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from score_reviews import assess, score


def make_review(kind="synthetic", fail=False, missing=False):
    records = []
    for case in (1, 2, 3, 4, 5):
        for repetition in (1, 2, 3):
            for reviewer in ("a", "b"):
                for condition, value in (("baseline", 2), ("thinking-outside", 4)):
                    records.append({
                        "case_id": case, "round": repetition,
                        "reviewer": reviewer, "condition": condition,
                        "scores": {key: value for key in
                                   ("utility", "originality", "diversity", "feasibility", "adherence")},
                        "critical_failure": bool(fail and case == 1 and repetition == 1 and condition == "thinking-outside"),
                        "evidence": "" if missing else f"runs/{case}/{repetition}/{reviewer}/{condition}.md"
                    })
    return {"provenance": {"kind": kind}, "records": records}


class QualityTest(unittest.TestCase):
    def test_score_weights(self):
        scores = {key: 5 for key in ("utility", "originality", "diversity", "feasibility", "adherence")}
        self.assertEqual(score({"scores": scores, "critical_failure": False}), 5.0)

    def test_synthetic_cannot_pass_release_gate(self):
        result = assess(make_review())
        self.assertEqual(result["creative_pairs"], 30)
        self.assertEqual(result["pairwise_preference"], 1.0)
        self.assertFalse(result["eligible_for_maintainer_review"])

    def test_claiming_real_without_evidence_cannot_pass(self):
        self.assertFalse(assess(make_review(kind="real"))["eligible_for_maintainer_review"])

    def test_verified_blind_human_records_eligible_for_review(self):
        data = make_review(kind="real")
        data["provenance"].update(review_kind="human", blinded=True)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for r in data["records"]:
                path = root / r["evidence"]
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("Synthetic test fixture, not model evidence")
                r["evidence_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertTrue(assess(data, root)["eligible_for_maintainer_review"])
            path.write_text("tampered")
            self.assertFalse(assess(data, root)["eligible_for_maintainer_review"])

    def test_automated_review_not_release_evidence(self):
        data = make_review(kind="real")
        data["provenance"].update(review_kind="automated", blinded=True)
        self.assertFalse(assess(data)["eligible_for_maintainer_review"])

    def test_critical_candidate_cannot_win_on_score(self):
        data = make_review(fail=True)
        result = assess(data)
        self.assertEqual(result["losses"], 2)

    def test_exact_preference_margin_counts_as_tie(self):
        data = make_review()
        data["records"] = data["records"][:2]
        baseline, candidate = data["records"]
        candidate["scores"] = dict(baseline["scores"], utility=2.5)
        self.assertEqual(assess(data)["ties"], 1)

    def test_nonfinite_rejected(self):
        for value in (float("nan"), float("inf")):
            data = make_review()
            data["records"][0]["scores"]["utility"] = value
            with self.assertRaises(ValueError):
                assess(data)

    def test_invalid_provenance_rejected(self):
        data = make_review()
        data["provenance"] = "real"
        with self.assertRaises(ValueError):
            assess(data)

    def test_critical_failure_blocks(self):
        r = assess(make_review(kind="real", fail=True))
        self.assertGreater(r["critical_failures"], 0)
        self.assertFalse(r["eligible_for_maintainer_review"])

    def test_missing_evidence_blocks(self):
        self.assertFalse(assess(make_review(kind="real", missing=True))["eligible_for_maintainer_review"])

    def test_duplicate_rejected(self):
        data = make_review()
        data["records"].append(dict(data["records"][0]))
        with self.assertRaises(ValueError):
            assess(data)

    def test_unpaired_rejected(self):
        data = make_review()
        data["records"].pop()
        with self.assertRaises(ValueError):
            assess(data)

    def test_invalid_score_rejected(self):
        data = make_review()
        data["records"][0]["scores"]["utility"] = 7
        with self.assertRaises(ValueError):
            assess(data)


if __name__ == "__main__":
    unittest.main()
