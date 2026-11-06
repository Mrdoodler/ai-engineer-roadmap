# /// script
# requires-python = ">=3.12"
# dependencies = ["openai>=1.40", "psycopg[binary]>=3.2"]
# ///
"""Week 0 setup check. Run from the repo root:

    uv run 00-setup/check_setup.py

It tests the three things every later week needs:
  1. Ollama chat model answers
  2. Ollama embedding model returns a vector
  3. Postgres (Docker) is reachable and pgvector is enabled
"""

import os
import sys

import psycopg
from openai import OpenAI

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
CHAT_MODEL = os.getenv("CHAT_MODEL", "qwen2.5:3b")
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5433/roadmap")

# Ollama ignores the API key, but the OpenAI SDK requires one to be set.
client = OpenAI(base_url=LLM_BASE_URL, api_key="ollama")


def chat() -> str:
    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": "Say hello in five words."}],
    )
    return resp.choices[0].message.content.strip()


def embed() -> str:
    resp = client.embeddings.create(model=EMBED_MODEL, input=["hello world"])
    return f"got a vector with {len(resp.data[0].embedding)} numbers"


def database() -> str:
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        (version,) = conn.execute(
            "SELECT extversion FROM pg_extension WHERE extname = 'vector'"
        ).fetchone()
        return f"pgvector {version} is enabled"


FIXES = {
    "Ollama chat": f"Is Ollama running? Try `ollama run {CHAT_MODEL} hi`. Missing model? `ollama pull {CHAT_MODEL}`",
    "Ollama embeddings": f"Run `ollama pull {EMBED_MODEL}`",
    "Postgres + pgvector": "Run `docker compose up -d` from the repo root, wait 5 seconds, try again",
}


def main() -> int:
    ok = True
    for name, fn in [("Ollama chat", chat), ("Ollama embeddings", embed), ("Postgres + pgvector", database)]:
        try:
            print(f"[ OK ] {name}: {fn()}")
        except Exception as e:  # show every failure, not just the first
            ok = False
            print(f"[FAIL] {name}: {type(e).__name__}: {e}")
            print(f"       Fix: {FIXES[name]}")
    print("\nAll good. Week 0 is done!" if ok else "\nFix the [FAIL] lines above and run again.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
