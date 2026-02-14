document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal Observer
    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1 // Trigger when 10% of the element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Initial check for elements
    const elements = document.querySelectorAll('[class*="reveal"]');
    elements.forEach(el => observer.observe(el));

    // Optional: Back to top button logic if you want to include it
    const btn = document.getElementById('back-to-top');
    if (btn) {
        window.onscroll = function() {
            if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
                btn.classList.remove('hidden');
            } else {
                btn.classList.add('hidden');
            }
        };
    }
});

/**
 * Hero Slideshow Component
 * Handles dynamic image transitions for any number of images.
 */
document.addEventListener('alpine:init', () => {
    Alpine.data('heroSlideshow', (totalImages) => ({
        active: 0,
        total: totalImages,
        init() {
            if (this.total > 1) {
                setInterval(() => {
                    this.active = (this.active + 1) % this.total;
                }, 6000); // Transitions every 6 seconds
            }
        }
    }));
});
