from fastapi import FastAPI

app = FastAPI(
    title="Task CRUD API",
    description="A simple task management API built with FastAPI to demonstrate full CRUD operations.",
    version="1.0.0",
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
