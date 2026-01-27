# Quick Reference Guide - Softline Infotech

## 🚀 Getting Started (30 seconds)

```bash
# 1. Copy environment template
cp .env.example .env

# 2. Edit .env with your database credentials
nano .env

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup database
mysql -u root -p < database_schema.sql

# 5. Run app
python app.py
```

Visit: **http://localhost:5000**

---

## 📍 Key URLs

| Page | URL | Access |
|------|-----|--------|
| Home | `/` | Public |
| Products | `/products` | Public |
| Product Detail | `/product/<id>` | Public |
| Cart | `/cart` | Public |
| Checkout | `/checkout` | Public |
| Order Success | `/order-success/<id>` | Public |
| Admin Login | `/softline-control-panel-94xk` | Public (login required) |
| Admin Dashboard | `/admin` | Admin only |
| View Orders | `/admin/orders` | Admin only |
| Add Product | `/admin/add-product` | Admin only |
| Add Order Manually | `/admin/add-order` | Admin only |
| Admin Logout | `/admin/logout` | Admin |

---

## 👨‍💼 Admin Operations

### Login
1. Go to: `/softline-control-panel-94xk`
2. Enter username & password from `.env`
3. Click "Login"

### View Products
1. Dashboard shows all products in table
2. Click "View Details" to see full product
3. Click "Delete" to remove product

### Add New Product
1. Click "➕ Add Product"
2. Fill product details
3. Upload product image
4. Click "✅ Add Product"

### View Customer Orders
1. Click "📦 View Orders"
2. See all orders with status
3. Click order to expand details
4. See customer info and items

### Update Order Status
1. Go to order
2. Click appropriate button:
   - ✅ Confirm Order (pending → confirmed)
   - 📦 Mark as Shipped (confirmed → shipped)
   - 🎉 Mark as Delivered (shipped → delivered)
3. Optionally send WhatsApp message

### Log WhatsApp Order
1. Click "➕ Log WhatsApp Order"
2. Enter customer details
3. Select products and quantities
4. System calculates total
5. Click "Save Order"

---

## 🛍️ Customer Checkout Flow

1. **Browse Products** → Click on product
2. **Add to Cart** → "Add to Cart" button
3. **View Cart** → Click cart icon
4. **Checkout** → "Proceed to Checkout"
5. **Fill Details** → Name, Phone (10 digits), Address
6. **Confirm** → Click "Confirm & Place Order"
7. **WhatsApp Opens** → With order details
8. **Send Message** → To your WhatsApp number
9. **Success Page** → Shows order confirmation

---

## 🔧 Configuration

### Change Admin Credentials
Edit `.env`:
```
ADMIN_USERNAME=new_username
ADMIN_PASSWORD=new_password
```
Restart app.

### Change WhatsApp Number
Edit `.env`:
```
WHATSAPP_BUSINESS_NUMBER=91XXXXXXXXXX
```

### Change Database
Edit `.env`:
```
DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_db_name
```

### Generate Secure Secret Key
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Copy output to `SECRET_KEY` in `.env`

---

## 📦 Database Tables

### orders
- id (INT, primary key)
- name (VARCHAR)
- phone (VARCHAR)
- address (TEXT)
- total (DECIMAL)
- status (VARCHAR) - pending, confirmed, shipped, delivered
- payment_status (VARCHAR)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

### order_items
- id (INT, primary key)
- order_id (INT, foreign key)
- product_id (INT, foreign key)
- quantity (INT)
- price (DECIMAL)
- subtotal (DECIMAL, calculated)

### products
- id (INT, primary key)
- name (VARCHAR)
- description (TEXT)
- price (DECIMAL)
- category_id (INT)
- image (VARCHAR)
- stock_quantity (INT)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)

### categories
- id (INT, primary key)
- name (VARCHAR)
- description (TEXT)
- created_at (TIMESTAMP)

### contacts
- id (INT, primary key)
- name (VARCHAR)
- phone (VARCHAR)
- email (VARCHAR)
- message (TEXT)
- created_at (TIMESTAMP)

---

## 🐛 Troubleshooting

### Database Connection Failed
```
Error: Can't connect to MySQL server
Solution: 
1. Check MySQL is running
2. Verify DB credentials in .env
3. Ensure database 'soft_db' exists
```

### Admin Login Shows "Invalid Credentials"
```
Solution:
1. Check .env has correct ADMIN_PASSWORD
2. Make sure password doesn't have special chars that need escaping
3. Try clearing browser cookies
```

### Images Not Showing
```
Solution:
1. Check static/uploads/ folder exists
2. Verify image files are in that folder
3. Check file permissions (readable)
4. Check image filename in database
```

### WhatsApp Link Not Working
```
Solution:
1. Verify WHATSAPP_BUSINESS_NUMBER in .env is correct
2. Format must be: 91XXXXXXXXXX (country code + 10 digits)
3. Make sure phone number is not in quotes in .env
```

### 404 or 500 Errors
```
Solution:
1. Check app.py terminal for error messages
2. Verify all routes exist
3. Check templates are in correct folders
4. Verify database is connected
```

---

## 💾 Backup & Maintenance

### Daily
- Check orders dashboard
- Process pending orders
- Monitor admin logs

### Weekly
```bash
# Backup database
mysqldump -u root -p soft_db > backup_$(date +%Y%m%d).sql
```

### Monthly
- Archive old orders
- Clean up product images
- Update inventory
- Review sales

---

## 📞 Support

### Check Logs
```bash
# Terminal shows real-time logs when running with:
python app.py
```

### Common Issues
1. **Forms not submitting** → Check browser console for errors
2. **Images not uploading** → Check file size (max 5MB)
3. **Orders not saving** → Check database connection
4. **WhatsApp not opening** → Check phone number format

---

## 🚀 Deploy to Production

### Prerequisites
- Linux/Windows Server
- Python 3.8+
- MySQL 5.7+
- SSL Certificate (HTTPS)

### Steps
1. Copy files to server
2. Setup `.env` with production values
3. Run database setup
4. Install Gunicorn: `pip install gunicorn`
5. Run: `gunicorn -w 4 -b 0.0.0.0:8000 app:app`
6. Configure reverse proxy (Nginx/Apache)
7. Enable HTTPS/SSL
8. Start MySQL service

---

## 📋 Checklist Before Going Live

- [ ] Database backed up
- [ ] Admin credentials changed
- [ ] SECRET_KEY is secure
- [ ] WhatsApp number configured
- [ ] HTTPS/SSL enabled
- [ ] All features tested
- [ ] Mobile layout verified
- [ ] Backup strategy in place
- [ ] Team trained on admin panel
- [ ] Support plan ready

---

**Version**: 1.0.0  
**Last Updated**: January 24, 2026
