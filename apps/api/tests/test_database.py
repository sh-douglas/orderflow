from app.core.config import Settings


def test_database_url():
    settings = Settings(
        _env_file=None,
        POSTGRES_USER="test",
        POSTGRES_PASSWORD="test123",
        POSTGRES_DB="orderflow_test",
        POSTGRES_HOST="localhost",
        POSTGRES_PORT=5435,
    )

    assert settings.DATABASE_URL == (
        "postgresql+asyncpg://test:test123@localhost:5435/orderflow_test"
    )
