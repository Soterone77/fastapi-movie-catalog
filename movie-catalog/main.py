from fastapi import (
    FastAPI,
    Request,
)

from api import router as api_router

app = FastAPI(
    title="Movie Catalog",
    description="An application for working with movie catalogs",
)

app.include_router(api_router)


@app.get("/")
def read_root(
    request: Request,
    name: str = "World",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello {name}!",
        "docs_url": str(docs_url),
    }
