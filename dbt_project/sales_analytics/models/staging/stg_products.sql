SELECT
    id AS product_id,
    title,
    description,
    category,
    brand,
    price,
    "discountPercentage" AS discount_percentage,
    rating,
    stock
FROM {{ source('raw', 'raw_products') }}