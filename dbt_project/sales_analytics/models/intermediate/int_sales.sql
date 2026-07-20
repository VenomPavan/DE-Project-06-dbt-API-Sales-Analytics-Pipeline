SELECT

    o.cart_id,
    o.user_id,

    u.first_name,
    u.last_name,
    u.email,
    u.gender,

    o.product_id,

    p.product_name,
    p.category,
    p.brand,

    o.quantity,
    o.price,
    o.total,
    o.discounted_total

FROM {{ ref('stg_orders') }} o

LEFT JOIN {{ ref('stg_users') }} u
    ON o.user_id = u.user_id

LEFT JOIN (

    SELECT
        product_id,
        title AS product_name,
        category,
        brand

    FROM {{ ref('stg_products') }}

) p

ON o.product_id = p.product_id