# Asynchronous Distributed Task Queue API

A complete backend powered by FastAPI‚ Celery and Redis‚ which shifts heavy‚ long-lived tasks (such as generating PDF bank statements) to background threads for a high level of concurrency API responsiveness․

Tech Stack
* Web Framework: FastAPI & Uvicorn
* Task Queue & Broker: Celery & Redis
* Containerization: Docker & Docker Compose

API Endpoints
* POST /statements/generate - Starts a background job and returns its task ID immediately (Status code: 202 Accepted)․
* GET /tasks/{task_id} - Returns the live processing status (PENDING‚ SUCCESS‚ or FAILURE) of a task by its ID․

## Live Demo & Testing
https://async-task-queue-3.onrender.com/docs
