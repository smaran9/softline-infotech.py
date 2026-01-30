console.log("Softline Infotech website loaded");
function sendWhatsAppMessage(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const message = document.getElementById("message").value.trim();

    const whatsappNumber = "919409415293"; // Softline WhatsApp number

    const text =
        `New Service Enquiry%0A` +
        `--------------------%0A` +
        `Name: ${encodeURIComponent(name)}%0A` +
        `Phone: ${encodeURIComponent(phone)}%0A` +
        `Message: ${encodeURIComponent(message)}`;

    const url = `https://wa.me/${whatsappNumber}?text=${text}`;

    window.open(url, "_blank");
}

// Navbar active link highlighting
document.addEventListener('DOMContentLoaded', function () {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav .nav-link');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});