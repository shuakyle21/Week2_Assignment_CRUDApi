from fastapi import FastAPI

app = FastAPI()

tasks = [
    { "id": 1, "title": "Clean room", "done": False },
    { "id": 2, "title": "Buy groceries", "done": True },
    { "id": 3, "title": "Walk the dog", "done": False }
]   

@app.get("/")
async def root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
async def health():
    return { "status": "ok" }

@app.get("/tasks")
async def get_tasks(id: int = None, title: str = None, done: bool = None):
    for task in tasks:
        print(f"Task: {task}")
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return { "error": "Task not found" }