# Journal d'audit

Playbook §8 : trace datée de ce qui a été trouvé, corrigé, et laissé ouvert.

## 2026-08-20 — Audit du site Wix d'origine

Site audité : `https://freyfilmscr.wixsite.com/lean-forward`

### Bugs factuels constatés

| # | Constat | Règle | Statut |
|---|---|---|---|
| 1 | Slugs par défaut `/blank`, `/blank-1`, `/blank-2`, `/blank-3` | §4 | Corrigé — slugs descriptifs |
| 2 | Aucune meta description sur l'accueil | §4 | Corrigé — 5 descriptions de 136 à 157 car. |
| 3 | Aucun JSON-LD sur tout le site | §2 | Corrigé — LocalBusiness, WebSite, WebPage, BreadcrumbList, Service, Review, FAQPage |
| 4 | Deux `<h1>` sur l'accueil | §6 | Corrigé — un seul H1 par page |
| 5 | 8 images sur 15 sans attribut `alt` | §6 | Corrigé — 100 % des images ont un `alt` |
| 6 | `<title>` « Home \| Lean Forward », sans mot-clé ni lieu | §7 | Corrigé |
| 7 | `og:image` et `og:description` absents | §4 | Corrigé |
| 8 | Contraste insuffisant du titre hero (gris clair sur photo claire) | §6 | Corrigé — voile dégradé + texte blanc |
| 9 | Pas de `robots.txt`, `sitemap.xml` ni `llms.txt` | §3 §4 | Corrigé |
| 10 | Prix détaillés de The Foundation ($90/$80/$75) absents de l'accueil | §7 | Corrigé — tableau de tarifs complet |

### Opportunités d'optimisation (distinctes des bugs, §8)

- Passer les JPEG en `<picture>` WebP + fallback (§5) — en attente des vraies photos.
- Créer une fiche Google Business Profile pour obtenir une note et un nombre
  d'avis réels, seule voie légitime vers un `aggregateRating`.
- Acheter un vrai nom de domaine : `.wixsite.com` sous la marque « freyfilmscr »
  n'a aucune valeur de marque pour Lean Forward.

### Décisions explicites de ne pas corriger

- **Pas d'`aggregateRating`.** Deux avis sur quatre écrivent « 5 stars » dans
  leur texte, ce qui autorise un `reviewRating` sur ces deux avis précis. Mais
  ni la moyenne réelle ni le nombre total d'avis ne sont connus. Fabriquer
  `ratingValue` et `reviewCount` serait inventer une statistique — interdit
  par §2 et §7. À rouvrir quand la fiche Google Business Profile existera.
- **Pas de redirections 301 depuis les anciennes URLs.** Les slugs `/blank*`
  sur un sous-domaine `.wixsite.com` n'ont pas d'historique de référencement à
  préserver, et Wix ne permet pas de rediriger depuis ce sous-domaine.

### Reste ouvert

- Photos réelles à déposer dans `assets/img/` (voir `MANIFEST.md`). Le dossier
  contient pour l'instant des **placeholders générés**, aux bonnes dimensions,
  pour que la mise en page soit vérifiable en local.
- Textes alternatifs des bandeaux de pages internes et de la page Contact : à
  relire une fois les vraies photos en place.
- Nom de domaine à fixer, puis remplacer `www.leanforwardsurf.com` partout.

### Vérifications passées le 2026-08-20

- `verify.py` : 0 problème bloquant sur les 5 pages.
- Contenu présent dans le HTML brut sans JavaScript : 1624 / 482 / 403 / 444 / 282 mots.
- Responsive testé à 390, 768 et 1440 px : aucun débordement horizontal.
- Menu mobile : ouverture/fermeture et `aria-expanded` corrects.
- Avis : repli progressif fonctionnel, texte complet présent sans JS.
- Toutes les images se chargent, aucune référence morte.
- Liens internes : 5 cibles, aucune morte. `llms.txt` : toutes les URLs existent.

## Audit SEO/GEO — 2026-09-27

Quatre agents en lecture seule (revue « head of SEO/GEO » + balises, données
structurées, contenu/images), puis corrections appliquées le même jour.

### Corrigé

- **URL canonique unique par page.** L'accueil liait les copies `*.html` et
  chaque copie plate se déclarait canonique d'elle-même (risque de contenu
  dupliqué). Les liens de l'accueil sont passés en URL propres (`/about`…),
  et les copies plates déclarent désormais l'URL propre en `canonical`,
  `og:url` et JSON-LD. Les dossiers slug sont regénérés depuis les copies plates.
- **JSON-LD.** Les 3 `Service` de l'accueil avaient un `@id` en `.html`
  (entités dupliquées) ; offre Immersion alignée sur la tarification réelle
  (dès $230, sur devis) ; `reviewBody` = texte complet affiché (plus de phrases
  recollées) ; `image` et `logo` ajoutés à l'entité business ; fil d'Ariane des
  articles complété (`item` manquant) ; auteur/éditeur nommés et `dateModified`
  sur les `BlogPosting` ; liste `/blog` avec des `BlogPosting` complets.
- **Titres et descriptions** raccourcis (Progression Week, blog, articles,
  Foundation, Immersion) ; titre de l'accueil recentré pour ne plus concurrencer
  The Foundation sur « surf lessons Tamarindo ». `og:type=article` sur les articles.
- **Lien cassé** « Read the full story » sur /about (pointait vers /about).
- **Liens « More info » / « Read article »** remplacés par des libellés descriptifs.
- **Maillage** : chaque page service renvoie vers l'article de blog associé.
- **Hiérarchie de titres** : H2 (masqué visuellement) ajouté sur /blog et sur
  l'article « 5 signs ».
- **Images** : `why-playa` et `closing-band` servies en avif/webp via
  `image-set()` (why-playa : 471 Ko → 77 Ko) ; images Immersion recompressées.
- **Polices** : Bitter 800/900 ajoutés (le CSS les utilisait, le navigateur
  les simulait).
- **Aperçu hors ligne** : `noindex` + `Disallow` dans `robots.txt`, et checklist
  de mise en ligne complétée dans le README.

### Laissé au client (décision de contenu)

- H1 sans mot-clé : accueil (« Lean Forward »), Immersion (« Surf Beyond the
  Waves ») — choisis par le client ; Progression Week reprend le H2 de l'accueil
  (texte définitif attendu).
- Pages courtes : Blog, Contact, Immersion ; The Foundation gagnerait à dépasser
  400 mots (FAQ).
- Phrase « pairs a day of surfing with a half day of exploration » sur
  Foundation : conservée car formulée par le client, à reconfirmer.
- Image Open Graph propre à chaque page (aujourd'hui `og-cover.jpg` partout).

### Vérifications passées le 2026-09-27

- 21 pages : 1 H1, alt et dimensions sur toutes les images, JSON-LD valide,
  aucun lien mort, aucune URL `.html` dans les canonical / JSON-LD, titres ≤ 62
  et descriptions 110-160 caractères.
- Liens de l'accueil vérifiés sur serveur local ; fonds servis en avif.
