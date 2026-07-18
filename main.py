from fastapi import FastAPI, HTTPException

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
        
    raise HTTPException(status_code=404, detail=f"Task {id} not found")

@app.post("/tasks")
def create_task(task: dict):
    tasks.append({ "id": len(tasks) + 1, "title": task.get("title"), "done": task.get("done", False) })
    if task.get("title") is None:
        raise HTTPException(status_code=400, detail="Title is required")
    return {201: "Created", "task": tasks}