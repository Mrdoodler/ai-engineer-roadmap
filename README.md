# AI Engineer Roadmap: 16 Weeks, 10 hrs/week

My plan to go from **MERN (TypeScript) developer to AI engineer**, with **Java + Spring Boot** as a second track. The final project is the kind of thing enterprise job posts ask for: a Spring Boot + pgvector RAG/agent service with tracing, evals and CI.

| | |
|---|---|
| **Starting point** | 2 yrs MERN (TypeScript), a little GCP, no SQL, beginner Python |
| **Time** | 10 hrs/week for 16 weeks (about 160 hrs) |
| **Budget** | **$0.** All AI models run locally with [Ollama](https://ollama.com/) |
| **Outcome** | Portfolio projects with measured results, a resume and interview stories |

---

## 👉 Start here

1. **Open the current week's folder** (see [Progress](#progress)) and read its `README.md`.
2. **Do the steps in order.** Every week has the same 5 sessions, and each step is a checkbox.
3. **Tick each box** as you finish it (change `[ ]` to `[x]`).
4. **At the end of the week**, fill in that week's `notes.md`, tick the week below, and commit.

**Using Claude Code:** open a terminal in this folder, run `claude`, and ask **"what's next?"**. It reads [`CLAUDE.md`](CLAUDE.md), finds your first unticked step, and walks you through it with hints instead of answers.

---

## Progress

**Current week: 0**

| ✓ | Week | Topic | What you'll have at the end |
|---|---|---|---|
| [ ] | [0](00-setup/) | Setup | Ollama, uv and Postgres working |
| [ ] | [1](01-sql-basics/) | SQL basics | Your own job-tracker database + 10 queries |
| [ ] | [2](02-sql-indexes-transactions/) | Advanced SQL, indexes, transactions | 30 queries, an index before/after, a lost-update demo |
| [ ] | [3](03-python/) | Python | 3 tested CLI tools, Python talking to Postgres |
| [ ] | [4](04-llm-apis/) | LLM APIs | Streaming chat, tool calling, structured output, a cost logger |
| [ ] | [5](05-rag-ingestion/) | RAG 1: ingestion | Docs chunked and embedded in pgvector |
| [ ] | [6](06-rag-retrieval/) | RAG 2: retrieval | Hybrid search + reranker, answers with citations |
| [ ] | [7](07-rag-retrieval-evals/) | RAG 3: search evals | A 50-question golden set, recall@5, MRR |
| [ ] | [8](08-rag-answer-evals/) | RAG 4: answer evals | An LLM-as-judge checked against your own labels |
| [ ] | [9](09-agents-mcp/) | Agents + MCP | A hand-written agent + an MCP server used in Claude Code |
| [ ] | [10](10-agent-evals/) | Agent evals | Traces in Langfuse, a before/after table |
| [ ] | [11](11-java-basics/) | Java basics | Java 21 set up, a log analyzer |
| [ ] | [12](12-java-advanced/) | Java advanced | Streams, a virtual-threads demo, JUnit |
| [ ] | [13](13-spring-boot-api/) | Spring Boot API | A job tracker REST API on Postgres |
| [ ] | [14](14-spring-boot-security-tests/) | Spring Boot security + tests | Auth, Testcontainers, green CI |
| [ ] | [15](15-production/) | Production capstone | Spring AI RAG service, tracing, a CI eval gate |
| [ ] | [16](16-portfolio/) | Portfolio + interviews | Polished READMEs, a demo video, a resume |

Change `[ ]` to `[x]` here when a week is done, and update **Current week**.

---

## Every week looks like this

| Session | Time | What you do |
|---|---|---|
| 1 · Learn | 1 hr | Watch or read the listed resources |
| 2 · Build | 3 hrs | Hands-on steps |
| 3 · Learn | 1 hr | Watch or read |
| 4 · Build | 3 hrs | Hands-on steps |
| 5 · Wrap up | 2 hrs | README, `notes.md`, commit, tick the week |

**Rules**
1. **Build more than you watch.** If a video runs longer than the session, watch at 1.5x or only the parts you need.
2. **Every week ends with a commit.**
3. **Write down numbers:** latency, tokens, recall@5. Numbers become resume bullets.
4. **Stuck for more than 45 min?** Write down the exact question, check the docs, then ask Claude.

---

## How this repo is organized

```
ai-engineer-roadmap/
├── README.md            ← you are here: overview + progress
├── CLAUDE.md            ← instructions for Claude Code (your tutor)
├── RESOURCES.md         ← every link in one place
├── compose.yaml         ← Postgres + pgvector (docker compose up -d)
├── .env.example         ← model names + database URL
│
├── 00-setup/ … 16-portfolio/   ← one folder per week
│   ├── README.md        ← the steps for that week (checkboxes)
│   └── notes.md         ← your write-up for that week
│
└── projects/            ← all your code lives here
    ├── sql-playground/       weeks 1-2
    ├── llm-basics/           weeks 3-4
    ├── docs-copilot/         weeks 5-10 (the main project, Python)
    ├── java-katas/           weeks 11-12
    ├── job-tracker-api/      weeks 13-14
    └── docs-copilot-spring/  week 15 (the capstone, Java)
```

**Week folders** tell you *what to do*. **`projects/`** is *where you do it*.

## The main project: Docs Copilot

Rather than many toy projects, Weeks 5-15 grow **one** project: an assistant that answers questions about a documentation set (the FastAPI docs), with citations.

> **Weeks 5-8:** RAG in Python, with measured search and answer quality → **Weeks 9-10:** an agent + MCP server → **Week 15:** rebuilt in Spring Boot + Spring AI, traced, with a CI quality gate.

## The AI setup ($0)

- **Ollama** runs models on the laptop: `qwen2.5:3b` for chat, `nomic-embed-text` for embeddings, and `qwen2.5:7b` as the grader from Week 8.
- Code uses the **`openai` Python package** pointed at `http://localhost:11434/v1`. Switching to a hosted model later (OpenAI, Gemini, etc.) means changing one URL.
- Model names live in `.env` (see [`.env.example`](.env.example)), never hard-coded.

All links: [RESOURCES.md](RESOURCES.md)
