# Week 14 · Spring Boot: security, tests, CI

> **Goal:** make the job tracker production-style: login and roles, real tests against a real Postgres, and GitHub Actions running them on every push.
> **Time:** about 10 hrs · **Code goes in:** [`projects/job-tracker-api/`](../projects/job-tracker-api/) · **Notes:** [`notes.md`](notes.md)
> ⬅️ [Week 13](../13-spring-boot-api/) · ➡️ [Week 15](../15-production/)

---

## Session 1 · Learn (1 hr)

- [ ] **1.1** Do the Spring guide [Securing a Web Application](https://spring.io/guides/gs/securing-web/).
- [ ] **1.2** Skim [Baeldung: Spring Boot](https://www.baeldung.com/spring-boot) for the Spring Security pages you need.

## Session 2 · Build (3 hrs)

- [ ] **2.1** Add **Spring Security**: HTTP Basic auth to start, with two users: `user` (can read) and `admin` (can create and delete).
- [ ] **2.2** Protect the endpoints by role. Check that you get a 401 without login and a 403 with the wrong role.
- [ ] **2.3** Stretch: switch to **JWT** login (`POST /auth/login` returns a token).

## Session 3 · Learn (1 hr)

- [ ] **3.1** Read [Testcontainers for Java: Postgres module](https://java.testcontainers.org/modules/databases/postgres/). It starts a throwaway Postgres in Docker for each test run.
- [ ] **3.2** Read the [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart).

## Session 4 · Build (3 hrs)

- [ ] **4.1** **Unit tests** (JUnit + Mockito) for one service class.
- [ ] **4.2** **Integration tests** with Testcontainers: create a job via the API, read it back, and check the auth rules.
- [ ] **4.3** **CI:** `.github/workflows/job-tracker-api.yml` **at the repo root**, which runs `./mvnw test` with `working-directory: projects/job-tracker-api` on every push that touches that folder. Docker is available on GitHub's Ubuntu runners, so Testcontainers works.
- [ ] **4.4** Push, and watch it go green on the Actions tab.

## Session 5 · Wrap up (2 hrs)

- [ ] **5.1** README: auth rules, how to run the tests, and a CI badge.
- [ ] **5.2** Fill in [`notes.md`](notes.md).
- [ ] **5.3** Commit and push, then tick Week 14 in the [main README](../README.md#progress).

---

## ✅ Done when
- Endpoints are protected by role
- Integration tests run against a real Postgres via Testcontainers
- GitHub Actions is green

## Extra (only if you have time)
- 🗺️ [roadmap.sh/spring-boot](https://roadmap.sh/spring-boot), to spot gaps
