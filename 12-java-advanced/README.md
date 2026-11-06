# Week 12 · Java: generics, streams, concurrency, tests

> **Goal:** the Java features Spring Boot uses everywhere: generics, streams and lambdas, exceptions, concurrency, and JUnit tests.
> **Time:** about 10 hrs · **Code goes in:** [`projects/java-katas/`](../projects/java-katas/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 11](../11-java-basics/) · ➡️ [Week 13](../13-spring-boot-api/)

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Read [dev.java/learn](https://dev.java/learn/): the pages on **generics**, **lambdas** and the **Stream API**.

## Session 2 · Build (3 hrs)

- [ ] **2.1** MOOC.fi **Parts 5-7** (or as far as you get in 2 hrs).
- [ ] **2.2** Rewrite the log analyzer's loops using **streams** (`filter`, `map`, `collect(groupingBy(...))`).

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read [Baeldung: Java Concurrency](https://www.baeldung.com/java-concurrency): skim the list, then read ExecutorService and CompletableFuture.
- [ ] **3.2** Read [Virtual Threads](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html) (Oracle docs). It's Java 21's big feature: thousands of cheap threads.

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Concurrency demo** in `projects/java-katas/concurrency/`: call a public API (for example the weather API from Week 3) **20 times**:
  1. one by one (time it)
  2. with an `ExecutorService` thread pool (time it)
  3. with **virtual threads**, `Executors.newVirtualThreadPerTaskExecutor()` (time it)
  Print the three timings. It's the same idea as `Promise.all` in JS.
- [ ] **4.2** **Port your Week 4 cost logger to Java:** read `calls.jsonl` and print total tokens, total estimated cost, and p50/p95 latency per model.
- [ ] **4.3** **JUnit 5 tests** for the cost logger. See the [JUnit user guide](https://docs.junit.org/current/user-guide/), "Writing Tests".

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** Update the `java-katas` README with your three concurrency timings.
- [ ] **5.2** Fill in [`notes.md`](notes.md).
- [ ] **5.3** Commit and push, then tick Week 12 in the [main README](../README.md#progress).

---

## ✅ Done when
- The concurrency demo prints 3 timings, and virtual threads are clearly faster than sequential
- The cost logger works in Java with passing JUnit tests
- You can explain a lambda and a stream to someone who knows JS
