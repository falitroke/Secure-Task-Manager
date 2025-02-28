# API Documentation

## Base URL
`http://localhost:5000/api`

## Endpoints

### POST /login
Authenticate a user and return a JWT token.
- **Request Body**: `{ "username": "string", "password": "string" }`
- **Response**: `{ "access_token": "jwt_string" }`
- **Status Codes**: 200 (Success), 401 (Unauthorized)

### GET /tasks
Retrieve all tasks (authenticated).
- **Headers**: `Authorization: Bearer <token>`
- **Response**: `[ { "id": int, "title": "string", "assignee": "string" } ]`
- **Status Codes**: 200 (Success), 401 (Unauthorized)

### POST /tasks
Create a new task (authenticated).
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**: `{ "title": "string", "assignee": "string" }`
- **Response**: `{ "id": int, "title": "string", "assignee": "string" }`
- **Status Codes**: 201 (Created), 400 (Bad Request), 401 (Unauthorized)