from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status
from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import prefetch_movie_by_slug
from schemas.movie import SMovie, SMovieUpdate

router = APIRouter(
    prefix="/{slug}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Movie with slug 'slug' not found",
                    }
                }
            },
        },
    },
)

MovieBySlug = Annotated[
    SMovie,
    Depends(prefetch_movie_by_slug),
]


@router.get(
    "/",
    response_model=SMovie,
)
def get_film_by_slug(
    movie: MovieBySlug,
) -> SMovie:
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: MovieBySlug,
) -> None:
    storage.delete(movie=movie)


@router.put(
    "/",
    status_code=status.HTTP_200_OK,
)
def delete_movie(
    movie: MovieBySlug,
    movie_in: SMovieUpdate,
) -> SMovie:
    return storage.update(
        movie=movie,
        movie_in=movie_in,
    )
