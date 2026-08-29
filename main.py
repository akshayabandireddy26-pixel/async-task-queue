from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_worker import celery_app, generate_statement_task

app = FastAPI(
    title="Asynchronous Task Queue API",
    description="Backend engine offloading heavy PDF statement generation to Celery workers.",
    version="1.0.0"
)


# Pydantic Schema for incoming user request
class StatementRequest(BaseModel):
    user_id: int
    month: str


@app.get("/")
def read_root():
    return {
        "status": "online",
        "service": "Async Task Engine",
        "docs": "/docs"
    }


# Route 1: Trigger background task (Returns immediately in milliseconds!)
@app.post("/statements/generate", status_code=202)
def trigger_statement_generation(request: StatementRequest):
    # Pass task to Celery worker using .delay()
    task = generate_statement_task.delay(request.user_id, request.month)
    
    return {
        "message": "Statement generation started in the background.",
        "task_id": task.id,
        "status_check_url": f"/tasks/{task.id}"
    }


# Route 2: Check Task Status by Task ID
@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    
    if task_result.state == "PENDING":
        return {
            "task_id": task_id,
            "status": "PENDING",
            "message": "Task is waiting in Redis queue or being processed"
        }
    
    elif task_result.state == "SUCCESS":
        return {
            "task_id": task_id,
            "status": "SUCCESS",
            "result": task_result.result
        }
    
    elif task_result.state == "FAILURE":
        return {
            "task_id": task_id,
            "status": "FAILED",
            "error": str(task_result.info)
        }
    
    return {"task_id": task_id, "status": task_result.state}