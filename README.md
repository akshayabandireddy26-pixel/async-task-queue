# Asynchronous Distributed Task Queue API

A robust backend service built with **FastAPI**, **Celery**, and **Redis** designed to offload heavy, long-running processes (such as PDF bank statement generation) to background worker threads, ensuring high-concurrency API responsiveness.

## Tech Stack
* **Web Framework:** FastAPI & Uvicorn
* **Task Queue & Broker:** Celery & Redis
* **Containerization:** Docker & Docker Compose

## API Endpoints
* `POST /statements/generate` - Triggers a background job and returns a task ID instantly (Status code: `202 Accepted`).
* `GET /tasks/{task_id}` - Checks the live processing status (`PENDING`, `SUCCESS`, or `FAILURE`) of a given task ID.