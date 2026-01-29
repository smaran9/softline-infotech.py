# Google Reviews Section - Code Reference & Examples

## HTML Structure Overview

### Full Section Markup
```html
<!-- ================= GOOGLE REVIEWS ================= -->
<section class="section google-reviews-section">
    <div class="container">
        <div class="section-header">
            <h2 class="section-title">Trusted by Our Clients</h2>
            <p class="section-subtitle">Real reviews from Google</p>
        </div>

        <!-- Google Reviews Trust Card -->
        <div class="reviews-trust-container">
            <div class="reviews-trust-card">
                <!-- Google Logo & Rating -->
                <div class="reviews-header">
                    <div class="google-logo-section">
                        <!-- SVG Google Logo for authenticity -->
                        <svg class="google-logo" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <text x="2" y="18" font-size="14" font-weight="700" fill="#4285F4">G</text>
                            <text x="7" y="18" font-size="14" font-weight="700" fill="#EA4335">o</text>
                            <text x="12" y="18" font-size="14" font-weight="700" fill="#FBBC04">o</text>
                            <text x="17" y="18" font-size="14" font-weight="700" fill="#4285F4">g</text>
                            <text x="21" y="18" font-size="14" font-weight="700" fill="#34A853">l</text>
                            <text x="23" y="18" font-size="14" font-weight="700" fill="#EA4335">e</text>
                        </svg>
                    </div>
                    <div class="rating-display">
                        <div class="stars">
                            <span class="star-filled">★</span>
                            <span class="star-filled">★</span>
                            <span class="star-filled">★</span>
                            <span class="star-filled">★</span>
                            <span class="star-filled">★</span>
                        </div>
                        <div class="rating-text">4.8 out of 5</div>
                    </div>
                </div>

                <!-- Reviews Count -->
                <div class="reviews-count">
                    <p class="count-text"><strong>120+</strong> reviews on Google</p>
                </div>

                <!-- Call-to-Action Button to Google Reviews -->
                <div class="reviews-cta">
                    <a href="https://www.google.com/search?q=Softline+Infotech+reviews" 
                       target="_blank" rel="noopener noreferrer" class="btn btn-reviews">
                        <span class="btn-icon">📍</span>
                        View All Reviews on Google
                    </a>
                </div>

                <!-- Trust Badges -->
                <div class="trust-badges">
                    <div class="trust-badge">
                        <span class="badge-icon">✓</span>
                        <span class="badge-text">Verified Reviews</span>
                    </div>
                    <div class="trust-badge">
                        <span class="badge-icon">🛡️</span>
                        <span class="badge-text">Authentic Feedback</span>
                    </div>
                    <div class="trust-badge">
                        <span class="badge-icon">⭐</span>
                        <span class="badge-text">Highly Rated</span>
                    </div>
                </div>
            </div>

            <!-- Individual Review Cards -->
            <div class="reviews-showcase">
                <div class="review-card">
                    <div class="review-rating">
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                    </div>
                    <p class="review-text">
                        "Excellent service! They fixed my laptop in just 2 hours. Very professional and trustworthy."
                    </p>
                    <p class="review-author">- Raj P., via Google Reviews</p>
                </div>

                <div class="review-card">
                    <div class="review-rating">
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                    </div>
                    <p class="review-text">
                        "Best CCTV installation service in town. Very knowledgeable team and great after-sales support."
                    </p>
                    <p class="review-author">- Priya M., via Google Reviews</p>
                </div>

                <div class="review-card">
                    <div class="review-rating">
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                        <span class="star-sm">★</span>
                    </div>
                    <p class="review-text">
                        "Highly recommend! Solved my security concerns quickly and professionally. Worth every penny."
                    </p>
                    <p class="review-author">- Vikram S., via Google Reviews</p>
                </div>
            </div>
        </div>
    </div>
</section>
```

---

## CSS Classes Reference

### Main Container
```css
.google-reviews-section {
    background: linear-gradient(135deg, rgba(13, 27, 42, 0.03) 0%, rgba(29, 78, 216, 0.03) 100%);
    padding: 80px 0;
}

@media (min-width: 1024px) {
    .google-reviews-section {
        padding: 100px 0;
    }
}
```

### Trust Card
```css
.reviews-trust-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 48px;
    box-shadow: var(--shadow-md);
    transition: var(--transition);
    text-align: center;
}

.reviews-trust-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(29, 78, 216, 0.15);
    border-color: var(--secondary);
}
```

### Google Logo
```css
.google-logo {
    width: 80px;
    height: 40px;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.08));
}

@media (min-width: 1024px) {
    .google-logo {
        width: 100px;
        height: 50px;
    }
}
```

