from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


def find_env_file():
    diretorio = Path(__file__).resolve().parent
    diretorios = [diretorio, *diretorio.parents]

    for diretorio in diretorios:
        arquivo = diretorio / ".env"
        if arquivo.is_file():
            return arquivo

    return None


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5435
    POSTGRES_HOST: str = "localhost"

    model_config = SettingsConfigDict(
        env_file=find_env_file(),
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            database=self.POSTGRES_DB,
        )


settings = Settings()
