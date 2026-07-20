SELECT

    cart_id,
    user_id,
    product_id,
    quantity,
    price,
    total,
    discounted_total

FROM {{ ref('int_sales') }}