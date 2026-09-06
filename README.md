# Asynchronous Distributed Task Queue API

A large backend infrastructure using FastAPI‚ Celery‚ and Redis‚ which allows to offload expensive and long-running operations to backend processes while keeping APIs responsive‚ has been developed․

Technologies used
Framework: FastAPI & Uvicorn
Task manager: Celery and Redis
Docker containers and Docker Compose

Methods of API
To start an operation in the background you send a POST request to /statements/generate‚ which then replies with the task ID and the HTTP 202 Accepted response․
GET /tasks/{task_id} - Returns the current status of the task․

## Live Demo & Testing
https://async-task-queue-3.onrender.com/docs
