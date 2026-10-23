import json, os, re, html as H
import pages as pt
import pages_en as en
from common import posts as P, cats, e, S
from en_data import posts as PE, cats_en, CAT_SLUG, CAT_OBJ as CAT_OBJ_EN, TAG, by_pt

M = pt.M
raw = json.load(open(f"{S}/wp/posts.json"))
catmap = {c["id"]: c for c in json.load(open(f"{S}/wp/cats.json"))}
tagmap = {t["id"]: t for t in json.load(open(f"{S}/wp/tags.json"))}
CATS_OF = {r["slug"]: [catmap[i]["slug"] for i in r["categories"]] for r in raw}
TAGS_OF = {r["slug"]: [tagmap[i]["slug"] for i in r["tags"]] for r in raw}
obj, arrow = pt.obj, pt.arrow

# ---------------------------------------------------------------- Category pages
root = "../../"
def cat_nav(current):
    items = [f'          <li><a class="tag" href="{root}br/blog.html">Todos<span class="category-nav__count">{len(P)}</span></a></li>']
    for c in sorted(cats, key=lambda c: c["name"]):
        cur = ' aria-current="page"' if c["slug"] == current else ""
        items.append(f'          <li><a class="tag" href="{root}br/{c["slug"]}/"{cur}>{e(c["name"])}<span class="category-nav__count">{c["count"]}</span></a></li>')
    return "\n".join(items)

for c in cats:
    ps = [p for p in P if c["slug"] in CATS_OF[p["slug"]]]
    wall = "\n".join("          " + pt.polaroid(p, root) for p in ps)
    n = len(ps)
    page = pt.head(f"{c['name']} · Blog · gui carvalho", f"{n} posts sobre {c['name']} no blog do Gui.", root) + f'''
    <site-header root="{root}" current="blog" alternate="{root}en/{CAT_SLUG[c['slug']]}/"></site-header>

    <main id="main">
      <section class="container" aria-labelledby="cat-title">
        <nav aria-label="Você está em" style="margin-block-start: var(--space-xl)">
          <ol class="breadcrumb" role="list"><li><a href="{root}br/blog.html">Blog</a></li><li>Categoria</li></ol>
        </nav>
        <div class="board-title" style="margin-block-start: var(--space-sm)">
          <span class="sticker" style="--r:-8deg">{obj(pt.CAT_OBJ.get(c["name"], "bulb"))}</span>
          <div>
            <h1 id="cat-title" style="font-size: var(--text-3xl)">{e(c["name"])}</h1>
            <p class="text-muted" style="font-size: var(--text-md)">{n} {"post colado" if n == 1 else "posts colados"} aqui sobre {e(c["name"].lower() if c["name"] not in ("Irlanda",) else c["name"])}.</p>
          </div>
        </div>
        <nav class="category-nav" aria-label="Categorias">
          <ul class="category-nav__list" role="list">
{cat_nav(c["slug"])}
          </ul>
        </nav>
        <div class="wall">
{wall}
        </div>
      </section>

      {pt.newsletter()}
    </main>
''' + pt.foot(root)
    os.makedirs(f"{M}/br/{c['slug']}", exist_ok=True)
    open(f"{M}/br/{c['slug']}/index.html", "w").write(page)

