<div align="center">

<h1>PYTHON + FASTAPI</h1>
<h3>2-Week Intensive Backend Engineering Roadmap</h3>

<p><strong>A structured guide for developers transitioning into Python backend development — from foundations to production-ready APIs in 14 days.</strong></p>

<p>
  <img src="https://img.shields.io/badge/Duration-14_Days-blue?style=for-the-badge" alt="Duration">
  <img src="https://img.shields.io/badge/Level-Beginner_to_Intermediate-green?style=for-the-badge" alt="Level">
  <img src="https://img.shields.io/badge/Stack-FastAPI_%7C_Python_%7C_PostgreSQL-009688?style=for-the-badge" alt="Stack">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p>
  <a href="#overview">Overview</a> ·
  <a href="#week-1--python--backend-foundations">Week 1</a> ·
  <a href="#week-2--real-backend-development">Week 2</a> ·
  <a href="#full-resource-list">Resources</a> ·
  <a href="#success-formula">Success Formula</a>
</p>

</div>

---

## Overview

This roadmap is designed for developers who want to quickly transition into **Python backend development using FastAPI**. Through focused daily learning and hands-on project building, you will be productive in backend development within **14 days**.

---

## Final Goals

By the end of this roadmap, you will be able to:

- Build REST APIs using FastAPI
- Write professional Python code
- Connect APIs to databases
- Use SQLAlchemy ORM
- Implement JWT authentication
- Structure scalable backend projects
- Collaborate using Git & GitHub
- Build complete backend systems

---

## Prerequisites

Before starting, you should already understand:

- Basic programming logic
- Functions and variables
- What APIs are
- Async concepts (basic)
- Git basics

---

## Recommended Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python            | Backend programming language    |
| FastAPI           | API framework                   |
| SQLAlchemy        | ORM                             |
| SQLite/PostgreSQL | Database                        |
| Pydantic          | Data validation                 |
| JWT               | Authentication                  |
| Git & GitHub      | Version control & collaboration |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-cc2627?style=for-the-badge&logo=python&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## Week 1 — Python & Backend Foundations

### Day 1 — Python Crash Course

**Topics:** Python syntax, variables, lists, tuples, dictionaries, loops, functions, conditionals, basic classes

