import logging

from pydantic import BaseModel, ValidationError

from core.config import MOVIES_STORAGE_FILEPATH
from schemas.movie import (
    SMovie,
    SMovieCreate,
    SMovieUpdate,
    SMoviePartialUpdate,
)

log = logging.getLogger(__name__)


class Storage(BaseModel):
    slug_to_smovies: dict[str, SMovie] = {}

    def save_state(self) -> None:
        MOVIES_STORAGE_FILEPATH.write_text(self.model_dump_json(indent=2))
        log.info("Saved movies to storage file.")

    @classmethod
    def from_state(cls) -> "Storage":
        if not MOVIES_STORAGE_FILEPATH.exists():
            log.warning("Movies storage doesn't exist.")
            return Storage()
        return cls.model_validate_json(MOVIES_STORAGE_FILEPATH.read_text())

    def get(self) -> list[SMovie]:
        return list(self.slug_to_smovies.values())

    def get_by_slug(
        self,
        slug,
    ) -> SMovie | None:
        return self.slug_to_smovies.get(slug)

    def create(
        self,
        smovie_in: SMovieCreate,
    ) -> SMovie:
        smovie = SMovie(**(smovie_in.model_dump()))
        self.slug_to_smovies[smovie_in.slug] = smovie
        self.save_state()
        log.info("Saved new movie with slug - %s.", smovie.slug)
        return smovie

    def delete_by_slug(
        self,
        slug: str,
    ):
        self.slug_to_smovies.pop(
            slug,
            None,
        )
        self.save_state()

    def delete(
        self,
        movie: SMovie,
    ):
        self.delete_by_slug(slug=movie.slug)

    def update(
        self,
        movie: SMovie,
        movie_in: SMovieUpdate,
    ):
        for field_name, value in movie_in:
            setattr(
                movie,
                field_name,
                value,
            )
        self.save_state()
        return movie

    def partial_update(
        self,
        movie: SMovie,
        movie_in: SMoviePartialUpdate,
    ):

        for field_name, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(
                movie,
                field_name,
                value,
            )
        self.save_state()
        return movie


try:
    storage = Storage.from_state()
    log.warning("Recovered data from storage file")

except ValidationError:
    storage = Storage()
    storage.save_state()
    log.warning("Rewritten storage file due to validation error")

# storage.create(
#     SMovieCreate(
#         slug="brat",
#         name="Брат",
#         description="История демобилизованного солдата Данилы Багрова, который приезжает в Петербург к брату, но оказывается втянут в криминальный мир города.",
#         release_year=1997,
#     )
# )
# storage.create(
#     SMovieCreate(
#         slug="irony-of-fate",
#         name="Ирония судьбы, или С лёгким паром!",
#         description="В новогоднюю ночь москвич Женя Лукашин по ошибке оказывается в Ленинграде, в квартире незнакомой женщины, что становится началом невероятной истории любви.",
#         release_year=1975,
#     )
# )
# storage.create(
#     SMovieCreate(
#         slug="stalker",
#         name="Сталкер",
#         description="Философская притча о трёх людях, отправившихся в загадочную Зону в поисках комнаты, где якобы исполняются желания.",
#         release_year=1979,
#     )
# )
# storage.create(
#     SMovieCreate(
#         slug="moscow-doesnt-believe-in-tears",
#         name="Москва слезам не верит",
#         description="История трёх подруг, приехавших покорять Москву в поисках счастья и любви на протяжении двух десятилетий их жизни.",
#         release_year=1980,
#     )
# )
