# Week 4 · LLM API fundamentals

> **Goal:** learn the 5 building blocks every AI app uses: chat with history, streaming, tool calling, structured output, and logging tokens and cost.
> **Time:** about 10 hrs · **Code goes in:** [`projects/llm-basics/`](../projects/llm-basics/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 3](../03-python/) · ➡️ [Week 5](../05-rag-ingestion/)

**How we call the model:** the `openai` Python package pointed at Ollama. The same code works with OpenAI, Gemini, Groq and others by changing `base_url` and `api_key`.

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
```

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Watch [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (Andrej Karpathy, 1 hr). This is the mental model for everything after.

## Session 2 · Build (3 hrs)

- [ ] **2.1** `uv add openai` in `projects/llm-basics`.
- [ ] **2.2** **Chat CLI with memory:** `chat.py` loops: read user input → append to a `messages` list → call the model → print the reply → append it. Notice the model only "remembers" because you resend the whole list every time.
- [ ] **2.3** **Streaming:** add `stream=True` and print tokens as they arrive (like ChatGPT typing). See the [openai-python README](https://github.com/openai/openai-python#streaming-responses).
- [ ] **2.4** **System prompt:** add a `{"role": "system", ...}` message that gives the bot a personality. Try 3 different ones and see how the answers change.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read Ollama's [Tool support](https://ollama.com/blog/tool-support) and [Structured outputs](https://ollama.com/blog/structured-outputs) posts.
- [ ] **3.2** Read the [OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility) page for Ollama. It lists what works through the `openai` package.
- [ ] **3.3** Skim the [Prompt Engineering Guide](https://www.promptingguide.ai/): the "Introduction" and "Techniques: zero-shot, few-shot, chain-of-thought" sections.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Tool calling (text-to-SQL):** `sql_agent.py`
  1. Define one tool, `run_sql(query: str)`, that runs a **SELECT** on your Week 1 job tracker database.
  2. Safety: create a **read-only** Postgres user (`CREATE ROLE reader LOGIN PASSWORD '...'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader;`) and connect as it. The model must not be able to delete your data.
  3. Ask "Which company has the most applications?" The model should call the tool, you run it and send back the result, and the model answers in words.
- [ ] **4.2** **Structured output:** `extract.py` turns a pasted job post into a pydantic object `Job(title, company, skills: list[str], salary: str | None)`. Pass `response_format` with your model's JSON schema (`Job.model_json_schema()`), then check it with `Job.model_validate_json(...)`.
- [ ] **4.3** **Token and cost logger:** a function every call goes through that appends one line to `calls.jsonl`: model, `usage.prompt_tokens`, `usage.completion_tokens`, latency in ms, and *what it would have cost* on a paid API (put a price per 1M tokens in a config dict).
- [ ] **4.4** **Retries and cache:**
  - Wrap calls with retries and exponential backoff, using [tenacity](https://tenacity.readthedocs.io/) or your own loop. Test it by stopping Ollama mid-run (`sudo systemctl stop ollama`).
  - Add a simple cache: the same prompt returns the saved answer instead of calling the model (a dict or a JSON file keyed by a hash of the prompt).

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Update `projects/llm-basics/README.md` with a section per feature and a sample of `calls.jsonl`.
- [ ] **5.2** Fill in [`notes.md`](notes.md). How many tokens did your longest chat use? How slow is the 3B model on your laptop (tokens per second)?
- [ ] **5.3** Commit and push, then tick Week 4 in the [main README](../README.md#progress).

---

## ✅ Done when
- The chat CLI streams and remembers context
- The model answers a question by calling `run_sql`, and it cannot write to the database
- `extract.py` returns valid pydantic objects for 3 different job posts
- Every call is logged with tokens, latency and an estimated cost

## Extra (only if you have time)
- 🎥 [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (Karpathy). Watch over a few sessions.
- 🎓 [Anthropic courses](https://github.com/anthropics/courses): the prompt engineering tutorial is excellent, and the ideas apply to any model
- 💻 [OpenAI Cookbook](https://cookbook.openai.com/): examples work with Ollama by changing `base_url`
