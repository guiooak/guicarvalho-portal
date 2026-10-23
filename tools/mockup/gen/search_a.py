"""Search page, option A: a big line to write the search on, a post-it count,
category stickers and the hits as polaroids. Writes /br/busca.html and /en/search.html."""
import re
import pages as pt
import pages_en as en
from common import posts as P, cats, e
from en_data import posts as PE, cats_en, CAT_OBJ as CAT_OBJ_EN

obj = pt.obj
M = pt.M


def search_page(lang):
    root = "../"
    if lang == "pt":
        q, none_q = "vida", "mergulho em marte"
        hits = [dict(title=p["title"], excerpt=p["excerpt"], cat=p["cat"], date=pt.sdate(p["date"]), iso=p["date"],
                     cover=p["cover"], href=root + p["path"].lstrip("/"))
                for p in P if q in (p["title"] + " " + p["excerpt"]).lower()]
        T = dict(head=pt.head, foot=pt.foot, title="Buscar", desc="Busca nos posts do blog.", h1="O que você está procurando?",
                 label="Buscar no blog", placeholder="Escreva aqui…", go="Buscar", alt="../en/search.html",
                 results="Resultados", empty_label="Nenhum resultado",
                 count=lambda n: f"{n} {'achado' if n == 1 else 'achados'} para “{q}”",
                 none=f"Nada colado aqui sobre “{none_q}”. Tenta outra palavra, ou puxa um destes adesivos:",
                 state="Estado:", s1="Com resultados", s2="Sem resultados",
                 mock=f"Neste estado, imagine que a busca foi por “{none_q}”: o campo mostraria o termo buscado.")
        variants = ["", " topic-sticker--paper", " topic-sticker--note", " topic-sticker--sage", ""]
        tilts = ["-4deg", "3deg", "-2deg", "5deg", "-3deg"]
        sugg = "".join(
            f'<a class="topic-sticker{v}" href="{root}br/{c["slug"]}/" style="--r:{r}">{obj(pt.CAT_OBJ.get(c["name"], "bulb"))}{e(c["name"])}</a>'
            for c, v, r in zip(cats[:5], variants, tilts))
    else:
        q, none_q = "life", "diving on mars"
        hits = [dict(title=p["title"], excerpt=p["excerpt"], cat=p["cat"], date=en.sdate(p["date"]), iso=p["date"],
                     cover=p["cover"], href=root + p["path"].lstrip("/"))
                for p in PE if q in (p["title"] + " " + p["excerpt"]).lower()]
        T = dict(head=en.head, foot=en.foot, title="Search", desc="Search the blog posts.", h1="What are you looking for?",
                 label="Search the blog", placeholder="Write here…", go="Search", alt="../br/busca.html",
                 results="Results", empty_label="No results",
                 count=lambda n: f"{n} find{'s' if n != 1 else ''} for “{q}”",
                 none=f"Nothing pinned here about “{none_q}”. Try another word, or peel off one of these stickers:",
                 state="State:", s1="With results", s2="No results",
                 mock=f"In this state, imagine the search was for “{none_q}”: the field would show the searched term.")
        variants = ["", " topic-sticker--paper", " topic-sticker--note", " topic-sticker--sage", ""]
        tilts = ["-4deg", "3deg", "-2deg", "5deg", "-3deg"]
        sugg = "".join(
            f'<a class="topic-sticker{v}" href="{root}en/{c["slug"]}/" style="--r:{r}">{obj(CAT_OBJ_EN.get(c["name"], "bulb"))}{e(c["name"])}</a>'
            for c, v, r in zip(cats_en[:5], variants, tilts))

    def mark(t):
        return re.sub(f"({re.escape(q)})", r"<mark>\1</mark>", e(t), flags=re.I)

    def snippet(t, n=150):
        i = t.lower().find(q)
        st = max(0, i - 60) if i >= 0 else 0
        return ("…" if st else "") + t[st:st + n] + ("…" if st + n < len(t) else "")

    by_cat = {}
    for h in hits:
        by_cat[h["cat"]] = by_cat.get(h["cat"], 0) + 1
    chips = "".join(
        f'<a class="topic-sticker{v}" href="#" style="--r:{r}">{e(c)}<span class="topic-sticker__count">{n}</span></a>'
        for (c, n), v, r in zip(by_cat.items(), ["", " topic-sticker--paper", " topic-sticker--note", " topic-sticker--sage"],
                                ["-4deg", "3deg", "-2deg", "4deg"]))
    cards = []
    for h in hits:
        cards.append(
            f'          <a class="polaroid" href="{h["href"]}"><span class="polaroid__tag">{e(h["cat"])}</span>'
            f'<img src="{root}assets/images/covers/{h["cover"]}" alt="" loading="lazy"><span class="polaroid__caption">'
            f'<span class="polaroid__title">{mark(h["title"])}</span><span class="polaroid__snippet">{mark(snippet(h["excerpt"]))}</span>'
            f'<time class="polaroid__meta" datetime="{h["iso"]}">{h["date"]}</time></span></a>')
    wall = "\n".join(cards)

    return T["head"](f"{T['title']} · gui carvalho", T["desc"], root) + f"""
    <site-header root="{root}" alternate="{T['alt']}"></site-header>

    <main id="main" class="mockup-stateful">
      <section class="container search-hero" aria-labelledby="search-title">
        <h1 id="search-title">{T['h1']}</h1>
        <form class="search-line" role="search" action="#" onsubmit="return false">
          <label class="visually-hidden" for="q">{T['label']}</label>
          <input class="search-line__input" id="q" type="search" name="q" placeholder="{T['placeholder']}" value="{q}">
          <button class="search-line__go" type="submit" aria-label="{T['go']}"><svg aria-hidden="true"><use href="#icon-search"/></svg></button>
        </form>
      </section>

      <section class="container" data-state="results" aria-label="{T['results']}" aria-live="polite">
        <div class="search-summary">
          <div class="sticky-note" style="--r:-3deg">{T['count'](len(hits))}</div>
          <div class="cluster" style="--cluster-gap: var(--space-sm)">{chips}</div>
        </div>
        <div class="wall">
{wall}
        </div>
      </section>

      <section class="container search-empty" data-state="no-results" aria-label="{T['empty_label']}">
        <span class="sticker" style="--sticker-size: 6rem; --r: 8deg">{obj('map')}</span>
        <div class="sticky-note" style="--r:2deg">{T['none']}</div>
        <aside class="mockup-note">{T['mock']}</aside>
        <div class="cluster" style="justify-content: center; --cluster-gap: var(--space-sm)">{sugg}</div>
      </section>

      <fieldset class="mockup-states mockup-states--floating">
        <legend class="visually-hidden">{T['state']}</legend>
        <span>{T['state']}</span>
        <label><input type="radio" name="search-state" value="results" checked>{T['s1']}</label>
        <label><input type="radio" name="search-state" value="no-results">{T['s2']}</label>
      </fieldset>
    </main>
""" + T["foot"](root)


open(f"{M}/br/busca.html", "w").write(search_page("pt"))
open(f"{M}/en/search.html", "w").write(search_page("en"))
print("search ok")
