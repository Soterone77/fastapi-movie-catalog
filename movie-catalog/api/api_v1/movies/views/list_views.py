from fastapi import (
    APIRouter,
    status,
    BackgroundTasks,
    Depends,
)

from api.api_v1.movies.crud import storage
from api.api_v1.movies.dependencies import (
    save_storage_state,
    user_basic_auth_required_for_unsafe_methods,
)
from schemas.movie import (
    SMovie,
    SMovieCreate,
    SMovieRead,
)

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
    dependencies=[
        Depends(save_storage_state),
        Depends(user_basic_auth_required_for_unsafe_methods),
    ],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Unauthenticated. Only for unsafe methods.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid API Token",
                    }
                }
            },
        }
    },
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
):
    return storage.create(movie_create)