### Star Rating
```css
.stars {
    display: flex;
    gap: 4px;
    font-size: 24px;
}

.star-filled {
    color: #FFB800;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.rating-text {
    font-size: 16px;
    font-weight: 600;
    color: var(--text);
}

@media (min-width: 1024px) {
    .stars {
        font-size: 28px;
    }
}
```

### Review Count
```css
.reviews-count {
    background: linear-gradient(135deg, rgba(29, 78, 216, 0.08) 0%, rgba(59, 130, 246, 0.08) 100%);
    padding: 20px;
    border-radius: var(--radius-md);
    margin: 24px 0;
}

.count-text {
    font-size: 18px;
    color: var(--text);
    margin: 0;
}

.count-text strong {
    color: var(--secondary);
    font-size: 20px;
}
```

### CTA Button
```css
.btn-reviews {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, var(--secondary) 0%, #1e40af 100%);
    color: white;
    padding: 16px 32px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
    transition: var(--transition);
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(29, 78, 216, 0.3);
}

.btn-reviews:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(29, 78, 216, 0.4);
}

.btn-reviews:active {
    transform: translateY(-1px);
}

@media (max-width: 768px) {
    .btn-reviews {
        width: 100%;
        justify-content: center;
    }
}
```

### Trust Badges
```css
.trust-badges {
    display: flex;
    justify-content: center;
    gap: 24px;
    margin-top: 32px;
    flex-wrap: wrap;
}

.trust-badge {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 16px 20px;
    background: rgba(13, 27, 42, 0.04);
    border-radius: var(--radius-md);
    transition: var(--transition);
}

.trust-badge:hover {
    background: rgba(29, 78, 216, 0.08);
    transform: translateY(-2px);
}

.badge-icon {
    font-size: 24px;
    line-height: 1;
}

.badge-text {
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    text-align: center;
}
```

### Review Cards
```css
.reviews-showcase {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-top: 40px;
}

.review-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 24px;
    transition: var(--transition);
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.review-card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-md);
    border-color: var(--secondary);
}

.review-rating {
    display: flex;
    gap: 3px;
    font-size: 16px;
}

.star-sm {
    color: #FFB800;
}

.review-text {
    font-size: 15px;
    color: var(--text);
    line-height: 1.6;
    margin: 0;
    font-style: italic;
}

.review-author {
    font-size: 13px;
    color: var(--text-light);
    margin: 0;
    font-weight: 500;
}

@media (min-width: 1024px) {
    .reviews-showcase {
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
        margin-top: 60px;
    }
}
```

---

## Customization Code Examples

### Example 1: Change Star Rating
```html
<!-- Change from 5 stars to 4 stars -->
<div class="stars">
    <span class="star-filled">★</span>
    <span class="star-filled">★</span>
    <span class="star-filled">★</span>
    <span class="star-filled">★</span>
    <!-- Remove one star -->
</div>
<div class="rating-text">4.2 out of 5</div>
```

### Example 2: Update Review Count
```html
<!-- Change from 120+ to 250+ -->
<p class="count-text"><strong>250+</strong> reviews on Google</p>
```

### Example 3: Add New Review Card
```html
<!-- Duplicate and modify a review card -->
<div class="review-card">
    <div class="review-rating">
        <span class="star-sm">★</span>
        <span class="star-sm">★</span>
        <span class="star-sm">★</span>
        <span class="star-sm">★</span>
        <span class="star-sm">★</span>
    </div>
    <p class="review-text">
        "Your new review text here"
    </p>
    <p class="review-author">- Your Client Name, via Google Reviews</p>
</div>
```

### Example 4: Update CTA Button Link
```html
<!-- Replace with your Google Business Profile URL -->
<!-- Get URL from: https://business.google.com/u/0/manage/YOUR_BUSINESS_ID -->

<!-- Before -->
<a href="https://www.google.com/search?q=Softline+Infotech+reviews" ...>

<!-- After -->
<a href="https://www.google.com/maps/place/Softline+Infotech+Himmatnagar/@..." ...>
```

### Example 5: Change Colors (CSS)
```css
/* Update in style.css - change secondary color */
:root {
    --primary: #0a2540;
    --secondary: #2563eb; /* Changed from #1d4ed8 */
}
```

### Example 6: Add Google Reviews Widget API
```html
<!-- Add to templates/base.html <head> section -->
<script src="https://www.gstatic.com/business/content/hosting_review_widget.min.js"></script>

<!-- Replace review showcase div with -->
<div class="review-embed" data-profile="YOUR_GOOGLE_PROFILE_ID"></div>
```

