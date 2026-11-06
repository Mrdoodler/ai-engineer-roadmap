# Week 5 · RAG part 1: ingestion

> **Goal:** load a documentation set, split it into chunks, turn each chunk into a vector (embedding), and store it in Postgres with pgvector.
> **Time:** about 10 hrs · **Code goes in:** [`projects/docs-copilot/`](../projects/docs-copilot/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 4](../04-llm-apis/) · ➡️ [Week 6](../06-rag-retrieval/)

**What RAG is, in one line:** before asking the model a question, *search* your docs for the relevant pieces and paste them into the prompt, so it answers from your data instead of from memory.

**This week starts "Docs Copilot"**, the project you'll grow until Week 15. Recommended doc set: the **FastAPI docs**. They're Markdown files in a public GitHub repo, well organized, and you already used FastAPI in Week 3.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Watch the first 4-5 videos of [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) (LangChain), which cover overview, indexing and retrieval. Understand the ideas; we won't use LangChain itself.
- [ ] **1.2** Read the [pgvector README](https://github.com/pgvector/pgvector): "Getting Started", "Querying", and "HNSW".

## Session 2 · Build (3 hrs)

- [ ] **2.1** Create the project:
  ```bash
  cd projects/docs-copilot
  uv init
  uv add openai "psycopg[binary]" pgvector python-dotenv
  ```
- [ ] **2.2** Get the docs into `projects/docs-copilot/data/raw/`, which is git-ignored:
  ```bash
  git clone --depth 1 https://github.com/fastapi/fastapi.git /tmp/fastapi
  mkdir -p data/raw && cp -r /tmp/fastapi/docs/en/docs/* data/raw/
  ```
- [ ] **2.3** Create the table, in `db/schema.sql`:
  ```sql
  CREATE EXTENSION IF NOT EXISTS vector;
  CREATE TABLE chunks (
    id        bigserial PRIMARY KEY,
    source    text NOT NULL,      -- file path
    heading   text,               -- section title
    content   text NOT NULL,
    strategy  text NOT NULL,      -- 'fixed' or 'heading' (for comparing later)
    embedding vector(768)         -- nomic-embed-text gives 768 numbers
  );
  ```
- [ ] **2.4** `ingest.py`, **fixed-size chunking:** read every `.md` file → split into chunks of about 500 tokens with about 50 overlap (about 2,000 characters is fine to start) → save with `strategy = 'fixed'`, with no embeddings yet.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read about embeddings with [pgvector-python](https://github.com/pgvector/pgvector-python) (the "Psycopg 3" section) and the [nomic-embed-text model page](https://ollama.com/library/nomic-embed-text).
- [ ] **3.2** Important tip: nomic-embed-text expects a **prefix**. Embed documents as `"search_document: " + text` and questions as `"search_query: " + text`. Skipping this makes search noticeably worse.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Heading-aware chunking:** a second chunker that splits on Markdown headings (`#`, `##`, `###`), so each chunk is one section, and keeps the heading. Save with `strategy = 'heading'`.
- [ ] **4.2** **Embed:** for every chunk, call `client.embeddings.create(model="nomic-embed-text", input=[...])` in **batches** of about 32 and store the vector. Log how long it takes. On CPU, expect a few minutes for the whole doc set.
- [ ] **4.3** **Index:** `CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);`
- [ ] **4.4** **First search:** `search.py "how do I add query parameters"`. Embed the question, then
  ```sql
  SELECT source, heading, left(content, 200)
  FROM chunks WHERE strategy = 'heading'
  ORDER BY embedding <=> %s LIMIT 5;
  ```
  Do the top 5 results make sense? Try 5 questions.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Start `projects/docs-copilot/README.md`: what it is, how to run ingestion, number of files, chunks and embedding time.
- [ ] **5.2** Fill in [`notes.md`](notes.md). Which chunking looked better on your 5 questions?
- [ ] **5.3** Commit and push, then tick Week 5 in the [main README](../README.md#progress).

---

## ✅ Done when
- `chunks` holds both strategies with embeddings, plus an HNSW index
- `search.py` returns sensible chunks for most of your test questions
- You can explain what an embedding is and what `<=>` (cosine distance) means

## Extra (only if you have time)
- 🎥 [RAG From Scratch as one 2.5-hr video](https://www.youtube.com/watch?v=sVcwVQRHIc8) (freeCodeCamp)
- 📖 [Eugene Yan: Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/), the "Retrieval-Augmented Generation" section
