from typing import Annotated

from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
)
from fastapi.params import Depends

from schemas.movie import SMovie

app = FastAPI(
    title="Movie Catalog",
    description="An application for working with movie catalogs",
)


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


MOVIES = [
    SMovie(
        id=1,
        name="Брат",
        description="История демобилизованного солдата Данилы Багрова, который приезжает в Петербург к брату, но оказывается втянут в криминальный мир города.",
        release_year=1997,
    ),
    SMovie(
        id=2,
        name="Ирония судьбы, или С лёгким паром!",
        description="В новогоднюю ночь москвич Женя Лукашин по ошибке оказывается в Ленинграде, в квартире незнакомой женщины, что становится началом невероятной истории любви.",
        release_year=1975,
    ),
    SMovie(
        id=3,
        name="Сталкер",
        description="Философская притча о трёх людях, отправившихся в загадочную Зону в поисках комнаты, где якобы исполняются желания.",
        release_year=1979,
    ),
    SMovie(
        id=4,
        name="Москва слезам не верит",
        description="История трёх подруг, приехавших покорять Москву в поисках счастья и любви на протяжении двух десятилетий их жизни.",
        release_year=1980,
    ),
    SMovie(
        id=5,
        name="Вий",
        description="Экранизация повести Н.В. Гоголя о студенте-философе, вынужденном провести три ночи у гроба ведьмы в старой церкви.",
        release_year=1967,
    ),
]


@app.get(
    "/movies/",
    response_model=list[SMovie],
)
def get_all_movies():
    return MOVIES


def prefetch_movie_by_id(movie_id: int):
    movie: SMovie | None = next(
        (movie for movie in MOVIES if movie.id == movie_id), None
    )
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie with id {movie_id} not found",
    )


@app.get(
    "/movie/{movie_id}",
    response_model=SMovie,
)
def get_film_by_id(movie: Annotated[SMovie, Depends(prefetch_movie_by_id)]):
    return movie
