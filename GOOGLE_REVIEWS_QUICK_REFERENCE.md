# Google Maps Live Reviews - Quick Reference

## ⚡ 5-Minute Setup

### What You Need
1. Google Maps API Key
2. Your Google Business Place ID
3. 2 minutes to update the code

### Where It Goes
**File:** `templates/index.html`  
**Line:** 78 (in the iframe src attribute)

### Current Code
```html
src="https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=place_id:YOUR_PLACE_ID"
```

### What To Replace
- `YOUR_API_KEY` → Your Google Maps API Key
- `YOUR_PLACE_ID` → Your business Place ID

### How It Displays
- **Mobile:** 400px tall map
- **Tablet:** 500px tall map
- **Desktop:** 600px tall map
- **Always:** 100% width, responsive

---

## 🔑 Getting Your Keys

### Google Maps API Key
```
1. Visit: https://console.cloud.google.com/
2. Create new project
3. Enable "Maps Embed API"
4. Go to Credentials
5. Create API Key
6. Copy the key
```

### Your Place ID
```
1. Visit: https://business.google.com
2. Sign in with business account
3. Select your business
4. Settings → Place ID
5. Copy the ID (starts with ChIJ)
```

---

## ✏️ Edit Instructions

### Step 1: Open File
`templates/index.html`

### Step 2: Find Line 78
Search for: `src="https://www.google.com/maps/embed/v1/place?key=`

### Step 3: Replace Both Values
```
Before:
src="https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=place_id:YOUR_PLACE_ID"

After (example):
src="https://www.google.com/maps/embed/v1/place?key=AIzaSyBu-ZI_jkp4YN0b3jmjJ-6Y6EpuFxRJ4DI&q=place_id:ChIJ8fczN8BPvDkRMqGQTfG_48o"
```

### Step 4: Save
File → Save (Ctrl+S)

### Step 5: Deploy
Push to production

### Step 6: Test
Visit website, scroll to reviews section, verify embed displays

---

## 🎯 What You'll See

Live from Google:
- ✓ Your business name
- ✓ Current star rating
- ✓ Real customer reviews
- ✓ Photo gallery
- ✓ Business hours
- ✓ Contact info
- ✓ Directions button

Click map → Opens Google Maps page

---

## 📊 Code Reference

### HTML Location
**File:** `templates/index.html`  
**Lines:** 47-85  
**Section:** Below hero, above services

### CSS Location
**File:** `static/style.css`  
**Lines:** 1868-1941  
**Classes:**
- `.google-reviews-section`
- `.google-reviews-embed-container`
- `.google-reviews-iframe`
- `.reviews-info`

### Responsive Heights
- Mobile: 400px
- Tablet: 500px
- Desktop: 600px

---

## ✅ Verification Checklist

After setup:
- [ ] API Key is valid (no "Invalid API Key" error)
- [ ] Place ID is correct (shows your business name)
- [ ] Map displays with 5 stars
- [ ] Reviews show up
- [ ] Mobile view is 400px tall
- [ ] Desktop view is 600px tall
- [ ] No JavaScript errors in console
- [ ] Clicking map opens Google Maps
- [ ] Photos display correctly
- [ ] Loads within 2 seconds

---

## 🐛 Quick Fixes

### Shows "For development purposes only"
→ Check Maps Embed API is enabled in Cloud Console

### Shows "Invalid API Key"
→ Create new API Key and replace in code

### Shows wrong business name
→ Verify Place ID is correct

### Not loading
→ Clear browser cache (Ctrl+Shift+Delete)
→ Check browser console for errors (F12)

### Showing example place ID
→ Replace YOUR_PLACE_ID with your actual ID

---

## 📍 Placement on Page

```
1. Header
2. Hero Section
3. ✨ GOOGLE REVIEWS (Google Maps Embed) ← HERE
4. Services Section
5. Why Us Section
```

Perfect position: right after hero, highest visibility for trust signals

---

## 🔗 Useful Links

| Resource | URL |
|----------|-----|
| Google Cloud Console | https://console.cloud.google.com/ |
| Google Business | https://business.google.com |
| Maps API Docs | https://developers.google.com/maps/documentation/embed |
| Find Place ID | https://developers.google.com/maps/documentation/places/web-service/place-id |

---

## 💡 Pro Tips

1. **Test First** - Deploy to staging before production
2. **Verify Business Info** - Ensure Google Business Profile is complete
3. **Encourage Reviews** - Ask customers to leave Google reviews
4. **Monitor** - Check analytics for embed engagement
5. **Respond to Reviews** - Reply to all customer reviews

---

## 🚀 That's It!

Two edits, one deploy, live reviews forever.

**Before:** Fake reviews, manual updates, low trust  
**After:** Real reviews, automatic updates, maximum trust

Your website now shows authentic customer feedback! ✨

---

**Time to Deploy:** 5 minutes  
**Result:** Real Google reviews  
**Maintenance:** Zero  
**Benefit:** Maximum credibility  

