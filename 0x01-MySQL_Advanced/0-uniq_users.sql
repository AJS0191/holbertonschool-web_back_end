-- Creates a table named user
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) IS NOT NULL,
    name VARCHAR(255)
);
