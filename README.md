# Vacation Rental App

A vacation rental application for customers, hosts, and admins.

## Project structure

```text
backend/app/  FastAPI application
tests/        API tests
```

## Getting started

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
uvicorn app.main:app --app-dir backend --reload
```

The API is available at `http://127.0.0.1:8000`; interactive documentation is
at `http://127.0.0.1:8000/docs`.

Run tests with `pytest`.

## Project details

- Team name: TBD
- Team members and contribution areas: TBD
- Project journal: TBD
- Product/sprint backlog: TBD
