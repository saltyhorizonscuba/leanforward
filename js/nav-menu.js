/* Lean Forward — menu mobile.
   Chargé dynamiquement par main.js plutôt que déclaré en ligne : sous un
   en-tête position:sticky, un écouteur de clic attaché pendant l'analyse
   du document HTML initial n'applique pas ses mutations DOM de façon
   fiable dans Chromium (confirmé en isolant le cas — le même écouteur,
   attaché via un script inséré après coup, fonctionne normalement). */
(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");
  if (!toggle || !nav) return;

  var mq = window.matchMedia("(max-width: 900px)");

  function apply() {
    if (mq.matches) {
      nav.classList.add("nav--collapsed");
      toggle.setAttribute("aria-expanded", "false");
    } else {
      nav.classList.remove("nav--collapsed");
      toggle.setAttribute("aria-expanded", "true");
    }
  }

  apply();
  mq.addEventListener("change", apply);

  toggle.addEventListener("click", function () {
    var open = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!open));
    nav.classList.toggle("nav--collapsed", open);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && mq.matches && !nav.classList.contains("nav--collapsed")) {
      toggle.setAttribute("aria-expanded", "false");
      nav.classList.add("nav--collapsed");
      toggle.focus();
    }
  });
})();
