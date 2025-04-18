import random
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel


class SMovieBase(BaseModel):
    name: str
    description: str
    release_year: int


class SMovie(SMovieBase):
    """
    Модель фильма
    """

    notes: str = "pu-pu-pu"
    slug: str


class SMovieRead(SMovieBase):
    """
    Модель фильма для чтения данных
    """

    slug: str


class SMovieCreate(SMovieBase):
    """
    Модель для создания фильма
    """

    slug: str


class SMovieUpdate(SMovieBase):
    """
    Модель для обновления фильма
    """


class SMoviePartialUpdate(SMovieBase):
    """
    Модель для обновления фильма
    """

    name: str | None = None
    description: str | None = None
    release_year: int | None = None