# ---------------------------------------------------------------- Tag page
tag = next(t for t in tagmap.values() if t["slug"] == "desenvolvimento-pessoal")
tps = [p for p in P if tag["slug"] in TAGS_OF[p["slug"]]]
troot = "../../../"
twall = "\n".join("          " + pt.polaroid(p, troot) for p in tps)
tag_page = pt.head(f"#{tag['name']} · Blog · gui carvalho", f"Posts com a tag {tag['name']}.", troot) + f'''
    <site-header root="{troot}" current="blog" alternate="{troot}en/tag/{TAG[tag['slug']][1]}/"></site-header>

    <main id="main">
      <section class="container" aria-labelledby="tag-title">
        <nav aria-label="Você está em" style="margin-block-start: var(--space-xl)">
          <ol class="breadcrumb" role="list"><li><a href="{troot}br/blog.html">Blog</a></li><li>Tag</li></ol>
        </nav>
        <div class="board-title" style="margin-block-start: var(--space-sm)">
          <span class="sticker" style="--r:6deg">{obj("bulb")}</span>
          <div>
            <h1 id="tag-title" style="font-size: var(--text-3xl)"><span class="text-muted">#</span>{e(tag["name"].lower())}</h1>
            <p class="text-muted" style="font-size: var(--text-md)">{len(tps)} posts com esta tag. As tags são mais específicas que as categorias e aparecem no rodapé de cada post.</p>
          </div>
        </div>
        <div class="wall">
{twall}
        </div>
        <aside class="mockup-note" style="margin-block-start: var(--space-md)">O blog atual tem 36 tags, quase todas usadas uma vez só. Vale decidir na migração se elas continuam ou se ficam só as categorias.</aside>
      </section>

      {pt.newsletter()}
    </main>
''' + pt.foot(troot)
os.makedirs(f"{M}/br/tag/{tag['slug']}", exist_ok=True)
open(f"{M}/br/tag/{tag['slug']}/index.html", "w").write(tag_page)


# ---------------------------------------------------------------- English category and tag pages
def cat_nav_en(current):
    items = [f'          <li><a class="tag" href="{root}en/blog.html">All<span class="category-nav__count">{len(PE)}</span></a></li>']
    for c in sorted(cats_en, key=lambda c: c["name"]):
        cur = ' aria-current="page"' if c["slug"] == current else ""
        items.append(f'          <li><a class="tag" href="{root}en/{c["slug"]}/"{cur}>{e(c["name"])}<span class="category-nav__count">{c["count"]}</span></a></li>')
    return "\n".join(items)

for c in cats_en:
    ps = [by_pt[p["slug"]] for p in P if c["pt_slug"] in CATS_OF[p["slug"]]]
    wall = "\n".join("          " + en.polaroid(p, root) for p in ps)
    n = len(ps)
    page = en.head(f"{c['name']} · Blog · gui carvalho", f"{n} posts about {c['name']} on Gui's blog.", root) + f'''
    <site-header root="{root}" current="blog" alternate="{root}br/{c['pt_slug']}/"></site-header>

    <main id="main">
      <section class="container" aria-labelledby="cat-title">
        <nav aria-label="You are here" style="margin-block-start: var(--space-xl)">
          <ol class="breadcrumb" role="list"><li><a href="{root}en/blog.html">Blog</a></li><li>Category</li></ol>
        </nav>
        <div class="board-title" style="margin-block-start: var(--space-sm)">
          <span class="sticker" style="--r:-8deg">{obj(CAT_OBJ_EN.get(c["name"], "bulb"))}</span>
          <div>
            <h1 id="cat-title" style="font-size: var(--text-3xl)">{e(c["name"])}</h1>
            <p class="text-muted" style="font-size: var(--text-md)">{n} {"post" if n == 1 else "posts"} pinned here about {e(c["name"].lower() if c["name"] not in ("Ireland",) else c["name"])}.</p>
          </div>
        </div>
        <nav class="category-nav" aria-label="Categories">
          <ul class="category-nav__list" role="list">
{cat_nav_en(c["slug"])}
          </ul>
        </nav>
        <div class="wall">
{wall}
        </div>
      </section>

      {en.newsletter()}
    </main>
''' + en.foot(root)
    os.makedirs(f"{M}/en/{c['slug']}", exist_ok=True)
    open(f"{M}/en/{c['slug']}/index.html", "w").write(page)

