-- Lab 04: SQL query using JOIN and WHERE.
-- This selects posts written by users who live in Charlottesville.

SELECT
    u.username,
    u.city,
    p.title,
    p.created_at
FROM users AS u
JOIN posts AS p
    ON u.user_id = p.user_id
WHERE u.city = 'Charlottesville'
ORDER BY p.created_at;
