# Images attendues

Le site référence les fichiers ci-dessous. Ce dossier contient actuellement des
**placeholders générés** aux dimensions exactes, pour que la mise en page soit
vérifiable en local. Ils sont reconnaissables : dégradé bleu-vert avec le nom du
fichier et sa taille écrits dessus. **Tous sont à remplacer par les vraies photos.**

## Pourquoi elles ne sont pas déjà là

Le CDN Wix (`static.wixstatic.com`) est bloqué par le proxy réseau de
l'environnement où le site a été construit — impossible d'y télécharger les
originaux. Deux façons de les récupérer :

1. **Wix Media Manager** → sélectionner les fichiers → *Download*. C'est la
   meilleure source : Wix y conserve les originaux non recompressés.
2. Les photos brutes d'origine, si Mateo les a encore (préférable : elles
   n'ont subi aucune recompression).

## Fichiers à fournir

| Fichier attendu | Rôle | Taille cible (playbook §12) | Contenu |
|---|---|---|---|
| `logo-lean-forward.png` | Logo en-tête | ~240px de large, fond transparent | Wordmark bleu dessiné à la main |
| `hero-wave-2400.jpg` | Hero accueil | 2400px de large | Surfeur sur la face d'une vague propre |
| `og-cover.jpg` | Aperçu réseaux sociaux | **1200 × 630 exactement** | Recadrage du hero |
| `mateo-portrait-1500.jpg` | Section « My Story » | 1500px de haut, portrait | Mateo sur la plage, rashguard noir |
| `foundation-card-900.jpg` | Carte accueil | 900px de large, 4/3 | Coach poussant un élève sur un longboard |
| `exploration-card-900.jpg` | Carte accueil | 900px de large, 4/3 | Deux surfeurs entrant dans l'eau |
| `immersion-card-900.jpg` | Carte accueil | 900px de large, 4/3 | Planches sanglées sur le toit d'une voiture |
| `progression-1500.jpg` | Section Progression | 1500px de haut, portrait | Mateo discutant avec une cliente sur le sable |
| `foundation-hero-2000.jpg` | Bandeau The Foundation | 2000px de large, 20/9 | Session de coaching |
| `exploration-hero-2000.jpg` | Bandeau The Exploration | 2000px de large, 20/9 | Surf trip / spot hors Tamarindo |
| `immersion-hero-2000.jpg` | Bandeau The Immersion | 2000px de large, 20/9 | Aventure surf & nature |
| `mateo-contact-1200.jpg` | Page Contact | 1200px de large, 4/3 | Portrait de Mateo |

## Identifiants Wix repérés

Ces identifiants apparaissent dans le HTML du site Wix ; ils aident à retrouver
les bons fichiers dans le Media Manager. Préfixe commun : `315592_`.

- `a616c2d65dc34b339e70a51df7e2bb16~mv2.png` — logo
- `51b6d26989…` — hero accueil (surfeur sur la vague)
- `6e14918cc89941949fd0209a4e6e487b~mv2.jpg` — portrait « My Story »
- `88d6766881e44009812e6ac207c30c67~mv2.jpg` — triptyque Philosophy
- `734e0cc62da042f9998b9827fd5e09aa~mv2.jpg` — triptyque Philosophy
- `1d5cebcd0e264339910f9a77d48caa1f~mv2.jpg` — triptyque Philosophy
- `352c2190c63c423d9ec0ef01de4a2a8a~mv2.jpg`, `7c4cd6406bfb4a44a6bb8928a9b15e11~mv2.jpg`,
  `b6bfa3539805453186a991b98f345026~mv2.jpg`, `83e561ec980a438da3452ced10c20714~mv2.jpg`,
  `397ad11ad10f4962a62b425eb2b8636b~mv2.jpg`, `b3997ee05db04822b5fbd5604ec48512~mv2.jpg`,
  `5175e8e2cae54c739a6afc83ef99db2b~mv2.jpg`, `dc703c3bb11e4f90b0e65b3d6c0d6459~mv2.jpg` — accueil
- `f5d7b022e46f4994b729b7005333069c~mv2.jpg`, `90065be98c404a1daab4af25bcb9a715~mv2.jpg` — The Exploration
- `a7afdff4d5e442089aeae2110c508a01~mv2.jpg` — The Immersion
- `a68e1ddd39c543b99a7c43bcc1623730~mv2.jpg`, `82f602173c0f40c2bb3d313e43f78830~mv2.jpg`,
  `550d49734663491a9bdecc48243068b1~mv2.jpg`, `dadbb75a08b74589a872c37ad01ce326~mv2.jpg` — Contact

## ⚠️ Textes alternatifs à vérifier

Les `alt` déjà écrits décrivent ce qui a été **réellement observé** sur les
captures du site Wix (hero, portrait Mateo, les trois cartes d'offres, la
section Progression). Ceux des bandeaux de pages internes et de la page
Contact sont des suppositions raisonnables et **doivent être relus** une fois
les photos en place — un `alt` qui décrit autre chose que l'image est une
incohérence contenu/balisage (playbook §7).

## Conversion WebP (playbook §5)

Une fois les JPEG en place, générer les variantes WebP et passer les `<img>`
en `<picture>` :

```bash
for f in *.jpg; do cwebp -q 86 "$f" -o "${f%.jpg}.webp"; done
```

## Photos réelles en place (mise à jour du 19 septembre 2026)

Les placeholders ci-dessus ont été remplacés par de vraies photos (sources dans
`images/`), générées en avif / webp / jpg :

| Fichier | Source | Usage |
|---|---|---|
| `hero-home.*` | `hero.jpg` | Hero de l'accueil (2400 px) |
| `foundation-card.*`, `exploration-card.*`, `immersion-card.*` | `DSC00363.jpg`, `exploration1.JPG`, `lifestyle2.jpg` | Cartes de l accueil découpées en shortboard / fish / longboard (ratio 5/12) |
| `foundation-hero.*` | `DSC00359.jpg` | Bandeau Foundation |
| `exploration-hero.*` | `DSC07851.jpg` | Bandeau Exploration |
| `progression.*` | `DSC00251.jpg` | Section Progression de l'accueil (4/5) |
| `progression-hero.*` | `DSC00251.jpg` | Bandeau Signature Progression Week |
| `about-hero.*` | `hero1.jpg` | Bandeau About |
| `philo-1…6.*` | `69E469DB`, `DSC00420`, `6EFE6EB3`, `0769db67`, `DSC00347`, `909D9B06` | Bande de 6 photos « The Philosophy » |
| `story-lifestyle.*`, `why-playa.jpg`, `mateo-portrait.*` | `lifestyle5.jpg`, `playa.png`, `hero1.jpg` | My Story / Why Lean Forward |

**Encore à fournir** : `DSC04901` (hero — `hero.jpg` est utilisé en attendant) et
`DSC00454` (portrait de Mateo pour My Story — la photo actuelle est inchangée).

## Blog (ajouté le 27 septembre 2026)

| Fichier | Source | Usage |
|---|---|---|
| `blog-hero.*` | `hero2.jpg` | Hero de la page /blog |
| `blog-signs-hero.*`, `blog-signs-card.*` | `group5.jpg`, `group4.jpg` | Article « 5 Signs You're Ready for More » |
| `blog-spots-hero.*`, `blog-spots-card.*` | `hero3.jpg`, `group7.jpg` | Article « Best Surf Spots Around Tamarindo » |
| `blog-adventure-hero.*`, `blog-adventure-card.*` | `lifestyle4.jpg`, `lifestyle3.jpg` | Article « Plan a Surf & Nature Adventure Week » |
