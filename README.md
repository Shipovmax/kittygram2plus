# Kittygram 2

Django REST Framework API for cats — next learning step after [kittygram_plus](https://github.com/Shipovmax/kittygram_plus). Replaces the custom `Owner` model with Django's built-in `User` and adds read-only user endpoints.

> For the production-ready version see [kittygram_backend](https://github.com/Shipovmax/kittygram_backend).

---

## What's different from kittygram_plus

- **Owner → User** — `Cat.owner` is now a FK to `django.contrib.auth.User` instead of a custom `Owner` model
- **UserViewSet** — read-only (`ReadOnlyModelViewSet`); exposes `/users/` with `id`, `username`, `first_name`, `last_name`, and reverse `cats` relation
- **AchievementViewSet** — full CRUD endpoint for achievements at `/achievements/`
- **UserSerializer** — `cats` as `StringRelatedField(many=True, read_only=True)`
- **JWT via simplejwt** — `djangorestframework-simplejwt 4.8` instead of webcolors; `/auth/jwt/create/`, `/auth/jwt/refresh/`

---

## Tech Stack

| | |
|---|---|
| Framework | Django 3.2, DRF 3.12 |
| Auth | Djoser 2.1 + SimpleJWT 4.8 |
| Database | SQLite3 |

---

## Quick Start

```bash
git clone https://github.com/Shipovmax/kittygram2
cd kittygram2

python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

API at `http://127.0.0.1:8000/`

---

## Endpoints

| Endpoint | ViewSet | Actions |
|----------|---------|---------|
| `/cats/` | `CatViewSet` | Full CRUD |
| `/users/` | `UserViewSet` | Read-only |
| `/achievements/` | `AchievementViewSet` | Full CRUD |
| `/auth/jwt/create/` | — | Obtain JWT pair |
| `/auth/jwt/refresh/` | — | Refresh token |

---

## Author

- GitHub: [Shipovmax](https://github.com/Shipovmax)
- Email: shipov.max@icloud.com
