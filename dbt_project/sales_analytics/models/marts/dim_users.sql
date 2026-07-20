SELECT DISTINCT

    user_id,
    first_name,
    last_name,
    email,
    gender

FROM {{ ref('int_sales') }}