# Week 6 · RAG part 2: better search + answers with citations

> **Goal:** combine vector search with keyword search (**hybrid**), re-sort the results with a **reranker**, then generate answers that cite their sources.
> **Time:** about 10 hrs · **Code goes in:** [`projects/docs-copilot/`](../projects/docs-copilot/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 5](../05-rag-ingestion/) · ➡️ [Week 7](../07-rag-retrieval-evals/)

**Why hybrid?** Vector search finds *meaning* ("send data to the server" ≈ "request body"), but misses exact words like `Depends` or `422`. Keyword search catches those. Combined, they beat either one alone.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval). It's the clearest explanation of hybrid search + reranking, with measured gains.
- [ ] **1.2** Read [Postgres full text search: Introduction](https://www.postgresql.org/docs/current/textsearch-intro.html) (sections 12.1.1-12.1.2).

## Session 2 · Build (3 hrs)

- [ ] **2.1** **Keyword search:** add a full-text column and index:
  ```sql
  ALTER TABLE chunks ADD COLUMN tsv tsvector
    GENERATED ALWAYS AS (to_tsvector('english', coalesce(heading,'') || ' ' || content)) STORED;
  CREATE INDEX ON chunks USING gin (tsv);
  ```
  Query it with `WHERE tsv @@ websearch_to_tsquery('english', %s) ORDER BY ts_rank(tsv, ...) DESC`.
- [ ] **2.2** **Hybrid with RRF** (Reciprocal Rank Fusion): take the top 20 from vector search and the top 20 from keyword search. Give each chunk the score `1/(60 + rank)` from each list, add the two scores, and sort. That's about 15 lines of Python.
- [ ] **2.3** Make `search.py` take a `--mode vector|keyword|hybrid` flag, and compare all three on your 5 test questions from last week.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read the [Sentence-Transformers cross-encoder usage](https://sbert.net/docs/cross_encoder/usage/usage.html) page and look at the [bge-reranker-base](https://huggingface.co/BAAI/bge-reranker-base) model page. A reranker reads the *question and chunk together*, so it's slower but more accurate than embeddings.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Reranker:** `uv add sentence-transformers`. This is a large download, because it includes PyTorch for CPU. Take the top 20 hybrid results → score each `(question, chunk)` pair with `CrossEncoder("BAAI/bge-reranker-base")` → keep the top 5. Add `--mode hybrid_rerank`.
- [ ] **4.2** **Answer with citations:** `ask.py "question"`
  1. Retrieve the top 5 chunks (hybrid + rerank)
  2. Build a prompt: *"Answer only from the sources below. Cite them like [1], [2]. If the answer isn't there, say you don't know."* + numbered chunks
  3. Stream the answer, then print the sources list (file + heading)
- [ ] **4.3** Ask 5 questions whose answers **are not** in the docs. Does it say "I don't know", or does it make something up? Tweak the prompt.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** README: add a "How search works" section with a simple diagram: question → vector + keyword → RRF → rerank → top 5 → LLM.
- [ ] **5.2** Fill in [`notes.md`](notes.md), including the latency of each mode (time it).
- [ ] **5.3** Commit and push, then tick Week 6 in the [main README](../README.md#progress).

---

## ✅ Done when
- `search.py` supports 4 modes: vector, keyword, hybrid, hybrid_rerank
- `ask.py` answers with `[n]` citations and admits when it doesn't know
- You can explain RRF and why reranking helps

## Extra (only if you have time)
- 🎥 The rest of [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) (query translation, routing)
