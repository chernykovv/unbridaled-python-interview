import unittest

from .configs import client


class ProductsTestCase(unittest.TestCase):
    def test_create_product(self):
        data = {
            "name": "string",
            "uom": "us",
            "category_name": "string",
            "is_producible": True,
            "is_purchasable": True,
            "type": "product",
            "additional_info": "string",
            "purchase_uom": "string",
            "purchase_uom_conversion_rate": "string",
            "batch_tracked": True,
            "created_at": "2022-11-23T10:29:19.376Z",
            "updated_at": "2022-11-23T10:29:19.376Z",
            "variants": [
                {
                    "sku": "string",
                    "sales_price": 0,
                    "purchase_price": 0,
                    "config_attributes": [{"Test": "TEST"}],
                },
                {
                    "sku": "sdfdf",
                    "sales_price": 10,
                    "purchase_price": 11,
                    "config_attributes": [{"Test": "TEST"}],
                },
            ],
        }
        response = client.post(
            "/v1/products/create",
            json=data,
        )
        self.assertTrue(response.status_code == 200)
        response_data = response.json()
        self.assertEqual(data["name"], response_data["name"])
        self.assertEqual(len(data["variants"]), len(response_data["variants"]))

    def test_create_product_with_missed_purchase_uom_conversion_rate(self):
        data = {
            "name": "string",
            "uom": "string",
            "category_name": "string",
            "is_producible": True,
            "is_purchasable": True,
            "type": "product",
            "additional_info": "string",
            "purchase_uom": "resr",
            "purchase_uom_conversion_rate": None,
            "batch_tracked": True,
            "created_at": "2022-11-23T10:29:19.376Z",
            "updated_at": "2022-11-23T10:29:19.376Z",
        }

        response = client.post(
            "/v1/products/create",
            json=data,
        )
        self.assertTrue(response.status_code == 400)
        response_data = response.json()
        self.assertEqual(
            response_data["detail"],
            "purchase_uom_conversion_rate must be populated when purchase_uom is populated",
        )

    def test_create_product_with_same_uom_and_purchase_uom(self):
        data = {
            "name": "string",
            "uom": "string",
            "category_name": "string",
            "is_producible": True,
            "is_purchasable": True,
            "type": "product",
            "additional_info": "string",
            "purchase_uom": "string",
            "purchase_uom_conversion_rate": "test",
            "batch_tracked": True,
            "created_at": "2022-11-23T10:29:19.376Z",
            "updated_at": "2022-11-23T10:29:19.376Z",
        }

        response = client.post(
            "/v1/products/create",
            json=data,
        )
        self.assertTrue(response.status_code == 400)
        response_data = response.json()
        self.assertEqual(
            response_data["detail"],
            "product must have a purchase_uom that is different from uom",
        )
