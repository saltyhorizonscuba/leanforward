# -*- coding: utf-8 -*-
"""Génère les 6 pages internes (Foundation, Exploration, Immersion,
Signature Progression Week, About, Contact) via build_pages.page().
Le corps de chaque page est le HTML complet et statique : ce fichier ne
sert qu'à garder en-tête et pied de page identiques entre les pages.

Le blog (/blog + 3 articles, ajoutés le 27 septembre 2026) n'est PAS généré
ici : ses pages ont un fil d'Ariane à 3 niveaux (Home > Blog > Article) alors
que build_pages.page()/graph() ne géraient qu'un fil à 2 niveaux (Home >
Page) au moment de l'ajout. Leur HTML est écrit et maintenu directement dans
blog.html/blog-*.html + blog*/index.html — c'est la source de vérité pour ces
4 pages, pas ce script."""
from build_pages import page, BASE, BID

# ------------------------------------------------------------ Foundation
page(
  "surf-coaching-tamarindo",
  "Surf Lessons in Tamarindo, Costa Rica | Lean Forward",
  "Private surf lessons in Tamarindo from $100, semi-private $90 and group coaching $80 per person. 2-hour sessions, 13% taxes included. Board, ocean safety and personal feedback included.",
  "The Foundation",
  [
    {
      "@type": "Service",
      "@id": BASE + "/surf-coaching-tamarindo#service",
      "name": "The Foundation — Private & Small-Group Surf Coaching",
      "serviceType": "Surf lesson",
      "description": "Personalized surf coaching in Tamarindo for beginners and developing surfers. Ocean safety, surf fundamentals, technique coaching and personalized feedback, board included.",
      "url": BASE + "/surf-coaching-tamarindo",
      "provider": {"@id": BID},
      "areaServed": {"@type": "Place", "name": "Tamarindo, Guanacaste, Costa Rica"},
      "offers": [
        {"@type": "Offer", "name": "Private Session — 2 hours", "price": "100", "priceCurrency": "USD", "availability": "https://schema.org/InStock"},
        {"@type": "Offer", "name": "Semi-Private — 2 hours, per person", "price": "90", "priceCurrency": "USD", "availability": "https://schema.org/InStock"},
        {"@type": "Offer", "name": "Group Coaching — 2 hours, per person", "price": "80", "priceCurrency": "USD", "availability": "https://schema.org/InStock"}
      ]
    }
  ],
  u'''
  <section class="hero hero--page">
    <div class="hero__media">
      <picture><source srcset="/assets/img/foundation-hero.avif" type="image/avif"><source srcset="/assets/img/foundation-hero.webp" type="image/webp"><img src="/assets/img/foundation-hero.jpg" alt="Two surfers paddling out into calm blue water at Tamarindo" fetchpriority="high" width="2400" height="1603"></picture>
    </div>
    <div class="wrap hero__inner">
      <p class="eyebrow">The Foundation</p>
      <h1>Private &amp; small-group surf coaching in Tamarindo</h1>
      <p class="hero__tagline">Designed for beginners and developing surfers who want personalized instruction in Tamarindo.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split split--narrow">
      <div class="blob-accent blob-accent--tl blob-accent--sand">
        <h2>What's included</h2>
        <ul class="ticks">
          <li>Ocean safety and surf fundamentals</li>
          <li>Technique coaching</li>
          <li>Board included</li>
          <li>Personalized feedback</li>
          <li>Suitable for all levels</li>
        </ul>
      </div>
      <div>
        <table class="pricing">
          <caption>Pricing</caption>
          <thead>
            <tr><th scope="col">Format</th><th scope="col">Duration</th><th scope="col">Price</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Private session</th><td>2 hours</td><td>$100</td></tr>
            <tr><th scope="row">Semi-private</th><td>2 hours</td><td>$90 per person</td></tr>
            <tr><th scope="row">Group coaching</th><td>2 hours</td><td>$80 per person</td></tr>
          </tbody>
        </table>
        <p class="pricing__note">All prices include the 13% tax.</p>
        <a class="btn btn--primary" href="/contact">Book a session</a>
      </div>
    </div>
  </section>


  <section class="section section--sand">
    <div class="wrap split">
      <div class="blob-accent blob-accent--tr blob-accent--blue">
        <h2>Who it's for</h2>
        <p>The Foundation is the starting point at Lean Forward. It works for two kinds of surfer: someone who has never stood on a board and wants a safe, patient introduction to the ocean, and someone who already catches waves but wants the technique broken down properly instead of guessing.</p>
        <p>Because the format runs from a one-on-one private session up to a group of three or more, the coaching stays personal at every price point. What changes between the formats is how much of the session is direct attention, not how much care goes into it.</p>
      </div>
      <div>
        <h2>Where it leads</h2>
        <p>Once you are catching waves consistently in Tamarindo, <a href="/guided-surf-tours">The Exploration</a> takes you to spots further along the Guanacaste coast, and <a href="/surf-nature-adventures">The Immersion</a> pairs a day of surfing with a half day of exploration.</p>
        <p>For a full itinerary experience, the <a href="/signature-progression-week">Signature Progression Week</a> is the one to look at — a structured roadmap rather than isolated lessons, with video analysis, wave reading sessions and a written plan you keep after the trip.</p>
      </div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="wrap">
      <h2>Ready when you are</h2>
      <p class="lede">Tell us your level, your dates and how many of you there are — we'll build the session around it.</p>
      <a class="btn btn--primary" href="/contact">Contact us</a>
    </div>
  </section>
''',
  "found")

