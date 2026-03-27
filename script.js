// Scroll Progress Bar
function updateProgressBar() {
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = window.scrollY;
    const scrollPercent = (scrolled / scrollHeight) * 100;
    document.querySelector('.progress-bar').style.width = scrollPercent + '%';
}

window.addEventListener('scroll', updateProgressBar);

// Back to Top Button
const backToTopBtn = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTopBtn.classList.add('show');
    } else {
        backToTopBtn.classList.remove('show');
    }
});

backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Dark Mode Toggle
const themeToggle = document.getElementById('themeToggle');
const htmlElement = document.documentElement;

// Check for saved theme preference or default to light mode
const currentTheme = localStorage.getItem('theme') || 'light';
if (currentTheme === 'dark') {
    document.body.classList.add('dark-mode');
    updateThemeIcon();
}

themeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    
    // Save preference to localStorage
    const newTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('theme', newTheme);
    
    // Update icon
    updateThemeIcon();
});

function updateThemeIcon() {
    const icon = themeToggle.querySelector('.theme-icon');
    if (document.body.classList.contains('dark-mode')) {
        icon.textContent = '☀️';
    } else {
        icon.textContent = '🌙';
    }
}

// Animated Counter for Metrics
function animateCounters() {
    const metricNumbers = document.querySelectorAll('.metric-number');
    
    metricNumbers.forEach(element => {
        const target = parseInt(element.getAttribute('data-target'));
        const isYear = target > 1900; // Simple check for year values
        
        if (element.dataset.animated) return; // Skip if already animated
        element.dataset.animated = 'true';
        
        let current = 0;
        const increment = target / 60;
        
        const updateCount = () => {
            current += increment;
            if (current < target) {
                element.textContent = isYear ? Math.floor(current) : Math.ceil(current).toLocaleString();
                requestAnimationFrame(updateCount);
            } else {
                element.textContent = target.toLocaleString();
            }
        };
        
        updateCount();
    });
}

// Intersection Observer for triggering animations
const observerOptions = {
    threshold: 0.3,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            if (entry.target.classList.contains('metrics-grid')) {
                animateCounters();
                observer.unobserve(entry.target);
            }
            
            // Add visible class for scroll animations
            entry.target.classList.add('in-view');
        }
    });
}, observerOptions);

// Observe all sections with fade-in class
document.querySelectorAll('.fade-in').forEach(element => {
    observer.observe(element);
});

// Observe metrics grid
const metricsGrid = document.querySelector('.metrics-grid');
if (metricsGrid) {
    observer.observe(metricsGrid);
}

// Smooth scroll behavior for links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#') {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

// Add parallax effect on scroll
window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const header = document.querySelector('header');
    if (header) {
        header.style.backgroundPosition = `0 ${scrolled * 0.5}px`;
    }
});

// Keyboard accessibility - ESC to hide back to top
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && backToTopBtn.classList.contains('show')) {
        backToTopBtn.classList.remove('show');
    }
});

// Add hover effects to cards
const cards = document.querySelectorAll('.factor-card, .enabler-card, .metric-card');
cards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.zIndex = '10';
    });
    card.addEventListener('mouseleave', function() {
        this.style.zIndex = '1';
    });
});

// Prefetch hover state for internal links
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.05)';
    });
    link.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
});

// Performance: Throttle scroll events
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

const throttledProgressBar = throttle(updateProgressBar, 100);
window.addEventListener('scroll', throttledProgressBar, { passive: true });

// Print functionality hint
document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
        console.log('Print mode activated - designed to look great in print!');
    }
});

// Page load animation
window.addEventListener('load', () => {
    document.body.style.opacity = '1';
    document.querySelectorAll('.fade-in').forEach((el, index) => {
        setTimeout(() => {
            el.style.animation = 'fadeInUp 0.8s ease-out forwards';
        }, index * 100);
    });
});

// Add loading state
document.body.style.opacity = '0.95';
