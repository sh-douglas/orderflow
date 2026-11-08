import os

import pytest
from httpx import ASGITransport, AsyncClient

os.environ.setdefault("POSTGRES_USER", "test")
os.environ.setdefault("POSTGRES_PASSWORD", "test123")
os.environ.setdefault("POSTGRES_DB", "orderflow_test")
os.environ.setdefault("POSTGRES_HOST", "localhost")
os.environ.setdefault("POSTGRES_PORT", "5435")


from app.db.database import engine
from app.main import app


@pytest.fixture(autouse=True)
async def dispose_engine_after_test():
    yield
    await engine.dispose()


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as client:
        yield client
