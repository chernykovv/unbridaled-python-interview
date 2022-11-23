from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr


class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


BaseModel = declarative_base(cls=BaseModel)
