# Week 0 · Setup

> **Goal:** install everything once, so every later week is just learning.
> **Time:** about 1-2 hrs (mostly downloads) · **Cost:** $0, everything runs on your laptop
> ➡️ Next: [Week 1](../01-sql-basics/)

**What you're installing, and why**

| Tool | What it is (MERN comparison) | Used in |
|---|---|---|
| **Ollama** | Runs AI models on your laptop. Like having a free, private ChatGPT API at `localhost:11434` | Weeks 3-15 |
| **uv** | Python's npm (`uv add` = `npm install`, `uv run` = `npx`) | Weeks 3-10 |
| **Docker Postgres + pgvector** | A SQL database (instead of Mongo). pgvector adds AI "embedding" search | Weeks 1-15 |

You already have: Docker ✅, Python 3.14 ✅, Java 17 (Java 21 comes in Week 11, not now).

---

## Step 1 · Install Ollama (about 15 min)

- [ ] **1.1** Install it:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```
- [ ] **1.2** Download the two models (about 2.3 GB in total):
  ```bash
  ollama pull qwen2.5:3b         # chat model: small enough for 12 GB RAM, good at tool calling
  ollama pull nomic-embed-text   # embedding model: turns text into vectors for search (RAG)
  ```
- [ ] **1.3** Talk to it once:
  ```bash
  ollama run qwen2.5:3b "Explain what an API is in one sentence."
  ```
  You should get an answer in a few seconds. Your laptop has no NVIDIA GPU, so it runs on the CPU, which is a bit slow but fine.

## Step 2 · Install uv (about 2 min)

- [ ] **2.1** Install it, then reload your shell:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  source ~/.bashrc
  ```
- [ ] **2.2** Check it works: `uv --version`

## Step 3 · Start Postgres (about 3 min)

- [ ] **3.1** From the **repo root** (`~/personal/ai-engineer-roadmap`):
  ```bash
  docker compose up -d
  ```
  This reads [`compose.yaml`](../compose.yaml) and starts Postgres with pgvector on port **5433**.
- [ ] **3.2** Open a SQL prompt inside it:
  ```bash
  docker compose exec db psql -U postgres -d roadmap
  ```
  Type `SELECT 1 + 1;` and press Enter. Type `\q` to leave.

## Step 4 · Run the setup check (about 2 min)

- [ ] **4.1** From the repo root:
  ```bash
  uv run 00-setup/check_setup.py
  ```
  The first run downloads two Python packages. You want to see three `[ OK ]` lines:
  ```
  [ OK ] Ollama chat: Hello there, how are you?
  [ OK ] Ollama embeddings: got a vector with 768 numbers
  [ OK ] Postgres + pgvector: pgvector 0.8.x is enabled
  ```
  Any `[FAIL]` line prints the fix under it.
- [ ] **4.2** Open [`check_setup.py`](check_setup.py) and read it. It's about 60 lines. Notice that it uses the **`openai`** package to talk to Ollama. Ollama speaks the same API format as OpenAI, so most tutorials online work by only changing `base_url`.

## Step 5 · Use Claude Code as your tutor (about 2 min)

- [ ] **5.1** From the repo root, run `claude`.
- [ ] **5.2** Ask it: **"what's next?"** It reads [`CLAUDE.md`](../CLAUDE.md), finds your first unticked step, and guides you through it. It is set up to give hints rather than write your homework.

## Step 6 · Save your progress

- [ ] **6.1** Tick the boxes in this file (change `[ ]` to `[x]`). Claude can do it for you.
- [ ] **6.2** Tick **Week 0** in the [main README](../README.md#progress).
- [ ] **6.3** Commit and push:
  ```bash
  git add -A && git commit -m "Week 0: setup done" && git push
  ```

---

## ✅ Done when
- `uv run 00-setup/check_setup.py` prints three `[ OK ]` lines
- You can explain in one line each what Ollama, uv and pgvector are for

## Good to know
- **Ollama runs in the background** as a service and starts on boot. `ollama ps` shows loaded models.
- **Postgres keeps running** too (`restart: unless-stopped`). Use `docker compose stop` to free RAM, and `docker compose up -d` to start it again. Your data is kept in a Docker volume.
- **Changing models later:** copy [`.env.example`](../.env.example) to `.env` and edit it. The model name lives in one place, never hard-coded.
- **Bigger judge model:** in Week 8 you'll also pull `qwen2.5:7b` (about 4.7 GB) for grading answers. Not needed now.
