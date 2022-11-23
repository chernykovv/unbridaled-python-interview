from datetime import datetime
from typing import List, Optional

from fastapi import HTTPException
from pydantic import BaseModel, root_validator


class BaseProductVariantSchema(BaseModel):
    sku: str
    sales_price: float
    purchase_price: float
    config_attributes: List[dict]

    class Config:
        orm_mode = True


class ReadProductVariantSchema(BaseProductVariantSchema):
    id: int


class CreateProductVariantSchema(BaseProductVariantSchema):
    pass


class BaseProductSchema(BaseModel):
    name: str
    uom: str
    category_name: str
    is_producible: bool
    is_purchasable: bool
    type: str = "product"
    additional_info: Optional[str] = None
    purchase_uom: Optional[str] = None
    purchase_uom_conversion_rate: Optional[str] = None
    batch_tracked: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    variants: Optional[List[CreateProductVariantSchema]] = []

    class Config:
        orm_mode = True


class CreateProductSchema(BaseProductSchema):
    @root_validator
    @classmethod
    def validate_input(cls, values):
        purchase_uom = values.get("purchase_uom")
        uom = values.get("uom")
        purchase_uom_conversion_rate = values.get(
            "purchase_uom_conversion_rate"
        )
        if purchase_uom and not purchase_uom_conversion_rate:
            raise HTTPException(
                status_code=400,
                detail="purchase_uom_conversion_rate must be populated when purchase_uom is populated",
            )
        if purchase_uom_conversion_rate and uom == purchase_uom:
            raise HTTPException(
                status_code=400,
                detail="product must have a purchase_uom that is different from uom",
            )

        return values


class ReadProductSchema(BaseProductSchema):
    id: int
