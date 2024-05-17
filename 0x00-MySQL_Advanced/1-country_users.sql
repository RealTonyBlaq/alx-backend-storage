-- Script creates an SQL table users

CREATE TABLE IF NOT EXISTS userS (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US',
    CONSTRAINT check_country CHECK (country IN ('US', 'CO', 'TN'))
);
