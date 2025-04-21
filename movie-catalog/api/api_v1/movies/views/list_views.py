from fastapi import (
    APIRouter,
    status,
    BackgroundTasks,
)

from api.api_v1.movies.crud import storage
from schemas.movie import (
    SMovie,
    SMovieCreate,
    SMovieRead,
)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[SMovieRead],
)
def get_all_movies():
    return storage.get()


@router.post(
    "/",
    response_model=SMovieRead,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    movie_create: SMovieCreate,
    background_task: BackgroundTasks,
):
    background_task.add_task(storage.save_state)
    return storage.create(movie_create)
