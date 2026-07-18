# Week 2 Assignment - Task CRUD API

A FastAPI-based REST API for managing a task list with full CRUD (Create, Read, Update, Delete) operations. This API allows users to create, retrieve, update, and delete tasks with support for filtering and status tracking.

## How to run

```bash
# Install dependencies
pip install fastapi uvicorn

# Start the server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## Endpoints

| Method | Path         | Description                              |
|--------|--------------|------------------------------------------|
| GET    | /            | Welcome message with API info            |
| GET    | /health      | Health check endpoint                    |
| GET    | /tasks       | Retrieve all tasks                       |
| GET    | /tasks/{id}  | Retrieve a specific task by ID           |
| POST   | /tasks       | Create a new task                        |
| PUT    | /tasks/{id}  | Update an existing task                  |
| DELETE | /tasks/{id}  | Delete a task                            |

## Example request

```bash
# Get all tasks
curl -i http://localhost:8000/tasks

# Get a specific task
curl -i http://localhost:8000/tasks/1

# Create a new task
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Study FastAPI", "done": false}'

# Update a task
curl -i -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Study FastAPI", "done": true}'

# Delete a task
curl -i -X DELETE http://localhost:8000/tasks/1
```

## Swagger UI

![Screenshot](images/screenshot.png)

