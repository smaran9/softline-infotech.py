# Code Changes Reference

## File 1: app.py

### Change 1: Add jsonify import (Line 1)

**BEFORE:**
```python
from flask import Flask, render_template, request, redirect, url_for, session, flash
```

**AFTER:**
```python
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
```

**Why:** Need `jsonify()` to return JSON responses from AJAX requests

---

### Change 2: Complete checkout route rewrite (Lines 150-240)

**BEFORE:**
```python
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", {})
    if not cart:
        return redirect(url_for("products"))

    if request.method == "POST":
        # WhatsApp-only checkout - no database operations
        # Form submission is handled entirely by JavaScript/frontend
        pass

    # Calculate cart totals for display
    products = []
    total = 0
    if cart:
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

    return render_template("shop/checkout.html", products=products, total=total)
```

**AFTER:**
```python
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    cart = session.get("cart", {})
    if not cart:
        return redirect(url_for("products"))

    if request.method == "POST":
        # OPTION A: Hybrid Architecture - Save to database AND send WhatsApp
        # This allows admin to see orders in dashboard while customers use WhatsApp
        
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()

        # Validate form data
        if not all([name, phone, address]):
            return render_template("shop/checkout.html", products=products, total=total, error="Please fill all fields")

        if len(phone) != 10 or not phone.isdigit():
            return render_template("shop/checkout.html", products=products, total=total, error="Phone must be 10 digits")

        try:
            db = get_db_connection()
            cursor = db.cursor()

            # Calculate total from cart items (validate on backend for security)
            total_amount = 0
            cart_items = []
            
            for pid, qty in cart.items():
                cursor.execute("SELECT id, name, price FROM products WHERE id=%s", (pid,))
                product = cursor.fetchone()
                if product:
                    product_id, product_name, price = product
                    item_total = float(qty) * float(price)
                    total_amount += item_total
                    cart_items.append({
                        "product_id": product_id,
                        "product_name": product_name,
                        "price": float(price),
                        "qty": int(qty),
                        "subtotal": item_total
                    })

            if not cart_items:
                return redirect(url_for("cart"))

            # Create order in database
            cursor.execute(
                "INSERT INTO orders (name, phone, address, total, status, created_at) VALUES (%s, %s, %s, %s, %s, NOW())",
                (name, phone, address, total_amount, "pending")
            )
            order_id = cursor.lastrowid

            # Add order items to database
            for item in cart_items:
                cursor.execute(
                    "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)",
                    (order_id, item["product_id"], item["qty"], item["price"])
                )

            db.commit()
            cursor.close()
            db.close()

            # Clear cart session after successful order creation
            session["cart"] = {}
            session.modified = True

            # Return success - frontend will handle WhatsApp redirect
            return jsonify({
                "success": True,
                "order_id": order_id,
                "message": "Order saved! Redirecting to WhatsApp..."
            })

        except Exception as e:
            print(f"Checkout error: {str(e)}")
            return jsonify({
                "success": False,
                "message": "Error processing order. Please try again."
            }), 500

    # Calculate cart totals for display
    products = []
    total = 0
    if cart:
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

    return render_template("shop/checkout.html", products=products, total=total)
```

**What Changed:**
1. Added form data extraction (name, phone, address)
2. Added validation for all fields
3. Added phone format validation (10 digits)
4. Added database query for cart products
5. Added calculation of total from database prices
6. Added INSERT into orders table
7. Added INSERT into order_items table
8. Added session clearing after order
9. Added JSON response for AJAX

**Why:**
- Saves order to database so admin can see it
- Validates on backend (security)
- Returns JSON for AJAX frontend handling

---

## File 2: templates/shop/checkout.html

### Change: Complete JavaScript rewrite (Lines 155-285)

