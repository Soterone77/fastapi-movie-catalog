from pydantic import BaseModel

from schemas.movie import SMovie, SMovieCreate


class Storage(BaseModel):
    slug_to_smovies: dict[str, SMovie] = {}

    def get(self) -> list[SMovie]:
        return list(self.slug_to_smovies.values())

    def get_by_slug(self, slug) -> SMovie | None:
        return self.slug_to_smovies.get(slug)

    def create(self, smovie_in: SMovieCreate) -> SMovie:
        smovie = SMovie(**(smovie_in.model_dump()))
        self.slug_to_smovies[smovie_in.slug] = smovie
        return smovie

    def delete_by_slug(self, slug: str):
        self.slug_to_smovies.pop(slug, None)

    def delete(self, movie: SMovie):
        self.delete_by_slug(slug=movie.slug)


storage = Storage()

storage.create(
    SMovieCreate(
        slug="brat",
        name="Брат",
        description="История демобилизованного солдата Данилы Багрова, который приезжает в Петербург к брату, но оказывается втянут в криминальный мир города.",
        release_year=1997,
    )
)
storage.create(
    SMovieCreate(
        slug="irony-of-fate",
        name="Ирония судьбы, или С лёгким паром!",
        description="В новогоднюю ночь москвич Женя Лукашин по ошибке оказывается в Ленинграде, в квартире незнакомой женщины, что становится началом невероятной истории любви.",
        release_year=1975,
    )
)
storage.create(
    SMovieCreate(
        slug="stalker",
        name="Сталкер",
        description="Философская притча о трёх людях, отправившихся в загадочную Зону в поисках комнаты, где якобы исполняются желания.",
        release_year=1979,
    )
)
storage.create(
    SMovieCreate(
        slug="moscow-doesnt-believe-in-tears",
        name="Москва слезам не верит",
        description="История трёх подруг, приехавших покорять Москву в поисках счастья и любви на протяжении двух десятилетий их жизни.",
        release_year=1980,
    )
)