### Example 7: Add More Trust Badges
```html
<!-- Add additional badges to trust-badges div -->
<div class="trust-badge">
    <span class="badge-icon">⏱️</span>
    <span class="badge-text">Quick Response</span>
</div>
```

### Example 8: Change Button Text
```html
<!-- Change button text -->
<span class="btn-icon">📍</span>
Your New Button Text Here
```

---

## CSS Variables Available

```css
:root {
    --primary: #0a2540;           /* Dark blue - headings */
    --secondary: #1d4ed8;         /* Bright blue - buttons */
    --success: #059669;
    --danger: #dc2626;
    --warning: #f59e0b;
    --bg: #f8fafc;                /* Light background */
    --bg-light: #f1f5f9;
    --text: #1f2937;              /* Dark gray - main text */
    --text-light: #6b7280;        /* Light gray - secondary */
    --border: #e5e7eb;            /* Borders */
    --white: #ffffff;             /* White */

    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;

    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 12px 24px rgba(0, 0, 0, 0.12);

    --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
```

---

## Breakpoint Media Queries

```css
/* Mobile First Approach */
/* Default styles for mobile */

/* Tablet and up (640px) */
@media (min-width: 640px) {
    /* Tablet optimizations */
}

/* Tablet and up (768px) */
@media (max-width: 768px) {
    /* Specific mobile overrides */
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
    /* Desktop optimizations */
}
```

---

## Flexbox & Grid Layout

### Trust Container (Flex)
```css
.reviews-trust-container {
    display: flex;
    flex-direction: column;
    gap: 48px;
    margin-bottom: 20px;
}
```

### Reviews Header (Flex)
```css
.reviews-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 32px;
    margin-bottom: 24px;
    flex-wrap: wrap;
}
```

### Review Showcase (Grid)
```css
.reviews-showcase {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-top: 40px;
}

/* Desktop: Force 3 columns */
@media (min-width: 1024px) {
    .reviews-showcase {
        grid-template-columns: repeat(3, 1fr);
        gap: 32px;
    }
}
```

---

## Animation Techniques

### Transform Animations
```css
/* Card lift on hover */
.reviews-trust-card:hover {
    transform: translateY(-8px);
}

/* Review card lift */
.review-card:hover {
    transform: translateY(-6px);
}

/* Button lift */
.btn-reviews:hover {
    transform: translateY(-3px);
}
```

### Box Shadow Animations
```css
/* Shadow expansion on hover */
.reviews-trust-card:hover {
    box-shadow: 0 20px 40px rgba(29, 78, 216, 0.15);
}

.btn-reviews:hover {
    box-shadow: 0 8px 20px rgba(29, 78, 216, 0.4);
}
```

### Color Transitions
```css
/* Border color change */
.review-card:hover {
    border-color: var(--secondary);
}

/* Background color change */
.trust-badge:hover {
    background: rgba(29, 78, 216, 0.08);
}
```

---

## Mobile Optimization

### Full-Width Button
```css
@media (max-width: 768px) {
    .btn-reviews {
        width: 100%;
        justify-content: center;
    }
}
```

### Responsive Grid
```css
/* Auto-fit with minimum 280px */
.reviews-showcase {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}
```

### Responsive Padding
```css
/* Reduced padding on mobile */
@media (max-width: 768px) {
    .reviews-trust-card {
        padding: 24px;
    }
}
```

---

## Testing Code Examples

### Verify Styles Applied
```javascript
// In browser console
const section = document.querySelector('.google-reviews-section');
console.log(window.getComputedStyle(section).backgroundColor);
```

### Test Animations
```javascript
// Check if animations work
const card = document.querySelector('.reviews-trust-card');
card.addEventListener('mouseenter', () => {
    console.log('Hover animation triggered');
});
```

### Check Responsive Breakpoints
```javascript
// Test media query
const mql = window.matchMedia('(min-width: 1024px)');
console.log('Is desktop?', mql.matches);
```

---

## Performance Optimization Tips

```css
/* Use transform for animations (GPU accelerated) */
.card:hover {
    transform: translateY(-6px); /* ✅ Good - GPU accelerated */
    /* Avoid: top: -6px; - causes reflow */
}

/* Use opacity for fade effects */
.element:hover {
    opacity: 0.8; /* ✅ Good - GPU accelerated */
    /* Avoid: display: none/block - causes reflow */
}

/* Batch animations with same duration */
transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); /* ✅ Good */
```

---

This code reference provides all the key components, customization examples, and CSS specifications for the Google Reviews section. Use these as a starting point for any modifications or enhancements.

