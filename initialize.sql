-- Lab 04: Working with SQL
-- Case Study 1: Create related users and posts tables.

DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    created_at DATETIME NOT NULL
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(150) NOT NULL,
    body TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, username, email, city, created_at) VALUES
(1, 'alex', 'alex@example.com', 'Charlottesville', '2026-09-01 09:00:00'),
(2, 'maya', 'maya@example.com', 'Charlottesville', '2026-09-02 10:30:00'),
(3, 'liam', 'liam@example.com', 'Richmond', '2026-09-03 11:15:00'),
(4, 'sophia', 'sophia@example.com', 'Virginia Beach', '2026-09-04 12:00:00'),
(5, 'noah', 'noah@example.com', 'Charlottesville', '2026-09-05 13:20:00'),
(6, 'emma', 'emma@example.com', 'Roanoke', '2026-09-06 14:10:00'),
(7, 'oliver', 'oliver@example.com', 'Charlottesville', '2026-09-07 15:00:00'),
(8, 'ava', 'ava@example.com', 'Arlington', '2026-09-08 16:45:00'),
(9, 'ethan', 'ethan@example.com', 'Charlottesville', '2026-09-09 17:30:00'),
(10, 'mia', 'mia@example.com', 'Norfolk', '2026-09-10 18:00:00');

INSERT INTO posts (post_id, user_id, title, body, created_at) VALUES
(1, 1, 'Welcome to the lab', 'Learning SQL and databases.', '2026-09-11 09:00:00'),
(2, 2, 'SQL practice', 'Working on joins and filters.', '2026-09-11 10:00:00'),
(3, 3, 'Database notes', 'Reviewing primary and foreign keys.', '2026-09-12 11:00:00'),
(4, 4, 'Weekend plans', 'Planning a trip to the beach.', '2026-09-12 12:00:00'),
(5, 5, 'Python and SQL', 'Connecting Python to MySQL.', '2026-09-13 13:00:00'),
(6, 6, 'Data cleaning', 'Removing missing values before upload.', '2026-09-13 14:00:00'),
(7, 7, 'Group by practice', 'Counting rows by category.', '2026-09-14 15:00:00'),
(8, 8, 'ETL ideas', 'Thinking about data pipelines.', '2026-09-14 16:00:00'),
(9, 9, 'Query practice', 'Testing parameterized queries.', '2026-09-15 17:00:00'),
(10, 10, 'Final review', 'Reviewing the SQL lab.', '2026-09-15 18:00:00');
