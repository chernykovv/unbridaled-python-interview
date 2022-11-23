from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db.connection import get_db
from db.crud import CRUDProducts
from schemas import CreateProductSchema, ReadProductSchema

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post("/create", response_model=ReadProductSchema)
def create_new_product(
    product_data: CreateProductSchema, db: Session = Depends(get_db)
):
    product_data = jsonable_encoder(product_data)
    product = CRUDProducts().create(db=db, **product_data)
    return product
