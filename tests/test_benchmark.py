"""Synthetic transport fixtures test the harness, never model quality."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from benchmark import result_of
from blind_review import prepare


def stream(*items):
    return "\n".join(json.dumps(i) for i in items)


class BenchmarkTest(unittest.TestCase):
    def test_partial_answer_without_completed_turn_fails(self):
        stdout = stream({"type": "item.completed", "item": {"type": "agent_message", "text": "partial"}})
        self.assertEqual(result_of(stdout, 0)["status"], "failed")

    def test_usage_limit_is_distinguished_from_model_failure(self):
        stdout = stream({"type": "turn.failed", "error": {"message": "You’ve hit your usage limit."}})
        self.assertEqual(result_of(stdout, 1)["status"], "quota")

    def test_core_prompts_and_snapshot_match_canonical_utf8(self):
        root = Path(__file__).resolve().parents[1]
        read = lambda path: (root / path).read_text(encoding="utf-8")
        plan = json.loads(read("benchmarks/core-plan.json"))
        evals = json.loads(read("thinking-outside/evals/evals.json"))["evals"]
        self.assertEqual([(c["id"], c["prompt"], c["rubric"]) for c in plan["cases"]],
                         [(f'T{e["id"]:02}', e["prompt"], e["expectations"]) for e in evals])
        snapshot = "\n".join(read("thinking-outside/" + p) for p in
                             ("SKILL.md", "references/methods.md", "references/quality.md"))
        self.assertEqual(read("benchmarks/" + plan["conditions"]["C"]), snapshot)

    def test_tools_disqualify_controlled_no_tool_run(self):
        stdout = stream({"type": "item.started", "item": {"type": "command_execution"}},
                        {"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}},
                        {"type": "turn.completed", "usage": {"input_tokens": 40}})
        self.assertEqual(result_of(stdout, 0)["status"], "failed")

    def test_success_requires_exit_zero(self):
        stdout = stream({"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}},
                        {"type": "turn.completed", "usage": {"input_tokens": 40}})
        self.assertEqual(result_of(stdout, 0)["usage"]["input_tokens"], 40)
        self.assertEqual(result_of(stdout, 1)["status"], "failed")

    def test_completed_only_or_unrecognized_tool_is_rejected(self):
        for kind in ("command_execution", "file_change", "future_tool"):
            stdout = stream({"type": "item.completed", "item": {"type": kind}},
                            {"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}},
                            {"type": "turn.completed", "usage": {}})
            self.assertEqual(result_of(stdout, 0)["status"], "failed")

    def test_blinding_preserves_all_answers_without_condition_names(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            plan = {"model": "test-fixture", "effort": "low", "repetitions": 1,
                    "cases": [{"id": "case", "prompt": "Task"}], "conditions": {"A": None, "C": None}}
            (root / "manifest.json").write_text(json.dumps({"plan": plan}))
            for condition in ("A", "C"):
                (root / (condition + ".json")).write_text(json.dumps({"id": condition, "case_id": "case",
                    "condition": condition, "repetition": 1, "status": "ok", "answer": "fixture " + condition}))
            prepare(root)
            mapping = json.loads((root / "blind-map.json").read_text())
            self.assertEqual(set(mapping["case-r1"].values()), {"A", "C"})
            prepare(root)
            (root / "reviews").mkdir()
            (root / "reviews" / "manifest.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "Review already started"):
                prepare(root)
            (root / "C.json").unlink()
            with self.assertRaises(ValueError):
                prepare(root)


if __name__ == "__main__":
    unittest.main()