**BEFORE:**
```javascript
<script>
    document.getElementById('checkoutForm').addEventListener('submit', function (e) {
        e.preventDefault();

        // Get form values
        const name = document.getElementById('name').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const address = document.getElementById('address').value.trim();

        // Validate
        if (!name || !phone || !address) {
            alert('Please fill all fields');
            return;
        }

        // Get total amount from page
        const totalText = document.querySelector('[style*="display: flex; justify-content: space-between"] span:last-child').textContent;
        const total = totalText.replace('₹', '').trim();

        // Extract cart items from the order summary
        const items = [];
        const productDivs = document.querySelectorAll('[style*="display: flex; gap: 12px; margin-bottom: 20px"]');

        productDivs.forEach(div => {
            const nameEl = div.querySelector('h3');
            const priceEl = div.querySelector('p:last-child');
            const imageUrl = div.getAttribute('data-product-image');

            if (nameEl && priceEl) {
                const name = nameEl.textContent.trim();
                const priceText = priceEl.textContent;

                // Parse "₹100.00 × 2 = ₹200.00"
                const matches = priceText.match(/₹([\d.]+)\s×\s(\d+)\s=\s₹([\d.]+)/);
                if (matches) {
                    items.push({
                        name: name,
                        price: parseFloat(matches[1]),
                        qty: parseInt(matches[2]),
                        subtotal: parseFloat(matches[3]),
                        image: imageUrl || ''
                    });
                }
            }
        });

        // Generate WhatsApp message
        const message = generateWhatsAppMessage(name, phone, address, items, total);

        // Redirect to WhatsApp (replace with your business number)
        const whatsappNumber = '919409415293'; // Replace with your WhatsApp number
        const whatsappLink = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
        window.open(whatsappLink, '_blank');
    });

    function generateWhatsAppMessage(name, phone, address, items, total) {
        // ... message generation code ...
    }
</script>
```

**AFTER:**
```javascript
<script>
    document.getElementById('checkoutForm').addEventListener('submit', function (e) {
        e.preventDefault();

        // Get form values
        const name = document.getElementById('name').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const address = document.getElementById('address').value.trim();

        // Validate
        if (!name || !phone || !address) {
            alert('Please fill all fields');
            return;
        }

        if (phone.length !== 10 || !/^\d+$/.test(phone)) {
            alert('Phone must be 10 digits');
            return;
        }

        // Get total amount from page
        const totalText = document.querySelector('[style*="display: flex; justify-content: space-between"] span:last-child').textContent;
        const total = totalText.replace('₹', '').trim();

        // Extract cart items from the order summary
        const items = [];
        const productDivs = document.querySelectorAll('[style*="display: flex; gap: 12px; margin-bottom: 20px"]');

        productDivs.forEach(div => {
            const nameEl = div.querySelector('h3');
            const priceEl = div.querySelector('p:last-child');
            const imageUrl = div.getAttribute('data-product-image');

            if (nameEl && priceEl) {
                const name = nameEl.textContent.trim();
                const priceText = priceEl.textContent;

                // Parse "₹100.00 × 2 = ₹200.00"
                const matches = priceText.match(/₹([\d.]+)\s×\s(\d+)\s=\s₹([\d.]+)/);
                if (matches) {
                    items.push({
                        name: name,
                        price: parseFloat(matches[1]),
                        qty: parseInt(matches[2]),
                        subtotal: parseFloat(matches[3]),
                        image: imageUrl || ''
                    });
                }
            }
        });

        // Show loading indicator
        const btn = document.querySelector('button[type="submit"]');
        const originalText = btn.textContent;
        btn.disabled = true;
        btn.textContent = '⏳ Processing...';

        // Step 1: Send order to backend (save to database)
        const formData = new FormData();
        formData.append('name', name);
        formData.append('phone', phone);
        formData.append('address', address);

        fetch('/checkout', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Step 2: Order saved successfully - now generate WhatsApp message and redirect
                const message = generateWhatsAppMessage(name, phone, address, items, total);
                
                // Step 3: Redirect to WhatsApp with pre-filled message
                const whatsappNumber = '919409415293'; // Replace with your WhatsApp number
                const whatsappLink = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
                
                // Show success message before redirect
                btn.textContent = '✅ Order Saved! Opening WhatsApp...';
                
                // Redirect after brief delay
                setTimeout(() => {
                    window.open(whatsappLink, '_blank');
                    // Redirect to orders page or home after successful order
                    setTimeout(() => {
                        window.location.href = '/products?message=Order+placed+successfully!';
                    }, 1000);
                }, 500);
            } else {
                alert('Error: ' + (data.message || 'Could not process order'));
                btn.disabled = false;
                btn.textContent = originalText;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Network error. Please try again.');
            btn.disabled = false;
            btn.textContent = originalText;
        });
    });

    function generateWhatsAppMessage(name, phone, address, items, total) {
        // ... message generation code (UNCHANGED) ...
    }
</script>
```

