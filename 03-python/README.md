# Week 3 · Python for a JavaScript developer

> **Goal:** go from beginner to comfortable in Python: the language, packages with uv, data validation with pydantic, and tests with pytest.
> **Time:** about 10 hrs · **Code goes in:** [`projects/llm-basics/`](../projects/llm-basics/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 2](../02-sql-indexes-transactions/) · ➡️ [Week 4](../04-llm-apis/)

**Cheat sheet: JS/TS → Python**

| JS / TS | Python |
|---|---|
| `const x = [1, 2].map(n => n * 2)` | `x = [n * 2 for n in [1, 2]]` (list comprehension) |
| `{a: 1}` object | `{"a": 1}` dict |
| `interface User { name: string }` | `class User(BaseModel): name: str` (pydantic) |
| `async/await`, `Promise.all` | `async/await`, `asyncio.gather` |
| `try/catch` | `try/except` |
| `npm init`, `npm i x`, `node app.js` | `uv init`, `uv add x`, `uv run app.py` |
| Jest | pytest |
| Express | FastAPI |

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Watch [Learn Python: Full Course](https://www.youtube.com/watch?v=rfscVS0vtbw) (freeCodeCamp) at 1.5-2x. Skip anything that works the same as JS, and focus on lists, dicts, loops, functions, classes and exceptions.
- [ ] **1.2** Read the [uv guide: working on projects](https://docs.astral.sh/uv/guides/projects/) (10 min).

## Session 2 · Build (3 hrs)

- [ ] **2.1** Create the project:
  ```bash
  cd projects/llm-basics
  uv init
  uv add pydantic httpx python-dotenv
  uv add --dev pytest
  ```
- [ ] **2.2** Build **3 small CLI tools** in `projects/llm-basics/tools/`:
  1. `wordcount.py`: read a text file and print the 10 most common words (practice: files, dicts, sorting)
  2. `weather.py`: call a free public API with `httpx` and print the result (practice: HTTP, JSON). For example `https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current=temperature_2m` (no key needed).
  3. `jobs.py`: read a JSON file of job posts into **pydantic** models and print the ones matching a skill (practice: classes, validation)
- [ ] **2.3** Run each one with `uv run tools/<name>.py`.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Watch 3 [Corey Schafer videos](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU): **list comprehensions**, **decorators**, and **context managers** (the `with` statement).
- [ ] **3.2** Read the [Pydantic docs: Models](https://docs.pydantic.dev/latest/concepts/models/), the first half.

## Session 4 · Build (3 hrs)

- [ ] **4.1** Write **pytest tests** for all 3 tools in `projects/llm-basics/tests/`, and run them with `uv run pytest`. Read the [pytest getting started guide](https://docs.pytest.org/en/stable/getting-started.html) first.
- [ ] **4.2** Connect Python to your Week 1 database with [psycopg](https://www.psycopg.org/psycopg3/docs/basic/usage.html):
  ```bash
  uv add "psycopg[binary]"
  ```
  Write `tools/db_report.py`, which runs 3 of your Week 1 queries and prints the results. Read the connection URL from the environment (`DATABASE_URL` in `.env`, loaded with `python-dotenv`).
- [ ] **4.3** Your first AI call from your own code. Copy the `chat()` part of [`00-setup/check_setup.py`](../00-setup/check_setup.py) into `llm_hello.py` and ask the model a question about Python.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Add a `projects/llm-basics/README.md`: what each tool does and how to run the tests.
- [ ] **5.2** Fill in [`notes.md`](notes.md). What felt different from JS?
- [ ] **5.3** Commit and push, then tick Week 3 in the [main README](../README.md#progress).

---

## ✅ Done when
- 3 tools run, and `uv run pytest` passes
- Python can read from your Postgres database
- `llm_hello.py` gets an answer from Ollama

## Extra (only if you have time)
- 📖 [The official Python tutorial](https://docs.python.org/3/tutorial/), sections 4-9
- 📖 [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/): turn `jobs.py` into a tiny API (it feels like Express)