# ----------------------------------------------------------- Exploration
page(
  "guided-surf-tours",
  "Guided Surf Tours in Guanacaste, Costa Rica | Lean Forward",
  "Three-hour guided surf tours beyond Tamarindo from $130 per person. Playa Avellanas, Playa Grande, Guiones and Marbella, chosen on the day.",
  "The Exploration",
  [
    {
      "@type": "Service",
      "@id": BASE + "/guided-surf-tours#service",
      "name": "The Exploration — Guided Surf Tours",
      "serviceType": "Guided surf tour",
      "description": "Three-hour guided surf experiences for intermediate surfers at spots beyond Tamarindo, with spot selection based on conditions, board, snacks and hydration.",
      "url": BASE + "/guided-surf-tours",
      "provider": {"@id": BID},
      "areaServed": {"@type": "Place", "name": "Guanacaste, Costa Rica"},
      "offers": {
        "@type": "Offer",
        "price": "130",
        "priceCurrency": "USD",
        "description": "Starting price per person; varies depending on destination and group size.",
        "availability": "https://schema.org/InStock"
      }
    }
  ],
  u'''
  <section class="hero hero--page">
    <div class="hero__media">
      <picture><source srcset="/assets/img/exploration-hero.avif" type="image/avif"><source srcset="/assets/img/exploration-hero.webp" type="image/webp"><img src="/assets/img/exploration-hero.jpg" alt="Surfboards laid out on the ground beside a car at a Guanacaste surf spot" fetchpriority="high" width="2400" height="1080"></picture>
    </div>
    <div class="wrap hero__inner">
      <p class="eyebrow">The Exploration</p>
      <h1>Guided surf tours beyond Tamarindo</h1>
      <p class="hero__tagline">For intermediate surfers ready to discover the best waves on the Guanacaste coast.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split split--narrow">
      <div class="blob-accent blob-accent--tl blob-accent--sand">
        <h2>Spots we explore</h2>
        <ul class="ticks">
          <li>Playa Avellanas</li>
          <li>Playa Grande</li>
          <li>Guiones</li>
          <li>Marbella</li>
        </ul>
        <p>The destination is chosen on the day, based on swell, wind and tide.</p>
      </div>
      <div>
        <h2>What's included</h2>
        <ul class="ticks">
          <li>3-hour guided surf experience</li>
          <li>Transportation guidance</li>
          <li>Surf spot selection based on conditions</li>
          <li>Board included</li>
          <li>Snacks &amp; hydration</li>
        </ul>
        <p>Photo, video and drone packages are available at an extra, optional price.</p>
        <p class="card__price">Starting from $130 per person</p>
        <p>Pricing varies depending on destination and group size.</p>
        <a class="btn btn--primary" href="/contact">Plan a tour</a>
      </div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="wrap split">
      <div class="blob-accent blob-accent--tr blob-accent--blue">
        <h2>Why the spot changes</h2>
        <p>Guanacaste has a lot of coastline and no two beaches work on the same conditions. Rather than committing to a destination in advance, the spot is picked on the day so the group surfs where the swell, wind and tide actually line up.</p>
        <p>That is the difference between a surf tour and a surf transfer: the point is not the drive, it is arriving somewhere that is working.</p>
      </div>
      <div>
        <h2>Before you book</h2>
        <p>The Exploration assumes you can already catch and ride green waves independently and feel comfortable managing yourself in the water.</p>
        <p>You don't need to be an expert. Mateo stays in the water with you throughout the session, offering in-water coaching, guidance and safety support to help you progress. The goal is to explore different breaks around the coast, like Playa Grande or Avellanas, while choosing conditions that match your level and comfort.</p>
        <p>If you're still building your foundation, start with <a href="/surf-coaching-tamarindo">The Foundation</a> in Tamarindo. The two can also work beautifully together during the same trip.</p>
      </div>
    </div>
  </section>
''',
  "expl")

