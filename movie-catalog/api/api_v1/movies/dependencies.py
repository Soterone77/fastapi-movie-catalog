import logging

from fastapi import (
    HTTPException,
    BackgroundTasks,
    status,
)

from api.api_v1.movies.crud import storage
from schemas.movie import SMovie

log = logging.getLogger(__name__)


def prefetch_movie_by_slug(slug: str):

    movie: SMovie | None = storage.get_by_slug(slug)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie with slug {slug!r} not found",
    )


def save_storage_state(background_tasks: BackgroundTasks):
    # исполнение кода до входа внутрь view функции
    yield
    # исполнение кода после покидания view функции
    log.info("Add background task to  save storage")
    background_tasks.add_task(storage.save_state)
