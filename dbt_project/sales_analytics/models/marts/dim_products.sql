SELECT DISTINCT

    product_id,
    product_name,
    category,
    brand

FROM {{ ref('int_sales') }}