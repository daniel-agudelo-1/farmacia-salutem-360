// Header scroll effect
window.addEventListener('scroll', function () {
    const header = document.getElementById('mainHeader');
    if (header) {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }
});

// Countdown timer
function updateCountdown() {
    const now = new Date();
    const endDate = new Date(now.getTime() + 7 * 24 * 60 * 60 * 1000); // 7 días desde ahora
    const totalSeconds = Math.floor((endDate - now) / 1000);

    const daysElem = document.getElementById('days');
    const hoursElem = document.getElementById('hours');
    const minutesElem = document.getElementById('minutes');
    const secondsElem = document.getElementById('seconds');

    if (!daysElem || !hoursElem || !minutesElem || !secondsElem) return;

    if (totalSeconds <= 0) {
        daysElem.textContent = '00';
        hoursElem.textContent = '00';
        minutesElem.textContent = '00';
        secondsElem.textContent = '00';
        return;
    }

    const days = Math.floor(totalSeconds / (24 * 60 * 60));
    const hours = Math.floor((totalSeconds % (24 * 60 * 60)) / (60 * 60));
    const minutes = Math.floor((totalSeconds % (60 * 60)) / 60);
    const seconds = Math.floor(totalSeconds % 60);

    daysElem.textContent = days.toString().padStart(2, '0');
    hoursElem.textContent = hours.toString().padStart(2, '0');
    minutesElem.textContent = minutes.toString().padStart(2, '0');
    secondsElem.textContent = seconds.toString().padStart(2, '0');
}

setInterval(updateCountdown, 1000);
updateCountdown();

// Product hover effect
document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('mouseenter', function () {
        this.style.transform = 'translateY(-10px)';
        this.style.boxShadow = '0 15px 30px rgba(0, 0, 0, 0.15)';
    });

    card.addEventListener('mouseleave', function () {
        this.style.transform = 'translateY(-5px)';
        this.style.boxShadow = '0 10px 25px rgba(0, 0, 0, 0.15)';
    });
});

// Wishlist button toggle
document.querySelectorAll('.wishlist-btn').forEach(button => {
    button.addEventListener('click', function (e) {
        e.preventDefault();
        const icon = this.querySelector('i');
        if (icon) {
            if (icon.classList.contains('far')) {
                icon.classList.remove('far');
                icon.classList.add('fas');
                icon.style.color = '#ff6b6b';
            } else {
                icon.classList.remove('fas');
                icon.classList.add('far');
                icon.style.color = '';
            }
        }
    });
});

// Add to cart animation
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function (e) {
        e.preventDefault();

        this.textContent = '¡Añadido!';
        this.style.backgroundColor = '#4CAF50';

        setTimeout(() => {
            this.textContent = 'Añadir al carrito';
            this.style.backgroundColor = '';
        }, 2000);

        const cartCount = document.querySelector('.cart-count');
        if (cartCount) {
            let count = parseInt(cartCount.textContent) || 0;
            cartCount.textContent = count + 1;

            cartCount.parentElement.style.transform = 'scale(1.2)';
            setTimeout(() => {
                cartCount.parentElement.style.transform = 'scale(1)';
            }, 300);
        }
    });
});

// Search toggle for mobile
const searchToggle = document.getElementById('searchToggle');
const searchBar = document.querySelector('.search-bar');
if (searchToggle && searchBar) {
    searchToggle.addEventListener('click', function (e) {
        e.preventDefault();
        searchBar.classList.toggle('active');
    });
}

// Mobile menu toggle (placeholder)
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function () {
        alert('Menú móvil se abriría aquí. Se necesita más implementación.');
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        if (targetId === '#') return;

        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 100,
                behavior: 'smooth'
            });
        }
    });
});
