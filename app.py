from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import mysql.connector
import os
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.getenv("SECRET_KEY", "change_me_in_production")

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ====== ADMIN CREDENTIALS (from environment variables) ======
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "softline_admin")
ADMIN_PASSWORD_HASH = generate_password_hash(os.getenv("ADMIN_PASSWORD", "admin@123"))

# WhatsApp Business Number (from environment variables)
WHATSAPP_BUSINESS_NUMBER = os.getenv("WHATSAPP_BUSINESS_NUMBER", "919409415293")

# ====== DATABASE CONNECTION ======
def get_db_connection():
    """Create and return a MySQL database connection using environment variables"""
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "smaran@1973"),
            database=os.getenv("DB_NAME", "soft_db")
        )
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        raise

# ====== ADMIN LOGIN REQUIRED DECORATOR ======
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("secret_admin_login"))
        return f(*args, **kwargs)
    return decorated_function

# ---------------- BASIC PAGES -----------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()

        # Validation
        if not name or not phone or not message:
            flash("Please fill all fields", "error")
            return redirect(url_for("contact"))

        try:
            db = get_db_connection()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO contacts (name, phone, message) VALUES (%s,%s,%s)",
                (name, phone, message)
            )
            db.commit()
            cursor.close()
            db.close()

            flash("Thank you! We'll get back to you soon.", "success")
            return redirect(url_for("contact"))
        except Exception as e:
            print(f"Contact form error: {str(e)}")
            flash("Error submitting contact form. Please try again.", "error")
            return redirect(url_for("contact"))

    return render_template("contact.html")

