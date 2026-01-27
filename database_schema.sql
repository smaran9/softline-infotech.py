-- ============================================================
-- Softline Infotech E-Commerce Database Schema
-- ============================================================
-- Run these SQL commands to set up your database

-- Create Database
CREATE DATABASE IF NOT EXISTS soft_db;
USE soft_db;

-- ============================================================
-- CATEGORIES TABLE
-- ============================================================
CREATE TABLE IF NOT EXISTS categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- PRODUCTS TABLE
-- ============================================================
CREATE TABLE IF NOT EXISTS products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    image VARCHAR(255),
    stock_quantity INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    INDEX idx_category (category_id),
    INDEX idx_price (price)
);

-- ============================================================
-- ORDERS TABLE
-- ============================================================
CREATE TABLE IF NOT EXISTS orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    total DECIMAL(12, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    payment_status VARCHAR(50) DEFAULT 'pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_created (created_at)
);

-- ============================================================
-- ORDER ITEMS TABLE
-- ============================================================
CREATE TABLE IF NOT EXISTS order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2),
    subtotal DECIMAL(12, 2) GENERATED ALWAYS AS (quantity * price) STORED,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id),
    INDEX idx_order (order_id),
    INDEX idx_product (product_id)
);

-- ============================================================
-- CONTACTS TABLE
-- ============================================================
CREATE TABLE IF NOT EXISTS contacts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255),
    message TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_created (created_at)
);

-- ============================================================
-- SAMPLE DATA
-- ============================================================

-- Insert sample categories
INSERT INTO categories (name, description) VALUES
('CCTV Cameras', 'Professional CCTV surveillance cameras'),
('DVR/NVR', 'Digital and Network Video Recorders'),
('Laptop Accessories', 'Genuine laptop parts and accessories'),
('Chargers & Batteries', 'Original laptop chargers and batteries');

-- Insert sample products
INSERT INTO products (name, description, price, category_id, stock_quantity) VALUES
('HD CCTV Camera 2MP', 'Professional 2MP HD security camera with night vision', 2500.00, 1, 15),
('4MP Dome Camera', 'Compact dome CCTV camera, ideal for indoor surveillance', 3500.00, 1, 10),
('DVR 4 Channel', 'Digital Video Recorder for 4 cameras, 1TB storage', 5000.00, 2, 8),
('Laptop Charger Dell', 'Original Dell laptop charger 65W', 1200.00, 3, 20),
('16GB RAM DDR4', 'Samsung 16GB DDR4 RAM memory upgrade', 4500.00, 3, 12);

-- ============================================================
-- USEFUL QUERIES
-- ============================================================

-- View all orders with items
-- SELECT o.id, o.name, o.phone, o.total, COUNT(oi.id) as items_count
-- FROM orders o
-- LEFT JOIN order_items oi ON o.id = oi.order_id
-- GROUP BY o.id
-- ORDER BY o.created_at DESC;

-- View a specific order with details
-- SELECT o.*, p.name as product_name, oi.quantity, oi.price
-- FROM orders o
-- JOIN order_items oi ON o.id = oi.order_id
-- JOIN products p ON oi.product_id = p.id
-- WHERE o.id = 1;

-- Get product inventory status
-- SELECT id, name, price, stock_quantity
-- FROM products
-- ORDER BY stock_quantity ASC;

-- Get sales summary by category
-- SELECT c.name as category, COUNT(oi.id) as items_sold, SUM(oi.subtotal) as total_sales
-- FROM categories c
-- LEFT JOIN products p ON c.id = p.category_id
-- LEFT JOIN order_items oi ON p.id = oi.product_id
-- GROUP BY c.id
-- ORDER BY total_sales DESC;

-- ============================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================
-- Already created above, but here are important ones:
-- - products.category_id (for category filtering)
-- - products.price (for price filtering)
-- - orders.status (for order status filtering)
-- - orders.created_at (for date filtering)
-- - contacts.status (for contact status)

-- ============================================================
-- USER PERMISSIONS (Optional - for multi-user setup)
-- ============================================================
-- CREATE USER 'softline_user'@'localhost' IDENTIFIED BY 'password123';
-- GRANT SELECT, INSERT, UPDATE ON soft_db.* TO 'softline_user'@'localhost';
-- GRANT ALL PRIVILEGES ON soft_db.* TO 'softline_admin'@'localhost' IDENTIFIED BY 'admin_password';

-- ============================================================
-- BACKUP COMMAND
-- ============================================================
-- Backup: mysqldump -u root -p soft_db > soft_db_backup.sql
-- Restore: mysql -u root -p soft_db < soft_db_backup.sql

-- ============================================================
-- END OF SCHEMA
-- ============================================================
