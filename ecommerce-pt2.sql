CREATE DATABASE ecommerce;
USE ecommerce;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    total DECIMAL(10, 2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO users (username, password, email) VALUES 
('johndoe', 'password123', 'johndoe@example.com'),
('janedoe', 'password456', 'janedoe@example.com');

INSERT INTO products (name, description, price, stock) VALUES 
('Laptop', 'Laptop de última geração', 1500.00, 10),
('Smartphone', 'Smartphone com excelente câmera', 800.00, 20),
('Tablet', 'Tablet com alta resolução', 600.00, 15);

INSERT INTO orders (user_id, total) VALUES 
(1, 2300.00),
(2, 800.00);

INSERT INTO order_details (order_id, product_id, quantity, price) VALUES 
(1, 1, 1, 1500.00),  -- Pedido 1: 1 Laptop
(1, 3, 1, 600.00),   -- Pedido 1: 1 Tablet
(2, 2, 1, 800.00);   -- Pedido 2: 1 Smartphone

SELECT * FROM users;                                                                                                                                                                                                                                                                                                                                          
SELECT * FROM products;
SELECT 
    o.order_id,
    o.order_date,
    u.username,
    p.name AS product_name,
    od.quantity,
    od.price
FROM 
    orders o
JOIN 
    users u ON o.user_id = u.user_id
JOIN 
    order_details od ON o.order_id = od.order_id
JOIN 
    products p ON od.product_id = p.product_id;