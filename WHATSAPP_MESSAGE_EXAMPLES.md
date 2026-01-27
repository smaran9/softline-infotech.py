# WhatsApp Message Format Examples

## 📋 Standard Order Message

### Example 1: Single Product Order
```
*NEW ORDER - Softline Infotech* 📱
=============================================

*👤 CUSTOMER DETAILS*
Name: Rajesh Kumar
Phone: 9876543210
Address: 42 MG Road, Bangalore 560001

*📦 ORDER ITEMS*
1. E-Commerce Website
   Price: ₹45,000.00
   Qty: 1
   Subtotal: ₹45,000.00

=============================================
*💰 TOTAL AMOUNT: ₹45,000.00*
=============================================

Thank you for ordering! We'll confirm shortly. 🙏
```

### Example 2: Multiple Products
```
*NEW ORDER - Softline Infotech* 📱
=============================================

*👤 CUSTOMER DETAILS*
Name: Priya Sharma
Phone: 9123456789
Address: Sector 5, DLF Cyber City, Gurgaon, Haryana 122001

*📦 ORDER ITEMS*
1. Website Design & Development
   Price: ₹75,000.00
   Qty: 1
   Subtotal: ₹75,000.00

2. Mobile App Development
   Price: ₹1,50,000.00
   Qty: 1
   Subtotal: ₹1,50,000.00

3. SEO Optimization (3 months)
   Price: ₹25,000.00
   Qty: 1
   Subtotal: ₹25,000.00

=============================================
*💰 TOTAL AMOUNT: ₹2,50,000.00*
=============================================

Thank you for ordering! We'll confirm shortly. 🙏
```

### Example 3: Bulk Order
```
*NEW ORDER - Softline Infotech* 📱
=============================================

*👤 CUSTOMER DETAILS*
Name: Amit Patel
Phone: 9987654321
Address: Unit 304, Tech Park, Mumbai 400001

*📦 ORDER ITEMS*
1. Premium Support Package
   Price: ₹5,000.00
   Qty: 5
   Subtotal: ₹25,000.00

2. Training Session
   Price: ₹10,000.00
   Qty: 3
   Subtotal: ₹30,000.00

=============================================
*💰 TOTAL AMOUNT: ₹55,000.00*
=============================================

Thank you for ordering! We'll confirm shortly. 🙏
```

---

## 🎨 Message Formatting Features

### Elements Used:
- **Bold Text**: `*text*` → converts to **text**
- **Emojis**: 📱 🎯 💰 ✅ etc.
- **Line Breaks**: `\n` creates new line
- **Separators**: `=` repeated for visual separation
- **Line Count**: ~15-20 lines for single product, ~30+ for multiple

### Formatting in Code:
```javascript
let message = `*NEW ORDER - Softline Infotech* 📱\n`;
message += `${'='.repeat(45)}\n\n`;  // Creates visual separator
message += `*👤 CUSTOMER DETAILS*\n`;
message += `Name: ${name}\n`;
// ... etc
```

---

## ✨ Optional Customizations

### Version with Business Hours
```
*NEW ORDER - Softline Infotech* 📱
*⏰ Business Hours: 9 AM - 6 PM IST (Monday-Friday)*

=============================================
*👤 CUSTOMER DETAILS*
...
```

### Version with Order ID Reference
```
*NEW ORDER - Softline Infotech* 📱
Order ID: #ORD-20260123-001

=============================================
*👤 CUSTOMER DETAILS*
...
```

### Version with Payment Instructions
```
*NEW ORDER - Softline Infotech* 📱

=============================================
*👤 CUSTOMER DETAILS*
...

*💰 TOTAL AMOUNT: ₹45,000.00*
=============================================

*PAYMENT METHODS:*
💳 Bank Transfer: [Account Details]
🏦 UPI: softline.infotech@upi
📱 Phone Pay / Google Pay: 9876543210

Thank you for ordering! We'll confirm shortly. 🙏
```

### Version with Delivery Timeline
```
*NEW ORDER - Softline Infotech* 📱

=============================================
*👤 CUSTOMER DETAILS*
...

*⏱️ ESTIMATED DELIVERY: 5-7 Business Days*
*💰 TOTAL AMOUNT: ₹45,000.00*
=============================================

Thank you for ordering! We'll confirm shortly. 🙏
```

