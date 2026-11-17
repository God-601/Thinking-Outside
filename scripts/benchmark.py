"""Real isolated Codex CLI runs. No dependencies, no fabricated model outputs.

Requires an authenticated CLI. Credentials stay in a temporary local home and
are never included in artifacts. Usage: python scripts/benchmark.py plan.json
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import tempfile
import time


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def events(stdout):
    result = []
    for line in stdout.splitlines():
        try:
            result.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return result


def result_of(stdout, returncode, allow_tools=False):
    data = events(stdout)
    completed = [e for e in data if e.get("type") == "turn.completed"]
    answers = [e["item"]["text"] for e in data if e.get("type") == "item.completed"
               and e.get("item", {}).get("type") == "agent_message"]
    tool_calls = {e.get("item", {}).get("id", str(i)) for i, e in enumerate(data)
                  if e.get("type") in ("item.started", "item.completed")
                  and e.get("item", {}).get("type") not in ("agent_message", "reasoning", "error")}
    ok = returncode == 0 and bool(completed) and bool(answers) and (allow_tools or not tool_calls)
    return {"status": "ok" if ok else "failed", "answer": "\n\n".join(answers),
            "usage": completed[-1].get("usage", {}) if completed else {},
            "tool_calls": len(tool_calls), "returncode": returncode}


def run_plan(plan_path):
    plan_path = Path(plan_path).resolve()
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    root = plan_path.parent
    out = (root / plan["output"]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    # A run directory is immutable: never mix settings, overwrite, or silently resume.
    if (out / "manifest.json").exists():
        raise ValueError("Output already has a manifest; choose a new output directory")
    tasks = []
    for case in plan["cases"]:
        for repetition in range(1, plan["repetitions"] + 1):
            for condition, instruction in plan["conditions"].items():
                text = (root / instruction).read_text(encoding="utf-8") if instruction else ""
                tasks.append((case, repetition, condition, text))
    random.Random(plan["order_seed"]).shuffle(tasks)
    if "include_runs" in plan:
        requested = set(plan["include_runs"])
        tasks = [t for t in tasks if f'{t[0]["id"]}-{t[1]}-{t[2]}' in requested]
        if len(tasks) != len(requested) or not tasks:
            raise ValueError("include_runs must identify existing unique runs")
    cli = shutil.which("codex")
    if not cli:
        raise RuntimeError("codex CLI unavailable")
    source_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    with tempfile.TemporaryDirectory(prefix="to-benchmark-") as scratch:
        task_home = Path(scratch)
        workspace = task_home / "workspace"
        workspace.mkdir()
        auth = source_home / "auth.json"
        if auth.exists():
            shutil.copy2(auth, task_home / "auth.json")
        env = dict(os.environ, CODEX_HOME=str(task_home))
        native = plan.get("native_skill")
        if native:
            shutil.copytree(root / native, task_home / "skills/thinking-outside")
        disabled = list((Path.home() / ".agents/skills").glob("*/SKILL.md"))
        disabled += list((source_home / "skills").glob("**/SKILL.md"))
        # System skills are seeded in CODEX_HOME by the CLI. Disable their future paths too.
        disabled += [task_home / "skills/.system" / name / "SKILL.md" for name in
                     ("imagegen", "openai-docs", "skill-creator", "skill-installer")]
        settings = "skills.config=[" + ",".join(
            '{path=' + json.dumps(str(p).replace('\\', '/')) + ',enabled=false}' for p in disabled
        ) + "]"
        config = ["-c", settings, "-c", 'model=' + json.dumps(plan["model"]),
                  "-c", 'model_reasoning_effort=' + json.dumps(plan["effort"]),
                  "-c", "features.apps=false", "-c", "features.remote_plugin=false"]
        if not native:
            config += ["-c", "features.shell_tool=false", "-c", 'web_search="disabled"']
        audit = subprocess.run([cli, "debug", "prompt-input", *config, "probe"],
                               cwd=workspace, env=env, capture_output=True, text=True,
                               encoding="utf-8", timeout=120)
        if audit.returncode:
            raise RuntimeError("Context audit failed: " + audit.stderr[-1000:])
        context = json.loads(audit.stdout)
        context_text = "\n".join(c.get("text", "") for m in context for c in m.get("content", []))
        # Fail closed on leaked discovery catalogs or inherited user/project instructions.
        if (not native and "### Available skills\n-" in context_text) or "# AGENTS.md instructions" in context_text:
            raise RuntimeError("Global skill/instruction contamination detected")
        if native and "thinking-outside/SKILL.md" not in context_text:
            raise RuntimeError("Native skill not discovered")
        version = subprocess.check_output([cli, "--version"], text=True).strip()
        manifest = {"started_utc": datetime.now(timezone.utc).isoformat(), "cli": version,
                    "plan": plan, "context_sha256": digest(context_text),
                    "context_chars": len(context_text), "disabled_skill_paths": len(disabled),
                    "isolation": "temporary CODEX_HOME; catalogs disabled; fresh exec per sample",
                    "temperature": "CLI default; not exposed", "runs": len(tasks)}
        manifest["tool_policy"] = "native read-only" if native else "shell disabled; web disabled; reject every tool event"
        manifest["instruction_sha256"] = {condition: digest(instruction) for _, _, condition, instruction in tasks}
        for condition, source in plan["conditions"].items():
            if source:
                shutil.copy2(root / source, out / (condition + ".instruction.md"))
        (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

        def run(task):
            case, repetition, condition, instruction = task
            run_id = f'{case["id"]}-{repetition}-{condition}'
            prompt = ("Complete a tarefa abaixo em português. Não utilize ferramentas nem leia arquivos. "
                      "Não execute mudanças externas. Responda ao pedido em até 650 palavras, salvo limite menor pedido. "
                      "Não mencione a condição experimental nem nomes de skills.\n")
            if native:
                prompt = ("Responda à tarefa em português. Você pode ler a skill quando pertinente, "
                          "mas não altere arquivos nem execute outras ações externas.\n")
            if instruction:
                prompt += "\n<skill-instructions>\n" + instruction + "\n</skill-instructions>\n"
            prompt += "\n<tarefa>\n" + case["prompt"] + "\n</tarefa>"
            start = time.monotonic()
            try:
                native_context = None
                if native:
                    check = subprocess.run([cli, "debug", "prompt-input", *config, prompt],
                                           cwd=workspace, env=env, capture_output=True,
                                           text=True, encoding="utf-8", timeout=120)
                    if check.returncode:
                        raise RuntimeError("Native context audit failed")
                    visible = json.loads(check.stdout)
                    visible_text = "\n".join(c.get("text", "") for m in visible for c in m.get("content", []))
                    skill_text = (task_home / "skills/thinking-outside/SKILL.md").read_text(encoding="utf-8")
                    native_context = {"sha256": digest(visible_text), "chars": len(visible_text),
                                      "full_skill_in_prompt": skill_text in visible_text}
                    (out / (run_id + ".context.json")).write_text(check.stdout, encoding="utf-8")
                proc = subprocess.run([cli, "exec", "--ignore-user-config", "--ephemeral",
                                       "--skip-git-repo-check", "--json", *config, "-"],
                                      input=prompt, cwd=workspace, env=env, capture_output=True,
                                      text=True, encoding="utf-8", timeout=plan.get("timeout", 240))
                result = result_of(proc.stdout, proc.returncode, allow_tools=bool(native))
                if native_context is not None:
                    result["native_context"] = native_context
                (out / (run_id + ".jsonl")).write_text(proc.stdout, encoding="utf-8")
                (out / (run_id + ".stderr.txt")).write_text(proc.stderr, encoding="utf-8")
            except subprocess.TimeoutExpired as exc:
                def decoded(value):
                    return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value or ""
                (out / (run_id + ".jsonl")).write_text(decoded(exc.output), encoding="utf-8")
                (out / (run_id + ".stderr.txt")).write_text(decoded(exc.stderr), encoding="utf-8")
                result = {"status": "timeout", "answer": "", "usage": {}}
            result.update(id=run_id, case_id=case["id"], repetition=repetition,
                          condition=condition, seconds=round(time.monotonic() - start, 3),
                          prompt_sha256=digest(prompt), instruction_sha256=digest(instruction))
            (out / (run_id + ".json")).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            print(run_id, result["status"], result["seconds"], flush=True)
            return result["status"]

        with ThreadPoolExecutor(max_workers=plan.get("workers", 3)) as pool:
            statuses = list(pool.map(run, tasks))
        if any(s != "ok" for s in statuses):
            raise RuntimeError("Some runs failed; retained explicitly in artifacts")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan")
    run_plan(parser.parse_args().plan)
