function footerChg() {
  if (Math.random() < .1) {
    ft=document.getElementById("footerText");
    // ft.innerHTML = "©🏴󠁧󠁢󠁳󠁣󠁴󠁿🐦\n🚫🥷💾&or;🧑🏻‍💻👇🍌👉👤🍕";
    ft.innerHTML = '<i class="fa-regular fa-copyright"></i>&nbsp;<i class="fa-regular fa-flag"></i>&nbsp;<i class="fa-solid fa-crow"></i>&nbsp;\n<i class="fa-solid fa-ban"></i>&nbsp;<i class="fa-solid fa-user-ninja"></i>&nbsp;<i class="fa-solid fa-code"></i>&nbsp;<i class="fa-solid fa-v"></i>&nbsp;<i class="fa-solid fa-user-tie"></i>&nbsp;<i class="fa-solid fa-hand-point-down"></i>&nbsp;<i class="fa-solid fa-carrot"></i>&nbsp;<i class="fa-solid fa-user"></i>&nbsp;<i class="fa-solid fa-pizza-slice"></i>&nbsp;';
    ft.style.cursor = "pointer";
    ft.onclick = function() {alert('Copyright Scottish Puffin. Don\'t steal code or I\'ll put carrot on your pizza.');};
  }
}