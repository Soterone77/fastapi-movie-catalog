from fastapi import APIRouter, status

from api.api_v1.movies.crud import storage
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
    return storage.get()


@router.post(
    "/",
    response_model=SMovie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: SMovieCreate,
):
    return storage.create(movie_create)
