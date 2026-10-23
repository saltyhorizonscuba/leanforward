# -*- coding: utf-8 -*-
"""Contrôle de conformité au PROJECT_PLAYBOOK.md.
Analyse le HTML brut sur disque — donc exactement ce qu'un crawler
sans JavaScript reçoit (playbook §1)."""
import io, json, os, re, sys
from html.parser import HTMLParser

PAGES = ["index.html", "surf-coaching-tamarindo/index.html",
         "guided-surf-tours/index.html", "surf-nature-adventures/index.html",
         "signature-progression-week/index.html", "about/index.html",
         "contact/index.html", "blog/index.html",
         "blog-signs-ready-for-more/index.html",
         "blog-best-surf-spots-tamarindo/index.html",
         "blog-plan-surf-nature-week/index.html"]

problems, notes = [], []


class Scan(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.h1 = []
        self.imgs = []
        self.ld = []
        self.meta = {}
        self.links = []
        self.interactive = []
        self._grab = None
        self._buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self._grab = "h1"; self._buf = []
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._grab = "ld"; self._buf = []
        elif tag == "meta":
            k = a.get("name") or a.get("property")
            if k: self.meta[k] = a.get("content", "")
        elif tag == "link" and a.get("rel") == "canonical":
            self.meta["canonical"] = a.get("href", "")
        elif tag == "title":
            self._grab = "title"; self._buf = []
        elif tag == "a":
            self.links.append(a)
            if not a.get("aria-label"):
                self.interactive.append(("a", a))
        elif tag == "button":
            self.interactive.append(("button", a))

    def handle_data(self, d):
        if self._grab: self._buf.append(d)

    def handle_endtag(self, tag):
        if self._grab == "h1" and tag == "h1":
            self.h1.append("".join(self._buf).strip()); self._grab = None
        elif self._grab == "ld" and tag == "script":
            self.ld.append("".join(self._buf)); self._grab = None
        elif self._grab == "title" and tag == "title":
            self.meta["title"] = "".join(self._buf).strip(); self._grab = None


print("=" * 68)
print("VÉRIFICATION — conformité PROJECT_PLAYBOOK.md")
print("=" * 68)

business_ids = set()
all_internal = set()

for path in PAGES:
    if not os.path.exists(path):
        problems.append("page manquante : " + path); continue
    raw = io.open(path, encoding="utf-8").read()
    s = Scan(); s.feed(raw)
    print("\n--- " + path)

    # §6 : un seul H1
    if len(s.h1) != 1:
        problems.append("%s : %d <h1> (attendu 1)" % (path, len(s.h1)))
    else:
        print("  h1 ............ OK  « %s »" % s.h1[0][:58])

    # title / description
    t = s.meta.get("title", "")
    d = s.meta.get("description", "")
    if not (10 < len(t) <= 65):
        notes.append("%s : <title> de %d caractères (idéal 50-60)" % (path, len(t)))
    if not (110 <= len(d) <= 165):
        notes.append("%s : meta description de %d caractères (idéal 120-160)" % (path, len(d)))
    print("  title ......... %d car. | description %d car." % (len(t), len(d)))

    # §4 : robots + canonical explicites
    for k in ("robots", "canonical"):
        if not s.meta.get(k):
            problems.append("%s : %s manquant" % (path, k))

    # OpenGraph
    for k in ("og:title", "og:description", "og:image", "og:url", "og:type"):
        if not s.meta.get(k):
            problems.append("%s : %s manquant" % (path, k))

    # §5 §6 : alt + dimensions sur chaque image
    noalt = [i for i in s.imgs if i.get("alt") is None]
    nodim = [i for i in s.imgs if not (i.get("width") and i.get("height"))]
    if noalt:
        problems.append("%s : %d <img> sans attribut alt" % (path, len(noalt)))
    if nodim:
        problems.append("%s : %d <img> sans width/height (risque de CLS)"
                        % (path, len(nodim)))
    print("  images ........ %d | sans alt %d | sans width/height %d"
          % (len(s.imgs), len(noalt), len(nodim)))

    # §2 : JSON-LD valide, une seule entité business
    if not s.ld:
        problems.append("%s : aucun JSON-LD" % path)
    for blob in s.ld:
        try:
            data = json.loads(blob)
        except Exception as e:
            problems.append("%s : JSON-LD invalide — %s" % (path, e)); continue
        nodes = data.get("@graph", [data])
        types = []
        for n in nodes:
            ty = n.get("@type")
            types.append(",".join(ty) if isinstance(ty, list) else ty)
            if "LocalBusiness" in str(ty):
                business_ids.add(n.get("@id"))
            # §2 : jamais d'aggregateRating fabriqué
            if "aggregateRating" in json.dumps(n):
                problems.append("%s : aggregateRating présent — vérifier "
                                "qu'il vient d'une vraie source" % path)
        print("  json-ld ....... OK  %d nœuds : %s" % (len(nodes), ", ".join(types)))

    # §1 : le contenu doit exister dans le HTML brut
    body = raw.split("<main", 1)[-1].split("</main>", 1)[0]
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    if words < 120:
        problems.append("%s : seulement %d mots dans <main> du HTML brut" % (path, words))
    print("  contenu brut .. %d mots dans <main> (sans JS)" % words)

    # liens internes
    for a in s.links:
        h = a.get("href", "")
        if h.startswith("/") and not h.startswith("//"):
            all_internal.add(h.split("#")[0])

    # §6 : nom accessible sur les boutons
    for tag, a in s.interactive:
        if tag == "button" and not (a.get("aria-label") or a.get("aria-labelledby")):
            problems.append("%s : <button> sans nom accessible" % path)

# §2 : une seule entité business pour tout le site
print("\n--- entité business")
if len(business_ids) == 1:
    print("  OK  un seul @id référencé partout : %s" % list(business_ids)[0])
else:
    problems.append("plusieurs @id business : %s" % business_ids)

# §4 : cohérence sitemap / pages réelles
print("\n--- sitemap & liens")
sm = io.open("sitemap.xml", encoding="utf-8").read()
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
expected = {"/", "/surf-coaching-tamarindo", "/guided-surf-tours",
            "/surf-nature-adventures", "/signature-progression-week",
            "/about", "/contact", "/blog", "/blog-signs-ready-for-more",
            "/blog-best-surf-spots-tamarindo", "/blog-plan-surf-nature-week"}
got = set(re.sub(r"^https://[^/]+", "", l) or "/" for l in locs)
if got != expected:
    problems.append("sitemap incohérent : %s" % (got ^ expected))
else:
    print("  sitemap ....... OK  %d URLs, toutes existantes" % len(locs))

# liens internes morts
dead = []
for h in sorted(all_internal):
    if h in ("/",):
        target = "index.html"
    elif h.startswith("/css/") or h.startswith("/js/") or h.startswith("/assets/"):
        continue
    else:
        target = h.strip("/") + "/index.html"
    if not os.path.exists(target):
        dead.append(h)
if dead:
    problems.append("liens internes morts : %s" % dead)
else:
    print("  liens internes  OK  %d cibles, aucune morte" % len(all_internal))

# §3 : llms.txt — chaque URL listée doit exister
lt = io.open("llms.txt", encoding="utf-8").read()
for u in re.findall(r"\]\((https://[^)]+)\)", lt):
    p = re.sub(r"^https://[^/]+", "", u)
    tgt = "index.html" if p == "/" else p.strip("/") + "/index.html"
    if not os.path.exists(tgt):
        problems.append("llms.txt pointe vers une page inexistante : %s" % u)
print("  llms.txt ...... OK  toutes les URLs listées existent")

# §3 : robots.txt autorise les bots IA
rb = io.open("robots.txt", encoding="utf-8").read()
for bot in ["GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended"]:
    if bot not in rb:
        problems.append("robots.txt : %s absent" % bot)
print("  robots.txt .... OK  bots IA explicitement autorisés")

print("\n" + "=" * 68)
if problems:
    print("PROBLÈMES (%d)" % len(problems))
    for p in problems: print("  ✗ " + p)
else:
    print("Aucun problème bloquant.")
if notes:
    print("\nÀ AFFINER (%d)" % len(notes))
    for n in notes: print("  · " + n)
print("=" * 68)
sys.exit(1 if problems else 0)
