# -*- coding: utf-8 -*-
"""Génère les 6 pages internes à partir d'un gabarit commun.
Pas d'étape de build en production : ce script sert uniquement à garder
l'en-tête et le pied de page identiques entre les pages. Le HTML produit
est complet et statique (playbook §1)."""
import io, json, os

BASE = "https://www.leanforwardsurf.com"
BID  = BASE + "/#business"

HEAD = u'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lean Forward">
<meta property="og:locale" content="en_US">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{base}/assets/img/og-cover.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="A surfer riding a clean wave at Tamarindo, Costa Rica">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bitter:wght@300;400;500;600;700;800;900&family=Assistant:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/css/style.css?v=48">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="logo" href="/" aria-label="Lean Forward — home">
      <img src="/assets/img/logo-lean-forward.png" alt="Lean Forward" width="240" height="144">
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open the main menu">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 7h20M3 13h20M3 19h20"/></svg>
    </button>
    <nav class="nav" id="primary-nav" aria-label="Main">
      <a href="/"{c_home}>Home</a>
      <a href="/about"{c_about}>About</a>
      <a href="/surf-coaching-tamarindo"{c_found}>The Foundation</a>
      <a href="/guided-surf-tours"{c_expl}>The Exploration</a>
      <a href="/surf-nature-adventures"{c_imm}>The Immersion</a>
      <a href="/signature-progression-week"{c_prog}>Progression Week</a>
      <a href="/blog"{c_blog}>Blog</a>
      <a href="/contact"{c_cont}>Contact</a>
    </nav>
  </div>
</header>

<main id="main">
  <nav class="breadcrumb wrap" aria-label="Breadcrumb">
    <ol>
      <li><a href="/">Home</a></li>
      <li><span aria-current="page">{crumb}</span></li>
    </ol>
  </nav>
'''

FOOT = u'''</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h3>Lean Forward</h3>
        <p>Surf coaching, guided tours and surf &amp; nature adventures in Tamarindo, Guanacaste, Costa Rica.</p>
        <p><strong>Lean Forward — Smooth Connection.</strong></p>
        <p><a href="/about">About Mateo</a></p>
        <p><a href="/blog">Blog</a></p>
      </div>
      <div data-acc>
        <h3>Experiences</h3>
        <ul>
          <li><a href="/surf-coaching-tamarindo">The Foundation</a></li>
          <li><a href="/guided-surf-tours">The Exploration</a></li>
          <li><a href="/surf-nature-adventures">The Immersion</a></li>
          <li><a href="/signature-progression-week">Signature Progression Week</a></li>
        </ul>
      </div>
      <div data-acc>
        <h3>Get in touch</h3>
        <ul>
          <li><a href="https://wa.me/50672446227">WhatsApp +506 7244-6227</a></li>
          <li><a href="mailto:contact.leanforward@gmail.com">contact.leanforward@gmail.com</a></li>
          <li><a href="https://www.instagram.com/leanforwardsurf/" rel="me noopener">Instagram @leanforwardsurf</a></li>
          <li><a href="https://www.facebook.com/profile.php?id=61591034983027" rel="me noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__bottom">
      <p>© 2026 Lean Forward. All rights reserved.</p>
      <p>Tamarindo, Guanacaste, Costa Rica</p>
    </div>
  </div>
</footer>

<a class="whatsapp-float" href="https://wa.me/50672446227" aria-label="Message Lean Forward on WhatsApp"><svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.004 3C9.377 3 4 8.377 4 15.004c0 2.377.7 4.59 1.902 6.447L4 29l7.73-1.865A11.94 11.94 0 0 0 16.004 27C22.63 27 28 21.623 28 15.004 28 8.377 22.63 3 16.004 3Zm6.988 16.84c-.298.837-1.47 1.58-2.412 1.783-.642.137-1.48.246-4.302-.924-3.61-1.497-5.933-5.157-6.114-5.397-.174-.24-1.463-1.946-1.463-3.714 0-1.768.914-2.634 1.24-2.994.298-.328.652-.41.87-.41.218 0 .436.002.626.012.2.01.47-.076.735.56.298.717 1.014 2.478 1.104 2.659.09.18.15.394.03.634-.12.24-.18.394-.36.6-.18.21-.376.468-.538.628-.18.18-.368.375-.158.735.21.36.933 1.54 2.004 2.494 1.377 1.228 2.538 1.608 2.898 1.788.36.18.57.15.78-.09.21-.24.9-1.05 1.14-1.41.24-.36.48-.3.81-.18.33.12 2.1.99 2.46 1.17.36.18.6.27.69.42.09.15.09.87-.208 1.706Z"/></svg></a>

<script src="/js/main.js?v=10"></script>
</body>
</html>
'''


def unesc(s):
    """Le HTML veut &amp;, le JSON-LD veut le caractère brut."""
    return s.replace("&amp;", "&")


def graph(slug, title, desc, crumb, extra):
    """Un seul LocalBusiness par site, référencé par @id (playbook §2)."""
    url = BASE + "/" + slug if slug else BASE + "/"
    title, desc = unesc(title), unesc(desc)
    g = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title,
         "description": desc, "inLanguage": "en",
         "isPartOf": {"@id": BASE + "/#website"},
         "about": {"@id": BID}},
        {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": crumb, "item": url}]},
    ]
    g.extend(extra)
    return json.dumps({"@context": "https://schema.org", "@graph": g},
                      indent=2, ensure_ascii=False)


def page(slug, title, desc, crumb, extra, body, current):
    url = BASE + "/" + slug
    cur = ' aria-current="page"'
    head = HEAD.format(
        title=title, desc=desc, url=url, base=BASE,
        ld=graph(slug, title, desc, crumb, extra), crumb=crumb,
        c_home=cur if current == "home" else "",
        c_found=cur if current == "found" else "",
        c_expl=cur if current == "expl" else "",
        c_imm=cur if current == "imm" else "",
        c_about=cur if current == "about" else "",
        c_prog=cur if current == "prog" else "",
        c_blog=cur if current == "blog" else "",
        c_cont=cur if current == "cont" else "")
    os.makedirs(slug, exist_ok=True)
    with io.open(os.path.join(slug, "index.html"), "w", encoding="utf-8") as f:
        f.write(head + body + FOOT)
    print("écrit: " + slug + "/index.html")
