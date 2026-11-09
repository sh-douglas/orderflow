import pytest
from sqlalchemy import text

from app.db.database import AsyncSessionLocal


@pytest.mark.integration
async def test_async_session_executes_query() -> None:
    async with AsyncSessionLocal() as session:
        result = await session.execute(text("SELECT 1"))

        assert result.scalar_one() == 1