---

## 🔄 URL Encoding Reference

The JavaScript automatically handles URL encoding. Examples of what gets encoded:

| Character | Encoded |
|-----------|---------|
| Space | %20 |
| * (bold) | %2A |
| # (hash) | %23 |
| & (ampersand) | %26 |
| ₹ (rupee) | %E2%82%B9 |
| Newline | %0A |

### Example Full URL:
```
https://wa.me/919409415293?text=*NEW%20ORDER*%0A%0AName%3A%20John%20Doe%0APhone%3A%209876543210%0A...
```

---

## 📱 Testing Messages

### Test Case 1: Minimal Order
```
Customer: Test User
Phone: 9000000000
Address: Test Address
Product: Basic Package (₹1,000)
Qty: 1
```

### Test Case 2: Corporate Order
```
Customer: Company Name
Phone: 9111111111
Address: Office Address, City, State, ZIP
Products: Multiple (Website, App, Support)
Qty: Various
Total: ₹5,00,000+
```

### Test Case 3: International Customer
```
Customer: John Smith
Phone: +1-2025550123 (converted to WhatsApp format)
Address: New York, USA
Note: Ensure WhatsApp accepts international numbers
```

---

## 🛠️ How to Customize in Code

**File:** `templates/shop/checkout.html`  
**Function:** `generateWhatsAppMessage(name, phone, address, items, total)`

### Add Custom Header:
```javascript
function generateWhatsAppMessage(name, phone, address, items, total) {
    let message = `*SOFTLINE INFOTECH - ORDER PLACED* 🎉\n`;
    message += `Thank you for choosing us!\n\n`;
    // ... rest of message
}
```

### Add Custom Footer:
```javascript
    message += `${'='.repeat(45)}\n`;
    message += `*💰 TOTAL AMOUNT: ${total}*\n`;
    message += `${'='.repeat(45)}\n\n`;
    message += `*NEXT STEPS:*\n`;
    message += `1️⃣ We'll review your order\n`;
    message += `2️⃣ Send you payment details\n`;
    message += `3️⃣ Confirm delivery timeline\n\n`;
    message += `Thank you for ordering! 🙏`;
    
    return message;
```

### Add Product Image Links:
```javascript
items.forEach((item, index) => {
    message += `${index + 1}. ${item.name}\n`;
    if (item.image) {
        message += `   Image: /static/uploads/${item.image}\n`;
    }
    message += `   Price: ₹${item.price.toFixed(2)}\n`;
    // ...
});
```

---

## 📊 Message Statistics

**Standard Single Product Message:**
- Lines: ~15
- Characters: ~350-400
- Delivery Time: Instant
- File Size: < 1 KB

**Multiple Products (3 items):**
- Lines: ~30
- Characters: ~800-1000
- Delivery Time: Instant
- File Size: < 2 KB

---

## ✅ Message Validation Checklist

Before sending order to WhatsApp, verify:
- ✅ Customer name is not empty
- ✅ Phone number is 10 digits
- ✅ Address is complete
- ✅ All product names are correct
- ✅ Prices match product database
- ✅ Quantities are positive integers
- ✅ Total = sum of all subtotals
- ✅ Message length < 4096 characters (WhatsApp limit)
- ✅ No SQL injection attempts in name/address
- ✅ Special characters properly URL-encoded

---

## 🚀 Live Testing

### Step 1: Go to Checkout
```
http://localhost:5000/checkout
```

### Step 2: Add Test Data
```
Name: Softline Test
Phone: 9409415293
Address: 123 Test Street, Test City, Test State 100001
```

### Step 3: Click Button
- Button opens WhatsApp Web or App
- Message appears pre-filled
- Review message content
- Send to verify

### Step 4: Verify in Business Account
- Message received with all order details
- All formatting preserved
- Images/URLs properly linked
- Ready to confirm and process

---

**Version:** 1.0  
**Last Updated:** January 2026  
**Message Format:** UTF-8 Encoded  
**Character Limit:** 4096 chars (safe)
