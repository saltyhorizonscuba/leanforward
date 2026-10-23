# SEO / GEO Playbook — Portable Guidelines

Extrait des principes appliqués et vérifiés sur un site de plongée (Salty Horizon Diving), généralisés pour être réutilisables sur n'importe quel nouveau site, quel que soit son design ou sa stack technique (HTML statique, React, WordPress, etc.). Ce fichier ne contient aucune information propre à ce projet — tout ce qui suit est un principe transférable.

**Comment l'utiliser :** dépose ce fichier à la racine de ton nouveau projet (ex. `PROJECT_PLAYBOOK.md`) et donne-le en contexte à ton assistant IA en début de session, ou colle-le directement dans ton prompt. Partie 1 = SEO/GEO. Partie 2 = discipline de travail (git, CSS, images, pièges techniques) qui fait gagner du temps sur n'importe quel projet web, indépendamment du SEO.

---

## Partie 1 — SEO / GEO

### 1. Le principe fondateur : ce qu'un crawler ne voit pas n'existe pas

La majorité des bugs SEO/GEO rencontrés viennent d'une seule cause récurrente : **du contenu qui n'existe que côté client (JavaScript), donc invisible pour un crawler qui n'exécute pas de JS.**

- GPTBot, ClaudeBot, PerplexityBot et la plupart des crawlers IA **ne rendent généralement pas le JavaScript**. Google le fait, mais avec un délai et un coût de crawl-budget.
- Règle : tout contenu textuel important (titres, descriptions, prix, FAQ, avis) doit exister **dans le HTML brut livré par le serveur**, pas seulement injecté après coup par un script.
- Si le site est multilingue et que la langue est choisie/rendue côté JS (ex. un objet de traduction chargé en JS qui réécrit le DOM), un crawler qui ne l'exécute pas verra toujours la langue par défaut. La solution robuste est une **vraie route/page statique par langue** (`/fr/...`, `/es/...`), pas un switch JS.
- Un `<select>`, une carte produit, une description : si la balise existe mais reste vide en attendant le JS (`<p data-i18n="x"></p>`), un crawler sans JS voit une coquille vide. Toujours mettre un **texte de repli statique** dans la balise, même si le JS le remplace ensuite au chargement.

### 2. Données structurées (JSON-LD)