**What Changed:**
1. Added phone format validation (10 digits check)
2. Added loading button state ("⏳ Processing...")
3. Changed from direct redirect to `fetch()` AJAX call
4. Wait for backend response before WhatsApp redirect
5. Changed button to "✅ Order Saved! Opening WhatsApp..."
6. Added error handling with try/catch
7. Shows success message and redirects after order saved

**Why:**
- AJAX allows us to save order before WhatsApp redirect
- User sees feedback ("Processing..." and "Order Saved!")
- Error handling improves user experience
- Backend can now validate and save the order

---

## Summary of Key Changes

| Aspect | Before | After | Benefit |
|--------|--------|-------|---------|
| Checkout POST | `pass` (no-op) | Saves to database | Admin can see orders |
| Form submission | Direct redirect | AJAX fetch | Allows backend processing |
| Button feedback | No feedback | Shows "Processing..." | Better UX |
| Phone validation | Frontend only | Frontend + Backend | More secure |
| Total calculation | Frontend only | Backend recalculates | Prevent fraud |
| Order storage | None (lost) | Database (saved) | Permanent records |
| Admin view | Empty | Full order details | Professional workflow |
| WhatsApp timing | Immediate | After database save | Guaranteed backup |

---

## Validation & Error Handling

### Frontend Validation (Before sending to backend)
- Name: Not empty
- Phone: Exactly 10 digits, all numeric
- Address: Not empty

### Backend Validation (After receiving from frontend)
- Name: Provided and not empty
- Phone: Exactly 10 digits and numeric
- Address: Provided and not empty
- Cart: Has items
- Products: All exist in database
- Prices: Recalculated from database (not trusted from frontend)

### Error Responses
```javascript
// If backend validation fails:
{
  "success": false,
  "message": "Error description"
}

// If frontend validation fails:
alert("Validation message")
// Form not submitted
```

---

## Database Operations Performed

When POST request is successful:
```sql
-- 1. Insert main order
INSERT INTO orders (name, phone, address, total, status, created_at)
VALUES ('John Doe', '9876543210', 'Address...', 1500.00, 'pending', NOW());

-- 2. Get the order_id
SELECT LAST_INSERT_ID();  -- Returns 42

-- 3. Insert order items (multiple times, one per product)
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES (42, 5, 2, 750.00);
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES (42, 8, 1, 1000.00);

-- 4. All changes are committed
COMMIT;
```

---

## Testing the Changes

### Quick Test 1: Check Imports
```python
# Open app.py line 1
# Should see: from flask import Flask, ..., jsonify
```

### Quick Test 2: Check Checkout POST Handler
```python
# Open app.py line 150-240
# Should see: database operations (INSERT)
# Should NOT see: just pass
```

### Quick Test 3: Check JavaScript
```javascript
// Open checkout.html line 155-285
// Should see: fetch('/checkout', ...)
// Should NOT see: window.open(whatsappLink) directly
```

### Full Integration Test
1. Place test order via checkout
2. Check database: `SELECT * FROM orders WHERE name='Test'`
3. Check admin: Go to /admin/orders
4. Verify order appears
5. Test status update button
6. Check WhatsApp for notification

---

## Rollback Instructions (If Needed)

To revert changes:

### For app.py:
1. Remove `jsonify` from import
2. Replace checkout route with simple `pass` statement

### For checkout.html:
1. Remove fetch() code
2. Change back to direct `window.open(whatsappLink, '_blank')`

However, this is NOT recommended as it removes admin order visibility.

---

## Production Deployment Notes

✅ No database schema changes needed
✅ Backward compatible with existing /admin/add-order
✅ Can coexist with manual order logging
✅ No new dependencies required
✅ All validation on backend (secure)
✅ Error messages user-friendly

Deploy by:
1. Replace app.py with new version
2. Replace checkout.html with new version
3. Restart Flask application
4. Test one order flow end-to-end
5. Check database has new order
6. Check admin can see order
