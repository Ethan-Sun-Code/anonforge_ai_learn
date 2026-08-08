# Repository Guidelines

## Project Structure & Module Organization

This backend is at an early stage: the repository currently contains `requirements.txt` and a local `.venv/`. Keep application code in `app/`, with the FastAPI entry point at `app/main.py`. Group API routes under `app/api/`, database models and sessions under `app/db/`, request/response schemas under `app/schemas/`, and video-generation logic under `app/services/`. Put automated tests in `tests/`, mirroring the application layout (for example, `tests/api/test_videos.py`). Do not commit `.venv/`, generated videos, caches, credentials, or local database files.

## Build, Test, and Development Commands

Run commands from the repository root on PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

The first three commands create the environment and install FastAPI, SQLModel, PostgreSQL, Pillow, HTTPX, and CrewAI dependencies. The final command starts the development API once `app/main.py` exists. There is no separate build step currently. Record any new runtime dependency in `requirements.txt`.

## Coding Style & Naming Conventions

Use Python 3 conventions: four-space indentation, type hints on public functions, and concise docstrings where behavior is not obvious. Name modules, functions, and variables with `snake_case`; classes and Pydantic/SQLModel models with `PascalCase`; constants with `UPPER_SNAKE_CASE`. Keep route handlers thin and move external API, image, and video work into services. No formatter or linter is configured yet; format consistently with Black-compatible style and keep imports organized.

## Testing Guidelines

No test framework or coverage threshold is configured. New features should introduce `pytest` tests and add the necessary development dependency. Name files `test_*.py` and tests `test_<behavior>`. Run the suite with `python -m pytest`. Mock HTTP, database, CrewAI, and filesystem boundaries; avoid network-dependent tests by default.

## Commit & Pull Request Guidelines

Git history is unavailable in this directory, so no established commit convention can be inferred. Use short, imperative subjects such as `Add video creation endpoint`, keeping each commit focused. Pull requests should explain the change, list verification commands, link relevant issues, and call out schema or configuration changes. Include sample requests/responses for API changes and screenshots only when output is visual.

## Security & Configuration

Load database URLs, API keys, and service credentials from environment variables. Never commit secrets or a populated `.env`; provide sanitized examples in `.env.example` when configuration is introduced. Validate uploaded files, restrict accepted media types and sizes, and use bounded timeouts for external HTTP calls.
