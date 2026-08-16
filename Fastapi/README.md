# AI-Powered Task Manager API

A production-ready REST API built with **FastAPI** and **PostgreSQL**, featuring JWT authentication, full Task CRUD, and **AI-powered productivity tools** using Groq (LLaMA 3.3).

---

## 🚀 Live Demo

> Run locally or with Docker — see setup instructions below.

---

## ✨ Features

- 🔐 **User Authentication** — Register, login with JWT tokens and bcrypt password hashing
- ✅ **Task Management** — Create, read, update, delete tasks with priority levels and status tracking
- 🤖 **AI Integration** — Smart task prioritization, goal breakdown, and daily planning powered by Groq AI
- 🖥️ **Frontend UI** — Connected HTML/CSS/JS frontend served directly from FastAPI
- 🐳 **Dockerized** — Fully containerized with Docker Compose (app + PostgreSQL)
- 👤 **Per-user isolation** — Every user only sees their own tasks

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI, Python 3.11 |
| Database | PostgreSQL, SQLAlchemy ORM |
| Authentication | JWT (python-jose), bcrypt (passlib) |
| AI | Groq API (LLaMA 3.3 70B) |
| Frontend | HTML5, CSS3, JavaScript |
| DevOps | Docker, Docker Compose |
| Tools | Git, VS Code |

---

## 📁 Project Structure

```
ai-task-manager/
├── main.py           # FastAPI app, all routes
├── model.py          # SQLAlchemy database models
├── schemas.py        # Pydantic request/response schemas
├── database.py       # Database connection and session
├── auth.py           # JWT token creation and verification
├── ai.py             # Groq AI integration (3 functions)
├── frontend.html     # Frontend UI
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker image configuration
├── docker-compose.yml# Multi-container setup
└── .env              # Environment variables (not committed)
```

---

## 🤖 AI Endpoints

### 1. Priority Suggester
Analyzes your task title and description and suggests priority level, estimated time, and reasoning.

```
POST /ai/priority
```
```json
{
  "title": "Fix login bug",
  "description": "Users getting 401 error after latest deployment"
}
```

### 2. Goal Breakdown
Breaks a big goal into small actionable subtasks.

```
POST /ai/breakdown
```
```json
{
  "goal": "Build and deploy a REST API with authentication"
}
```

### 3. Daily Summary
Reads all your real tasks from the database and generates a smart daily plan.

```
GET /ai/summary
```
> No input needed — AI reads your actual tasks and tells you what to focus on first.

---

## ⚡ Quick Start

### Option 1 — Docker (Recommended)

Make sure Docker Desktop is running, then:

```bash
git clone https://github.com/ayush22205/ai-task-manager.git
cd ai-task-manager
```

Create a `.env` file:
```env
DATABASE_URL=postgresql://postgres:yourpassword@db:5432/taskmanager
SECRET_KEY=your_secret_key_here
GROQ_API_KEY=your_groq_api_key_here
```

Run:
```bash
docker compose up --build
```

Open browser: [http://localhost:8000/app](http://localhost:8000/app)

---

### Option 2 — Local Setup

**Prerequisites:** Python 3.11+, PostgreSQL

```bash
git clone https://github.com/ayush22205/ai-task-manager.git
cd ai-task-manager

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file:
```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskmanager
SECRET_KEY=your_secret_key_here
GROQ_API_KEY=your_groq_api_key_here
```

Run:
```bash
uvicorn main:app --reload
```

Open browser: [http://localhost:8000/app](http://localhost:8000/app)

---

## 📖 API Documentation

FastAPI provides interactive API docs automatically:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)


---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | JWT signing secret key |
| `GROQ_API_KEY` | Groq API key (get free at console.groq.com) |

---

## 📬 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register new user |
| POST | `/login` | Login and get JWT token |
| GET | `/me` | Get current user info |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks` | Create a new task |
| GET | `/tasks` | Get all your tasks |
| GET | `/tasks/{id}` | Get task by ID |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

### AI
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/ai/priority` | Get AI priority suggestion |
| POST | `/ai/breakdown` | Break goal into subtasks |
| GET | `/ai/summary` | Get AI daily plan |

---

## 👨‍💻 Author

**Ayush Kumar**
- GitHub: [@ayush22205](https://github.com/ayush22205)
- Email: ayushk20708090@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
