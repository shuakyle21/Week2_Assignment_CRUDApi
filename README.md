# Task CRUD API

A simple task management REST API built with **FastAPI**. It demonstrates a complete Create, Read, Update, and Delete (CRUD) workflow over an in-memory list of tasks, with request validation and clear, field-level error messages.

## What is this?

This project is a small, self-contained backend service for managing a to-do list of tasks. Each task is represented as:

```json
{
  "id": 1,
  "title": "Buy groceries",
  "done": false
}
```

It's intentionally simple — no database, no authentication — so the focus stays on demonstrating clean REST API design: proper HTTP methods, status codes, validation, and error handling.

## Purpose

This API was built as a hands-on exercise in designing and implementing a full CRUD service with FastAPI, covering:

- Structuring an API around a single resource (`tasks`)
- Returning appropriate HTTP status codes (`200`, `201`, `404`, `422`)
- Validating incoming request bodies and surfacing clear, field-named error messages
- Auto-generated interactive documentation via Swagger UI

## How to Copy / Run Locally

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Week2_Assignment_CRUDApi
   ```

2. **Install dependencies**

   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the server**

   ```bash
   uvicorn main:app --reload
   ```

4. **Open the API**

   - Base URL: `http://127.0.0.1:8000`
   - Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Endpoint          | Description                              | Success Response  | Error Response(s)                        |
|--------|-------------------|-------------------------------------------|--------------------|--------------------------------------------|
| GET    | `/`               | Entry point / welcome message             | `200 OK`           | —                                          |
| GET    | `/health`         | Health check — confirms the server is up  | `200 OK`           | —                                          |
| GET    | `/tasks`          | Retrieve all tasks                        | `200 OK`           | —                                          |
| GET    | `/tasks/{id}`     | Retrieve a single task by id              | `200 OK`           | `404 Not Found`                            |
| POST   | `/tasks`          | Create a new task                         | `201 Created`      | `422 Unprocessable Entity`                 |
| PUT    | `/tasks/{id}`     | Update an existing task                   | `200 OK`           | `404 Not Found`, `422 Unprocessable Entity`|
| DELETE | `/tasks/{id}`     | Delete a task by id                       | `200 OK`           | `404 Not Found`                            |

### Validation

- **POST `/tasks`** requires a `title` (non-empty string). `done` is optional and defaults to `false`. `id` is assigned automatically by the server.
- **PUT `/tasks/{id}`** requires both `title` (non-empty string) and `done` (boolean).
- Any validation failure returns `422 Unprocessable Entity` with the offending field named explicitly, e.g.:

  ```json
  {
    "detail": "Validation failed",
    "errors": [
      { "field": "title", "message": "String should have at least 1 character" }
    ]
  }
  ```

- Requesting, updating, or deleting a task that doesn't exist returns `404 Not Found`, e.g.:

  ```json
  { "detail": "Task with id 42 not found" }
  ```

### Example Requests

**Create a task**

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "done": false}'
```

**Update a task**

```bash
curl -X PUT http://127.0.0.1:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries and cook dinner", "done": true}'
```

**Delete a task**

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```

## Swagger UI

FastAPI automatically generates interactive API documentation via Swagger UI, available at `/docs` once the server is running. It lets you explore and try out every endpoint directly from the browser.

![Swagger UI screenshot](images/screenshot.png)

*(Run the server and visit `http://127.0.0.1:8000/docs` to see it live.)*