tag_name, tag_slug = TAG[tag["slug"]]
etps = [by_pt[p["slug"]] for p in tps]
etwall = "\n".join("          " + en.polaroid(p, troot) for p in etps)
en_tag = en.head(f"#{tag_name} · Blog · gui carvalho", f"Posts tagged {tag_name}.", troot) + f'''
    <site-header root="{troot}" current="blog" alternate="{troot}br/tag/{tag['slug']}/"></site-header>

    <main id="main">
      <section class="container" aria-labelledby="tag-title">
        <nav aria-label="You are here" style="margin-block-start: var(--space-xl)">
          <ol class="breadcrumb" role="list"><li><a href="{troot}en/blog.html">Blog</a></li><li>Tag</li></ol>
        </nav>
        <div class="board-title" style="margin-block-start: var(--space-sm)">
          <span class="sticker" style="--r:6deg">{obj("bulb")}</span>
          <div>
            <h1 id="tag-title" style="font-size: var(--text-3xl)"><span class="text-muted">#</span>{e(tag_name.lower())}</h1>
            <p class="text-muted" style="font-size: var(--text-md)">{len(etps)} posts with this tag. Tags are more specific than categories and show up at the bottom of each post.</p>
          </div>
        </div>
        <div class="wall">
{etwall}
        </div>
        <aside class="mockup-note" style="margin-block-start: var(--space-md)">The current blog has 36 tags, almost all used only once. It's worth deciding during the migration whether they stay or only the categories remain.</aside>
      </section>

      {en.newsletter()}
    </main>
''' + en.foot(troot)
os.makedirs(f"{M}/en/tag/{tag_slug}", exist_ok=True)
open(f"{M}/en/tag/{tag_slug}/index.html", "w").write(en_tag)

# Search lives in search_a.py
import search_a  # noqa: F401  (writes the search pages)

# ---------------------------------------------------------------- Simple centered pages (sign in, newsletter, 404)
def google_btn(label): return f'<a class="button button--google" href="#"><svg aria-hidden="true"><use href="#icon-google"/></svg>{label}</a>'

def simple(lang, root, alt, title, desc, sticker, card_cls, inner, after=""):
    h, f = (pt.head, pt.foot) if lang == "pt" else (en.head, en.foot)
    return h(f"{title} · gui carvalho", desc, root) + f'''
    <site-header root="{root}" alternate="{alt}"></site-header>

    <main id="main" class="container">
      <section class="center-stage">
        <span class="sticker center-stage__sticker" style="--r:-8deg">{obj(sticker)}</span>
        <div class="{card_cls} center-stage__card" style="--r:-1deg">
{inner}
        </div>
      </section>
{after}
    </main>
''' + f(root)

def recent(root, lang):
    if lang == "pt":
        items = "\n".join("          " + pt.polaroid(p, root) for p in P[:4])
        title = "Enquanto isso, que tal um destes?"
    else:
        items = "\n".join("          " + en.polaroid(p, root) for p in PE[:4])
        title = "Meanwhile, how about one of these?"
    return f'''      <section aria-labelledby="recent-title">
        <div class="board-title"><span class="sticker" style="--r:6deg">{obj("plane")}</span><h2 id="recent-title">{title}</h2></div>
        <div class="wall">
{items}
        </div>
      </section>'''

PAGES = []
# Sign in
PAGES.append(("br/entrar.html", simple("pt", "../", "../en/sign-in.html", "Entrar", "Entre com sua conta Google para comentar.", "chat", "sheet", f'''          <h1>Entre para comentar</h1>
          <p class="text-muted">Use sua conta Google para comentar nos posts e acompanhar as respostas.</p>
          {google_btn("Entrar com Google")}
          <p class="center-stage__fine">Usamos só seu nome e sua foto do Google. Nunca publicamos seu e-mail.</p>''',
    '''      <div class="cluster" style="justify-content: center; margin-block-end: var(--space-2xl)">
        <div class="sticky-note" style="--r:3deg; max-width: 20rem"><span class="sticky-note__title">Por que só Google?</span>Menos uma senha para lembrar, e bem menos spam nos comentários.</div>
      </div>''')))
PAGES.append(("en/sign-in.html", simple("en", "../", "../br/entrar.html", "Sign in", "Sign in with your Google account to comment.", "chat", "sheet", f'''          <h1>Sign in to comment</h1>
          <p class="text-muted">Use your Google account to comment on posts and follow the replies.</p>
          {google_btn("Sign in with Google")}
          <p class="center-stage__fine">We only use your Google name and photo. We never publish your email.</p>''',
    '''      <div class="cluster" style="justify-content: center; margin-block-end: var(--space-2xl)">
        <div class="sticky-note" style="--r:3deg; max-width: 20rem"><span class="sticky-note__title">Why only Google?</span>One less password to remember, and far less spam in the comments.</div>
      </div>''')))

