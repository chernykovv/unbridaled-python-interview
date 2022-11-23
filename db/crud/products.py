from sqlalchemy.orm import Session

from db.crud.base import BaseCRUD
from models import Product, ProductVariant
from schemas import (
    CreateProductSchema,
    CreateProductVariantSchema,
    ReadProductSchema,
    ReadProductVariantSchema,
)


class CRUDProductVariants(
    BaseCRUD[
        ReadProductVariantSchema,
        CreateProductVariantSchema,
        CreateProductVariantSchema,
    ]
):
    model = ProductVariant


class CRUDProducts(
    BaseCRUD[ReadProductSchema, CreateProductSchema, CreateProductSchema]
):
    model = Product
    crud_variants = CRUDProductVariants()

    def create(self, db: Session, **kwargs) -> ReadProductSchema:
        product_variants = kwargs.pop("variants", [])
        product = super().create(db, **kwargs)
        db.add(product)
        db.commit()

        for product_variant in product_variants:
            self.link_product_variant(
                db=db, product_id=product.id, product_variant=product_variant
            )

        db.refresh(product)
        return product

    def link_product_variant(
        self, db: Session, product_id: int, product_variant: dict
    ):
        return self.crud_variants.create(
            db, **{"product_id": product_id, **product_variant}
        )
