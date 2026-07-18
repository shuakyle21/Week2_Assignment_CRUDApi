from typing import List

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task CRUD API",
    description="A simple task management API built with FastAPI to demonstrate full CRUD operations.",
    version="1.0.0",
)


class Task(BaseModel):
    id: int
    title: str
    done: bool = False


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the task")
    done: bool = Field(default=False, description="Whether the task is completed")


class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1, description="Title of the task")
    done: bool = Field(..., description="Whether the task is completed")


tasks: List[Task] = []
next_id = 1


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Return validation errors with the offending field name called out explicitly."""
    errors = [
        {"field": str(error["loc"][-1]), "message": error["msg"]}
        for error in exc.errors()
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": "Validation failed", "errors": errors},
    )


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


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(payload: TaskCreate):
    """Create a new task. `title` must be a non-empty string; `id` is assigned automatically."""
    global next_id
    new_task = Task(id=next_id, title=payload.title, done=payload.done)
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, payload: TaskUpdate):
    """Update an existing task's title and done status. Both fields are required."""
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(id=task_id, title=payload.title, done=payload.done)
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")


@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    """Delete a task by its id."""
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": f"Task with id {task_id} deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
