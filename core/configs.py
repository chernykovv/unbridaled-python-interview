import os
from pathlib import Path

from pydantic import BaseSettings

PROJECT_DIR = Path(Path(__file__).parent).parent


class Configs(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_NAME: str
    TEST_DB_NAME: str

    class Config:
        env_file = os.path.join(PROJECT_DIR, ".env")


configs = Configs()
