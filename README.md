# Lean Forward — site statique

## ⚠️ Ne pas ouvrir `index.html` par double-clic

Ouvert en `file://`, le navigateur n'affiche que du texte brut : les feuilles de
style, le script et les images sont référencés en chemins absolus (`/css/style.css`,
`/assets/img/…`), qui pointent vers la racine du disque et non vers le dossier du
projet. C'est le comportement normal, pas un bug — et ces chemins absolus sont
exactement ceux qu'il faut une fois le site hébergé.

Deux façons de le voir correctement :

- **`apercu-lean-forward.html`** (à la racine du projet) : les 11 pages à la suite
  dans un fichier autonome, CSS et images inclus. Double-clic, ça marche.
- **Le vrai site**, avec ses 11 URLs séparées : lancer un serveur local (ci-dessous).

Typographie : titres en **Bitter**, texte en **Assistant** (Google Fonts).
Le menu compte 8 entrées (Home, About, The Foundation, The Exploration,
The Immersion, Progression Week, Blog, Contact). Un bouton WhatsApp flotte en
bas à droite sur toutes les pages (`.whatsapp-float`, hors `<main>`/`<footer>`).

Reconstruction du site Wix `freyfilmscr.wixsite.com/lean-forward` en HTML/CSS/JS
statique, conforme au `PROJECT_PLAYBOOK.md`.

## Lancer en local

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

Le serveur de dev de Python sert `dossier/index.html` sur `/dossier/`, donc les
URLs sans extension fonctionnent tel quel.

## Structure

```
index.html                        /
surf-coaching-tamarindo/          /surf-coaching-tamarindo   (The Foundation)
guided-surf-tours/                /guided-surf-tours         (The Exploration)
surf-nature-adventures/           /surf-nature-adventures    (The Immersion)
signature-progression-week/       /signature-progression-week (Signature Progression Week)
about/                            /about                     (About Mateo)
blog/                              /blog                      (index du blog)
blog-*/                            /blog-*                    (3 articles, voir ci-dessous)
contact/                          /contact
css/style.css                     feuille unique
js/main.js                        menu mobile + repli des avis (enrichissement seul)
assets/img/                       photos — voir MANIFEST.md
robots.txt sitemap.xml llms.txt   SEO / GEO (le blog y est listé)
PROJECT_PLAYBOOK.md               les règles suivies
PROJECT_CONTEXT.md                source de vérité factuelle (tarifs, contacts)
content/                          verbatim récupéré du site Wix
build_pages.py gen.py             génération de 6 pages internes (dev seulement, PAS le blog — voir gen.py)
```

## Mobile (≤ 700px, ajouté le 27 septembre 2026)

Le rendu desktop n'est pas modifié ; tout est piloté par deux attributs HTML
et `js/main.js` :

- `data-more="N"` sur un bloc de texte : sur mobile il est replié à N px avec un
  bouton « See more ». Sans JS, le texte est affiché en entier.
- `data-acc` sur un bloc titre + contenu : sur mobile il devient un menu
  déroulant (piliers « Why », éléments de la Progression Week, colonnes
  Immersion, colonnes du pied de page).
- Planches, blobs du blog et bande de photos « Philosophy » deviennent des
  carrousels à glisser (CSS seul).
- Chaque bandeau (hero) a un recadrage vertical dédié au téléphone, taillé pour
  la forme réelle du bloc : `*-m-780` (écrans ×2) et `*-m` (1170px, écrans ×3),
  en avif/webp/jpg, servis via `<source media="(max-width: 700px)">`. Même principe
  pour les fonds `why-playa` et `closing-band` (CSS). Ne pas servir une image
  paysage réduite : recadrée en hauteur sur mobile, elle serait floue.

## Blog (ajouté le 27 septembre 2026)

`/blog` liste 3 articles ; chacun a son fichier plat + son dossier slug :

- `blog-signs-ready-for-more` — 5 signs you're ready to move beyond beginner surf lessons
- `blog-best-surf-spots-tamarindo` — A local's guide to the best surf spots around Tamarindo
- `blog-plan-surf-nature-week` — How to plan a surf & nature adventure week in Costa Rica

Ce sont des articles éditoriaux (conseils génériques de surf/voyage), pas des
faits sur l'entreprise : le playbook §2/§7 (ne jamais inventer un chiffre ou
un avis) ne s'y applique pas au même titre que le reste du site, mais les prix
et les noms de spots qu'ils citent doivent quand même rester cohérents avec
`PROJECT_CONTEXT.md`.

`build_pages.py` et `gen.py` ne sont pas nécessaires en production (et reflètent
le site tel qu'il était au 19 septembre 2026, avant le blog — voir la note en
haut de `gen.py`. À relancer seulement après avoir
mis à jour leurs corps de page si le HTML a été modifié à la main). Ils servent à
regénérer les pages internes quand l'en-tête ou le pied de page change, pour
éviter que les cinq pages divergent : `python3 gen.py`.

## ⚠️ À faire avant la mise en ligne

0. **Ne déployer que les URLs propres.** Ne pas mettre en ligne `apercu-lean-forward.html`
   (aperçu hors ligne, porte déjà un `noindex`) ni, idéalement, les copies plates `*.html`
   de la racine (hors `index.html`) ; si elles sont déployées, rediriger `/*.html` en 301
   vers l'URL propre. Leurs `canonical` pointent déjà vers l'URL propre.
1. **Nom de domaine.** Le code utilise `https://www.leanforwardsurf.com` comme
   valeur de remplacement dans les `canonical`, l'OpenGraph, le JSON-LD, le
   sitemap et `llms.txt`. Remplacer partout par le vrai domaine :
   ```bash
   grep -rl 'www.leanforwardsurf.com' . | xargs sed -i 's|www\.leanforwardsurf\.com|VOTRE-DOMAINE|g'
   ```
2. **Photos.** `assets/img/` contient des placeholders générés (dégradé avec le
   nom du fichier écrit dessus). Les remplacer par les vraies photos, en gardant
   les mêmes noms et les mêmes dimensions — voir `assets/img/MANIFEST.md`. Puis
   supprimer la règle de repli `img { background: linear-gradient(...) }` dans
   `css/style.css`.
3. **`og-cover.jpg`** en 1200 × 630 exactement, sinon l'aperçu des liens partagés
   sera recadré n'importe comment.
4. **Google Business Profile.** Créer ou récupérer la fiche pour obtenir la vraie
   note moyenne et le vrai nombre d'avis. C'est la seule façon d'ajouter un
   `aggregateRating` sans inventer de chiffre (playbook §2 et §7).
5. **Cache-bust.** Incrémenter `?v=N` sur `style.css` et `main.js` à chaque
   modification (playbook §11) :
   ```bash
   grep -rn '?v=' --include='*.html' .
   ```

## Vérification

```bash
python3 verify.py
```
