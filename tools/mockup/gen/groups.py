"""The blog's two groups, Vida and Tech, shared by the pt and en generators.

Tech stays hidden on the real site until the first tech post is published and
it is switched on in the admin. The mockup shows both states with a switch
(tech-on / tech-off); tech-on is the default so the new layout is what you see.
"""
from html import escape as e
from tech_data import GROUPS, posts as tech_posts, cats as tech_cats, shot

T = {
    "pt": dict(loc="br", latest="Mais recente", read="Ler agora", see_all="Ver todos", everything="Tudo", all="Todos",
               state="Seção Tech:", on="Visível", off="Oculta", legend="Seção Tech no mockup", groups="Grupos do blog",
               from_blog="Do blog", browse="Folhear todos os posts",
               home_note="A seção Tech fica oculta até o primeiro post tech ser publicado e ela ser ligada no admin. Use a chave acima para ver a home com e sem ela. Os posts tech são fictícios, só para validar o layout.",
               blog_note="Com a seção Tech oculta, o blog fica como hoje: sem o seletor de grupos e sem as categorias tech. Os posts tech são fictícios.",
               group_note="O seletor no topo troca entre Tudo, Vida e Tech, e os filtros mostram só as categorias do grupo.",
               stories=lambda n: f"{n} histórias coladas aqui desde 2015."),
    "en": dict(loc="en", latest="Latest", read="Read it now", see_all="See all", everything="All", all="All",
               state="Tech section:", on="Visible", off="Hidden", legend="Tech section in the mockup", groups="Blog groups",
               from_blog="From the blog", browse="Browse all posts",
               home_note="The Tech section stays hidden until the first tech post is published and it is switched on in the admin. Use the switch above to see the home with and without it. The tech posts are made up, just to validate the layout.",
               blog_note="With the Tech section hidden, the blog stays as it is today: no group switch and no tech categories. The tech posts are made up.",
               group_note="The switch at the top moves between All, Life and Tech, and the filters only show that group's categories.",
               stories=lambda n: f"{n} stories pinned here since 2015."),
}
ARROW = '<svg aria-hidden="true"><use href="#icon-arrow-right"/></svg>'


def obj(name):
    return f'<svg aria-hidden="true"><use href="#obj-{name}"/></svg>'


def states(lang, floating=False):
    t = T[lang]
    cls = "mockup-states mockup-states--floating" if floating else "mockup-states"
    style = "" if floating else ' style="margin-block: var(--space-xl) 0"'
    return (f'<fieldset class="{cls}"{style}><legend class="visually-hidden">{t["legend"]}</legend><span>{t["state"]}</span>'
            f'<label><input type="radio" name="tech-state" value="tech-on" checked>{t["on"]}</label>'
            f'<label><input type="radio" name="tech-state" value="tech-off">{t["off"]}</label></fieldset>')


def featured(lang, root, p, card, tilt, heading="h3"):
    t = T[lang]
    href = f'{root}{p["path"].lstrip("/")}'
    return f'''<div class="featured-entry blog-band__featured">
          {card}
          <div class="sticky-note featured-entry__note" style="--r:{tilt}">
            <span class="sticky-note__title">{t["latest"]}</span>
            <{heading} class="featured-entry__title"><a href="{href}">{e(p["title"])}</a></{heading}>
            <p>{e(p["excerpt"])}</p>
            <a class="featured-entry__more" href="{href}">{t["read"]} {ARROW}</a>
          </div>
        </div>'''


def group_head(lang, root, key):
    t = T[lang]
    name, slug, sticker, lead = GROUPS[lang][key]
    return (f'<header class="group-head"><span class="sticker" style="--r:{"-6deg" if key == "vida" else "5deg"}">{obj(sticker)}</span>'
            f'<div><h2 class="group-head__title" id="group-{key}-title">{name}</h2><p class="group-head__lead">{lead}</p></div>'
            f'<a class="section-heading__link" href="{root}{t["loc"]}/{slug}/">{t["see_all"]} {ARROW}</a></header>')


