-- Creates the table unique_id with id as INT with the default value 1 and must be unique, and name as VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
