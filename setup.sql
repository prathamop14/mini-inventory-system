DROP DATABASE IF EXISTS inventory_db;
CREATE DATABASE inventory_db;
USE inventory_db;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    quantity INT NOT NULL DEFAULT 0
);

INSERT INTO items (name, price, quantity) VALUES
('Notebook', 25.00, 50),
('Pen', 5.50, 200),
('Water Bottle', 120.00, 30);
