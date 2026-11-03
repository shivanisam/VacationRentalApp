import asyncio

import httpx

from app.main import app


def get(url: str, params: dict[str, str | int] | None = None) -> httpx.Response:
    async def request() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://test",
        ) as client:
            return await client.get(url, params=params)

    return asyncio.run(request())


def test_health_check() -> None:
    response = get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_search_filters_by_city_and_guest_capacity() -> None:
    response = get(
        "/api/listings",
        params={"city": "san", "guests": 3},
    )

    assert response.status_code == 200
    assert [listing["id"] for listing in response.json()] == ["rental-001"]


def test_search_accepts_a_stay_of_fourteen_nights() -> None:
    response = get(
        "/api/listings",
        params={"check_in": "2026-12-01", "check_out": "2026-12-15"},
    )

    assert response.status_code == 200


def test_search_rejects_a_stay_longer_than_fourteen_nights() -> None:
    response = get(
        "/api/listings",
        params={"check_in": "2026-12-01", "check_out": "2026-12-16"},
    )

    assert response.status_code == 422
    assert response.json()["detail"] == "A stay cannot exceed 14 nights"


def test_search_requires_both_stay_dates() -> None:
    response = get(
        "/api/listings",
        params={"check_in": "2026-12-01"},
    )

    assert response.status_code == 422
