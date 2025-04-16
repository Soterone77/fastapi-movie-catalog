from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from api.api_v1.movies.crud import MOVIES
from api.api_v1.movies.dependencies import prefetch_movie_by_id
from schemas.movie import SMovie


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
