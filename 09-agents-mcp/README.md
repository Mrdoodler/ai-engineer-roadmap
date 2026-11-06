# Week 9 · Agents + MCP

> **Goal:** build an agent loop **by hand** (no framework), then expose your Docs Copilot as an **MCP server** that tools like Claude Code can use.
> **Time:** about 10 hrs · **Code goes in:** [`projects/docs-copilot/`](../projects/docs-copilot/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 8](../08-rag-answer-evals/) · ➡️ [Week 10](../10-agent-evals/)

**An agent is just a loop:** call the model with tools → if it asks for a tool, run it and send back the result → repeat until it answers (or hits a limit). You already did one round of this in Week 4's `sql_agent.py`.

**MCP** (Model Context Protocol) is a standard way to offer tools to *any* AI app. It's like a REST API, but for AI assistants.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents). The key lesson: use the simplest pattern that works, and an agent is often not needed.
- [ ] **1.2** Read [Anthropic: Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents).

## Session 2 · Build (3 hrs)

- [ ] **2.1** **Tools:** in `agent/tools.py`, write 3 functions, each with a clear docstring:
  - `search_docs(query, k=5)` → your hybrid + rerank search from Week 6
  - `get_chunk(id)` → the full text of one chunk
  - `run_readonly_sql(query)` → reuse Week 4's read-only SQL tool
- [ ] **2.2** **Agent loop:** `agent/agent.py "question"`
  - Loop: model call with tools → run any tool calls → append the results → repeat
  - **Limits:** max 8 steps, and stop if total tokens go over a budget
  - Print every step, which tool was called with which arguments, so you can watch it think
- [ ] **2.3** Try 5 questions that need **more than one** search, for example "compare X and Y". Note when it goes wrong.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read [MCP: Introduction](https://modelcontextprotocol.io/docs/getting-started/intro) and [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) (the Python tab).
- [ ] **3.2** Watch [Intro to MCP Servers with Python](https://www.youtube.com/watch?v=DosHnyq78xY) (freeCodeCamp) at 1.5x, or just the first half.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **MCP server:** `uv add "mcp[cli]"`, then create `mcp_server.py` using `FastMCP` with your 3 tools (`@mcp.tool()` on each). See the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).
- [ ] **4.2** **Test it with the Inspector:**
  ```bash
  npx @modelcontextprotocol/inspector uv run mcp_server.py
  ```
  Call each tool from the web UI.
- [ ] **4.3** **Connect it to Claude Code:** see [Claude Code MCP docs](https://code.claude.com/docs/en/mcp).
  ```bash
  claude mcp add docs-copilot -- uv --directory "$PWD" run mcp_server.py
  ```
  Then ask Claude a FastAPI question and watch it call *your* search tool.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** README: an "Agent" section and an "MCP server" section, with how to run each and an example transcript.
- [ ] **5.2** Fill in [`notes.md`](notes.md). When did the agent pick the wrong tool or loop forever?
- [ ] **5.3** Commit and push, then tick Week 9 in the [main README](../README.md#progress).

---

## ✅ Done when
- The hand-written agent answers multi-step questions within the step limit
- The MCP server works in the Inspector **and** in Claude Code
- You can explain "workflow vs. agent" from the Anthropic post

## Extra (only if you have time)
- 🎓 [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) and [Agents Course](https://huggingface.co/learn/agents-course) (free)
- 🎓 [Anthropic Academy](https://anthropic.skilljar.com/): *Introduction to Model Context Protocol*
- 📖 [Lilian Weng: LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
