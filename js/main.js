/* Lean Forward — enrichissement progressif uniquement.
   Aucun contenu textuel n'est produit ici : tout existe déjà dans le HTML
   livré par le serveur (playbook §1). Ce script ne fait que replier du
   contenu déjà présent et piloter le menu mobile. */
(function () {
  "use strict";

  /* --- Menu mobile -------------------------------------------------------
     Sous un en-tête position:sticky, un écouteur de clic attaché pendant
     l'analyse du document HTML initial n'applique pas ses mutations DOM de
     façon fiable dans Chromium (confirmé en isolant le cas — le même
     écouteur, attaché via un script inséré après coup, fonctionne
     normalement ; ni un délai, ni "defer" ne suffisent, seule l'insertion
     dynamique du script change quelque chose). L'état initial (synchrone,
     hors écouteur) est donc posé ici pour éviter tout flash du menu
     déplié, et js/nav-menu.js — chargé dynamiquement — porte les
     écouteurs réels. */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  if (toggle && nav) {
    if (window.matchMedia("(max-width: 900px)").matches) {
      nav.classList.add("nav--collapsed");
      toggle.setAttribute("aria-expanded", "false");
    } else {
      toggle.setAttribute("aria-expanded", "true");
    }

    var navScript = document.createElement("script");
    /* Résolu à partir de l'URL de main.js lui-même : un chemin absolu
       ("/js/…") casse le menu dès que la page est ouverte hors serveur. */
    var self = document.currentScript && document.currentScript.src;
    navScript.src = self ? new URL("nav-menu.js?v=2", self).href : "/js/nav-menu.js?v=2";
    document.body.appendChild(navScript);
  }

  /* --- Témoignages longs : repli après coup -----------------------------
     Le texte complet est dans le HTML et visible sans JS. On ne le replie
     qu'une fois le script exécuté, pour ne jamais cacher de contenu à un
     crawler qui n'exécute pas JavaScript. */
  Array.prototype.forEach.call(document.querySelectorAll(".quote"), function (fig) {
    var rest = fig.querySelector(".quote__rest");
    if (!rest) return;

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "quote__more";
    btn.setAttribute("aria-expanded", "false");
    rest.hidden = true;

    var name = fig.querySelector("figcaption");
    var who = name ? name.textContent.trim().split("\n")[0] : "this review";
    btn.textContent = "Read the full review";
    btn.setAttribute("aria-label", "Read the full review from " + who);

    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
      rest.hidden = open;
      btn.textContent = open ? "Read the full review" : "Show less";
    });

    rest.parentNode.insertBefore(btn, rest.nextSibling);
  });

  /* --- Carrousel des avis --------------------------------------------------
     Le titre défile nativement (overflow-x + scroll-snap) même sans JS ;
     les flèches ne sont ajoutées qu'une fois le script confirmé actif. */
  var track = document.getElementById("reviewsTrack");
  if (track) {
    var carousel = track.closest(".reviews-carousel");
    var nav = document.createElement("div");
    nav.className = "carousel-nav";

    var prevBtn = document.createElement("button");
    prevBtn.type = "button";
    prevBtn.className = "carousel-nav__btn";
    prevBtn.setAttribute("aria-label", "Previous review");
    prevBtn.innerHTML = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M12 4l-6 6 6 6"/></svg>';

    var nextBtn = document.createElement("button");
    nextBtn.type = "button";
    nextBtn.className = "carousel-nav__btn";
    nextBtn.setAttribute("aria-label", "Next review");
    nextBtn.innerHTML = '<svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M8 4l6 6-6 6"/></svg>';

    nav.appendChild(prevBtn);
    nav.appendChild(nextBtn);
    carousel.appendChild(nav);

    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function scrollStep(dir) {
      track.scrollBy({ left: dir * track.clientWidth * .86, behavior: reduceMotion ? "auto" : "smooth" });
    }
    prevBtn.addEventListener("click", function () { scrollStep(-1); });
    nextBtn.addEventListener("click", function () { scrollStep(1); });

    function updateEdges() {
      prevBtn.disabled = track.scrollLeft <= 4;
      nextBtn.disabled = track.scrollLeft >= track.scrollWidth - track.clientWidth - 4;
    }
    updateEdges();
    track.addEventListener("scroll", updateEdges, { passive: true });
    window.addEventListener("resize", updateEdges);
  }

  /* --- Mobile : « See more » et menus déroulants ---------------------------
     Le CSS ne replie qu'en dessous de 700px ; au-dessus, boutons invisibles
     et panneaux toujours ouverts, donc le rendu desktop ne change pas. */
  var mobile = window.matchMedia("(max-width: 700px)");

  var mores = Array.prototype.map.call(document.querySelectorAll("[data-more]"), function (el) {
    var limit = parseInt(el.getAttribute("data-more"), 10) || 260;
    el.classList.add("more");
    el.style.setProperty("--more-h", limit + "px");
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "more-btn";
    btn.setAttribute("aria-expanded", "false");
    btn.textContent = "See more";
    btn.addEventListener("click", function () {
      var open = el.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", String(open));
      btn.textContent = open ? "See less" : "See more";
      if (!open) el.scrollIntoView({ block: "nearest" });
    });
    el.parentNode.insertBefore(btn, el.nextSibling);
    return { el: el, limit: limit };
  });

  function measureMores() {
    mores.forEach(function (m) {
      m.el.classList.remove("more--short");
      if (mobile.matches && m.el.scrollHeight <= m.limit + 80) m.el.classList.add("more--short");
    });
  }
  measureMores();
  mobile.addEventListener("change", measureMores);
  window.addEventListener("load", measureMores);

  Array.prototype.forEach.call(document.querySelectorAll("[data-acc]"), function (item, i) {
    var head = item.querySelector("h2, h3, h4");
    if (!head) return;
    var panel = document.createElement("div");
    panel.className = "acc-panel";
    panel.id = "acc-panel-" + i;
    while (head.nextSibling) panel.appendChild(head.nextSibling);
    item.appendChild(panel);

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "acc-btn";
    btn.setAttribute("aria-controls", panel.id);
    btn.setAttribute("aria-expanded", "false");
    while (head.firstChild) btn.appendChild(head.firstChild);
    var icon = document.createElement("span");
    icon.className = "acc-btn__icon";
    icon.setAttribute("aria-hidden", "true");
    btn.appendChild(icon);
    head.appendChild(btn);
    item.classList.add("acc-ready");

    function sync() {
      var open = !mobile.matches || item.classList.contains("is-open");
      btn.setAttribute("aria-expanded", String(open));
      btn.tabIndex = mobile.matches ? 0 : -1;
    }
    btn.addEventListener("click", function () {
      if (!mobile.matches) return;
      item.classList.toggle("is-open");
      sync();
    });
    mobile.addEventListener("change", sync);
    sync();
  });

  /* --- Révélation douce au scroll -----------------------------------------
     N'ajoute l'état masqué qu'une fois le JS confirmé actif : sans JS ou
     avec IntersectionObserver indisponible, le contenu reste visible
     directement (playbook §1). Respecte prefers-reduced-motion via le CSS
     global (transitions ramenées à .01ms). */
  if ("IntersectionObserver" in window) {
    var targets = document.querySelectorAll(".reveal");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: .15, rootMargin: "0px 0px -8% 0px" });

    Array.prototype.forEach.call(targets, function (el) {
      el.classList.add("reveal--pre");
      io.observe(el);
    });
  }
})();