# Newsletter: check inbox
PAGES.append(("br/newsletter/confirme.html", simple("pt", "../../", "../../en/newsletter/check-your-inbox.html", "Confira seu e-mail", "Confirme sua inscrição na newsletter.", "envelope", "sticky-note", '''          <h1>Quase lá! Confira seu e-mail</h1>
          <p>Mandei um e-mail para <strong>seu@email.com</strong> com um link de confirmação. É só clicar nele para começar a receber os posts.</p>
          <p class="center-stage__fine">Não chegou em alguns minutos? Dá uma olhada na caixa de spam ou de promoções.</p>
          <div class="cluster center-stage__actions">
            <button class="button" type="button">Reenviar o e-mail</button>
            <a class="button button--secondary" href="../blog.html">Voltar ao blog</a>
          </div>''')))
PAGES.append(("en/newsletter/check-your-inbox.html", simple("en", "../../", "../../br/newsletter/confirme.html", "Check your inbox", "Confirm your newsletter subscription.", "envelope", "sticky-note", '''          <h1>Almost there! Check your inbox</h1>
          <p>I sent an email to <strong>you@email.com</strong> with a confirmation link. Just click it to start getting new posts.</p>
          <p class="center-stage__fine">Nothing after a few minutes? Take a look at your spam or promotions folder.</p>
          <div class="cluster center-stage__actions">
            <button class="button" type="button">Resend the email</button>
            <a class="button button--secondary" href="../blog.html">Back to the blog</a>
          </div>''')))
# Newsletter: confirmed
PAGES.append(("br/newsletter/confirmado.html", simple("pt", "../../", "../../en/newsletter/confirmed.html", "Inscrição confirmada", "Sua inscrição na newsletter está confirmada.", "envelope", "sticky-note", '''          <h1>Inscrição confirmada!</h1>
          <p>Pronto, você está no caderno. A partir de agora, cada post novo chega direto no seu e-mail.</p>
          <p class="center-stage__fine">Um e-mail por post, sem spam. Dá para sair quando quiser pelo link no rodapé de cada e-mail.</p>''', recent("../../", "pt"))))
PAGES.append(("en/newsletter/confirmed.html", simple("en", "../../", "../../br/newsletter/confirmado.html", "Subscription confirmed", "Your newsletter subscription is confirmed.", "envelope", "sticky-note", '''          <h1>You're in!</h1>
          <p>Your subscription is confirmed. From now on, every new post lands straight in your inbox.</p>
          <p class="center-stage__fine">One email per post, no spam. You can leave anytime through the link at the bottom of each email.</p>''', recent("../../", "en"))))
# Newsletter: unsubscribed
PAGES.append(("br/newsletter/descadastrado.html", simple("pt", "../../", "../../en/newsletter/unsubscribed.html", "Inscrição cancelada", "Você saiu da newsletter.", "envelope", "sheet", '''          <h1>Você saiu da newsletter</h1>
          <p class="text-muted">Pronto, você não vai mais receber os posts por e-mail. Se foi engano, é só voltar:</p>
          <button class="button" type="button">Me inscrever de novo</button>
          <form class="stack" action="#" onsubmit="return false" style="--stack-gap: var(--space-sm); width: 100%; margin-block-start: var(--space-md); padding-block-start: var(--space-md); border-top: 1px dashed var(--color-border)">
            <fieldset class="choice-list" style="border: 0; padding: 0">
              <legend class="field__label" style="margin-block-end: var(--space-2xs)">Se quiser, me conta por quê (opcional):</legend>
              <label><input type="radio" name="why" value="many">Recebia e-mails demais</label>
              <label><input type="radio" name="why" value="topics">Os assuntos não me interessam mais</label>
              <label><input type="radio" name="why" value="never">Não lembro de ter me inscrito</label>
              <label><input type="radio" name="why" value="other">Outro motivo</label>
            </fieldset>
            <button class="button button--secondary" type="submit" style="justify-self: center">Enviar</button>
          </form>''')))
