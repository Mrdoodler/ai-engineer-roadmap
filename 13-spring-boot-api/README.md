# Week 13 · Spring Boot: REST API + database

> **Goal:** build the job tracker from Week 1 as a real Spring Boot REST API backed by Postgres.
> **Time:** about 10 hrs · **Code goes in:** [`projects/job-tracker-api/`](../projects/job-tracker-api/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 12](../12-java-advanced/) · ➡️ [Week 14](../14-spring-boot-security-tests/)

**Coming from Express:** `@RestController` ≈ an Express router, `@GetMapping("/jobs")` ≈ `router.get("/jobs")`, a **JPA entity** ≈ a Mongoose model, and a **repository** ≈ `Model.find()` (but generated for you from method names).

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Watch [Spring Boot Tutorial for Beginners](https://www.youtube.com/watch?v=gJrjgg1KVL4) (Mosh), the first hour.
- [ ] **1.2** Do the Spring guide [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/) (about 15 min).

## Session 2 · Build (3 hrs)

- [ ] **2.1** Generate a project at [start.spring.io](https://start.spring.io/): Java 21, Maven, and these dependencies: **Spring Web, Spring Data JPA, PostgreSQL Driver, Flyway Migration, Validation**. Unzip it into `projects/job-tracker-api/`.
- [ ] **2.2** Point it at the roadmap Postgres in `application.properties`, using a **new database** so you don't touch Week 1's tables:
  ```properties
  spring.datasource.url=jdbc:postgresql://localhost:5433/jobtracker
  spring.datasource.username=postgres
  spring.datasource.password=postgres
  ```
  Create it first: `docker compose exec db createdb -U postgres jobtracker`
- [ ] **2.3** **Flyway migration:** copy your Week 1 `schema.sql` into `src/main/resources/db/migration/V1__init.sql`. Flyway creates the tables when the app starts.

## Session 3 · Learn (1 hr)

- [ ] **3.1** Do the Spring guide [Accessing Data with JPA](https://spring.io/guides/gs/accessing-data-jpa/).
- [ ] **3.2** Skim [Baeldung: Database migrations with Flyway](https://www.baeldung.com/database-migrations-with-flyway).

## Session 4 · Build (3 hrs)

- [ ] **4.1** Entities + repositories for `Company`, `Job`, `Application`.
- [ ] **4.2** REST endpoints: full CRUD for jobs and applications, plus `GET /jobs?company=...&page=0&size=20` with **pagination**.
- [ ] **4.3** **Validation** (`@NotBlank`, `@Valid`) and a **global error handler** (`@RestControllerAdvice`) that returns clean JSON errors, not stack traces.
- [ ] **4.4** Test every endpoint with `curl` or a `.http` file.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** `projects/job-tracker-api/README.md`: how to run it (`./mvnw spring-boot:run`) and an endpoint list.
- [ ] **5.2** Fill in [`notes.md`](notes.md). Express vs. Spring: what surprised you?
- [ ] **5.3** Commit and push, then tick Week 13 in the [main README](../README.md#progress).

---

## ✅ Done when
- The app starts and Flyway creates the tables
- CRUD + pagination work from `curl`
- Bad input returns a clean 400 JSON error

## Extra (only if you have time)
- 🎥 [Amigoscode](https://www.youtube.com/@amigoscode) and [Dan Vega](https://www.youtube.com/@danvega) on Spring Boot + Postgres
- 🎓 [Spring Academy](https://spring.academy/) (free official courses)
