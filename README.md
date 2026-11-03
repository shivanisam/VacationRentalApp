# Vacation Rental App

An application for customers to discover and book vacation rentals, hosts to
manage listings, and admins to review listings and view activity.

## Project status

The initial backend slice provides a health check and searchable mock rental
listings. It validates guest counts and requested stay dates, including the
14-night maximum. Listings and availability are in-memory demo data; bookings,
accounts, role-based access, persistence, the UI, and cloud deployment are not
implemented yet.

## Run the API

Requires Python 3.11 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
uvicorn app.main:app --app-dir backend --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive API
documentation is at `http://127.0.0.1:8000/docs`.

### Endpoints

- `GET /health` — service health
- `GET /api/listings` — search mock listings using `city`, `state`, `zip_code`,
  and/or `guests`; optionally provide both `check_in` and `check_out` as
  `YYYY-MM-DD` dates (stays may be at most 14 nights)

Invalid search input returns a JSON error response.

## Run tests

```bash
pytest
```

## Planned project work

- Customer, host, and admin registration, login, and role permissions
- Persistent listings, availability, bookings, cancellations, and reviews
- Host and admin analytics
- Web UI, maps integration, and cloud deployment
- Component/deployment diagrams, sprint artifacts, and project journal

## Team and project links

- Team name: TBD
- Team members and contribution areas: TBD
- Project journal: TBD
- Product/sprint backlog: TBD
