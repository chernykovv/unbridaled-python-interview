from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class Product(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    uom = Column(String)
    category_name = Column(String)
    is_producible = Column(Boolean)
    is_purchasable = Column(Boolean)
    type = Column(String, default="product")
    additional_info = Column(String, nullable=True)
    purchase_uom = Column(String, nullable=True)
    purchase_uom_conversion_rate = Column(String, nullable=True)
    batch_tracked = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now(), nullable=True)
    variants = relationship("ProductVariant", back_populates="product")


class ProductVariant(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String)
    sales_price = Column(Float)
    purchase_price = Column(Float)
    config_attributes = Column(JSON)

    product_id = Column(Integer, ForeignKey(Product.id))
    product = relationship(
        "Product",
        foreign_keys="ProductVariant.product_id",
        back_populates="variants",
    )
