from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from core.configs import configs
from models.base import BaseModel

engine = create_engine(
    f"postgresql://{configs.DB_USER}:{configs.DB_PASSWORD}@{configs.DB_HOST}/{configs.DB_NAME}",
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseModel.metadata.bind = engine


def get_db():
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError:
        db.rollback()
    finally:
        db.close()
