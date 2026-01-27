# Softline Infotech E-Commerce Setup & Deployment Guide

## Quick Start (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your values:
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_database_password
DB_NAME=soft_db
SECRET_KEY=generate_a_secure_random_key_here
ADMIN_USERNAME=softline_admin
ADMIN_PASSWORD=your_admin_password
WHATSAPP_BUSINESS_NUMBER=919409415293
```

### 3. Setup Database
```bash
mysql -u root -p < database_schema.sql
```

### 4. Run the Application
```bash
python app.py
```

Visit: `http://localhost:5000`

---

## Configuration Details

### Database Setup
1. Install MySQL/MariaDB
2. Create database:
   ```sql
   CREATE DATABASE soft_db;
   ```
3. Import schema:
   ```bash
   mysql -u root -p soft_db < database_schema.sql
   ```

### Admin Panel Access
- URL: `http://localhost:5000/softline-control-panel-94xk`
- Default Username: `softline_admin`
- Default Password: Check your `.env` file

**⚠️ Change these credentials immediately after first login!**

### WhatsApp Integration
- Orders are sent to your WhatsApp Business Number
- Update `WHATSAPP_BUSINESS_NUMBER` in `.env`
- Format: `91XXXXXXXXXX` (country code + 10-digit number)

---

## Features Included

### ✅ Customer Features
- **Mobile-first responsive design** - Works perfectly on all devices
- **Product catalog** with categories
- **Shopping cart** with add/remove functionality
- **Checkout flow** with WhatsApp integration
- **Order confirmation** page with order details
- **Contact form** for inquiries

### ✅ Admin Features
- **Protected admin dashboard** with session-based login
- **Product management** - Add/Edit/Delete products
- **Order management** - View all customer orders
- **Order status tracking** - Pending → Confirmed → Shipped → Delivered
- **WhatsApp notifications** - Send messages to customers
- **Manual order logging** - Log WhatsApp orders manually

### ✅ Security
- **Session-based authentication** for admin panel
- **Password hashing** using Werkzeug
- **Environment variables** for sensitive data
- **SQL injection prevention** using parameterized queries
- **File upload validation** - Secure filename handling
- **CSRF protection** - Session-based tokens

### ✅ Professional UI/UX
- **Modern design** with consistent color scheme
- **Smooth animations** and transitions
- **Clear error messages** with visual feedback
- **Mobile optimization** for tablet and phone
- **Professional typography** and spacing
- **Accessibility** - Semantic HTML, proper labels

---

## File Structure

```
softline infotech.py/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── database_schema.sql             # Database setup script
├── static/
│   ├── style.css                  # Main stylesheet
│   ├── images/                    # Brand images (logo, etc.)
│   ├── js/
│   │   └── main.js               # Frontend JavaScript
│   └── uploads/                  # Product images (auto-created)
└── templates/
    ├── base.html                  # Base template (header, footer)
    ├── index.html                 # Home page
    ├── about.html                 # About page
    ├── services.html              # Services page
    ├── contact.html               # Contact form
    ├── 404.html                   # 404 error page
    ├── 500.html                   # 500 error page
    ├── shop/
    │   ├── products.html          # Product listing
    │   ├── product_detail.html    # Product detail page
    │   ├── cart.html              # Shopping cart
    │   ├── checkout.html          # Checkout form
    │   └── order_success.html     # Order confirmation
    └── admin/
        ├── login.html             # Admin login
        ├── dashboard.html         # Admin dashboard
        ├── orders.html            # Order management
        ├── add_product.html       # Add product form
        └── add_manual_order.html  # Manual order form
```

---

## Checkout Flow

1. **Customer browses products** → Adds items to cart
2. **Proceeds to checkout** → Fills customer details
3. **Form validation** → Name, phone (10 digits), address
4. **Order saved to database** → Order gets unique ID
5. **WhatsApp opens** → Pre-filled message with order details
6. **Customer sends message** → To your WhatsApp business number
7. **Success page** → Shows order confirmation
8. **Admin receives order** → In dashboard and WhatsApp

---

## Admin Order Management

### View Orders
- Go to Admin Dashboard → Click "View Orders"
- See all customer orders with dates, amounts, status
- Click on order to see items and details

### Update Order Status
- **Pending** → New order received
- **Confirmed** → Ready to pack
- **Shipped** → On the way to customer
- **Delivered** → Reached customer

When you update status, you can send WhatsApp message to customer automatically.

### Log WhatsApp Orders
- Go to Admin Dashboard → Click "Log WhatsApp Order"
- Enter customer details
- Select products and quantities
- System saves order and calculates total

---

## Deployment

### For Production (Linux/Apache)

1. **Update `.env` with secure values**
   ```
   SECRET_KEY=generate_random_secure_key
   DEBUG=False
   ```

2. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

4. **Use Apache/Nginx as reverse proxy**
   - Configure SSL/HTTPS
   - Point to Gunicorn on port 8000

### For Windows Production

1. Use **WSGI server** like `waitress`
   ```bash
   pip install waitress
   waitress-serve app:app
   ```

2. Keep MySQL running as Windows service

---

## Troubleshooting

### Database Connection Error
- Check MySQL is running
- Verify credentials in `.env`
- Ensure `soft_db` database exists

### Admin Login Not Working
- Check credentials in `.env`
- Clear browser cookies/session
- Try incognito mode

### WhatsApp Link Not Opening
- Check phone number format (91XXXXXXXXXX)
- Ensure number is added to contacts as "Softline Infotech"
- Verify WHATSAPP_BUSINESS_NUMBER in `.env`

### Images Not Showing
- Check `static/uploads/` folder exists
- Verify image file names and formats
- Check file permissions

---

## Support & Maintenance

### Regular Tasks
- ✅ Monitor database disk space
- ✅ Backup database weekly
- ✅ Check error logs
- ✅ Update product inventory
- ✅ Archive old orders

### Contact for Issues
- Check error logs in terminal
- Review database for data integrity
- Verify all environment variables are set

---

## License & Security Notes

- **Never commit `.env` file** to version control
- **Change admin credentials** immediately after setup
- **Keep Python and dependencies updated**
- **Use HTTPS in production**
- **Regular database backups**
- **Monitor admin access logs**

---

Generated: January 2026
Version: 1.0 - Production Ready
