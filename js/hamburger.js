// Simple accessible hamburger nav toggle (vanilla JS)
// - Toggles the 'open' class on the <nav> element
// - Updates aria-expanded on the toggle button

document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('nav');
  const navList = document.getElementById('nav-list');

  if (!toggle || !nav || !navList) return; // nothing to do

  // Toggle function
  function setOpen(isOpen) {
    if (isOpen) {
      nav.classList.add('open');
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Close navigation');
    } else {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open navigation');
    }
  }

  // Click handler
  toggle.addEventListener('click', function (e) {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    setOpen(!expanded);
  });

  // Close menu when clicking a nav link (useful on mobile)
  navList.addEventListener('click', function (e) {
    if (e.target.tagName === 'A' && nav.classList.contains('open')) {
      setOpen(false);
    }
  });

  // Ensure proper state on window resize
  window.addEventListener('resize', function () {
    if (window.innerWidth > 768) {
      // ensure menu is visible and aria reflects desktop state
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open navigation');
    }
  });
});
