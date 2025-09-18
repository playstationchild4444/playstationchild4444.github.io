function loadTheme() {
  const themeName = getCookie('theme') || 'style.css';
  setTheme(themeName);
}
window.onload = loadTheme;
