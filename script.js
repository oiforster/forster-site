/* ============================================
   FORSTER FILMES — Site Institucional
   ============================================ */

// --- Nav scroll behavior ---
const nav = document.getElementById('nav');
const hero = document.getElementById('hero');
const isTypeHero = hero.classList.contains('hero--type');

function updateNav() {
  const scrollY = window.scrollY;
  const heroHeight = hero.offsetHeight;

  if (scrollY > heroHeight * 0.8) {
    nav.classList.add('nav--scrolled');
    nav.classList.remove('nav--hero');
    nav.classList.remove('nav--hero-light');
  } else {
    nav.classList.remove('nav--scrolled');
    nav.classList.add('nav--hero');
    if (isTypeHero) {
      nav.classList.add('nav--hero-light');
    }
  }
}

nav.classList.add('nav--hero');
if (isTypeHero) nav.classList.add('nav--hero-light');
window.addEventListener('scroll', updateNav, { passive: true });

// --- Scroll reveal ---
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('reveal--visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, {
  threshold: 0.15,
  rootMargin: '0px 0px -50px 0px'
});

// --- Auto-add reveal class to sections ---
document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('.trabalhos, .sobre, .contato');

  sections.forEach(section => {
    const elements = section.querySelectorAll(
      '.section-eyebrow, .section-title, .sobre__body, .sobre__body--subtle, ' +
      '.sobre__image, .sobre__roles, .trabalho-card, .contato__title, ' +
      '.contato__body, .contato__links'
    );

    elements.forEach((el, i) => {
      el.classList.add('reveal');
      el.style.transitionDelay = `${i * 0.08}s`;
      revealObserver.observe(el);
    });
  });
});

// --- Smooth scroll for nav links ---
document.querySelectorAll('.nav__links a').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});
