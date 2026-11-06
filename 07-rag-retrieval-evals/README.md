# Week 7 · RAG part 3: measure search quality (evals)

> **Goal:** stop judging search "by eye". Build a **golden set** of questions with known answers and compute **recall@k** and **MRR** for every search mode.
> **Time:** about 10 hrs · **Code goes in:** [`projects/docs-copilot/`](../projects/docs-copilot/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 6](../06-rag-retrieval/) · ➡️ [Week 8](../08-rag-answer-evals/)

**This is the skill most AI engineer interviews probe.** Anyone can build a RAG demo. Few can *prove* it works and show which change made it better.

**The two numbers:**
- **recall@5:** for what % of questions is the right chunk somewhere in the top 5?
- **MRR** (mean reciprocal rank): for each question, score 1/rank of the first right chunk (rank 1 → 1.0, rank 2 → 0.5, not found → 0), then average. Higher means the right answer is nearer the top.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/).
- [ ] **1.2** Skim [Hamel Husain: Evals FAQ](https://hamel.dev/blog/posts/evals-faq/), especially the questions about getting started and synthetic data.

## Session 2 · Build (3 hrs)

- [ ] **2.1** **Golden set, first 25:** `evals/golden.jsonl`, one JSON per line:
  ```json
  {"id": "q001", "question": "How do I make a query parameter optional?", "expected_sources": ["tutorial/query-params.md"]}
  ```
  Write them **yourself** by browsing the docs. Mix easy questions, vague questions and exact-keyword questions. Use `source` (the file) as the match target, so the set works for both chunking strategies.
- [ ] **2.2** **Eval script:** `evals/retrieval_eval.py --mode hybrid --strategy heading` runs every question, compares the top 5 sources with `expected_sources`, and prints recall@5, MRR, and the list of **failed questions**.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read the evaluation chapter in Chip Huyen's *AI Engineering* if you have it ([book resources](https://github.com/chiphuyen/aie-book)). If you don't, read [Shreya Shankar: In Defense of AI Evals](https://www.sh-reya.com/blog/in-defense-ai-evals/).
- [ ] **3.2** Look at your failed questions from 2.2. Why did each one fail: bad chunk boundaries, missing keyword, or a vague question? Write it down.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Golden set to 50+:** to save time, let the model *draft* questions. Pick 30 random chunks, ask the model "write a question a user would ask that this chunk answers", then **you** review, edit or delete each one. Never trust them blindly.
- [ ] **4.2** **Run the experiment grid** and save the results to `evals/results.md`:

  | Strategy | Mode | recall@5 | MRR | p50 latency |
  |---|---|---|---|---|
  | fixed | vector | | | |
  | heading | vector | | | |
  | heading | hybrid | | | |
  | heading | hybrid_rerank | | | |

- [ ] **4.3** Pick the worst result and try **one** fix (for example a different chunk size, or adding the file title to each chunk). Re-run it. Did the number go up?

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Put the results table in the project README. **This table is a resume bullet.**
- [ ] **5.2** Fill in [`notes.md`](notes.md).
- [ ] **5.3** Commit and push, then tick Week 7 in the [main README](../README.md#progress).

---

## ✅ Done when
- `golden.jsonl` has 50+ reviewed questions
- One command prints recall@5 and MRR for any mode
- The results table shows which setup is best, with numbers
