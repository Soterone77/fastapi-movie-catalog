import logging

from fastapi import (
    HTTPException,
    BackgroundTasks,
    status,
    Request,
)

from api.api_v1.movies.crud import storage
from schemas.movie import SMovie

log = logging.getLogger(__name__)

UNSAFE_METHODS = frozenset(
    {
        "POST",
        "PUT",
        "DELETE",
        "PATCH",
    }
)


def prefetch_movie_by_slug(slug: str):

    movie: SMovie | None = storage.get_by_slug(slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie with slug {slug!r} not found",
    )


def save_storage_state(
    request: Request,
    background_tasks: BackgroundTasks,
):
    # исполнение кода до входа внутрь view функции
    yield
    # исполнение кода после покидания view функции
    if request.method in UNSAFE_METHODS:
        background_tasks.add_task(
            storage.save_state,
        )
        log.info("Add background task to  save storage")
