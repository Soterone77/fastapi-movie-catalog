import random
from typing import Annotated

from fastapi import Depends
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


class SMovieCreate(BaseModel):
    """
    Модель для создания фильма
    """

    name: str
    description: str
    release_year: int
