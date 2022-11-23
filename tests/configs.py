from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.app import app
from core.configs import configs
from db.connection import get_db
from models.base import BaseModel

TEST_DATABASE_URL = f"postgresql://{configs.DB_USER}:{configs.DB_PASSWORD}@{configs.DB_HOST}/{configs.TEST_DB_NAME}"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

BaseModel.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
