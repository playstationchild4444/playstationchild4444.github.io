//https://github.com/victorqribeiro/radialMenu
//bleh

document.addEventListener('DOMContentLoaded', function () {
  const toggleSwitch = document.createElement('input');
  const label = document.createElement('label');
  const span = document.createElement('span');
  const darkModeLabel = document.createElement('span');
  
  toggleSwitch.type = 'checkbox';
  toggleSwitch.id = 'darkModeSwitch';
  label.className = 'switch';
  span.className = 'slider round';
  darkModeLabel.className = 'dark-mode-label';
  darkModeLabel.textContent = 'Un Dark Mode(WIP)';

  label.appendChild(toggleSwitch);
  label.appendChild(span);
  document.body.appendChild(label);
  document.body.appendChild(darkModeLabel);

  function switchTheme(e) {
    if (e.target.checked) {
      document.body.classList.add('dark-mode');
      document.body.classList.remove('light-mode');
      document.cookie = "theme=dark; path=/";
    } else {
      document.body.classList.add('light-mode');
      document.body.classList.remove('dark-mode');
      document.cookie = "theme=light; path=/";
    }
  }

  function getCookie(name) {
    let cookieArr = document.cookie.split(";");
    for (let i = 0; i < cookieArr.length; i++) {
      let cookiePair = cookieArr[i].split("=");
      if (name == cookiePair[0].trim()) {
        return decodeURIComponent(cookiePair[1]);
      }
    }
    return null;
  }

  toggleSwitch.addEventListener('change', switchTheme, false);

  const currentTheme = getCookie("theme");
  if (currentTheme === "dark") {
    toggleSwitch.checked = true;
    document.body.classList.add('dark-mode');
  } else {
    toggleSwitch.checked = false;
    document.body.classList.add('light-mode');
  }
});