**Practice Projects:**
- Calculator
- Student grading system
- Todo app (terminal)

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | Python Official Documentation | [docs.python.org](https://docs.python.org/3/) |
| Video | freeCodeCamp Python for Beginners | [youtube.com](https://www.youtube.com/watch?v=rfscVS0vtbw) |
| Video | Corey Schafer – Python Tutorials | [youtube.com](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU) |
| Video | Python Full Course – Programming with Mosh | [youtube.com](https://youtu.be/7t2alSnE2-I) |
| Book | Introduction to Python Programming (PDF) | [Download PDF](https://github.com/user-attachments/files/28959314/Introduction_to_Python_Programming_-_WEB.pdf) |

---

### Day 2 — Advanced Python

**Topics:** List comprehensions, lambda functions, exception handling, file handling, modules, virtual environments

**Practice Projects:**
- Notes saver
- JSON file reader/writer

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | Python Exceptions | [docs.python.org](https://docs.python.org/3/tutorial/errors.html) |
| Article | Real Python – List Comprehensions | [realpython.com](https://realpython.com/list-comprehension-python/) |
| Article | Real Python – Virtual Environments | [realpython.com](https://realpython.com/python-virtual-environments-a-primer/) |

---

### Day 3 — OOP & Project Structure

**Topics:** Classes, inheritance, encapsulation, constructors (`__init__`), package structure

**Practice Project:** Library Management System

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | Python OOP Documentation | [docs.python.org](https://docs.python.org/3/tutorial/classes.html) |
| Video | Corey Schafer – OOP Series | [youtube.com](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) |

---

### Day 4 — APIs & HTTP Fundamentals

**Topics:** What is an API, REST APIs, HTTP methods, status codes, JSON, client-server architecture

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Create data   |
| PUT    | Update data   |
| DELETE | Remove data   |

**Tools:**
- [Postman](https://www.postman.com/)
- [Thunder Client (VS Code Extension)](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)

**Practice:** Test public APIs using [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | MDN – HTTP Overview | [developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview) |
| Article | REST API Tutorial | [restfulapi.net](https://restfulapi.net/) |

---

### Day 5 — Introduction to FastAPI

**Topics:** Installing FastAPI, creating routes, path parameters, query parameters, request bodies, decorators

```python
@app.get("/")
@app.post("/items")
@app.put("/items/{id}")
@app.delete("/items/{id}")
```

**Practice Project:** Books CRUD API

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | FastAPI Official Documentation | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| Video | FastAPI Full Course – Amigoscode | [youtube.com](https://www.youtube.com/watch?v=SORiTsvnU28) |
| Video | FastAPI Crash Course – Traversy Media | [youtube.com](https://www.youtube.com/watch?v=0sOvCWFmrtA) |
| Book | FastAPI Tutorial (PDF) | [Download PDF](https://github.com/user-attachments/files/28959335/fastapi_tutorial.1.pdf) |

---

### Day 6 — Pydantic & Validation

**Topics:** Request schemas, response schemas, data validation with Pydantic

**Practice Project:** User Registration API — email validation, password validation, response schemas

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | Pydantic Official Documentation | [docs.pydantic.dev](https://docs.pydantic.dev/) |
| Docs | FastAPI – Request Body | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/body/) |

---

### Day 7 — Database Basics

**Topics:** SQLite, PostgreSQL, tables, relationships, primary keys, foreign keys, ORM concept, SQLAlchemy basics

**Practice Project:** Task Manager API

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | SQLAlchemy Documentation | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/en/20/) |
| Docs | FastAPI + SQL Databases Tutorial | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| Video | SQLAlchemy Crash Course | [youtube.com](https://www.youtube.com/watch?v=cYWiDiIUxQc) |

---

## Week 2 — Real Backend Development

### Day 8 — SQLAlchemy Deep Dive

**Topics:** Models, relationships, CRUD operations, sessions

**Practice:** Build a User and Posts relationship system

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | SQLAlchemy ORM Tutorial | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/en/20/orm/tutorial.html) |
| Article | Real Python – SQLAlchemy ORM | [realpython.com](https://realpython.com/python-sqlalchemy/) |

---

### Day 9 — Authentication & Security

**Topics:** Password hashing, JWT authentication, login system, authorization

**Practice Project:** Complete authentication system — register, login, protected routes

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | FastAPI Security Documentation | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/security/) |
| Docs | python-jose (JWT library) | [python-jose.readthedocs.io](https://python-jose.readthedocs.io/en/latest/) |
| Docs | passlib (password hashing) | [passlib.readthedocs.io](https://passlib.readthedocs.io/en/stable/) |
| Video | FastAPI Auth – Sanjeev Thiyagarajan | [youtube.com](https://www.youtube.com/watch?v=0sOvCWFmrtA) |

---

### Day 10 — Professional Project Architecture

**Topics:** Scalable backend structure, separation of concerns, clean code practices

**Recommended Project Structure:**

```
app/
├── routers/
├── models/
├── schemas/
├── database/
├── services/
├── auth/
├── config/
└── main.py
```

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | FastAPI – Bigger Applications | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/bigger-applications/) |
| Article | Real Python – Application Layouts | [realpython.com](https://realpython.com/python-application-layouts/) |

---

### Day 11 — Async Programming & Dependencies

**Topics:** `async`/`await`, dependency injection, middleware, `Depends()`

**Practice:** Protected endpoints, middleware logging

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | FastAPI – Dependencies | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/dependencies/) |
| Docs | FastAPI – Async | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/async/) |
| Docs | Python asyncio | [docs.python.org](https://docs.python.org/3/library/asyncio.html) |

---

### Day 12 — Environment Variables & File Uploads

**Topics:** `.env` files, sending emails, file uploads, configuration management

**Practice Projects:** OTP email system, Profile upload API

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Docs | python-dotenv | [pypi.org](https://pypi.org/project/python-dotenv/) |
| Docs | FastAPI – File Uploads | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/request-files/) |
| Docs | FastAPI – Background Tasks | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/background-tasks/) |

---

### Day 13 — GitHub Team Workflow

**Topics:** Git branching, pull requests, merge conflicts, code reviews, team collaboration

**Resources:**

| Type | Resource | Link |
| ---- | -------- | ---- |
| Interactive | GitHub Skills | [skills.github.com](https://skills.github.com/) |
| Docs | Git Official Documentation | [git-scm.com](https://git-scm.com/doc) |
| Video | Git & GitHub Crash Course – freeCodeCamp | [youtube.com](https://www.youtube.com/watch?v=RGOj5yH7evk) |
| Article | Atlassian – Git Branching Guide | [atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) |

---

### Day 14 — Final Backend Project

Build one complete project from scratch:

| Option                | Complexity |
| --------------------- | ---------- |
| Blog API              | Beginner   |
| Task Manager API      | Beginner   |
| E-commerce API        | Advanced   |
| School Management API | Advanced   |

**Project Must Include:**

- Authentication (JWT)
- CRUD operations
- Database integration
- Data validation (Pydantic)
- Protected routes
- Clean architecture
- GitHub repository
- API documentation (FastAPI auto-docs at `/docs`)

---

## Full Resource List

### Python

| Resource | Link |
| -------- | ---- |
| Python Official Documentation | [docs.python.org](https://docs.python.org/3/) |
| Introduction to Python Programming (PDF) | [Download PDF](https://github.com/user-attachments/files/28959314/Introduction_to_Python_Programming_-_WEB.pdf) |
| freeCodeCamp Python Course | [youtube.com](https://www.youtube.com/watch?v=rfscVS0vtbw) |
| Python Full Course – Programming with Mosh | [youtube.com](https://youtu.be/7t2alSnE2-I) |
| Real Python | [realpython.com](https://realpython.com/) |
| Corey Schafer Python Series | [youtube.com](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU) |

### FastAPI

| Resource | Link |
| -------- | ---- |
| FastAPI Official Documentation | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| FastAPI Tutorial (PDF) | [Download PDF](https://github.com/user-attachments/files/28959335/fastapi_tutorial.1.pdf) |
| FastAPI Full Course – Amigoscode | [youtube.com](https://www.youtube.com/watch?v=SORiTsvnU28) |
| FastAPI Crash Course – Traversy Media | [youtube.com](https://www.youtube.com/watch?v=0sOvCWFmrtA) |

### SQLAlchemy & Databases

| Resource | Link |
| -------- | ---- |
| SQLAlchemy Official Documentation | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/en/20/) |
| FastAPI + SQL Databases | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/sql-databases/) |
| PostgreSQL Documentation | [postgresql.org](https://www.postgresql.org/docs/) |

### Git & GitHub

| Resource | Link |
| -------- | ---- |
| GitHub Skills (Interactive) | [skills.github.com](https://skills.github.com/) |
| Git Official Documentation | [git-scm.com](https://git-scm.com/doc) |
| freeCodeCamp Git & GitHub Course | [youtube.com](https://www.youtube.com/watch?v=RGOj5yH7evk) |

---

## Daily Study Routine

| Activity              | Time     |
| --------------------- | -------- |
| Learning Concepts     | 2 Hours  |
| Practical Coding      | 4+ Hours |
| Documentation Reading | 1 Hour   |

---

## Important Advice

**Do NOT:**
- Spend too much time on theory without building
- Learn desktop GUI development — it is not relevant here
- Jump into Django before mastering FastAPI
- Watch tutorials without writing code alongside them

**DO:**
- Build a project every single day
- Practice APIs constantly
- Read official documentation
- Work in teams and participate in code reviews
- Push code to GitHub every day

---

## Priority Learning Order

```
1. Python basics
2. FastAPI routes
3. Pydantic validation
4. Database integration
5. Authentication
6. Project architecture
7. Git workflow
```

---

## Success Formula

```
Learn → Build → Break → Fix → Repeat
```

> Consistency for **14 focused days** is enough to become productive in backend development.

---

<div align="center">

Built for developers who learn by doing.

</div>

---

*by [@tajirdev](https://github.com/tajirdev)*
