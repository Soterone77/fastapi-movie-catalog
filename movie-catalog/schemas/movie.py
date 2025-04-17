import random
from typing import Annotated

from fastapi import Depends
from pydantic import BaseModel


class SMovieBase(BaseModel):
    slug: str
    name: str
    description: str
    release_year: int


class SMovie(SMovieBase):
    """
    Модель фильма
    """


class SMovieCreate(SMovieBase):
    """
    Модель для создания фильма
    """
