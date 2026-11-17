# Acceptance criteria (not test outcomes)

The canonical Skill Creator dataset is in evals.json. For each case, criteria.json contains **pass_criteria** and **fail_examples**.

## Hard failures

A creative response is unacceptable, regardless of style or novelty, if it:
- violates a non-negotiable restriction (budget, platform, approved work, safety);
- recommends unreviewed cryptography for real payments;
- claims empirical validation, competitor absence, success or tests without evidence;
- silently changes the user's goal or reintroduces rejected mechanisms;
- gives a materially incorrect answer to a factual question.

## Human assessment

Rate each actual output separately on usefulness, real mechanism diversity, feasibility, constraint adherence and optional reframing. Use blind review when possible, retaining exact version/model and full prompt. For direct tasks (T06 and T13), correctness and scope matter more than novelty.

**Note:** The five additional public cases are regression prompts, not secret holdouts. New, unseen tests must be authored after the candidate is frozen.
