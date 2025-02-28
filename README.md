
# Secure Task Manager

![Build Status](https://github.com/rafael-fuentes/secure-task-manager/actions/workflows/ci.yml/badge.svg)
![Code Coverage](https://img.shields.io/badge/coverage-90%25-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

A task management web application with secure authentication and real-time updates, built for team collaboration.

## Project Overview
Secure Task Manager enables users to create, assign, and manage tasks with JWT-based authentication and PostgreSQL-backed storage (defaults to SQLite if not configured). It leverages Flask for the backend and React for a responsive frontend, showcasing full-stack development and cybersecurity principles. This project demonstrates advanced skills in Python and JavaScript, REST API design, database integration, and secure authentication workflows.

Key features:
- RESTful APIs for task management
- JWT-based authentication with role-based access potential
- Responsive UI with real-time task updates
- Dockerized deployment with CI/CD integration

## Installation Guide
Follow these steps to set up the project locally:

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL (optional, defaults to SQLite)

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/rafael-fuentes/secure-task-manager.git
   cd secure-task-manager
   ```
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Node.js dependencies**:
   ```bash
   npm install
   ```
4. **Set up environment variables** in a `.env` file:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/tasks
   JWT_SECRET=your-secret-key
   ```
   - `DATABASE_URL`: Use your PostgreSQL connection string or omit for SQLite.
   - `JWT_SECRET`: A strong secret key for JWT signing (e.g., generated via `openssl rand -hex 32`).

5. **Run the app**:
   ```bash
   npm start
   ```
   - This builds the React frontend and starts the Flask server on `http://localhost:5000`.

## Usage Examples
Here’s how to interact with Secure Task Manager:

### Via the Web Interface
1. Open `http://localhost:5000` in your browser.
2. Click "Login" (uses default credentials: `admin`/`securepass`).
3. Enter a task title and assignee, then click "Add Task" to create a task.
4. View the updated task list in real-time.

### Via API (using `curl` or Postman)
- **Login**:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -d '{"username": "admin", "password": "securepass"}' \
        http://localhost:5000/api/login
   ```
   Response: `{"access_token": "<jwt_token>"}`

- **Create a Task**:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -H "Authorization: Bearer <jwt_token>" \
        -d '{"title": "Finish report", "assignee": "user1"}' \
        http://localhost:5000/api/tasks
   ```
   Response: `{"id": 1, "title": "Finish report", "assignee": "user1"}`

- **View Tasks**:
   ```bash
   curl -H "Authorization: Bearer <jwt_token>" \
        http://localhost:5000/api/tasks
   ```
   Response: `[ {"id": 1, "title": "Finish report", "assignee": "user1"} ]`

## API Documentation
The API is served under the base URL `http://localhost:5000/api`.

### POST /login
Authenticate a user and return a JWT token.
- **Request Body**: `{ "username": "string", "password": "string" }`
- **Response**: `{ "access_token": "jwt_string" }`
- **Status Codes**: 
  - 200: Success
  - 401: Unauthorized (invalid credentials)

### GET /tasks
Retrieve all tasks (authenticated).
- **Headers**: `Authorization: Bearer <token>`
- **Response**: `[ { "id": int, "title": "string", "assignee": "string" } ]`
- **Status Codes**: 
  - 200: Success
  - 401: Unauthorized (missing or invalid token)

### POST /tasks
Create a new task (authenticated).
- **Headers**: `Authorization: Bearer <token>`
- **Request Body**: `{ "title": "string", "assignee": "string" }`
- **Response**: `{ "id": int, "title": "string", "assignee": "string" }`
- **Status Codes**: 
  - 201: Created
  - 400: Bad Request (missing required fields)
  - 401: Unauthorized (missing or invalid token)

## Tutorial: Using Secure Task Manager
### Running Locally
1. After installation, start the app with `npm start`.
2. Access `http://localhost:5000` in your browser.
3. Log in with the default credentials (`admin`/`securepass`).
4. Add tasks via the form and see them listed immediately.

### Testing the API
1. Use a tool like Postman or `curl` to test the endpoints.
2. Start by logging in to get a JWT token, then use it in the `Authorization` header for subsequent requests.

### Deployment
- **Docker**: Build and run locally:
  ```bash
  docker build -t secure-task-manager .
  docker run -p 5000:5000 secure-task-manager
  ```
- **Heroku**: Deploy via the CI/CD pipeline (see Contributing Guidelines).

## Contributing Guidelines
Contributions are welcome! Follow these steps:

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
2. **Code Standards**:
   - Python: Adhere to PEP8 (use `flake8` for linting).
   - JavaScript: Follow ESLint rules (config in `.eslintrc.json`, not included but recommended).
3. **Testing**:
   - Add unit tests in `tests/` using `pytest`.
   - Aim for ≥85% code coverage (`pytest --cov=src`).
4. **Commit and Push**:
   - Use clear commit messages (e.g., `feat: add task deletion endpoint`).
   - Push your branch: `git push origin feature/new-feature`.
5. **Submit a Pull Request**:
   - Include a detailed description of changes.
   - Ensure the CI pipeline passes (tests, build).

### CI/CD Pipeline
- The GitHub Actions workflow (`ci.yml`) runs tests, builds a Docker image, and deploys to Heroku on `main` branch pushes.
- Set `HEROKU_API_KEY` in GitHub Secrets for deployment.

## License Information
MIT License

Copyright (c) 2025 Rafael Fuentes

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

---

### Notes on Consolidation
- **Unified Structure**: All sections (overview, installation, usage, API docs, tutorial, contributing, license) are now in one file, maintaining the required `readme_specs` sections and badges.
- **Clarity**: Each section is clearly separated with headers and includes all relevant details from the previous files.
- **Completeness**: The content covers the full scope of the project, including practical examples and deployment instructions, while adhering to the quality standards (e.g., documentation, best practices).

This single `README.md` serves as a comprehensive guide for users, contributors, and evaluators of Rafael Fuentes’ portfolio. Let me know if you’d like further adjustments or additional details!