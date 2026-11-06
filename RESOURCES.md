# Resources

Every link from the weekly plans in one place, plus extras. Each week's README says *which* ones to use *when*. This page is for browsing.

## Books
- **Chip Huyen, *AI Engineering*** (O'Reilly, 2025): the single best book for this path · [companion repo](https://github.com/chiphuyen/aie-book) · [blog](https://huyenchip.com/)
- **[Applied LLMs: What We've Learned From a Year of Building](https://applied-llms.org/)**: free and practical

## Foundations
- 🎥 Karpathy: [Intro to LLMs](https://www.youtube.com/watch?v=zjkBMFhNj_g) · [Deep Dive into LLMs](https://www.youtube.com/watch?v=7xTGNNLPyMI) · [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) (optional, deep)
- 🎥 [3Blue1Brown: Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi): visual intuition for transformers and attention

## Setup + tools
- [Ollama](https://ollama.com/) · [qwen2.5](https://ollama.com/library/qwen2.5) · [nomic-embed-text](https://ollama.com/library/nomic-embed-text) · [OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility) · [Tool support](https://ollama.com/blog/tool-support) · [Structured outputs](https://ollama.com/blog/structured-outputs)
- [uv docs](https://docs.astral.sh/uv/) · [Docker Compose](https://docs.docker.com/compose/) · [pgvector/pgvector image](https://hub.docker.com/r/pgvector/pgvector)
- [openai-python](https://github.com/openai/openai-python) (we point it at Ollama) · [OpenAI Cookbook](https://cookbook.openai.com/)
- [Langfuse docs](https://langfuse.com/docs) · [Langfuse Cloud](https://cloud.langfuse.com/)

## SQL / Postgres (Weeks 1-2)
- 🧩 [SQLBolt](https://sqlbolt.com/) · [pgexercises](https://pgexercises.com/)
- 📖 [Postgres tutorial](https://www.postgresql.org/docs/current/tutorial.html) · [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) · [Window functions](https://www.postgresql.org/docs/current/tutorial-window.html) · [CTEs](https://www.postgresql.org/docs/current/queries-with.html) · [Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
- 📖 [Use The Index, Luke](https://use-the-index-luke.com/)
- 🎥 [SQL full course](https://www.youtube.com/watch?v=HXV3zeQKqGY) · [PostgreSQL full course](https://www.youtube.com/watch?v=qw--VYLpxG4) · [Hussein Nasser](https://www.youtube.com/@hnasr) · [Docker for beginners](https://www.youtube.com/watch?v=pTFZFxd4hOI)

## Python (Week 3)
- 🎥 [Python full course](https://www.youtube.com/watch?v=rfscVS0vtbw) · [Corey Schafer playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
- 📖 [Python tutorial](https://docs.python.org/3/tutorial/) · [Real Python](https://realpython.com/) · [Pydantic](https://docs.pydantic.dev/latest/) · [pytest](https://docs.pytest.org/en/stable/getting-started.html) · [psycopg 3](https://www.psycopg.org/psycopg3/docs/basic/usage.html) · [FastAPI](https://fastapi.tiangolo.com/) · [tenacity](https://tenacity.readthedocs.io/)

## LLM apps, RAG, evals (Weeks 4-8)
- 📖 [Prompt Engineering Guide](https://www.promptingguide.ai/) · [Anthropic courses](https://github.com/anthropics/courses)
- 🎥 [RAG From Scratch playlist](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) · [as one video](https://www.youtube.com/watch?v=sVcwVQRHIc8) · [code](https://github.com/langchain-ai/rag-from-scratch)
- 📖 [pgvector](https://github.com/pgvector/pgvector) · [pgvector-python](https://github.com/pgvector/pgvector-python) · [Postgres full text search](https://www.postgresql.org/docs/current/textsearch-intro.html)
- 📖 [Anthropic: Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) · [Cross-encoders](https://sbert.net/docs/cross_encoder/usage/usage.html) · [bge-reranker-base](https://huggingface.co/BAAI/bge-reranker-base)
- 📖 Hamel Husain: [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) · [LLM-as-a-Judge](https://hamel.dev/blog/posts/llm-judge/) · [Field Guide](https://hamel.dev/blog/posts/field-guide/) · [Evals FAQ](https://hamel.dev/blog/posts/evals-faq/)
- 📖 [Shreya Shankar: In Defense of AI Evals](https://www.sh-reya.com/blog/in-defense-ai-evals/) · [Eugene Yan: LLM Patterns](https://eugeneyan.com/writing/llm-patterns/)

## Agents + MCP (Weeks 9-10)
- 📖 [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) · [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) · [Lilian Weng: Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)
- 📖 [MCP intro](https://modelcontextprotocol.io/docs/getting-started/intro) · [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) · [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) · [MCP Inspector](https://github.com/modelcontextprotocol/inspector) · [Claude Code + MCP](https://code.claude.com/docs/en/mcp)
- 🎥 [Intro to MCP Servers with Python](https://www.youtube.com/watch?v=DosHnyq78xY)
- 🎓 [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course) · [Agents Course](https://huggingface.co/learn/agents-course) · [LLM Course](https://huggingface.co/learn/llm-course) · [Anthropic Academy](https://anthropic.skilljar.com/) · [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/)
- 📖 [Langfuse: get started](https://langfuse.com/docs/observability/get-started) · [Langfuse + OpenAI SDK](https://langfuse.com/integrations/model-providers/openai-py)

## Java (Weeks 11-12)
- 🎓 [MOOC.fi Java Programming](https://java-programming.mooc.fi/) · 📖 [dev.java/learn](https://dev.java/learn/) · [Baeldung](https://www.baeldung.com/) · [Java Concurrency](https://www.baeldung.com/java-concurrency) · [Virtual threads](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html) · [JUnit 5](https://docs.junit.org/current/user-guide/)
- 🎥 [Java full course (Bro Code)](https://www.youtube.com/watch?v=xk4_1vDrzzo) · [IntelliJ IDEA](https://www.jetbrains.com/idea/download/)

## Spring Boot + Spring AI (Weeks 13-15)
- 🎥 [Spring Boot for beginners (Mosh)](https://www.youtube.com/watch?v=gJrjgg1KVL4) · [Dan Vega](https://www.youtube.com/@danvega) · [Amigoscode](https://www.youtube.com/@amigoscode) · [Spring Developer](https://www.youtube.com/@SpringSourceDev)
- 📖 [start.spring.io](https://start.spring.io/) · Guides: [REST](https://spring.io/guides/gs/rest-service/) · [JPA](https://spring.io/guides/gs/accessing-data-jpa/) · [Security](https://spring.io/guides/gs/securing-web/) · [all guides](https://spring.io/guides)
- 📖 [Baeldung: Spring Boot](https://www.baeldung.com/spring-boot) · [Flyway](https://www.baeldung.com/database-migrations-with-flyway) · [Testcontainers Postgres](https://java.testcontainers.org/modules/databases/postgres/) · [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart)
- 📖 [Spring AI reference](https://docs.spring.io/spring-ai/reference/) · [Ollama chat](https://docs.spring.io/spring-ai/reference/api/chat/ollama-chat.html) · [Ollama embeddings](https://docs.spring.io/spring-ai/reference/api/embeddings/ollama-embeddings.html) · [PGvector store](https://docs.spring.io/spring-ai/reference/api/vectordbs/pgvector.html)
- 🎓 [Spring Academy](https://spring.academy/)

## Optional: hosted models (Week 15 deploy only)
- [Gemini API](https://ai.google.dev/gemini-api/docs) · [OpenAI-compatible endpoint](https://ai.google.dev/gemini-api/docs/openai) · [pricing / free tier](https://ai.google.dev/gemini-api/docs/pricing) · [AI Studio](https://aistudio.google.com/). On the free tier, Google may use your prompts to improve its products, so only send public data.
- [Cloud Run docs](https://cloud.google.com/run/docs) · [quickstarts](https://cloud.google.com/run/docs/quickstarts)

## Interview prep + roadmaps
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [roadmap.sh/ai-engineer](https://roadmap.sh/ai-engineer) · [roadmap.sh/java](https://roadmap.sh/java) · [roadmap.sh/spring-boot](https://roadmap.sh/spring-boot)
