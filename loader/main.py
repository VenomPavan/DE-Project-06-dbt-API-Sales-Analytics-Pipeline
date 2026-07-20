from extract import (
    extract_users,
    extract_products,
    extract_orders
)

from load import load_to_postgres


print("Extracting Users...")
users = extract_users()

print("Extracting Products...")
products = extract_products()

print("Extracting Orders...")
orders = extract_orders()


print("Loading Users...")
load_to_postgres(users, "raw_users")

print("Loading Products...")
load_to_postgres(products, "raw_products")

print("Loading Orders...")
load_to_postgres(orders, "raw_orders")


print("\nPipeline Completed Successfully!")