PAGES.append(("en/newsletter/unsubscribed.html", simple("en", "../../", "../../br/newsletter/descadastrado.html", "Unsubscribed", "You left the newsletter.", "envelope", "sheet", '''          <h1>You left the newsletter</h1>
          <p class="text-muted">Done, you won't get posts by email anymore. If it was a mistake, come right back:</p>
          <button class="button" type="button">Subscribe again</button>
          <form class="stack" action="#" onsubmit="return false" style="--stack-gap: var(--space-sm); width: 100%; margin-block-start: var(--space-md); padding-block-start: var(--space-md); border-top: 1px dashed var(--color-border)">
            <fieldset class="choice-list" style="border: 0; padding: 0">
              <legend class="field__label" style="margin-block-end: var(--space-2xs)">If you like, tell me why (optional):</legend>
              <label><input type="radio" name="why" value="many">Too many emails</label>
              <label><input type="radio" name="why" value="topics">The topics no longer interest me</label>
              <label><input type="radio" name="why" value="never">I don't remember subscribing</label>
              <label><input type="radio" name="why" value="other">Something else</label>
            </fieldset>
            <button class="button button--secondary" type="submit" style="justify-self: center">Send</button>
          </form>''')))

# 404
def nf(lang):
    root = "../"
    if lang == "pt":
        inner = f'''          <h1>Essa página saiu do caderno</h1>
          <p class="text-muted">O link pode estar quebrado, ou a página mudou de lugar. Tenta buscar:</p>
          <form class="search-form" role="search" action="../br/busca.html">
            <label class="visually-hidden" for="nf-q">Buscar no blog</label>
            <input class="input" id="nf-q" type="search" name="q" placeholder="O que você procurava?">
            <button class="button" type="submit">Buscar</button>
          </form>
          <nav class="cluster center-stage__actions" aria-label="Ou vá para" style="--cluster-gap: var(--space-sm); margin-block-start: var(--space-xs)">
            <a class="index-card" href="{root}br/index.html" style="--r:-2deg"><span class="sticker sticker--sm">{obj("bulb")}</span><b>Início</b></a>
            <a class="index-card" href="{root}br/blog.html" style="--r:1.5deg"><span class="sticker sticker--sm">{obj("pencil")}</span><b>Blog</b></a>
            <a class="index-card" href="{root}br/apps.html" style="--r:-1deg"><span class="sticker sticker--sm">{obj("laptop")}</span><b>Apps</b></a>
          </nav>'''
        return simple("pt", root, "../en/404.html", "Página não encontrada", "Essa página não existe.", "map", "sheet", inner, recent(root, "pt"))
    inner = f'''          <h1>This page fell out of the notebook</h1>
          <p class="text-muted">The link may be broken, or the page moved somewhere else. Try searching:</p>
          <form class="search-form" role="search" action="../en/search.html">
            <label class="visually-hidden" for="nf-q">Search the blog</label>
            <input class="input" id="nf-q" type="search" name="q" placeholder="What were you looking for?">
            <button class="button" type="submit">Search</button>
          </form>
          <nav class="cluster center-stage__actions" aria-label="Or go to" style="--cluster-gap: var(--space-sm); margin-block-start: var(--space-xs)">
            <a class="index-card" href="{root}en/index.html" style="--r:-2deg"><span class="sticker sticker--sm">{obj("bulb")}</span><b>Home</b></a>
            <a class="index-card" href="{root}en/blog.html" style="--r:1.5deg"><span class="sticker sticker--sm">{obj("pencil")}</span><b>Blog</b></a>
            <a class="index-card" href="{root}en/apps.html" style="--r:-1deg"><span class="sticker sticker--sm">{obj("laptop")}</span><b>Apps</b></a>
          </nav>'''
    return simple("en", root, "../br/404.html", "Page not found", "This page doesn't exist.", "map", "sheet", inner, recent(root, "en"))
PAGES.append(("br/404.html", nf("pt")))
PAGES.append(("en/404.html", nf("en")))

for path, html in PAGES:
    os.makedirs(os.path.dirname(f"{M}/{path}"), exist_ok=True)
    open(f"{M}/{path}", "w").write(html)
print("ok", len(cats), "categories,", len(tps), "tag posts,", len(PAGES), "simple pages")
