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
            (root / "C.json").unlink()
            with self.assertRaises(ValueError):
                prepare(root)


if __name__ == "__main__":
    unittest.main()
