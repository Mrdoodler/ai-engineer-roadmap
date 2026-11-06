# Week 15 · Production: Docs Copilot in Spring Boot + Spring AI

> **Goal:** rebuild Docs Copilot as a Spring Boot + Spring AI service on pgvector, with tracing and a CI job that **fails the build if search quality drops**.
> **Time:** about 10 hrs · **Code goes in:** [`projects/docs-copilot-spring/`](../projects/docs-copilot-spring/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 14](../14-spring-boot-security-tests/) · ➡️ [Week 16](../16-portfolio/)

**This is the capstone.** It combines both tracks: the AI skills from Weeks 4-10 plus the Java skills from Weeks 11-14, in the shape enterprise job posts ask for.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read the [Spring AI reference](https://docs.spring.io/spring-ai/reference/): the intro, [Ollama chat](https://docs.spring.io/spring-ai/reference/api/chat/ollama-chat.html), [Ollama embeddings](https://docs.spring.io/spring-ai/reference/api/embeddings/ollama-embeddings.html), and the [PGvector store](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html).
- [ ] **1.2** Watch a [Dan Vega](https://www.youtube.com/@danvega) Spring AI RAG video (search his channel for "Spring AI RAG").

## Session 2 · Build (3 hrs)

- [ ] **2.1** New project from [start.spring.io](https://start.spring.io/): Spring Web, **Ollama**, **PGvector Vector Database**, Validation.
- [ ] **2.2** Point it at your existing `chunks` data. The simplest route is to re-ingest with Spring AI's `VectorStore`, using the same `nomic-embed-text` model so the vectors match.
- [ ] **2.3** `POST /ask {"question": ...}` → retrieve the top 5 → answer with `[n]` citations → return `{answer, sources[]}`.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read the [Langfuse docs](https://langfuse.com/docs) on OpenTelemetry, and how to send Spring AI traces there.
- [ ] **3.2** Decide on deployment. See the box below.

> **About deployment:** Cloud Run can't reach the Ollama on your laptop, so a *deployed* version needs a hosted model.
> - **Option A (default, $0):** run the whole stack with **Docker Compose** (app + Postgres + Ollama) and record a demo. This is fully fine for a portfolio.
> - **Option B (stretch):** deploy to [Cloud Run](https://cloud.google.com/run/docs) using the **Gemini free tier** through its [OpenAI-compatible endpoint](https://ai.google.dev/gemini-api/docs/openai). Cloud Run needs a billing account, so **set a $1 budget alert first**.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Tracing:** every LLM call visible in Langfuse with prompt, tokens and latency.
- [ ] **4.2** **Dockerfile** + add the app to a `compose.yaml` in the project, so `docker compose up` runs everything.
- [ ] **4.3** **CI eval gate:** a GitHub Actions workflow that, on each pull request:
  1. starts Postgres + Ollama in the runner and pulls **only** `nomic-embed-text` (small)
  2. ingests the docs and runs your Week 7 **retrieval eval** on 20 golden questions
  3. **fails the build if recall@5 is below your threshold** (for example 0.8)

  Retrieval-only keeps it fast and free. The judge would be too slow on CI CPUs.
- [ ] **4.4** Open a test PR that makes search worse on purpose (for example a tiny chunk size), and watch the gate fail it.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** README with an architecture diagram, how to run it, the eval gate, and a screenshot of a Langfuse trace.
- [ ] **5.2** Fill in [`notes.md`](notes.md).
- [ ] **5.3** Commit and push, then tick Week 15 in the [main README](../README.md#progress).

---

## ✅ Done when
- `docker compose up` gives a working `/ask` endpoint with citations
- Traces are in Langfuse
- CI blocks a PR that lowers recall@5
