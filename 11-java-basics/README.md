# Week 11 · Java basics (coming from TypeScript)

> **Goal:** set up Java 21 and get comfortable with the syntax, classes, interfaces, records, and collections.
> **Time:** about 10 hrs · **Code goes in:** [`projects/java-katas/`](../projects/java-katas/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 10](../10-agent-evals/) · ➡️ [Week 12](../12-java-advanced/)

**Good news:** TypeScript prepared you well. Classes, interfaces and types will feel familiar. What's new: everything lives in a class, types are checked at compile time for real (no `any`), and code is compiled before it runs.

| TypeScript | Java |
|---|---|
| `let n: number = 5` | `int n = 5;` or `var n = 5;` |
| `string[]`, `Map<string, number>` | `List<String>`, `Map<String, Integer>` |
| `type User = {name: string}` | `record User(String name) {}` |
| `arr.filter(...).map(...)` | `list.stream().filter(...).map(...).toList()` |
| `npm` + `package.json` | Maven + `pom.xml` (or Gradle) |

---

## Session 1 · Set up + learn (1 hr)

- [ ] **1.1** Install Java 21 (you have 17):
  ```bash
  sudo apt install openjdk-21-jdk
  sudo update-alternatives --config java   # pick 21
  java -version
  ```
- [ ] **1.2** Install [IntelliJ IDEA](https://www.jetbrains.com/idea/download/) (the free version).
- [ ] **1.3** Start the [MOOC.fi Java Programming](https://java-programming.mooc.fi/) course: read Part 1 and set up their exercise plugin as they describe.

## Session 2 · Build (3 hrs)

- [ ] **2.1** MOOC.fi **Parts 1-2**: you'll move fast through these, since it's mostly syntax you know from JS.
- [ ] **2.2** Commit your exercise solutions into `projects/java-katas/mooc/`.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read [dev.java/learn](https://dev.java/learn/): the pages on classes and objects, interfaces, and **records**.

## Session 4 · Build (3 hrs)

- [ ] **4.1** MOOC.fi **Parts 3-4**: lists, objects, files.
- [ ] **4.2** **Mini project:** a log analyzer CLI in `projects/java-katas/log-analyzer/` that reads a log file and prints counts per level (INFO/WARN/ERROR) and the top 5 error messages. Use classes, an interface, a record, `List`, `Map`, `Set`.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** `projects/java-katas/README.md`: what's there and how to run it.
- [ ] **5.2** Fill in [`notes.md`](notes.md). What's easier in Java than TS, and what's harder?
- [ ] **5.3** Commit and push, then tick Week 11 in the [main README](../README.md#progress).

---

## ✅ Done when
- Java 21 + IntelliJ work
- MOOC.fi Parts 1-4 are done
- The log analyzer runs on a sample log file

## Extra (only if you have time)
- 🎥 [Java Full Course](https://www.youtube.com/watch?v=xk4_1vDrzzo) (Bro Code), as a quick reference
- 🗺️ [roadmap.sh/java](https://roadmap.sh/java), to spot gaps
