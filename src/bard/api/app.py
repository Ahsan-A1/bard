from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ..storage import store
from .routes import characters, media, state, stories, turns


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    store.load_all()
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="Bard", lifespan=lifespan)
    app.include_router(stories.router)
    app.include_router(turns.router)
    app.include_router(media.router)
    app.include_router(state.router)
    app.include_router(characters.router)
    return app


app = create_app()
