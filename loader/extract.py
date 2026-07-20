import requests
import pandas as pd


BASE_URL = "https://dummyjson.com"


def extract_users():
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()

    df = pd.DataFrame(response.json()["users"])

    df = df[
        [
            "id",
            "firstName",
            "lastName",
            "age",
            "gender",
            "email",
            "phone",
            "username",
            "birthDate",
            "bloodGroup",
            "height",
            "weight",
            "eyeColor",
            "ip",
            "macAddress",
            "university",
            "role",
        ]
    ]

    return df


def extract_products():
    response = requests.get(f"{BASE_URL}/products")
    response.raise_for_status()

    df = pd.DataFrame(response.json()["products"])

    df = df[
        [
            "id",
            "title",
            "description",
            "category",
            "price",
            "discountPercentage",
            "rating",
            "stock",
            "brand",
        ]
    ]

    return df


def extract_orders():
    response = requests.get(f"{BASE_URL}/carts")
    response.raise_for_status()

    carts = response.json()["carts"]

    rows = []

    for cart in carts:
        for product in cart["products"]:
            rows.append({
                "cart_id": cart["id"],
                "user_id": cart["userId"],
                "product_id": product["id"],
                "quantity": product["quantity"],
                "price": product["price"],
                "total": product["total"],
                "discounted_total": product["discountedTotal"]
            })

    return pd.DataFrame(rows)