from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Тестовое задание Antipoff IT'
    database_url: str = 'sqlite+aiosqlite:///./test.db'

    class Config:
        env_file = '.env'


settings = Settings()
