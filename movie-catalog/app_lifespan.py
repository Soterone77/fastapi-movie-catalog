from fastapi import FastAPI

from api.api_v1.movies.crud import storage


async def lifespan(app: FastAPI):
    # действие до запуска приложения
    storage.init_storage_from_state()
    # ставим эту функцию на паузу на время работы приложения
    yield
    # выполняем завершение работы,
    # закрываем соединения, сохраняем файлы.
