# Lean Forward — Contexte projet

> Source de vérité factuelle du projet (playbook §8). Toute info citée dans le HTML,
> les meta ou le JSON-LD doit correspondre à ce fichier.

## Identité business

- **Nom** : Lean Forward (aussi cité par un client comme « Lean Forward Surf Academy »)
- **Baseline** : Surf Coaching Designed for Real Progress
- **Signature** : Lean Forward — Smooth Connection.
- **Fondateur / coach** : Mateo — né en Colombie, installé au Costa Rica à 13 ans
- **Localisation** : Tamarindo, Guanacaste, Costa Rica
- **Langue du site** : anglais uniquement (décision validée)

## Contact (vérifié sur la page Contact Wix)

- WhatsApp : +506 7244-6227
- Email : contact.leanforward@gmail.com
- Instagram : https://www.instagram.com/leanforwardsurf/ (@leanforwardsurf)
- Facebook : https://www.facebook.com/profile.php?id=61591034983027
- Horaires : Available daily by appointment
- Délai de réponse annoncé : usually within a few hours

## Offres et tarifs (chiffres réels — ne jamais arrondir ni inventer)

### The Foundation — Private & Small-Group Surf Coaching
Pour débutants et surfeurs en progression, à Tamarindo.
- Private Session, 2 h — **$100**
- Semi-Private, 2 h — **$90 / personne**
- Group Coaching, 2 h — **$80 / personne**
- Taxe de 13 % incluse dans les prix (mise à jour du 19 sept. 2026)
- Inclus : ocean safety and surf fundamentals, technique coaching, board included,
  personalized feedback, suitable for all levels

### The Exploration — Guided Surf Tours
Pour surfeurs intermédiaires, au-delà de Tamarindo.
- **À partir de $130 / personne** (varie selon destination et taille du groupe)
- Spots : Playa Avellanas, Playa Grande, Guiones, Marbella (Playa Negra retiré)
- Packs photo / vidéo / drone disponibles en option, à prix supplémentaire
- Inclus : 3-hour guided surf experience, transportation guidance, surf spot selection
  based on conditions, board included, snacks & hydration

### The Immersion — Surf & Nature Adventures
Surf + aventures Costa Rica (cascades, paysages volcaniques, expériences locales).
- **À partir de $230 / personne**, expérience privée au prix sur mesure selon :
  taille du groupe, sessions de surf, destination, activités, transport
  (devis personnalisé avant réservation)
- Trois axes : Surf / Adventure / Mix it up — aucun itinéraire fixe
- Exemples : 1 jour (surf + aventure côtière), 2 jours (surf + surf + cascade),
  3+ jours (mélange), ou une journée aventure sans surf
- Ancienne grille Half-Day $230 / Full-Day $350 / Multi-Day supprimée (19 sept. 2026)
- Inclus : personalized surf coaching, local guide and trip planning, transportation
  coordination, custom itinerary design

### Signature Progression Week (ex-« The Progression Program »)
Programme structuré sur plusieurs jours/semaines, pour voyageurs en villa/Airbnb.
Éléments disponibles : daily surf coaching, guided surf tours, video analysis,
technical breakdowns, surf theory seminars, wave reading sessions, mobility & recovery
guidance, yoga sessions, massage therapy, photo & video packages, personalized
progression plan.
Forfait à part, réservable en bloc, avec sa propre page (`/signature-progression-week`)
et une entrée de menu « Progression Week ». Pas de tarif public.
Texte définitif de la page : à fournir par le client (texte actuel repris de la home).

## Différenciateurs (section « Why Lean Forward »)

- Personalized Coaching — sessions tailored to your unique goals and current skill level
- Progress-Focused — a structured approach built to see real results in every wave
- Video Feedback — detailed technical analysis to refine your form and technique
- Nature-Centered — the ocean, coastline, and hidden beauty of Guanacaste beyond the
  typical tourist path

## Témoignages (verbatim — ne jamais modifier ni traduire, playbook §2 et §7)

4 avis réels, nominatifs : **Arbour**, **Dan Martin**, **Kristin Nicole Martin**, **Kelly**.
Textes complets conservés dans `content/testimonials.md`.

⚠️ Deux d'entre eux mentionnent explicitement « 5 stars » / « 5 Stars » dans leur texte.
Cela autorise un `Review.reviewRating` = 5 pour ces deux avis précis.
**Interdit** en revanche de publier un `aggregateRating` tant qu'on n'a pas le vrai
total d'avis et la vraie moyenne depuis Google Business Profile (playbook §2).

## Nouvelle arborescence d'URLs (remplace les slugs Wix /blank, /blank-1…)

| Ancienne URL Wix | Nouvelle URL | Titre affiché |
|---|---|---|
| `/lean-forward` | `/` | Home |
| `/lean-forward/blank` | `/surf-coaching-tamarindo` | The Foundation |
| `/lean-forward/blank-1` | `/guided-surf-tours` | The Exploration |
| `/lean-forward/blank-2` | `/surf-nature-adventures` | The Immersion |
| `/lean-forward/blank-3` | `/contact` | Contact Us |
| (nouvelle page) | `/signature-progression-week` | Signature Progression Week |
| (nouvelle page) | `/about` | About |
| (nouvelle page) | `/blog` | Blog |
| (nouvelle page) | `/blog-signs-ready-for-more` | 5 Signs You're Ready to Move Beyond Beginner Surf Lessons |
| (nouvelle page) | `/blog-best-surf-spots-tamarindo` | A Local's Guide to the Best Surf Spots Around Tamarindo |
| (nouvelle page) | `/blog-plan-surf-nature-week` | How to Plan a Surf & Nature Adventure Week in Costa Rica |

Aucune redirection 301 nécessaire : les anciennes URLs sont des slugs Wix par défaut
sans valeur SEO acquise, sur un sous-domaine `.wixsite.com` qui ne sera pas conservé.

## Audit du site Wix d'origine (20 août 2026)

| Point | État constaté |
|---|---|
| Slugs | `/blank`, `/blank-1`, `/blank-2`, `/blank-3` |
| Meta description | absente (accueil) |
| JSON-LD | aucun, sur tout le site |
| H1 | 2 sur l'accueil (« Lean Forward », « What Clients Say About Lean Forward ») |
| Images | 15 sur l'accueil, dont 8 sans `alt` |
| `<title>` accueil | « Home \| Lean Forward » — sans mot-clé ni localisation |
| OpenGraph | `og:image` et `og:description` absents |
| Domaine | sous-domaine `freyfilmscr.wixsite.com` |

## Conventions techniques retenues

- HTML/CSS/JS statique, sans étape de build
- Convention d'URL : sans extension `.html` (dossiers + `index.html`)
- Tout le contenu textuel dans le HTML brut (playbook §1)
- `?v=N` sur CSS/JS pour le cache-bust (playbook §11)
- Images : WebP + fallback JPEG via `<picture>`, variante card ~900px,
  hero ~2000-2400px, contenu ~1500px, qualité 84-88 (playbook §5 et §12)