# ------------------------------------------------------------- Immersion
page(
  "surf-nature-adventures",
  "Surf &amp; Nature Adventures in Costa Rica | Lean Forward",
  "Private, custom-priced surf and nature experiences in Guanacaste, Costa Rica: surf coaching, waterfalls, volcanoes, jungle and local experiences. From $230 per person.",
  "The Immersion",
  [
    {
      "@type": "Service",
      "@id": BASE + "/surf-nature-adventures#service",
      "name": "The Immersion — Surf & Nature Adventures",
      "serviceType": "Surf and nature adventure",
      "description": "Custom Costa Rican itineraries combining personalized surf coaching with waterfalls, volcanic landscapes and authentic local experiences.",
      "url": BASE + "/surf-nature-adventures",
      "provider": {"@id": BID},
      "areaServed": {"@type": "Place", "name": "Costa Rica"},
      "offers": {
        "@type": "Offer",
        "name": "Private custom surf and nature experience, per person",
        "price": "230",
        "priceCurrency": "USD",
        "description": "Starting price per person. Custom-priced based on group size, surf sessions, destination, activities and transportation; a personalized quote is provided before booking.",
        "availability": "https://schema.org/InStock"
      }
    }
  ],
  u'''
  <section class="hero hero--page">
    <div class="hero__media">
      <picture><source srcset="/assets/img/immersion-hero.avif" type="image/avif"><source srcset="/assets/img/immersion-hero.webp" type="image/webp"><img src="/assets/img/immersion-hero.jpg" alt="A surfboard held up against palm trees and blue sky in Guanacaste, Costa Rica" fetchpriority="high" width="1200" height="1600"></picture>
    </div>
    <div class="wrap hero__inner">
      <p class="eyebrow">The Immersion</p>
      <h1>Surf Beyond the Waves</h1>
      <p class="hero__tagline">Private surf and nature experiences in Guanacaste.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="blob-accent blob-accent--tl blob-accent--sand">
        <p class="eyebrow">More than a surf trip</p>
        <h2>More than surfing</h2>
        <p class="lede">The Immersion is completely tailored to your group.</p>
        <p>Choose how you want to spend your time:</p>
      </div>
      <div class="triptych">
        <div class="triptych__col">
          <h3>Surf</h3>
          <p>Private coaching adapted to your level and goals.</p>
        </div>
        <div class="triptych__col">
          <h3>Adventure</h3>
          <p>Waterfalls, volcanoes, jungle, kayaking, hidden beaches, and local experiences.</p>
        </div>
        <div class="triptych__col">
          <h3>Mix it up</h3>
          <p>One surf day + one adventure, several days of surfing + an adventure, or anything in between.</p>
        </div>
      </div>
      <p><strong>No fixed itinerary. We build it around you.</strong></p>
    </div>
  </section>

  <section class="section section--sand">
    <div class="wrap">
      <div class="blob-accent blob-accent--tr blob-accent--blue">
        <h2>Your experience, your way</h2>
        <p>For example:</p>
        <ul class="examples">
          <li><strong>1 day</strong><span>Surf + coastal adventure</span></li>
          <li><strong>2 days</strong><span>Surf + Surf + Waterfall</span></li>
          <li><strong>3+ days</strong><span>A mix of surf days and custom adventures</span></li>
        </ul>
        <p>Or simply book an Adventure Day without surfing.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split split--stretch">
      <div class="callout">
        <h2>Pricing</h2>
        <p class="card__price">From $230 per person</p>
        <p>Every experience is private and custom-priced based on:</p>
        <ul class="ticks">
          <li>Group size</li>
          <li>Surf sessions</li>
          <li>Destination</li>
          <li>Activities</li>
          <li>Transportation</li>
        </ul>
        <p>We'll create your itinerary and provide a personalized quote before booking.</p>
        <a class="btn btn--primary" href="/contact">Plan your experience &rarr;</a>
      </div>
      <div class="callout">
        <h2>Ready to explore?</h2>
        <p class="lede">Tell us what you're looking for, how many people are coming, and how you want to spend your time.</p>
        <p>We'll take it from there.</p>
        <a class="btn btn--primary" href="/contact">Start planning &rarr;</a>
      </div>
    </div>
  </section>
''',
  "imm")

