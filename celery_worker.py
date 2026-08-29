import os
import time
from celery import Celery

# 1. Connect to Redis (Fallback to local Redis if env variable isn't set)
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# 2. Initialize Celery App
celery_app = Celery(
    "tasks",
    broker=REDIS_URL,
    backend=REDIS_URL
)

# 3. Define a Heavy Background Task (e.g. Generating PDF Bank Statements)
@celery_app.task(name="generate_statement")
def generate_statement_task(user_id: int, month: str):
    """Simulates generating a complex PDF bank statement in the background."""
    print(f"Starting PDF generation for User {user_id} for month {month}...")
    
    # Simulate a heavy 10-second PDF processing job
    time.sleep(10)
    
    print(f"Finished PDF generation for User {user_id}!")
    
    return {
        "status": "COMPLETED",
        "user_id": user_id,
        "month": month,
        "download_url": f"https://storage.cloud.com/statements/user_{user_id}_{month}.pdf"
    }