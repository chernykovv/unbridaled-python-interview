from typing import Generic, TypeVar

from sqlalchemy.orm import Session

CreateModel = TypeVar("CreateModel")
UpdateModel = TypeVar("UpdateModel")
ReadModel = TypeVar("ReadModel")
Model = TypeVar("Model")


class BaseCRUD(Generic[ReadModel, CreateModel, UpdateModel]):
    model: Model

    def create(self, db: Session, **kwargs) -> ReadModel:
        new_object = self.model(**kwargs)
        db.add(new_object)
        db.commit()
        return new_object