# -------------------------------------------- Signature Progression Week
page(
  "signature-progression-week",
  "Signature Progression Week | Structured Surf Coaching in Tamarindo | Lean Forward",
  "The Signature Progression Week is a special multi-day package from Lean Forward: daily surf coaching, video analysis, wave reading and a personalized progression plan in Tamarindo, Costa Rica.",
  "Signature Progression Week",
  [
    {
      "@type": "Service",
      "@id": BASE + "/signature-progression-week#service",
      "name": "Signature Progression Week",
      "serviceType": "Multi-day surf coaching program",
      "description": "A structured multi-day surf coaching package in Tamarindo, Costa Rica, combining daily coaching, video analysis, wave reading and a personalized progression plan.",
      "url": BASE + "/signature-progression-week",
      "provider": {"@id": BID},
      "areaServed": {"@type": "Place", "name": "Tamarindo, Guanacaste, Costa Rica"}
    }
  ],
  u'''
  <section class="hero hero--page">
    <div class="hero__media">
      <picture><source srcset="/assets/img/progression-hero.avif" type="image/avif"><source srcset="/assets/img/progression-hero.webp" type="image/webp"><img src="/assets/img/progression-hero.jpg" alt="Two surfers riding a long green wave at Tamarindo, seen past a coach in the foreground" fetchpriority="high" width="2400" height="1080"></picture>
    </div>
    <div class="wrap hero__inner">
      <p class="eyebrow">Signature Progression Week</p>
      <h1>A structured roadmap, not isolated lessons</h1>
      <p class="hero__tagline">A special package you can book all together — for surfers who want real progress in a single week.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="blob-accent blob-accent--tl blob-accent--sand">
        <h2>Made for a full week of progress</h2>
        <p>For surfers staying in Costa Rica who want to make meaningful progress over several days or weeks. Designed for travelers renting villas, Airbnbs, or spending extended time in Tamarindo.</p>
        <p>Instead of booking lessons one by one, you book the whole week together — with a plan that connects each session to the next.</p>
        <p>Understand what to practice, why it matters, and how to continue improving long after your trip ends.</p>
        <a class="btn btn--primary" href="/contact">Request your week</a>
      </div>
      <div>
        <h2>Available elements</h2>
        <ul class="ticks ticks--2">
          <li>Daily surf coaching</li>
          <li>Guided surf tours</li>
          <li>Video analysis</li>
          <li>Technical breakdowns</li>
          <li>Surf theory seminars</li>
          <li>Wave reading sessions</li>
          <li>Mobility &amp; recovery guidance</li>
          <li>Yoga sessions</li>
          <li>Massage therapy</li>
          <li>Photo &amp; video packages</li>
          <li>Personalized progression plan</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="wrap split">
      <div class="blob-accent blob-accent--tr blob-accent--blue">
        <h2>How it fits with the rest</h2>
        <p><a href="/surf-coaching-tamarindo">The Foundation</a> covers the technique work in Tamarindo, <a href="/guided-surf-tours">The Exploration</a> takes you to other breaks along the coast, and <a href="/surf-nature-adventures">The Immersion</a> mixes surf with Costa Rican adventure. The Signature Progression Week ties them into a single structured plan.</p>
      </div>
      <div>
        <h2>Ready when you are</h2>
        <p class="lede">Tell us your level, your dates and how many of you there are — we'll build the week around it. Pricing is provided on request.</p>
        <a class="btn btn--primary" href="/contact">Contact us</a>
      </div>
    </div>
  </section>
''',
  "prog")

