from fastapi import HTTPException
from starlette import status

from api.api_v1.movies.crud import MOVIES
from schemas.movie import SMovie


def prefetch_movie_by_slug(slug: str):

    movie: SMovie | None = next((movie for movie in MOVIES if movie.slug == slug), None)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie with slug {slug!r} not found",
    )
