from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task CRUD API",
    description="A simple task management API built with FastAPI to demonstrate full CRUD operations.",
    version="1.0.0",
)


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


tasks: List[Task] = []


@app.get("/", tags=["Root"])
def read_root():
    """Entry point of the API."""
    return {
        "message": "Welcome to the Task CRUD API",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Check whether the server is up and running."""
    return {"status": "ok"}


@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def get_tasks():
    """Retrieve all tasks."""
    return tasks


@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: int):
    """Retrieve a single task by its id."""
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
