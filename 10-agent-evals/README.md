# Week 10 · Agent evals + tracing

> **Goal:** measure the agent the way you measured RAG: a task set, scores, reading traces, fixing the top failures, and showing a before/after.
> **Time:** about 10 hrs · **Code goes in:** [`projects/docs-copilot/`](../projects/docs-copilot/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 9](../09-agents-mcp/) · ➡️ [Week 11](../11-java-basics/)

**A trace** is the full record of one agent run: every model call, tool call, input, output, token count and duration. Reading traces is how you find *why* an agent fails.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read the [Langfuse docs: Get started with tracing](https://langfuse.com/docs/observability/get-started).
- [ ] **1.2** Sign up for [Langfuse Cloud](https://cloud.langfuse.com/) on the free Hobby plan. Create a project and put the keys in `projects/docs-copilot/.env`, which is git-ignored. Only send test data to it.

## Session 2 · Build (3 hrs)

- [ ] **2.1** **Tracing:** `uv add langfuse`, and switch your import to Langfuse's drop-in wrapper: `from langfuse.openai import OpenAI` (see the [Langfuse OpenAI integration](https://langfuse.com/integrations/model-providers/openai-py)). Every model call now shows up in Langfuse.
- [ ] **2.2** **Task set:** `evals/agent_tasks.jsonl` with 20+ tasks:
  ```json
  {"id": "t01", "task": "How do I add auth with OAuth2 and what do I need to install?", "expected_tools": ["search_docs"], "must_mention": ["OAuth2PasswordBearer"]}
  ```
- [ ] **2.3** **Agent eval script:** for each task, record **success** (the `must_mention` check, or the judge from Week 8), **right tool used**, **number of steps**, and **total tokens**. Print a summary table.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Re-read the "error analysis" part of [Hamel's Field Guide](https://hamel.dev/blog/posts/field-guide/).

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Read 30 traces** in Langfuse. For each failure, write a one-line category in `evals/failures.md` (for example "searched with the wrong keywords", "stopped too early", "ignored the tool result", "looped").
- [ ] **4.2** Count the categories, and **fix the top 3**: better tool descriptions, a better system prompt, a better search query, or a step limit.
- [ ] **4.3** Re-run the eval and write a **before/after table**: success rate, average steps, average tokens.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** README: an agent eval section with the before/after table and the failure categories.
- [ ] **5.2** Fill in [`notes.md`](notes.md). This is the end of the Python AI block, so write a longer one.
- [ ] **5.3** Commit and push, then tick Week 10 in the [main README](../README.md#progress).

---

## ✅ Done when
- 20+ agent tasks with automatic scoring
- Traces are visible in Langfuse
- A before/after table showing that your fixes moved the numbers