- Une seule entité business/organisation par site, référencée par `@id` partout où elle apparaît (ne jamais dupliquer un `Organization`/`LocalBusiness` sur chaque page — référencer le même `@id`).
- Types courants à couvrir selon le site : `Organization`/`LocalBusiness` (ou sous-type sectoriel), `WebPage`, `BreadcrumbList` (cohérent avec le fil d'ariane visuel), `FAQPage` (si contenu FAQ visible), `Product`/`Service`/`Course` selon l'activité, `Review`/`AggregateRating`.
- `aggregateRating` : **ne jamais fabriquer une note ou un total.** Si tu n'as pas le vrai chiffre (ex. depuis Google Business Profile), ne mets pas ce champ plutôt que d'inventer une valeur — un chiffre faux est un risque de confiance et potentiellement de pénalité.
- Les avis (`Review.reviewBody`) sont des citations attribuées à de vraies personnes : ne pas les traduire même sur un site multilingue, ça dénaturerait ce que la personne a réellement dit.
- Vérifier la cohérence entre le texte visible et le JSON-LD sur le même sujet (ex. une politique d'annulation affichée différemment du JSON-LD) — Google explique explicitement que ces deux sources doivent concorder.

### 3. GEO / AEO — optimisation pour les moteurs génératifs (ChatGPT, Perplexity, Claude, Gemini)

- `robots.txt` : autoriser explicitement les bots IA si tu veux être cité (`GPTBot`, `ChatGPT-User`, `ClaudeBot`, `Claude-Web`, `Google-Extended`, `PerplexityBot`, `CCBot`, `Bytespider`…), en plus de `User-agent: *`. Les bloquer par défaut coupe la visibilité dans les réponses IA.
- `llms.txt` (convention émergente, pas un standard officiel mais adoptée) : un résumé texte de l'activité + liste des pages clés, à la racine du site. Vérifier que chaque URL listée existe réellement (pas de lien mort).
- Contenu FAQ structuré (question/réponse claire, courte, autonome) : c'est le format que les moteurs génératifs extraient et citent le plus facilement. Une page ou section FAQ bien structurée vaut souvent plus, pour le GEO, qu'un long article narratif.
- Entités reliées par `@id` (voir section 2) aident un LLM à comprendre qu'il s'agit de la même entité business à travers tout le site, y compris entre langues.

### 4. Sitemap, robots, hygiène technique

- `sitemap.xml` : chaque `<lastmod>` doit refléter un vrai changement de contenu, pas la date du dernier commit trivial (ex. un simple bump de version de cache). Vérifier via l'historique git réel du fichier avant de mettre une date, pas à l'aveugle.
- Cohérence des URLs : choisir une convention (avec ou sans extension `.html`) et s'y tenir partout — canonical, hreflang, sitemap, liens internes. Un mélange crée un risque de contenu dupliqué.
- `hreflang` doit être réciproque et résolutif : chaque page liste toutes les variantes de langue avec leurs vraies URLs distinctes, jamais toutes pointant vers la même URL par erreur (bug fréquent).
- `<title>`/meta description/canonical doivent changer si la langue change, même si le changement de langue se fait côté client — sinon un visiteur FR/ES qui change de langue garde un titre d'onglet et un aperçu de lien en anglais.
- `<meta name="robots" content="index, follow">` explicite partout, plutôt que de compter sur le défaut implicite.

### 5. Images et performance (Core Web Vitals)

- Format moderne (WebP) avec fallback JPEG/PNG via `<picture>`.
- Servir une image à la taille réellement affichée, pas l'original pleine résolution partout. Une vignette de galerie de 120-400px affichés ne doit jamais télécharger un fichier de 1500-2400px — c'est l'erreur la plus fréquente et la plus coûteuse en poids de page.
- Pattern éprouvé : une variante "card" (~900px de large) pour les contextes vignette/carte, l'original en pleine résolution réservé aux usages qui en ont vraiment besoin (lightbox/zoom, hero plein écran).
- `width`/`height` explicites sur chaque `<img>` (évite le layout shift = CLS).
- `loading="lazy"` sous la ligne de flottaison ; `fetchpriority="high"` + `<link rel="preload">` uniquement sur le véritable élément LCP (souvent l'image de fond du hero, pas le logo).
- Avant de toucher à l'ordre de chargement (preload, defer, etc.) pour gagner en performance : mesurer avant/après avec un vrai test A/B, pas seulement sur intuition — certaines optimisations "logiques" n'ont aucun effet mesurable en pratique.
- Un identifiant de version en query string (`?v=N`) sur CSS/JS pour forcer le cache-bust à chaque changement, sinon les navigateurs/CDN servent une version périmée indéfiniment.

### 6. Accessibilité (chevauche directement le SEO/GEO)

- Chaque élément interactif (`<select>`, bouton icône seul, lien image seule) doit avoir un nom accessible (`aria-label`, `<label for>`, ou texte visible) — Google Lighthouse/PageSpeed le note explicitement, et une arborescence d'accessibilité bien formée aide aussi les agents IA à naviguer et interagir avec la page, pas seulement les lecteurs d'écran humains.
- Le `<h1>` de la page la plus importante ne doit pas être seulement une image de logo sans texte alternatif substantiel — c'est le signal de pertinence on-page le plus fort de la page.

### 7. Contenu et E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

- Ne jamais fabriquer d'avis, de notes, de statistiques ou de témoignages. Un seul chiffre inventé découvert un jour détruit la confiance dans tout le reste du contenu structuré.
- Contenu creux (page produit de 100 mots sans détails concrets) = signal faible. Mieux vaut une page complète que cinq pages fines.
- Attention à la cohérence : un service/produit mentionné dans les meta ou le schema mais absent de la page réelle (ou inversement) crée un risque de désindexation partielle ou de perte de confiance algorithmique.

### 8. Process — comment garder ce travail cohérent dans la durée

- Tenir un fichier de contexte projet à jour (identité business, inventaire des pages, conventions techniques, prix/infos factuelles) — sert de source de vérité vérifiable plutôt que de dépendre de la mémoire d'une IA d'une session à l'autre, qui peut dériver ou se tromper de date.
- Tenir un journal d'audit daté (ce qui a été trouvé, ce qui a été corrigé, ce qui reste ouvert) — évite de re-signaler un problème déjà réglé, et donne une trace de raisonnement pour les décisions "on ne corrige pas ça, et voici pourquoi" (ex. ne pas fabriquer une note moyenne).
- Avant de citer un fait technique ("ce fichier fait X", "cette page a Y"), revérifier contre le code réel plutôt que de faire confiance à un audit précédent — les fichiers changent, la mémoire d'un assistant IA ne se met pas à jour toute seule.
- Distinguer clairement dans tout audit : bug factuel concret (lien mort, incohérence schema/contenu, date fausse) vs opportunité d'optimisation théorique — les deux méritent d'être signalés, mais pas avec la même urgence.

---

## Partie 2 — Discipline de travail (gain de temps, tous projets)

Règles issues de vrais frottements rencontrés sur ce projet — chacune a coûté du temps ou causé un bug la première fois, à ne pas répéter sur le prochain site.

### 9. Git & déploiement

- Demander confirmation avant chaque push, pas seulement une fois en début de session — une autorisation donnée pour un changement ne vaut pas autorisation permanente pour tous les suivants. Committer en local librement ; c'est le push qui a besoin d'un feu vert.
- Si le workflow habituel est "dev puis main tout de suite après", une seule confirmation peut couvrir les deux — pas besoin de redemander deux fois si c'est la routine convenue avec l'utilisateur.
- Avant de pousser en prod : vérifier ce qui est réellement livré (`git status`/`git diff` ciblé sur les fichiers du commit), pas toute la divergence historique entre branches — ça évite une analyse énorme pour rien quand le contenu est déjà équivalent via des commits différents (cherry-pick, etc.).
- Ce qui reste vraiment utile à vérifier avant un push prod : des références cassées (asset supprimé mais encore utilisé), des pages listées dans le sitemap/nav mais pas encore publiées.
- Si plusieurs sessions/fenêtres travaillent sur le même repo en parallèle : du travail non commité peut disparaître silencieusement (une opération git lancée ailleurs peut toucher le même dossier de travail). Vérifier l'état réel avec des commandes git fraîches avant de supposer "ma dernière modif est toujours là", surtout après une pause ou juste avant un push. Committer plus souvent pendant un travail visuel long réduit ce qui peut être perdu.

### 10. Portée des changements CSS ("juste le mobile", "juste ce composant")

- Une demande "seulement sur mobile" (ou "seulement ce composant") = chaque changement doit rester strictement dans sa media query/son sélecteur. Ne jamais toucher une règle de base/partagée en passant, même pour corriger un bug qui semble évident — ça fuit vers des contextes que l'utilisateur n'a pas demandé de changer.
- Si un réordonnancement du DOM est nécessaire pour un seul breakpoint, fixer explicitement la position visuelle de l'autre breakpoint (`grid-column`/`order`…) plutôt que de supposer que le placement automatique reste neutre — vérifier, ne pas juste l'affirmer.

### 11. Cache-busting des assets statiques (sites sans étape de build)

- Les paramètres de version (`?v=N`) sur CSS/JS/images doivent être incrémentés à chaque changement du fichier sous-jacent, sinon navigateurs et CDN servent une version périmée pendant toute la durée du cache (vérifier le header `Cache-Control`/TTL réel de l'hébergeur).
- Chercher toutes les occurrences avant de bumper — un bump partiel (certaines pages mises à jour, d'autres non) crée des bugs déroutants du type "ça marche sur cette page mais pas celle-là".
- Sur une branche de travail avant mise en prod, ne bumper que ce qui va réellement partir en ligne, juste avant le push — bumper à chaque commit intermédiaire est un bruit inutile (à confirmer selon la préférence de l'utilisateur).

### 12. Convention de traitement d'image (à adapter, mais garder la logique)

- Redimensionner à ~1500px de côté le plus long pour les images de contenu normal, ~2000-2400px pour les images hero plein cadre (vues en plus grand, surtout sur mobile).
- Qualité d'export ~84-88 — suffisant pour survivre à un ré-encodage automatique côté hébergeur sans perte visible. Si une image ré-exportée reste "molle" malgré une qualité correcte, soupçonner une recompression côté serveur qui s'additionne à la tienne.
- Préserver le ratio natif sauf si le contexte de mise en page l'exige (les blocs `object-fit:cover` tolèrent n'importe quel ratio, les mises en page masonry/sans recadrage non).
- Ne jamais suréchantillonner au-delà de la résolution native de la source.
- Pour une vignette/carte affichée à 120-400px, générer une variante dédiée à cette taille plutôt que de servir l'original pleine résolution partout (voir section 5).

### 13. Piège Windows/PowerShell sur les remplacements en masse

- `Get-Content -Encoding UTF8 | Set-Content -Encoding UTF8` sous Windows PowerShell 5.1 ajoute silencieusement un BOM UTF-8 à chaque fichier touché. Ça ne casse rien visuellement mais pollue les diffs git et peut causer des soucis subtils de rendu. Pour un remplacement en masse sur de nombreux fichiers, préférer `sed -i` (via Git Bash) ou une méthode d'encodage explicite sans BOM.
- Après tout remplacement en masse via PowerShell, vérifier `head -c 3 fichier | xxd` — la présence de `ef bb bf` signale un BOM injecté par erreur.

### 14. Attentes autour d'une demande "réinvente/redesign"

- Quand on demande de "réinventer" ou vraiment redesigner l'ergonomie/UX d'une page, l'utilisateur attend un vrai nouveau design visuel/structurel (nouvelle mise en page, nouveau traitement des composants, nouvelle architecture de l'information) — pas juste des changements de texte, d'espacement ou des ajustements CSS mineurs posés sur la structure existante.
- Proposer 2 à 4 directions de concept distinctes (avec une courte description chacune) avant d'implémenter évite de brûler un cycle d'implémentation complet sur la mauvaise piste — le goût en design est subjectif, autant trancher avant de coder.
- Éviter le "texte marketing IA" générique (taglines à superlatifs, accroches génériques du type "5 étoiles sur Google") quand on écrit du copywriting de marque — viser une voix qui sonne comme si le vrai propriétaire du business l'avait écrite.

### 15. Vérifier avant d'affirmer

- Avant d'affirmer "rien n'a changé visuellement" ou "ce correctif fonctionne", vérifier empiriquement (comparaison de captures d'écran, calcul de ratio d'aspect, mesure réelle avant/après) plutôt que de raisonner uniquement par principe — une hypothèse plausible sur ce qui devrait aider peut être fausse, et une vérification rapide coûte moins cher qu'un correctif non testé livré avec confiance.
- Quand une optimisation de performance semble logique sur le papier (ex. retirer un `preload` qui semble concurrencer la bande passante), la tester avec une mesure avant/après contrôlée avant de l'appliquer largement — l'intuition sur les priorités de chargement du navigateur se trompe souvent en pratique.