# ----------------------------------------------------------------- About
page(
  "about",
  "About Mateo | Lean Forward Surf Coaching in Tamarindo",
  "Meet Mateo, founder and surf coach at Lean Forward in Tamarindo, Costa Rica: his story, the vision behind Lean Forward and what to expect from every session.",
  "About",
  [
    {
      "@type": "Person",
      "@id": BASE + "/#mateo",
      "name": "Mateo",
      "jobTitle": "Founder & Surf Coach",
      "worksFor": {"@id": BID},
      "url": BASE + "/about"
    }
  ],
  u'''
  <section class="hero hero--page">
    <div class="hero__media">
      <picture><source srcset="/assets/img/about-hero.avif" type="image/avif"><source srcset="/assets/img/about-hero.webp" type="image/webp"><img src="/assets/img/about-hero.jpg" alt="Mateo sitting on the sand at Tamarindo with his board, looking out at the surf" fetchpriority="high" width="2400" height="1080"></picture>
    </div>
    <div class="wrap hero__inner">
      <p class="eyebrow">About</p>
      <h1>Meet Mateo</h1>
      <p class="hero__tagline">Founder and surf coach at Lean Forward, Tamarindo, Guanacaste.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split split--narrow">
      <div class="blob-accent blob-accent--tl blob-accent--sand">
        <h2>My story</h2>
        <p>My name is Mateo. I moved from Colombia to Costa Rica when I was 13 years old. At the time, I had never surfed, didn't even know how to swim, and knew absolutely nothing about the ocean or surfboards. One day, while walking along Tamarindo Beach, I saw people surfing and was instantly captivated.</p>
        <p>Surfing taught me to respect the ocean, appreciate its beauty, and understand its constantly changing nature. More importantly, it showed me the power of sharing a passion with others — and I now strive to pass that passion on to every person I have the privilege to teach.</p>
      </div>
      <div>
        <p>Lean Forward was born from that purpose. My goal is not simply to teach people how to surf. It is to help them build confidence, connect with the ocean, discover what they are capable of, and experience the incredible feeling that comes from riding a wave.</p>
        <p>Because sometimes, one wave can change much more than your day. It can change your life.</p>
        <p><strong>Lean Forward — Smooth Connection.</strong></p>
        <a class="btn btn--primary" href="index.html#story">Read the full story</a>
      </div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="wrap split">
      <div class="blob-accent blob-accent--tr blob-accent--blue">
        <h2>The vision behind Lean Forward</h2>
        <p class="lede">To create ocean experiences that inspire growth, connection and progress.</p>
        <p>Through personalized surf coaching, guided adventures, and a deep respect for nature, we help people move beyond simply learning to surf. Our purpose is to create space for confidence, discovery, and meaningful experiences in and out of the water.</p>
      </div>
      <div>
        <h2>What to expect</h2>
        <ul class="ticks">
          <li>Personalized coaching: sessions tailored to your unique goals and current skill level</li>
          <li>Progress-focused: a structured approach built to see real results in every wave</li>
          <li>Video feedback: detailed technical analysis to refine your form and technique</li>
          <li>Nature-centered: the ocean, coastline, and hidden beauty of Guanacaste beyond the typical tourist path</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <h2>Ready to lean forward?</h2>
      <p class="lede">Tell us your level, your dates and how many of you there are — we'll build the session around it.</p>
      <a class="btn btn--primary" href="/contact">Contact us</a>
    </div>
  </section>
''',
  "about")

