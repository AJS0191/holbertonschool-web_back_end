-- Creates a table named user
CREATE TABLE if NOT EXISTS users (
    id int IS NOT NULL AUTO_INCREMENT,
    email varchar(255) IS NOT NULL,
    name varchar(255)
);
