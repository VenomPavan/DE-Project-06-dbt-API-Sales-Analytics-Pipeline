SELECT
    id AS user_id,
    "firstName" AS first_name,
    "lastName" AS last_name,
    age,
    gender,
    email,
    phone,
    username,
    "birthDate" AS birth_date,
    "bloodGroup" AS blood_group,
    height,
    weight,
    "eyeColor" AS eye_color,
    ip,
    "macAddress" AS mac_address,
    university,
    role
FROM {{ source('raw', 'raw_users') }}