def home_section(lang, root, vida, polaroid, sdate):
    """The home's blog area: two bands with Tech on, the single Vida list with it off."""
    t = T[lang]
    tech = tech_posts(lang)
    vida_feat = featured(lang, root, vida[0], polaroid(vida[0], root, lazy=False, extra_cls="polaroid--wide featured-entry__photo"), "3deg")
    vida_wall = "".join(polaroid(p, root) for p in vida[1:5])
    tech_feat = featured(lang, root, tech[0], shot(tech[0], root, sdate, lang, "polaroid--wide featured-entry__photo"), "-2.5deg")
    tech_wall = "".join(shot(p, root, sdate, lang) for p in tech[1:5])
    return f'''<div class="container mockup-stateful">
        {states(lang)}
        <section class="blog-band" aria-labelledby="group-vida-title" data-state="tech-on">
          {group_head(lang, root, "vida")}
          {vida_feat}
          <div class="wall wall--four">{vida_wall}</div>
        </section>
        <section class="blog-band blog-band--tech" aria-labelledby="group-tech-title" data-state="tech-on">
          {group_head(lang, root, "tech")}
          {tech_feat}
          <div class="wall wall--four">{tech_wall}</div>
        </section>
        <section class="blog-band" aria-labelledby="blog-title" data-state="tech-off">
          <div class="board-title" style="margin-block-start: 0">
            <span class="sticker" style="--r:-6deg">{obj("plane")}</span>
            <h2 id="blog-title">{t["from_blog"]}</h2>
            <a class="section-heading__link" href="{root}{t["loc"]}/blog.html">{t["browse"]} {ARROW}</a>
          </div>
          {vida_feat}
          <div class="wall wall--four">{vida_wall}</div>
        </section>
        <aside class="mockup-note">{t["home_note"]}</aside>
      </div>'''


def group_switch(lang, root, current):
    t = T[lang]
    g = GROUPS[lang]
    items = [(t["everything"], f"{root}{t['loc']}/blog.html", "all", None)] + \
            [(g[k][0], f"{root}{t['loc']}/{g[k][1]}/", k, g[k][2]) for k in ("vida", "tech")]
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if k == current else ""}>{obj(o) if o else ""}{e(n)}</a>' for n, h, k, o in items)
    return f'<nav class="group-switch" aria-label="{t["groups"]}">{links}</nav>'


def tech_nav_items(lang, root, current=None, attr=' data-state="tech-on"'):
    t = T[lang]
    return "\n".join(f'          <li{attr}><a class="tag" href="{root}{t["loc"]}/{c["slug"]}/"{" aria-current=\"page\"" if c["slug"] == current else ""}>{e(c["name"])}<span class="category-nav__count">{c["count"]}</span></a></li>'
                     for c in sorted(tech_cats(lang), key=lambda c: c["name"]))


def blog_featured_on(lang, root, sdate):
    p = tech_posts(lang)[0]
    return f'''<section class="container featured-entry" aria-label="{T[lang]["latest"]}" data-state="tech-on">
        {shot(p, root, sdate, lang, "polaroid--wide featured-entry__photo", "--r:-2deg")}
        <div class="sticky-note featured-entry__note" style="--r:3deg">
          <span class="sticky-note__title">{T[lang]["latest"]}</span>
          <h2 class="featured-entry__title"><a href="{root}{p["path"].lstrip("/")}">{e(p["title"])}</a></h2>
          <p>{e(p["excerpt"])}</p>
          <a class="featured-entry__more" href="{root}{p["path"].lstrip("/")}">{T[lang]["read"]} {ARROW}</a>
        </div>
      </section>'''


def blog_wall_on(lang, root, vida, polaroid, sdate):
    """The blog wall with Tech on: both groups mixed by date (Tech's newest is featured above)."""
    cards = [(p["date"], shot(p, root, sdate, lang)) for p in tech_posts(lang)[1:]] + [(p["date"], polaroid(p, root)) for p in vida]
    cards.sort(key=lambda c: c[0], reverse=True)
    return "\n".join("          " + c for _, c in cards[:12])
