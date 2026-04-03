// Morning Brew Coffee — Menu toggle script
// NOTE: The HTML calls openMenu() but this function is named showMenu()
// This is Bug #3 — the button will throw a ReferenceError when clicked

function showMenu() {
  const menuGrid = document.querySelector('.menu-grid');
  const btn = document.querySelector('.menu-btn');

  if (menuGrid.style.display === 'none') {
    menuGrid.style.display = 'grid';
    btn.textContent = 'Hide Menu';
  } else {
    menuGrid.style.display = 'none';
    btn.textContent = 'See Full Menu';
  }
}
