// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function() {
  const toggle = document.getElementById('navToggle');
  const list = document.getElementById('navList');
  if (toggle && list) {
    toggle.addEventListener('click', function() {
      list.classList.toggle('open');
    });
  }
});
