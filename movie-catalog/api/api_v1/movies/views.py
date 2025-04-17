import random
from typing import Annotated

from fastapi import APIRouter, status
from fastapi.params import Depends

from api.api_v1.movies.crud import MOVIES
from api.api_v1.movies.dependencies import prefetch_movie_by_id
from schemas.movie import SMovie, SMovieCreate

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[SMovie],
)
def get_all_movies():
    return MOVIES


@router.get(
    "/{movie_id}",
    response_model=SMovie,
)
def get_film_by_id(movie: Annotated[SMovie, Depends(prefetch_movie_by_id)]):
    return movie


@router.post(
    "/",
    response_model=SMovie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: SMovieCreate,
):
    return SMovie(
        id=random.randint(10, 20),
        **movie_create.model_dump(),
    )