# ---------------- PRODUCTS ----------------
@app.route("/products")
def products():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT products.*, categories.name AS category_name
        FROM products
        JOIN categories ON products.category_id = categories.id
    """)
    products = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("shop/products.html", products=products)

# ---------------- SINGLE PRODUCT ----------------
@app.route("/product/<int:product_id>")
def product_detail(product_id):
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()

        cursor.close()
        db.close()

        if not product:
            return render_template("404.html", message="Product not found"), 404

        return render_template("shop/product_detail.html", product=product)
    except Exception as e:
        print(f"Error loading product {product_id}: {str(e)}")
        return render_template("404.html", message="Error loading product"), 500

# ---------------- CART ----------------
@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})

    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart

    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    products = []
    total = 0

    if cart:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        for pid, qty in cart.items():
            cursor.execute("SELECT * FROM products WHERE id = %s", (pid,))
            product = cursor.fetchone()
            if product:
                product["qty"] = qty
                product["subtotal"] = qty * float(product["price"])
                total += product["subtotal"]
                products.append(product)

        cursor.close()
        db.close()

    return render_template("shop/cart.html", products=products, total=total)

@app.route("/remove-from-cart/<int:product_id>")
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)
    session["cart"] = cart
    return redirect(url_for("cart"))

# ====== CHECKOUT ======
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    """
    Checkout flow with order persistence
    - Validates customer info
    - Saves order to database
    - Provides WhatsApp link for admin notification
    """
    cart = session.get("cart", {})
    
    if request.method == "POST":
        # Server-side validation
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()

        # Validate all fields
        if not name:
            return jsonify({"success": False, "message": "Please enter your full name"}), 400
        if not phone:
            return jsonify({"success": False, "message": "Please enter your phone number"}), 400
        if not address:
            return jsonify({"success": False, "message": "Please enter your delivery address"}), 400
        
        # Validate phone format
        if len(phone) != 10 or not phone.isdigit():
            return jsonify({"success": False, "message": "Phone must be 10 digits"}), 400

        # Ensure cart is not empty
        if not cart:
            return jsonify({"success": False, "message": "Your cart is empty"}), 400

        try:
            db = get_db_connection()
            cursor = db.cursor(dictionary=True)

            # Calculate total and collect items
            total = 0
            items = []
            for pid, qty in cart.items():
                cursor.execute("SELECT * FROM products WHERE id=%s", (pid,))
                product = cursor.fetchone()
                if product:
                    price = float(product["price"])
                    subtotal = qty * price
                    total += subtotal
                    items.append({
                        "product_id": product["id"],
                        "product_name": product["name"],
                        "quantity": qty,
                        "price": price,
                        "subtotal": subtotal
                    })

            if not items:
                cursor.close()
                db.close()
                return jsonify({"success": False, "message": "No valid items in cart"}), 400

            # Insert order into database
            cursor.execute(
                "INSERT INTO orders (name, phone, address, total, status, payment_status, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (name, phone, address, total, "pending", "pending", datetime.now())
            )
            order_id = cursor.lastrowid

            # Insert order items
            for item in items:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                    (order_id, item["product_id"], item["quantity"], item["price"])
                )

            db.commit()
            cursor.close()
            db.close()

            # SUCCESS - return order ID for frontend to handle WhatsApp redirect
            return jsonify({
                "success": True,
                "order_id": order_id,
                "total": total,
                "items": items,
                "message": "Order saved successfully! Redirecting to WhatsApp..."
            })

        except Exception as e:
            print(f"Checkout error: {str(e)}")
            return jsonify({"success": False, "message": "Error processing order. Please try again."}), 500

    # GET request: Display checkout page with cart
    if not cart:
        return redirect(url_for("products"))

    products = []
    total = 0
    
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    for pid, qty in cart.items():
        cursor.execute("SELECT * FROM products WHERE id=%s", (pid,))
        product = cursor.fetchone()
        if product:
            product["qty"] = qty
            product["subtotal"] = qty * float(product["price"])
            total += product["subtotal"]
            products.append(product)
    
    cursor.close()
    db.close()

    return render_template("shop/checkout.html", products=products, total=total, whatsapp_number=WHATSAPP_BUSINESS_NUMBER)

# ====== CART CLEAR ======
@app.route("/cart/clear", methods=["POST"])
def clear_cart():
    """Clear session cart after successful order"""
    session.pop("cart", None)
    session.modified = True
    return jsonify({"success": True})

# ====== ORDER SUCCESS PAGE ======
@app.route("/order-success/<int:order_id>")
def order_success(order_id):
    """Display order confirmation page"""
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM orders WHERE id=%s", (order_id,))
        order = cursor.fetchone()
        
        if order:
            # Get order items
            cursor.execute("""
                SELECT oi.*, p.name as product_name, p.image as product_image
                FROM order_items oi
                LEFT JOIN products p ON oi.product_id = p.id
                WHERE oi.order_id=%s
            """, (order_id,))
            order['items'] = cursor.fetchall()
        
        cursor.close()
        db.close()
        
        if not order:
            return "Order not found", 404
        
        return render_template("shop/order_success.html", order=order)
    except Exception as e:
        cursor.close()
        db.close()
        return f"Error retrieving order: {str(e)}", 500

# ====== ADMIN LOGIN ======
@app.route("/softline-control-panel-94xk", methods=["GET", "POST"])
def secret_admin_login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            session["is_admin"] = True
            return redirect(url_for("admin"))
        else:
            return render_template("admin/login.html", error="Invalid credentials")

    return render_template("admin/login.html")

# ====== ADMIN LOGOUT ======
@app.route("/admin/logout")
def admin_logout():
    session.pop("is_admin", None)
    return redirect(url_for("home"))

# ====== ADMIN DASHBOARD ======
@app.route("/admin")
@admin_required
def admin():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # Get all products
    cursor.execute("SELECT * FROM products ORDER BY id DESC")
    products = cursor.fetchall()
    
    # Get order count from orders table (if exists)
    try:
        cursor.execute("SELECT COUNT(*) as count FROM orders")
        order_count = cursor.fetchone()['count'] if cursor.fetchone() else 0
        cursor.execute("SELECT COUNT(*) as count FROM orders")
        order_count = cursor.fetchone()['count'] if cursor.fetchone() else 0
    except:
        order_count = 0
    
    cursor.close()
    db.close()

    return render_template("admin/dashboard.html", products=products, order_count=order_count)

# ====== ADD PRODUCT ======
@app.route("/admin/add-product", methods=["GET", "POST"])
@admin_required
def add_product():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        price = request.form.get("price", "").strip()
        category_id = request.form.get("category_id", "").strip()
        image_file = request.files.get("image")
        
        # Validation
        if not all([name, description, price, category_id]):
            return render_template("admin/add_product.html", error="All fields are required")
        
        try:
            price = float(price)
            category_id = int(category_id)
        except ValueError:
            return render_template("admin/add_product.html", error="Invalid price or category ID")
        
        image_filename = None
        
        # Handle image upload
        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            # Add timestamp to filename to avoid duplicates
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")
            filename = timestamp + filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
            image_filename = filename
        
        db = get_db_connection()
        cursor = db.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO products (name, description, price, category_id, image) VALUES (%s, %s, %s, %s, %s)",
                (name, description, price, category_id, image_filename)
            )
            db.commit()
            cursor.close()
            db.close()
            
            return redirect(url_for("admin"))
        except Exception as e:
            db.rollback()
            cursor.close()
            db.close()
            return render_template("admin/add_product.html", error=f"Error adding product: {str(e)}")
    
    return render_template("admin/add_product.html")

# ====== VIEW ORDERS ======
@app.route("/admin/orders")
@admin_required
def view_orders():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM orders ORDER BY created_at DESC LIMIT 100")
        orders = cursor.fetchall()
        
        # Get order items for each order with product details
        for order in orders:
            cursor.execute("""
                SELECT oi.*, p.name as product_name, p.image as product_image
                FROM order_items oi
                LEFT JOIN products p ON oi.product_id = p.id
                WHERE oi.order_id=%s
            """, (order['id'],))
            order['items'] = cursor.fetchall()
    except Exception as e:
        orders = []
    
    cursor.close()
    db.close()

    return render_template("admin/orders.html", orders=orders)

# ====== ADD MANUAL ORDER ======
@app.route("/admin/add-order", methods=["GET", "POST"])
@admin_required
def add_manual_order():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()
        status = request.form.get("status", "pending").strip()
        
        if not name or not phone or not address:
            return render_template("admin/add_manual_order.html", error="All fields required")
        
        try:
            # Get product IDs and quantities from form
            cursor.execute("SELECT * FROM products ORDER BY name")
            products = cursor.fetchall()
            
            total = 0
            order_items_data = []
            
            for product in products:
                qty_key = f"qty_{product['id']}"
                qty = request.form.get(qty_key, "0").strip()
                if qty and int(qty) > 0:
                    qty = int(qty)
                    price = float(product['price'])
                    subtotal = qty * price
                    total += subtotal
                    order_items_data.append({
                        'product_id': product['id'],
                        'product_name': product['name'],
                        'quantity': qty,
                        'price': price,
                        'subtotal': subtotal
                    })
            
            if not order_items_data:
                return render_template("admin/add_manual_order.html", error="Add at least one product", products=products)
            
            # Insert order
            cursor.execute(
                "INSERT INTO orders (name, phone, address, total, status, created_at) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, phone, address, total, status, datetime.now())
            )
            order_id = cursor.lastrowid
            
            # Insert order items
            for item in order_items_data:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                    (order_id, item['product_id'], item['quantity'], item['price'])
                )
            
            db.commit()
            cursor.close()
            db.close()
            
            return redirect(url_for("view_orders"))
        except Exception as e:
            db.rollback()
            cursor.close()
            db.close()
            return render_template("admin/add_manual_order.html", error=f"Error: {str(e)}")
    
    # GET request - show form
    cursor.execute("SELECT * FROM products ORDER BY name")
    products = cursor.fetchall()
    cursor.close()
    db.close()
    
    return render_template("admin/add_manual_order.html", products=products)

# ====== UPDATE ORDER STATUS & SEND WHATSAPP ======
@app.route("/admin/update-order/<int:order_id>", methods=["POST"])
@admin_required
def update_order_status(order_id):
    new_status = request.form.get("status", "pending").strip()
    
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    try:
        # Get order details
        cursor.execute("SELECT * FROM orders WHERE id=%s", (order_id,))
        order = cursor.fetchone()
        
        if not order:
            cursor.close()
            db.close()
            return redirect(url_for("view_orders"))
        
        # Update order status
        cursor.execute(
            "UPDATE orders SET status=%s WHERE id=%s",
            (new_status, order_id)
        )
        db.commit()
        
        # Generate WhatsApp message based on status
        message = generate_status_message(order, new_status)
        
        # Send WhatsApp message
        whatsapp_message = f"Order%20%23{order_id}%20-%20{message}".replace(" ", "%20")
        whatsapp_link = f"https://wa.me/91{order['phone']}?text={whatsapp_message}"
        
        cursor.close()
        db.close()
        
        # Redirect back with success message and WhatsApp link
        return redirect(url_for("view_orders"))
        
    except Exception as e:
        db.rollback()
        cursor.close()
        db.close()
        return redirect(url_for("view_orders"))

def generate_status_message(order, status):
    """Generate WhatsApp message based on order status"""
    order_id = order['id']
    total = order['total']
    
    messages = {
        'confirmed': f"✅ Your order #{order_id} has been confirmed!%0ATotal: ₹{total:.2f}%0AWe'll ship it soon. Thank you!",
        'shipped': f"📦 Your order #{order_id} has been shipped!%0ATracking info coming soon.%0ATotal: ₹{total:.2f}",
        'delivered': f"🎉 Your order #{order_id} has been delivered!%0ATotal: ₹{total:.2f}%0AThank you for your purchase!"
    }
    
    return messages.get(status, f"Your order #{order_id} status updated to {status}")

# ====== DELETE PRODUCT ======
@app.route("/admin/delete-product/<int:product_id>", methods=["POST"])
@admin_required
def delete_product(product_id):
    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        cursor.close()
        db.close()

    return redirect(url_for("admin"))
# ==================== ERROR HANDLERS ====================
@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    return render_template("404.html", message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    print(f"Internal server error: {error}")
    return render_template("500.html", message="Internal server error"), 500

# ==================== RUN ====================
if __name__ == "__main__":
    app.run(debug=True)
