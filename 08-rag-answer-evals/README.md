# Week 8 · RAG part 4: grade the answers (LLM-as-judge)

> **Goal:** measure whether the *answers* are correct and grounded, using a model as the grader, and check the grader against your own judgment.
> **Time:** about 10 hrs · **Code goes in:** [`projects/docs-copilot/`](../projects/docs-copilot/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 7](../07-rag-retrieval-evals/) · ➡️ [Week 9](../09-agents-mcp/)

**Week 7 graded the search. This week grades the answer.** Two questions per answer:
- **Faithful:** is every claim supported by the retrieved chunks? (no made-up facts)
- **Correct:** does it actually answer the question?

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read [Hamel Husain: Creating an LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/). The key idea: a judge is only useful if it **agrees with you**.
- [ ] **1.2** Pull a bigger model for judging, since a 3B judge is too unreliable: `ollama pull qwen2.5:7b` (about 4.7 GB, slower, which is fine for grading).

## Session 2 · Build (3 hrs)

- [ ] **2.1** **Generate answers:** `evals/answer_eval.py` runs `ask.py`'s logic on the first 30 golden questions and saves `{question, chunks, answer}` to `evals/answers.jsonl`.
- [ ] **2.2** **Hand-label first:** before writing any judge, label all 30 answers yourself in `evals/labels.jsonl` as `{"id": "q001", "pass": true, "reason": "..."}`. It's boring but important, because it's your ground truth.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read [Hamel Husain: A Field Guide to Rapidly Improving AI Products](https://hamel.dev/blog/posts/field-guide/), especially "look at your data".

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Judge prompt:** give the model the question, the chunks and the answer, plus a short rubric. Ask for **structured output** (Week 4!): `{"faithful": bool, "correct": bool, "reason": str}`. Use `JUDGE_MODEL=qwen2.5:7b`.
- [ ] **4.2** **Agreement:** compare the judge with your labels. Print the % agreement and list every disagreement.
- [ ] **4.3** Read the disagreements, improve the rubric (add examples of a pass and a fail), and re-run. Aim for **80%+ agreement**.
- [ ] **4.4** Run the judge across your Week 7 configs and add a **judge pass rate** column to the results table.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Final RAG results table in the README: recall@5, MRR, judge pass rate, and p50 latency per config. Add one paragraph on what you learned.
- [ ] **5.2** Fill in [`notes.md`](notes.md). This is the end of the RAG block, so write a slightly longer one (it can become a blog post).
- [ ] **5.3** Commit and push, then tick Week 8 in the [main README](../README.md#progress).

---

## ✅ Done when
- 30 hand-labelled answers
- The judge agrees with you on 80%+ (or you've written down why not)
- The full experiment table is filled in

## Extra (only if you have time)
- 📖 [Applied LLMs: What We've Learned From a Year of Building](https://applied-llms.org/), the evaluation sections
