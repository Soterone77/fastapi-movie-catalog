from pydantic import BaseModel


class SMovieBase(BaseModel):
    id: int
    name: str
    description: str
    release_year: int


class SMovie(SMovieBase):
    """
    Модель фильма
    """
