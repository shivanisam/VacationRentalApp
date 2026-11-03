from datetime import date
from typing import Annotated

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(title="Vacation Rental App API", version="0.1.0")


class Listing(BaseModel):
    id: str
    name: str
    city: str
    state: str
    zip_code: str
    max_guests: int
    nightly_rate: float
    amenities: list[str]
    rating: float


LISTINGS = [
    Listing(
        id="rental-001",
        name="Sunny Mission Bungalow",
        city="San Diego",
        state="CA",
        zip_code="92109",
        max_guests=4,
        nightly_rate=185.00,
        amenities=["wifi", "kitchen", "parking"],
        rating=4.8,
    ),
    Listing(
        id="rental-002",
        name="Downtown San Jose Loft",
        city="San Jose",
        state="CA",
        zip_code="95112",
        max_guests=2,
        nightly_rate=140.00,
        amenities=["wifi", "workspace"],
        rating=4.6,
    ),
    Listing(
        id="rental-003",
        name="Lake Tahoe Family Cabin",
        city="South Lake Tahoe",
        state="CA",
        zip_code="96150",
        max_guests=6,
        nightly_rate=260.00,
        amenities=["wifi", "kitchen", "fireplace", "parking"],
        rating=4.9,
    ),
]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/listings", response_model=list[Listing])
def search_listings(
    city: str | None = None,
    state: str | None = None,
    zip_code: str | None = None,
    guests: Annotated[int | None, Query(ge=1)] = None,
    check_in: date | None = None,
    check_out: date | None = None,
) -> list[Listing]:
    if (check_in is None) != (check_out is None):
        raise HTTPException(
            status_code=422,
            detail="check_in and check_out must be provided together",
        )
    if check_in is not None and check_out is not None:
        nights = (check_out - check_in).days
        if nights < 1:
            raise HTTPException(
                status_code=422,
                detail="check_out must be after check_in",
            )
        if nights > 14:
            raise HTTPException(
                status_code=422,
                detail="A stay cannot exceed 14 nights",
            )

    return [
        listing
        for listing in LISTINGS
        if (city is None or city.casefold() in listing.city.casefold())
        and (state is None or state.casefold() == listing.state.casefold())
        and (zip_code is None or zip_code == listing.zip_code)
        and (guests is None or listing.max_guests >= guests)
    ]
