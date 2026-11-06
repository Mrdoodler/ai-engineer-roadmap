# Week 1 · SQL basics

> **Goal:** write everyday SQL comfortably: SELECT, WHERE, JOIN, GROUP BY, and design your own tables.
> **Time:** about 10 hrs · **Code goes in:** [`projects/sql-playground/`](../projects/sql-playground/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 0](../00-setup/) · ➡️ [Week 2](../02-sql-indexes-transactions/)

**Coming from MongoDB:** a *table* is a collection, a *row* is a document, a *column* is a field. The big difference is that every row in a table has the same columns, and you connect tables with **JOIN** instead of embedding documents or using `$lookup`.

**Before you start:** run `docker compose up -d` in the repo root.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Do [SQLBolt](https://sqlbolt.com/) lessons **1-6**: SELECT, WHERE, ORDER BY, LIMIT, and simple JOINs. It runs in the browser, so no setup is needed.
- [ ] **1.2** Watch the start of [SQL Tutorial: Full Database Course](https://www.youtube.com/watch?v=HXV3zeQKqGY) (freeCodeCamp) at 1.5x, up to and including "Basic Queries". Skip anything SQLBolt already covered.

## Session 2 · Build (3 hrs)

- [ ] **2.1** Finish [SQLBolt](https://sqlbolt.com/) lessons **7-18**: OUTER JOIN, NULLs, expressions, GROUP BY, INSERT/UPDATE/DELETE, CREATE/ALTER/DROP TABLE.
- [ ] **2.2** Do [pgexercises: Basic](https://pgexercises.com/questions/basic/) (all of them, about 1 hr). These are real Postgres exercises.
- [ ] **2.3** Open a SQL prompt (`docker compose exec db psql -U postgres -d roadmap`) and try `\dt` (list tables), `\d tablename` (describe a table), and `\?` (help).

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read the [Postgres tutorial](https://www.postgresql.org/docs/current/tutorial.html), **Chapter 2 (The SQL Language)**. Skim what you already know.
- [ ] **3.2** Learn about keys: a **primary key** is like Mongo's `_id`, and a **foreign key** is a column pointing to another table's primary key, which Postgres enforces (unlike Mongo refs).

## Session 4 · Build (3 hrs)

- [ ] **4.1** Do [pgexercises: Joins and Subqueries](https://pgexercises.com/questions/joins/).
- [ ] **4.2** Design a **job application tracker** database. You'll reuse it in Week 4 (the AI queries it) and Week 13 (the Spring Boot API). Create `projects/sql-playground/schema.sql` with 5 or more tables, for example:
  - `companies`, `jobs` (belongs to a company), `applications` (belongs to a job), `interviews` (belongs to an application), `skills` + `job_skills` (many-to-many)
  - Use `PRIMARY KEY`, `REFERENCES` (foreign keys), `NOT NULL`, `UNIQUE`, `CHECK`
- [ ] **4.3** Create `projects/sql-playground/seed.sql` with fake data: about 10 companies, 30 jobs, 40 applications. You can ask Ollama or Claude to generate the INSERT statements, but read them.
- [ ] **4.4** Load both files and check that they work:
  ```bash
  docker compose exec -T db psql -U postgres -d roadmap < projects/sql-playground/schema.sql
  docker compose exec -T db psql -U postgres -d roadmap < projects/sql-playground/seed.sql
  ```

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Write your first 10 queries on your own data in `projects/sql-playground/queries.sql`, for example "applications per company", "jobs I haven't applied to" (LEFT JOIN … IS NULL), "skills most asked for" (GROUP BY + COUNT). Put a comment above each one saying what it answers.
- [ ] **5.2** Fill in [`notes.md`](notes.md).
- [ ] **5.3** Commit and push, then tick Week 1 in the [main README](../README.md#progress).

---

## ✅ Done when
- `schema.sql` and `seed.sql` load with no errors
- 10 queries run, including at least 3 JOINs and 2 GROUP BYs
- You can explain the difference between `INNER JOIN` and `LEFT JOIN` out loud

## Extra (only if you have time)
- 🎥 [Learn PostgreSQL: Full Course](https://www.youtube.com/watch?v=qw--VYLpxG4) (freeCodeCamp / Amigoscode)
- 🎥 [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=pTFZFxd4hOI) (Mosh), if Docker still feels like magic
