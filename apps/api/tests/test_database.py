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

    url = settings.DATABASE_URL

    assert url.drivername == "postgresql+asyncpg"
    assert url.username == "test"
    assert url.password == "test123"
    assert url.host == "localhost"
    assert url.port == 5435
    assert url.database == "orderflow_test"


def test_database_url_with_special_password():
    settings = Settings(
        _env_file=None,
        POSTGRES_USER="test",
        POSTGRES_PASSWORD="minha@senha/123",
        POSTGRES_DB="orderflow_test",
        POSTGRES_HOST="localhost",
        POSTGRES_PORT=5435,
    )

    url = settings.DATABASE_URL

    assert url.password == "minha@senha/123"
    assert url.host == "localhost"
    assert url.database == "orderflow_test"
