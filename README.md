# CodeSage 🔍

### AI-Powered Code Reviewer & Security Assistant

CodeSage is a Python-focused code review and security assistant designed to help developers identify potential code-quality issues and security vulnerabilities through an extensible analysis pipeline.

The project follows a **hybrid LLM approach**: local development with Ollama and a hosted API for deployment. The initial development phase focuses on building a reliable, secure, and testable foundation before adding automated code analysis and AI-powered explanations.

> **Current status:** Week 1 — Foundation  
> **Completed:** Day 1 — Project Setup and Day 2 — Source Validation

---

## 🎯 Project Goals

- Validate submitted Python source files safely.
- Integrate static analysis tools for code quality and security.
- Standardize analysis findings into a consistent data structure.
- Build automated tests for reliable behavior.
- Add AI-powered explanations and code review capabilities in later stages.
- Keep the architecture modular and extensible for future language support.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| Backend API | FastAPI |
| ASGI Server | Uvicorn |
| Testing | Pytest |
| API Testing | FastAPI TestClient |
| HTTP Test Dependency | httpx / httpx2, according to the installed configuration |
| Version Control | Git and GitHub |
| Local LLM — planned | Ollama |
| Static Analysis — planned | Ruff |
| Security Analysis — planned | Bandit |

## 📁 Project Structure

```text
CodeSage/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── validators.py
├── tests/
│   ├── test_api.py
│   └── test_validators.py
├── .gitignore
├── README.md
└── requirements.txt
```

*This represents the current foundation; the structure will expand as new components are implemented.*

## ✅ Completed Features

### Day 1 — Project Foundation

- Set up the Python development environment.
- Created and activated a virtual environment.
- Initialized the Git repository and GitHub project.
- Installed the initial backend dependencies.
- Created the FastAPI application.
- Implemented a health-check endpoint.

### Day 2 — Python Source Validation

Implemented a dedicated source-validation module in `app/validators.py`.

**Validation capabilities:**

- Checks that a filename is provided.
- Enforces a maximum filename length of 255 characters.
- Rejects directory paths and path traversal-style filenames.
- Accepts valid `.py` filenames.
- Enforces a maximum source-file size of 1 MB.
- Requires UTF-8 encoded source content.
- Returns validated source metadata using an immutable `ValidatedSource` dataclass.
- Raises a dedicated `SourceValidationError` for validation failures.

**API endpoints**

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Checks whether the application is running. |
| POST | `/validate-source` | Accepts a Python file and validates its input. |

The upload endpoint returns validation metadata for accepted files and appropriate HTTP error responses for rejected files. Uploaded source is **not executed** during validation.

### Automated Testing

The project includes tests for both the validation module and API endpoints.

- Valid Python file uploads.
- Invalid file extensions.
- Oversized file uploads.
- Health-check endpoint behavior.
- Filename and encoding validation.
- Empty source content and other invalid inputs.

**Latest recorded test result:** 14 tests passed.

The final dependency-update verification is tracked separately from this recorded test result.

## 🚀 Getting Started

### 1. Clone the repository

```powershell
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd CodeSage
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the API server

```powershell
python -m uvicorn app.main:app --reload
```

### 5. Explore the API

Open these URLs in your browser while the server is running:

- **Interactive API documentation:** `http://127.0.0.1:8000/docs`
- **Health check:** `http://127.0.0.1:8000/health`

Use `/docs` to test the source-validation endpoint by uploading a Python file.

### 6. Run the test suite

```powershell
python -m pytest -v
```

Check dependency consistency with:

```powershell
python -m pip check
```

## 🔐 Security Principles

CodeSage is being developed with a security-first approach.

- Uploaded Python source is treated as untrusted input.
- File names, encoding, and file size are validated.
- The validation pipeline does not execute uploaded source code.
- Automated tests cover expected and invalid inputs.
- Static security analysis and additional safeguards will be introduced in subsequent milestones.

**Important:** Input validation is only one layer of security. The current implementation is a development foundation, not a complete production-hardened file-upload service.

## 🗺️ Development Roadmap

| Milestone | Focus | Status |
|---|---|---|
| Day 1 | Project setup and FastAPI foundation | Completed |
| Day 2 | Python source validation and API tests | Completed |
| Day 3 | Ruff integration for code quality | Planned |
| Day 4 | Bandit integration for security analysis | Planned |
| Day 5 | Standardized finding schema | Planned |
| Day 6 | Expanded automated testing | Planned |
| Day 7 | Week 1 review and foundation verification | Planned |
| Future phases | AI explanations, Ollama integration, hosted LLM support | Planned |

## 🤝 Development Approach

CodeSage is being built incrementally, with each milestone verified before moving to the next.

The priorities are correctness, modular design, security, testability, and clear documentation.

## 📜 License

A license has not yet been selected. Add a license before distributing the project publicly under specific reuse terms.
