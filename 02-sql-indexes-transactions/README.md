# Week 2 · Advanced SQL, indexes, transactions

> **Goal:** write advanced queries (aggregates, window functions, CTEs) and understand **why** a query is fast or slow and how to make it safe when two users write at once.
> **Time:** about 10 hrs · **Code goes in:** [`projects/sql-playground/`](../projects/sql-playground/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 1](../01-sql-basics/) · ➡️ [Week 3](../03-python/)

**Why this matters for AI:** RAG in Weeks 5-8 is "search a Postgres table really fast". Indexes and `EXPLAIN` are how you'll make that fast.

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read [Use The Index, Luke](https://use-the-index-luke.com/): the chapters "Anatomy of an Index" and "The Where Clause".
- [ ] **1.2** Read the Postgres docs on [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) (first section only) so you can read query plans.

## Session 2 · Build (3 hrs)

- [ ] **2.1** Do [pgexercises: Aggregates](https://pgexercises.com/questions/aggregates/), including the window function ones near the end.
- [ ] **2.2** Read the Postgres tutorial on [Window Functions](https://www.postgresql.org/docs/current/tutorial-window.html) and [WITH queries (CTEs)](https://www.postgresql.org/docs/current/queries-with.html) when the exercises need them.
- [ ] **2.3** Add 20 more queries to `projects/sql-playground/queries.sql` (30 in total), including at least 3 window functions (`ROW_NUMBER`, `RANK`, running totals) and 3 CTEs.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Watch [Hussein Nasser](https://www.youtube.com/@hnasr) on **ACID** and **transaction isolation levels**. Search his channel; each video is 20-40 min.
- [ ] **3.2** Skim the Postgres docs on [Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html): just Read Committed vs. Repeatable Read vs. Serializable.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Index experiment.** In `projects/sql-playground/indexes.sql`:
  1. Make a big table with fake rows: `INSERT INTO ... SELECT ... FROM generate_series(1, 1000000)`
  2. Run `EXPLAIN ANALYZE` on a slow query (for example filter by email or date). Save the output as a comment.
  3. Add an index (`CREATE INDEX ...`), and run `EXPLAIN ANALYZE` again. Save the output.
  4. Write one line: what changed in the plan (Seq Scan → Index Scan) and how much faster it got.
- [ ] **4.2** **Lost update demo.** In `projects/sql-playground/transactions.md`, open **two** terminals with `psql` and act out two users updating the same row:
  1. Show the bug: both read `balance = 100`, both write `balance - 10`, so one update is lost.
  2. Fix it with `SELECT ... FOR UPDATE` and show the second session waits.
  3. Show a `ROLLBACK` undoing a change.
  Paste the commands and outputs from both terminals.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Add a `projects/sql-playground/README.md`: what's in each file, how to run it, and your before/after index numbers.
- [ ] **5.2** Fill in [`notes.md`](notes.md).
- [ ] **5.3** Commit and push, then tick Week 2 in the [main README](../README.md#progress).

---

## ✅ Done when
- 30+ queries in `queries.sql`, including window functions and CTEs
- An `EXPLAIN ANALYZE` before/after with real timings
- A lost-update demo and its fix written down
- You can explain what an index is, and when it *doesn't* help

## Extra (only if you have time)
- [pgexercises](https://pgexercises.com/): the rest of the categories
- 🎥 [SQL Tutorial: Full Database Course](https://www.youtube.com/watch?v=HXV3zeQKqGY): the sections you skipped
