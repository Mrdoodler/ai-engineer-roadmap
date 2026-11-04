# AI Engineer Roadmap: 16 Weeks, 10 hrs/week

A self-directed plan to move from **MERN (TypeScript) developer to AI engineer**, with **Java + Spring Boot** as a second track so the final project looks like what enterprise job posts ask for: a Spring Boot + pgvector RAG/agent service with tracing, evals, and CI.

| | |
|---|---|
| **Starting point** | 2 yrs MERN (TypeScript), a little GCP, no SQL, beginner Python |
| **Time** | 10 hrs/week for 16 weeks (about 160 hrs) |
| **LLM budget** | **$0.** Gemini API free tier, with Ollama (local models) as a fallback |
| **Outcome** | 3-4 portfolio projects, written evals, a deployed service, a resume and interview story |

---

## Table of contents

- [How each week works](#how-each-week-works)
- [Setup (Week 0, about 1 hr)](#setup-week-0-about-1-hr)
- [Roadmap at a glance](#roadmap-at-a-glance)
- [The running project](#the-running-project)
- [Weeks 1-2: SQL + Postgres](#weeks-1-2-sql--postgres)
- [Weeks 3-4: Python + LLM API fundamentals](#weeks-3-4-python--llm-api-fundamentals)
- [Weeks 5-8: RAG on pgvector](#weeks-5-8-rag-on-pgvector)
- [Weeks 9-10: Agents + MCP](#weeks-9-10-agents--mcp)
- [Weeks 11-12: Java core](#weeks-11-12-java-core)
- [Weeks 13-14: Spring Boot](#weeks-13-14-spring-boot)
- [Week 15: Production](#week-15-production)
- [Week 16: Portfolio + interview prep](#week-16-portfolio--interview-prep)
- [Master resource list](#master-resource-list)
- [Progress tracker](#progress-tracker)

---

## How each week works

| Block | Time | What to do |
|-------|------|-----|
| Reading / watching | 2 x 1 hr | Videos, docs, book chapters listed for that week |
| Building | 2 x 3 hrs | Hands-on work on that week's deliverables |
| Write-up | 1 x 2 hrs | A short post or `notes/weekNN.md`: what I built, what broke, numbers, next steps |

**Rules I'm following**
1. **Build > watch.** If a video is longer than the reading block, watch at 1.5x or only the chapters I need.
2. **Every week ships something** to GitHub, even if it's small.
3. **Measure everything.** Latency, token counts, recall@k. Numbers become resume bullets.
4. **Stuck for more than 45 min?** Write down the question, look at the docs, then ask an LLM. Note the answer in the write-up.

---

## Setup (Week 0, about 1 hr)

### LLM: Gemini API free tier (default)
1. Get a free API key at [Google AI Studio](https://aistudio.google.com/). No billing account is needed for the free tier.
2. Follow the [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart) with the [`google-genai` Python SDK](https://github.com/googleapis/python-genai).
3. Check the [pricing page](https://ai.google.dev/gemini-api/docs/pricing) for which models are currently "Free of charge" (usually the **Flash** and **Flash-Lite** models plus **Gemini Embedding**). See [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits) for your actual quota in AI Studio.
4. Keep the key in `.env` and never commit it (`.env` goes in `.gitignore`).

> **Free tier caveats**
> - **Privacy:** on the free tier, Google may use your prompts to improve its products. Only send public or test data, never anything private or from work.
> - **Rate limits:** free tier quotas are per-minute and per-day. Cache results, add retries with backoff (`429 RESOURCE_EXHAUSTED`), and run evals on small batches.
> - **Model names change often.** Put the model name in config, not hard-coded.

### Fallback: Ollama (fully local, unlimited)
- Install [Ollama](https://ollama.com/). Pull a small chat model and [`nomic-embed-text`](https://ollama.com/library/nomic-embed-text) for embeddings.
- Use it when you hit the Gemini rate limit, or to run big eval batches for free.

### Portability tip
Gemini has an [OpenAI-compatible endpoint](https://ai.google.dev/gemini-api/docs/openai), and so does Ollama. If you write code against the OpenAI-style interface, you can swap providers by changing a base URL. Most tutorials (OpenAI Cookbook, DeepLearning.AI) then work as-is.

### Tools
- Docker, with images [`postgres`](https://hub.docker.com/_/postgres) and [`pgvector/pgvector`](https://hub.docker.com/r/pgvector/pgvector)
- Python 3.12+ with [uv](https://docs.astral.sh/uv/) for environments and packages
- JDK 21 + IntelliJ IDEA Community, and [start.spring.io](https://start.spring.io/)
- [Langfuse](https://langfuse.com/docs) (free cloud tier, or self-host with Docker) for tracing, from Week 4

---

## Roadmap at a glance

| Weeks | Track | Main deliverable |
|-------|-------|------------------|
| 1-2 | SQL + Postgres | `sql-playground` repo: schema, queries, EXPLAIN before/after, transaction demos |
| 3-4 | Python + LLM APIs | `llm-basics`: streaming chat, tool calling, structured output, cost/token logger |
| 5-8 | RAG on pgvector | `docs-rag`: hybrid search + reranking + an eval suite with recall@k, MRR, LLM-as-judge |
| 9-10 | Agents + MCP | MCP server over the RAG + an agent with an eval set |
| 11-12 | Java core | `java-katas`: OOP, collections, streams, concurrency |
| 13-14 | Spring Boot | REST API with JPA + Postgres, Security, Testcontainers tests |
| 15 | Production | Spring Boot + Spring AI RAG service on Cloud Run, traced in Langfuse, with a CI eval gate |
| 16 | Portfolio | Polished READMEs, demo video, resume bullets, mock interviews |

## The running project

To end with one strong project instead of many toy ones, weeks 5-15 build on a single domain:

> **"Docs Copilot"**: a question-answering assistant over a public documentation set (for example the Postgres docs, Spring docs, or your favorite OSS project).
> Week 5-8: Python RAG + evals → Week 9-10: agent + MCP server → Week 15: rebuilt as a Spring Boot + Spring AI service, deployed, traced and eval-gated.

---

## Weeks 1-2: SQL + Postgres

**Goal:** be comfortable writing real SQL and understand why queries are fast or slow, since pgvector RAG depends on it later.

### Watch / read
- 🎥 [SQL Tutorial: Full Database Course for Beginners](https://www.youtube.com/watch?v=HXV3zeQKqGY) (freeCodeCamp). Pick the chapters you need.
- 🎥 [Learn PostgreSQL: Full Course for Beginners](https://www.youtube.com/watch?v=qw--VYLpxG4) (freeCodeCamp / Amigoscode)
- 🎥 [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=pTFZFxd4hOI) (Programming with Mosh), if Docker is new to you
- 🎥 [Hussein Nasser](https://www.youtube.com/@hnasr): his videos on ACID, indexes and isolation levels are the best intuition builders
- 📖 [PostgreSQL official tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- 📖 [Use The Index, Luke](https://use-the-index-luke.com/): SQL indexing explained for developers
- 📖 [Postgres: Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)

### Practice
- 🧩 [SQLBolt](https://sqlbolt.com/): interactive basics (1-2 hrs)
- 🧩 [pgexercises.com](https://pgexercises.com/): real Postgres exercises (joins, aggregates, subqueries, window functions)

### Deliverables
- Postgres in Docker (`docker compose up`) with your own schema of 5+ tables (for example a mini e-commerce or job tracker)
- 30+ queries in a `queries.sql`: joins, GROUP BY, window functions, CTEs
- An `EXPLAIN ANALYZE` before/after showing an index changing the query plan
- Transaction demos: rollback, and two sessions showing a lost update and how `SELECT ... FOR UPDATE` or isolation fixes it

### Progress
- [ ] **Week 1:** Docker Postgres up · SQLBolt done · pgexercises: Basic, Joins · schema designed
- [ ] **Week 2:** pgexercises: Aggregates, subqueries · indexes + EXPLAIN · transactions demo · write-up

---

## Weeks 3-4: Python + LLM API fundamentals

**Goal:** move from beginner Python to comfortable, then learn the core LLM API building blocks every AI engineer uses.

### Python (week 3 focus)
- 🎥 [Learn Python: Full Course for Beginners](https://www.youtube.com/watch?v=rfscVS0vtbw) (freeCodeCamp). Skim what you already know from JS.
- 🎥 [Corey Schafer's Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU): short, deep videos on specific topics (virtualenvs, comprehensions, decorators, context managers)
- 📖 [The official Python tutorial](https://docs.python.org/3/tutorial/) · [Real Python](https://realpython.com/) for any topic
- 📖 [Pydantic](https://docs.pydantic.dev/latest/), the TypeScript-like data validation you'll use everywhere
- 📖 [FastAPI](https://fastapi.tiangolo.com/), which feels like Express for Python

### LLM fundamentals (week 4 focus)
- 🎥 [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (Andrej Karpathy, 1 hr). Watch it first.
- 🎥 [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (Karpathy). Watch over a few sessions.
- 📖 Gemini docs: [Text generation + streaming](https://ai.google.dev/gemini-api/docs/text-generation) · [Function calling](https://ai.google.dev/gemini-api/docs/function-calling) · [Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output) · [Context caching](https://ai.google.dev/gemini-api/docs/caching) · [Counting tokens](https://ai.google.dev/gemini-api/docs/tokens)
- 💻 [Gemini Cookbook](https://github.com/google-gemini/cookbook): runnable notebooks for every feature
- 📖 [Prompt Engineering Guide](https://www.promptingguide.ai/)
- 🎓 [Anthropic courses on GitHub](https://github.com/anthropics/courses): the prompt engineering material is excellent and provider-agnostic in concept

### Deliverables (`llm-basics` repo)
- Python: 3 small CLI tools (file processing, an HTTP API call, a pydantic model), with `pytest` tests
- A streaming chat CLI with conversation history
- Tool calling: the model calls a Python function that queries your Week 1-2 Postgres database (text-to-SQL, read-only user)
- Structured output: extract a pydantic object (for example a job post → `{title, skills[], salary}`)
- Context caching demo + a **token and cost logger**: tokens per call, latency, and what it *would* cost on the paid tier
- Retries with exponential backoff for `429` errors

### Progress
- [ ] **Week 3:** Python fundamentals · venv/uv · pydantic · pytest · first Gemini call
- [ ] **Week 4:** Streaming · tool calling · structured output · caching · cost logger · write-up

---

## Weeks 5-8: RAG on pgvector

**Goal:** build retrieval-augmented generation the way production teams do, then **prove it works with evals**. This is the core skill most AI engineer interviews probe.

### Watch / read
- 🎥 [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) (LangChain, Lance Martin) + [code](https://github.com/langchain-ai/rag-from-scratch). Also as [one 2.5 hr video](https://www.youtube.com/watch?v=sVcwVQRHIc8) on freeCodeCamp.
- 📖 [pgvector README](https://github.com/pgvector/pgvector): HNSW vs IVFFlat indexes, distance operators, filtering · [pgvector-python](https://github.com/pgvector/pgvector-python)
- 📖 [Gemini Embeddings](https://ai.google.dev/gemini-api/docs/embeddings) (task types for query vs document matter)
- 📖 [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval), the clearest write-up of hybrid search (BM25 + embeddings) + reranking, with measured gains
- 📖 [Sentence-Transformers cross-encoders](https://sbert.net/docs/cross_encoder/usage/usage.html) · [BAAI/bge-reranker-base](https://huggingface.co/BAAI/bge-reranker-base), a free local reranker
- 📖 Chip Huyen, *AI Engineering*, ch. on RAG and on evaluation ([book repo + resources](https://github.com/chiphuyen/aie-book))
- 📖 [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) · [Creating an LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/) · [Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- 📖 [Eugene Yan: Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/)

### Deliverables (`docs-rag` repo)
- **Week 5, ingestion:** load docs → chunk (try fixed-size vs. heading-aware) → embed → store in `pgvector` with metadata; build an HNSW index
- **Week 6, retrieval:** vector search, Postgres full-text search (`tsvector`), **hybrid** with reciprocal rank fusion, then a **reranker**. Answer generation with citations.
- **Week 7, retrieval evals:** a **golden set of 50+ questions** with the expected source chunks. Compute **recall@k** and **MRR** with a script, not by eye.
- **Week 8, answer evals:** **LLM-as-judge** for faithfulness/correctness. Hand-label 30 answers and measure how often the judge agrees with you.
- An **experiment table** in the README:

  | Config | recall@5 | MRR | Judge pass rate | p50 latency |
  |---|---|---|---|---|
  | vector only, 512-token chunks | | | | |
  | hybrid | | | | |
  | hybrid + rerank | | | | |

### Progress
- [ ] **Week 5:** Ingestion pipeline · chunking strategies · embeddings in pgvector · HNSW index
- [ ] **Week 6:** Vector + full-text + hybrid (RRF) · reranker · answers with citations
- [ ] **Week 7:** Golden set (50+) · recall@k · MRR script
- [ ] **Week 8:** LLM-as-judge · judge vs. human agreement · experiment table · write-up

---

## Weeks 9-10: Agents + MCP

**Goal:** understand when (and when not) to use agents, build one well, expose tools via MCP, and evaluate it.

### Watch / read
- 📖 [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents). Read twice: workflows vs. agents, and the five patterns.
- 📖 [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- 📖 [Lilian Weng: LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/), background and vocabulary
- 📖 [modelcontextprotocol.io](https://modelcontextprotocol.io/) (spec + concepts) · [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- 🎥 [Intro to MCP Servers: Model Context Protocol with Python](https://www.youtube.com/watch?v=DosHnyq78xY) (freeCodeCamp, about 1 hr)
- 🎓 [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) and [Agents Course](https://huggingface.co/learn/agents-course) (free, with certificates)
- 🎓 [Anthropic Academy](https://anthropic.skilljar.com/): free courses including *Introduction to Model Context Protocol*
- 🎓 [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/): pick the ones on agents, MCP, and evaluating agents (1-2 hrs each, free)

### Deliverables
- An **MCP server** exposing your Docs Copilot: `search_docs`, `get_chunk`, `run_readonly_sql`
- An **agent** (written by hand with plain function calling, no framework) that plans, calls tools, and answers. Add a step limit and a cost limit.
- An **agent eval set** of 20+ tasks scoring: task success, correct tool chosen, number of steps, tokens per task
- **Failure analysis:** read 30 traces, group failures into categories, fix the top 3, and re-run the evals (before/after table)

### Progress
- [ ] **Week 9:** Agent loop from scratch · MCP server · connect it to an MCP client
- [ ] **Week 10:** Agent eval set · trace review · top 3 fixes · before/after · write-up

---

## Weeks 11-12: Java core

**Goal:** solid Java fundamentals, coming from TypeScript (types and classes will feel familiar; the JVM, generics and concurrency are new).

### Watch / read
- 🎓 [MOOC.fi Java Programming](https://java-programming.mooc.fi/) (University of Helsinki, free, with exercises). This is the main course.
- 🎥 [Java Full Course for free](https://www.youtube.com/watch?v=xk4_1vDrzzo) (Bro Code), as a quick reference
- 📖 [dev.java/learn](https://dev.java/learn/), Oracle's modern Java tutorials (records, streams, virtual threads)
- 📖 [Baeldung](https://www.baeldung.com/), especially [Java Concurrency](https://www.baeldung.com/java-concurrency)
- 🗺️ [roadmap.sh/java](https://roadmap.sh/java), to check for gaps

### Deliverables (`java-katas` repo)
- MOOC.fi parts 1-7 (or as far as you get in about 12 hrs), solutions committed
- A CLI app using classes, interfaces, records, `List/Map/Set`, and streams (for example a log analyzer)
- Concurrency: `ExecutorService`, `CompletableFuture`, and a virtual-threads demo calling an HTTP API in parallel
- Port your Week 4 cost logger to Java, with JUnit 5 tests

### Progress
- [ ] **Week 11:** Syntax · OOP · interfaces · records · collections · MOOC.fi parts 1-4
- [ ] **Week 12:** Generics · streams/lambdas · exceptions · concurrency · JUnit · write-up

---

## Weeks 13-14: Spring Boot

**Goal:** build a production-style REST API like the ones enterprises run.

### Watch / read
- 🎥 [Spring Boot Tutorial for Beginners [2025]](https://www.youtube.com/watch?v=gJrjgg1KVL4) (Programming with Mosh)
- 🎥 [Amigoscode](https://www.youtube.com/@amigoscode), Spring Boot + Postgres + Docker videos
- 🎥 [Dan Vega](https://www.youtube.com/@danvega), Spring Developer Advocate, great on modern Spring Boot and Spring AI
- 📖 Spring guides: [REST service](https://spring.io/guides/gs/rest-service/) · [Accessing data with JPA](https://spring.io/guides/gs/accessing-data-jpa/) · [Securing a web app](https://spring.io/guides/gs/securing-web/) · [all guides](https://spring.io/guides)
- 🎓 [Spring Academy](https://spring.academy/), free official courses (Spring Boot, Spring Security)
- 📖 [Baeldung: Spring Boot](https://www.baeldung.com/spring-boot), the go-to answer for any "how do I…"
- 📖 [Testcontainers for Java](https://java.testcontainers.org/), real Postgres in tests
- 🗺️ [roadmap.sh/spring-boot](https://roadmap.sh/spring-boot)

### Deliverables
- A REST API (for example a job-application tracker): CRUD, validation, global error handling, pagination
- Spring Data JPA + Postgres with Flyway migrations
- Spring Security: JWT or basic auth, with role-based endpoints
- Tests: unit (JUnit + Mockito), integration with Testcontainers; GitHub Actions runs them on every push

### Progress
- [ ] **Week 13:** REST controllers · JPA entities/repositories · Postgres · Flyway
- [ ] **Week 14:** Security · validation/errors · Testcontainers · GitHub Actions CI · write-up

---

## Week 15: Production

**Goal:** combine both tracks into one deployable, observable, tested AI service.

### Read
- 📖 [Spring AI reference](https://docs.spring.io/spring-ai/reference/): [PGvector vector store](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html) · [Google GenAI (Gemini) chat](https://docs.spring.io/spring-ai/reference/api/chat/google-genai-chat.html) · [Ollama chat](https://docs.spring.io/spring-ai/reference/api/chat/ollama-chat.html)
- 📖 [Langfuse docs](https://langfuse.com/docs), tracing and evals
- 📖 [Cloud Run docs](https://cloud.google.com/run/docs) · [quickstarts](https://cloud.google.com/run/docs/quickstarts)
- 📖 [GitHub Actions](https://github.com/features/actions)

### Deliverables
- **Docs Copilot v2:** Spring Boot + Spring AI service with `/ask` (RAG with citations) and `/agent` endpoints, backed by pgvector
- **Langfuse tracing** of every LLM call: prompt, tokens, latency, cost
- **Deployed to Cloud Run** (containerized). Cloud Run has a monthly free allowance, but it needs a billing account, so **set a budget alert at $1**.
- **CI eval gate:** GitHub Actions runs the golden-set eval on each PR and fails the build if recall@5 or judge pass rate drops below a threshold

### Progress
- [ ] Spring AI + pgvector `/ask` endpoint
- [ ] Langfuse tracing
- [ ] Docker image + Cloud Run deploy + budget alert
- [ ] CI eval gate
- [ ] Write-up

---

## Week 16: Portfolio + interview prep

### Deliverables
- **Repos polished:** each one has a README with an architecture diagram, how to run it, **eval results table**, and design decisions and trade-offs
- **Demo video** (3-5 min): problem → architecture → live demo → eval numbers → what you'd do next
- **Resume bullets** with numbers, for example:
  - *"Built a RAG service (Spring Boot, Spring AI, pgvector) improving recall@5 from X to Y with hybrid search + reranking; CI eval gate blocks regressions"*
  - *"Designed an agent with MCP tools; cut failure rate X% through trace-driven error analysis"*
- **Interview prep:**
  - System design: "design a RAG system for 1M docs", "design a customer-support agent". Cover chunking, indexes, caching, evals, cost, and latency.
  - [System Design Primer](https://github.com/donnemartin/system-design-primer) for general backend design
  - SQL (pgexercises again) · Java/Spring fundamentals · one strong story per project (problem, decision, result)
  - [roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer) as a final gap check

### Progress
- [ ] READMEs + diagrams + eval tables
- [ ] Demo video recorded
- [ ] Resume + LinkedIn updated
- [ ] 3 mock interviews (system design, coding, project deep-dive)

---

## Master resource list

### Books
- **Chip Huyen, *AI Engineering*** (O'Reilly, 2025). The single best book for this path. [Companion repo](https://github.com/chiphuyen/aie-book) · [Chip's blog](https://huyenchip.com/)
- **[Applied LLMs: What We've Learned From a Year of Building](https://applied-llms.org/)**, free and practical

### Foundations (videos)
- [Karpathy: Intro to LLMs](https://www.youtube.com/watch?v=zjkBMFhNj_g) · [Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) · [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) (optional, deep)
- [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi), visual intuition for transformers and attention

### Providers and SDKs
- [Gemini API docs](https://ai.google.dev/gemini-api/docs) · [Gemini Cookbook](https://github.com/google-gemini/cookbook) · [AI Studio](https://aistudio.google.com/)
- [Ollama](https://ollama.com/)
- [Anthropic docs](https://docs.anthropic.com/) · [anthropics/courses](https://github.com/anthropics/courses) · [Anthropic Academy](https://anthropic.skilljar.com/)
- [OpenAI Cookbook](https://cookbook.openai.com/), whose patterns transfer to Gemini through the OpenAI-compatible endpoint

### Courses (free)
- [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/)
- [Hugging Face: LLM Course](https://huggingface.co/learn/llm-course) · [Agents Course](https://huggingface.co/learn/agents-course) · [MCP Course](https://huggingface.co/learn/mcp-course)
- [MOOC.fi Java Programming](https://java-programming.mooc.fi/) · [Spring Academy](https://spring.academy/)

### RAG, agents, evals
- [pgvector](https://github.com/pgvector/pgvector) · [RAG From Scratch](https://github.com/langchain-ai/rag-from-scratch) · [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) · [modelcontextprotocol.io](https://modelcontextprotocol.io/)
- Hamel Husain: [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) · [LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/) · [A Field Guide to Rapidly Improving AI Products](https://hamel.dev/blog/posts/field-guide/) · [Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- [Shreya Shankar: In Defense of AI Evals, for Everyone](https://www.sh-reya.com/blog/in-defense-ai-evals/)
- [Eugene Yan: Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/)

### SQL / Postgres
- [pgexercises.com](https://pgexercises.com/) · [SQLBolt](https://sqlbolt.com/) · [Use The Index, Luke](https://use-the-index-luke.com/) · [Postgres tutorial](https://www.postgresql.org/docs/current/tutorial.html) · [Hussein Nasser](https://www.youtube.com/@hnasr)

### Java / Spring
- [dev.java/learn](https://dev.java/learn/) · [Baeldung](https://www.baeldung.com/) · [spring.io/guides](https://spring.io/guides) · [Spring AI reference](https://docs.spring.io/spring-ai/reference/)
- YouTube: [Dan Vega](https://www.youtube.com/@danvega) · [Amigoscode](https://www.youtube.com/@amigoscode) · [Spring Developer](https://www.youtube.com/@SpringSourceDev)

### Roadmaps
- [roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer) · [roadmap.sh/java](https://roadmap.sh/java) · [roadmap.sh/spring-boot](https://roadmap.sh/spring-boot)

---

## Progress tracker

| Week | Topic | Done | Write-up |
|------|-------|------|----------|
| 1 | SQL basics + Docker Postgres | [ ] | [ ] |
| 2 | Indexes, EXPLAIN, transactions | [ ] | [ ] |
| 3 | Python fundamentals | [ ] | [ ] |
| 4 | LLM APIs: streaming, tools, structured output, caching | [ ] | [ ] |
| 5 | RAG ingestion + pgvector | [ ] | [ ] |
| 6 | Hybrid search + reranking | [ ] | [ ] |
| 7 | Golden set, recall@k, MRR | [ ] | [ ] |
| 8 | LLM-as-judge + experiments | [ ] | [ ] |
| 9 | Agent loop + MCP server | [ ] | [ ] |
| 10 | Agent evals + failure analysis | [ ] | [ ] |
| 11 | Java: OOP + collections | [ ] | [ ] |
| 12 | Java: streams + concurrency | [ ] | [ ] |
| 13 | Spring Boot: REST + JPA | [ ] | [ ] |
| 14 | Spring Boot: Security + tests + CI | [ ] | [ ] |
| 15 | Production: Spring AI, Langfuse, Cloud Run, eval gate | [ ] | [ ] |
| 16 | Portfolio + interview prep | [ ] | [ ] |

> Tip: checkboxes inside tables don't toggle on GitHub. Edit them to `[x]`, or use the checklists inside each week's section.
