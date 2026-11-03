from fastapi import FastAPI

app = FastAPI(title="Vacation Rental App API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
