# Softline Infotech - Production-Ready E-Commerce Platform

## 📋 Project Overview

This is a professional Flask-based e-commerce platform for Softline Infotech, a CCTV installation and laptop repair service provider. The platform has been upgraded to production quality with modern UI/UX, complete checkout flow, secure admin panel, and robust database integration.

---

## ✨ Key Features Implemented

### 1. **Modern UI/UX Design**
- Professional, clean design with consistent branding
- Responsive layout that works on desktop, tablet, and mobile
- Modern color scheme with primary (#0a2540), secondary (#1d4ed8), success (#059669) colors
- Smooth animations and transitions
- Professional typography and spacing
- CSS custom properties for maintainability

### 2. **Product Management**
- ✅ Product listing page with grid layout and professional cards
- ✅ Individual product detail pages with large images
- ✅ Product cards showing: image, name, description, price, and action buttons
- ✅ Category support through category_id
- ✅ Image upload and storage in `static/uploads/`

### 3. **Shopping Cart**
- ✅ Session-based cart (persists during user session)
- ✅ Add/Remove items functionality
- ✅ Cart count badge in navbar
- ✅ Cart page with product images, prices, quantities, subtotals
- ✅ Order summary with total calculation
- ✅ Empty cart state with helpful messaging

### 4. **Complete Checkout System**
- ✅ Professional checkout form with validation
- ✅ Customer information collection: name, phone, address
- ✅ Form validation (required fields, phone number format)
- ✅ Order summary preview before placement
- ✅ Order placement with database transaction
- ✅ Clear cart after successful order
- ✅ Order confirmation/success page with order details
- ✅ Order ID and timestamp tracking

### 5. **Admin Panel**
- ✅ **Secure Login**: Session-based authentication
- ✅ **Admin Dashboard**: View all products with image thumbnails
- ✅ **Add Product**: Form with image upload, drag-and-drop support
- ✅ **Delete Product**: Remove products from inventory
- ✅ **View Orders**: See all customer orders with items and details
- ✅ **Admin Protection**: Non-admin users cannot access admin pages
- ✅ **Logout**: Secure session cleanup

### 6. **Database Improvements**
- ✅ Parameterized queries (SQL injection protection)
- ✅ Proper table structure with foreign keys
- ✅ Order management tables (`orders`, `order_items`)
- ✅ Timestamp tracking for orders (`created_at`)
- ✅ Status field for order tracking

### 7. **Code Quality**
- ✅ Clean Flask routing with separation of concerns
- ✅ Reusable Jinja2 templates with `base.html`
- ✅ Professional CSS organization with variables and reusable classes
- ✅ Comments and documentation
- ✅ No duplicate code, DRY principles applied
- ✅ Decorator pattern for admin protection
- ✅ Error handling and validation

---

## 🗂️ Project Structure

```
softline infotech.py/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── templates/
│   ├── base.html                   # Base template (header, footer, navigation)
│   ├── index.html                  # Homepage with hero section
│   ├── about.html                  # About page
│   ├── services.html               # Services page
│   ├── contact.html                # Contact form
│   │
│   ├── shop/
│   │   ├── products.html           # Product listing page
│   │   ├── product_detail.html     # Single product detail page
│   │   ├── cart.html               # Shopping cart page
│   │   ├── checkout.html           # Checkout form
│   │   └── order_success.html      # Order confirmation page
│   │
│   └── admin/
│       ├── login.html              # Admin login
│       ├── dashboard.html          # Admin product management
│       ├── add_product.html        # Add product form
│       └── orders.html             # View customer orders
│
├── static/
│   ├── style.css                   # Professional CSS styling
│   ├── images/                     # Brand logo and assets
│   ├── js/
│   │   └── main.js                 # Client-side JavaScript
│   └── uploads/                    # Product images (auto-created)
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL database server
- pip package manager

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Create MySQL Database
```sql
CREATE DATABASE soft_db;
USE soft_db;

-- Products table
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    image VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Categories table
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

-- Orders table
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    total DECIMAL(12, 2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Order items table
CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Contacts table
CREATE TABLE contacts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Step 3: Update Database Credentials
Edit `app.py` and update the database connection credentials:
```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="soft_db"
    )
```

### Step 4: Run the Application
```bash
python app.py
```

Access the application at: `http://localhost:5000`

---

## 🔑 Admin Login Credentials

**Default Credentials:**
- Username: `softline_admin`
- Password: `admin@123`

⚠️ **IMPORTANT**: Change these credentials in production! Use environment variables:

```python
import os
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'softline_admin')
ADMIN_PASSWORD_HASH = os.getenv('ADMIN_PASSWORD_HASH', generate_password_hash('admin@123'))
```

---

## 📱 Routes Reference

### Public Routes
- `/` - Homepage
- `/about` - About page
- `/services` - Services page
- `/contact` - Contact form
- `/products` - Product listing
- `/product/<id>` - Product details
- `/add-to-cart/<id>` - Add item to cart
- `/cart` - View shopping cart
- `/remove-from-cart/<id>` - Remove item from cart
- `/checkout` - Checkout page
- `/order-success/<id>` - Order confirmation

### Admin Routes
- `/softline-control-panel-94xy` - Admin login
- `/admin` - Admin dashboard (protected)
- `/admin/add-product` - Add product form (protected)
- `/admin/delete-product/<id>` - Delete product (protected)
- `/admin/orders` - View orders (protected)
- `/admin/logout` - Logout

---

## 🎨 Design System

### Color Palette
- **Primary**: `#0a2540` (Dark Blue)
- **Secondary**: `#1d4ed8` (Bright Blue)
- **Success**: `#059669` (Green)
- **Danger**: `#dc2626` (Red)
- **Warning**: `#f59e0b` (Amber)
- **Background**: `#f8fafc` (Light Gray)
- **Border**: `#e5e7eb` (Medium Gray)
- **Text**: `#1f2937` (Dark Gray)

### Typography
- Font Family: System fonts (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto)
- Sizes: 11px - 48px
- Weights: 400, 500, 600, 700

### Components
- Cards with hover effects
- Buttons with smooth transitions
- Forms with focus states
- Responsive grids
- Professional tables
- Responsive navigation

---

## 🔒 Security Features

1. **Admin Protection Decorator**
   - Routes decorated with `@admin_required` are protected
   - Unauthorized access redirects to login

2. **Parameterized Queries**
   - All database queries use `%s` placeholders
   - Prevents SQL injection attacks

3. **Password Hashing**
   - Uses Werkzeug's `generate_password_hash` and `check_password_hash`
   - Never stores plain-text passwords

4. **Session Management**
   - Secure session key (`secret_key`)
   - Session-based cart (client-side session storage)
   - Proper session cleanup on logout

5. **File Upload Security**
   - `secure_filename()` for uploaded files
   - File extension validation
   - Stored outside web root (in `/uploads`)

---

## 📊 Database Schema

### Products Table
```
id (INT, PK)
name (VARCHAR)
description (TEXT)
price (DECIMAL)
category_id (INT, FK)
image (VARCHAR)
created_at (TIMESTAMP)
```

### Orders Table
```
id (INT, PK)
name (VARCHAR)
phone (VARCHAR)
address (TEXT)
total (DECIMAL)
status (VARCHAR)
created_at (TIMESTAMP)
```

### Order Items Table
```
id (INT, PK)
order_id (INT, FK)
product_id (INT, FK)
quantity (INT)
price (DECIMAL)
```

---

## 🎯 Production Deployment Checklist

- [ ] Change admin credentials and use environment variables
- [ ] Update MySQL password in environment variables
- [ ] Set `debug=False` in production
- [ ] Use strong `secret_key` (generate with `os.urandom(24)`)
- [ ] Enable HTTPS/SSL certificate
- [ ] Set up database backups
- [ ] Configure proper logging
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Add rate limiting for forms
- [ ] Implement email notifications for orders
- [ ] Set up monitoring and alerts
- [ ] Implement CDN for static files
- [ ] Add Google Analytics/tracking

---

## 🛠️ Maintenance

### Regular Tasks
- Monitor database for unused data
- Clean up old sessions
- Review and delete old orders after archival
- Update dependencies periodically
- Check server logs for errors

### Backup Strategy
- Daily database backups
- Store uploads separately
- Test restore procedures monthly

---

## 📝 Notes

### For Future Enhancements
1. **Payment Gateway**: Integrate Razorpay, PayPal, or Stripe
2. **Email Notifications**: Send order confirmations and updates
3. **User Accounts**: Allow customers to create profiles and view order history
4. **Product Reviews**: Add rating and review system
5. **Search & Filters**: Advanced product search and filtering
6. **Analytics**: Dashboard with sales metrics
7. **Inventory Management**: Stock tracking
8. **Multi-language Support**: Support for multiple languages

### Known Limitations
1. Cart is session-based (lost on browser close - use database for persistence)
2. No payment processing (manual orders only)
3. Single admin user (add multi-admin support for future)
4. No email notifications (add email service)
5. No SSL/TLS by default (add for production)

---

## 📞 Support & Documentation

- **Created**: January 2026
- **Version**: 1.0 (Production Ready)
- **Maintained by**: Development Team

For issues or questions, contact: bhattsmaran99@gmail.com

---

## 📄 License

This project is proprietary to Softline Infotech. All rights reserved.

---

**Last Updated**: January 31, 2026
