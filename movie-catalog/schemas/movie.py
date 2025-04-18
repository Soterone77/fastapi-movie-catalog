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