# --------------------------------------------------------------- Contact
page(
  "contact",
  "Contact Lean Forward — Book Surf Coaching in Tamarindo",
  "Plan surf coaching, a guided tour or a custom program in Tamarindo with Mateo. WhatsApp +506 7244-6227 or contact.leanforward@gmail.com.",
  "Contact",
  [
    {
      "@type": "ContactPage",
      "@id": BASE + "/contact#contactpage",
      "url": BASE + "/contact",
      "mainEntity": {"@id": BID}
    }
  ],
  u'''
  <section class="section" style="padding-top:2rem">
    <div class="wrap">
      <p class="eyebrow">Contact</p>
      <h1>Ready to lean forward?</h1>
      <p class="lede">Whether you're planning your first surf lesson, looking to explore the best waves in Guanacaste, or interested in a personalized coaching program, I'd love to hear about your goals and help create the right experience for you.</p>
      <p class="lede">Every experience is tailored to your level, schedule, and interests. Get in touch and let's start planning your time in Costa Rica.</p>
    </div>
  </section>

  <section class="section section--sky">
    <div class="wrap contact-grid">
      <div>
        <h2>Let's plan your experience</h2>
        <p>Tell us a little about yourself and we'll help create the perfect experience based on your goals, skill level, and time in Costa Rica.</p>
        <dl class="contact-list">
          <div>
            <dt>WhatsApp</dt>
            <dd style="margin:0"><a href="https://wa.me/50672446227">+506 7244-6227</a></dd>
          </div>
          <div>
            <dt>Email</dt>
            <dd style="margin:0"><a href="mailto:contact.leanforward@gmail.com">contact.leanforward@gmail.com</a></dd>
          </div>
          <div>
            <dt>Instagram</dt>
            <dd style="margin:0"><a href="https://www.instagram.com/leanforwardsurf/" rel="me noopener">@leanforwardsurf</a></dd>
          </div>
          <div>
            <dt>Hours</dt>
            <dd style="margin:0">Available daily by appointment</dd>
          </div>
        </dl>
        <p style="margin-top:2rem"><strong>Response time:</strong> usually within a few hours.</p>
        <a class="btn btn--primary" href="https://wa.me/50672446227">Message on WhatsApp</a>
      </div>
      <div>
        <h2>What to include in your message</h2>
        <ul class="ticks">
          <li>Your surfing level</li>
          <li>Number of surfers</li>
          <li>Preferred dates</li>
          <li>Which experience interests you</li>
          <li>Any questions or special requests</li>
        </ul>
        <figure style="margin:2.5rem 0 0">
          <picture><source srcset="/assets/img/mateo-contact.avif" type="image/avif"><source srcset="/assets/img/mateo-contact.webp" type="image/webp"><img src="/assets/img/mateo-contact.jpg" alt="Mateo smiling on the beach at Tamarindo, Guanacaste" loading="lazy" style="border-radius:4px" width="960" height="1200"></picture>
          <figcaption style="margin-top:.75rem;font-family:var(--serif);color:var(--ink)">Mateo — Founder &amp; Surf Coach<br><span style="font-family:var(--sans);font-size:.95rem;color:var(--ink-mute)">Tamarindo, Guanacaste, Costa Rica</span></figcaption>
        </figure>
      </div>
    </div>
  </section>
''',
  "cont")

