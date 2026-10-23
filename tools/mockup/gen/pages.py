import os, re
from common import posts as P, cats, e, fdate, sdate, S
from apps import APPS
from groups import home_section, group_switch, tech_nav_items, blog_featured_on, blog_wall_on, states, T as GT
from tech_data import posts as tech_posts

M = __import__("common").MOCKUP
article = open(f"{S}/wp/article-clean.html").read()
CAT_OBJ = {"Viva": "sprout", "Coaching": "target", "Homenagens": "heart", "Casos de Sucesso": "trophy", "Inspiração": "bulb",
           "Irlanda": "clover", "Geral": "mug", "Idiomas": "chat", "Liderança": "flag", "Presepadas": "laugh",
           "Viagens": "suitcase", "Empreendedorismo": "rocket", "Gestão de tempo": "clock", "Músicas": "note", "Princípios Básicos": "book"}

def obj(name): return f'<svg aria-hidden="true"><use href="#obj-{name}"/></svg>'
def link(p, root): return f"{root}{p['path'].lstrip('/')}"
def cover(p, root): return f"{root}assets/images/covers/{p['cover']}"

def head(title, desc, root, extra=""):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">{extra}
  <link rel="icon" href="{root}assets/images/brand/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{root}assets/stylesheets/application.css">
  <link rel="stylesheet" href="{root}assets/stylesheets/mockup.css">
  <script src="{root}assets/javascripts/mockup.js?v=2026-10-19f"></script>
</head>
<body class="paper">
  <div class="site">'''

def foot(root):
    return f'''
    <site-footer root="{root}"></site-footer>
  </div>

  <div class="mockup-toolbar" aria-label="Ferramentas do mockup">
    <button type="button" data-notes-toggle>Notas do mockup</button>
  </div>
</body>
</html>
'''

def polaroid(p, root, tag=True, lazy=True, extra_cls="", style=""):
    t = f'<span class="polaroid__tag">{e(p["cat"])}</span>' if tag else ""
    return f'''<a class="polaroid {extra_cls}" href="{link(p, root)}"{f' style="{style}"' if style else ''}>{t}<img src="{cover(p, root)}" alt="{e(p['alt'] or p['title'])}" width="768" height="512"{' loading="lazy"' if lazy else ''}><span class="polaroid__caption"><span class="polaroid__title">{e(p['title'])}</span><time class="polaroid__meta" datetime="{p['date']}">{sdate(p['date'])}</time></span></a>'''

def newsletter(title="Quer receber o próximo post? ✉️", r="-1.2deg"):
    return f'''<section class="container" aria-labelledby="newsletter-title">
        <div class="sticky-note newsletter-note" id="newsletter" style="--r:{r}">
          <h2 id="newsletter-title">{title}</h2>
          <p>Deixa seu e-mail aqui no bilhete. Um e-mail por post novo, sem spam, e dá para sair quando quiser.</p>
          <form action="#" onsubmit="return false">
            <label class="visually-hidden" for="newsletter-email">Seu e-mail</label>
            <input class="input" id="newsletter-email" type="email" placeholder="seu@email.com" autocomplete="email" required>
            <button class="button" type="submit">Colar meu e-mail</button>
          </form>
          <small>Você vai receber um e-mail para confirmar a inscrição.</small>
        </div>
      </section>'''

def arrow(): return '<svg aria-hidden="true"><use href="#icon-arrow-right"/></svg>'

# ---------------------------------------------------------------- Home
root = "../"
SHELF_R = ["-6deg", "5deg", "-3deg", "7deg"]
apps = "\n".join(f'''          <a class="apps-shelf__app" href="{root}br/apps.html#{a['id']}"><span class="sticker" style="--r:{SHELF_R[i]}">{obj(a['obj'])}</span><span>{e(a['name'])}<small>{e(a['short'])}</small></span></a>''' for i, a in enumerate(APPS))
ROT = ["-6deg", "4deg", "-2deg", "7deg", "-4deg", "3deg", "-8deg", "5deg", "-3deg", "6deg", "-5deg", "2deg", "-7deg", "4deg", "-1deg"]
VAR = ["", "topic-sticker--paper", "topic-sticker--note", "topic-sticker--sage"]
order = sorted(cats, key=lambda c: c["name"])
def tsize(n): return " topic-sticker--lg" if n >= 7 else (" topic-sticker--md" if n >= 4 else "")
def tvar(i): return (" " + VAR[i % 4]) if VAR[i % 4] else ""
topics = "\n".join(f'          <a class="topic-sticker{tsize(c["count"])}{tvar(i)}" href="{root}br/{c["slug"]}/" style="--r:{ROT[i % len(ROT)]}">{obj(CAT_OBJ.get(c["name"], "bulb"))}{e(c["name"])}<span class="topic-sticker__count" aria-label="{c["count"]} posts">{c["count"]}</span></a>' for i, c in enumerate(order))
wall = "\n".join("          " + polaroid(p, root) for p in P[:8])
home = head("gui carvalho · Histórias, metas, idiomas e apps", "O caderno de Guilherme Carvalho: histórias, metas, idiomas, viagens e os apps que ele constrói.", root) + f'''
    <site-header root="{root}" current="home" alternate="{root}en/index.html"></site-header>

    <main id="main">
      <section class="container desk" aria-labelledby="intro-title">
        <div>
          <h1 class="desk__title" id="intro-title">Oi, eu sou o <span class="scribble">Gui</span>.</h1>
          <p class="desk__lead">Este é o meu caderno: histórias, metas, idiomas, viagens e os apps que eu construo, colados aqui desde 2015.</p>
          <div class="cluster">
            <a class="button" href="{root}br/blog.html">Folhear o blog</a>
            <a class="button button--secondary" href="{root}br/apps.html">Meus apps</a>
          </div>
        </div>
        <div class="collage">
          <figure class="polaroid collage__photo" style="--r:-5deg">
            <img src="{root}assets/images/about/gui-paris.jpg" alt="Gui sorrindo em Paris, com a cidade ao fundo" width="768" height="576">
            <figcaption class="polaroid__caption"><span class="polaroid__title">Esse sou eu</span><span class="polaroid__meta">Paris, 2016</span></figcaption>
          </figure>
          <div class="sticky-note collage__note" style="--r:4deg">
            <span class="sticky-note__title">Quem escreve aqui</span>
            <ul>
              <li>Mineiro de Ipatinga</li>
              <li>Engenheiro front-end</li>
              <li>Marido da Joice</li>
              <li>Papai da Elisa</li>
              <li>Bateria, forró e surfe</li>
            </ul>
          </div>
          <nav class="collage__cards" aria-label="O que tem por aqui">
            <span class="collage__cards-title">O que tem por aqui</span>
            <a class="index-card" href="{root}br/blog.html" style="--r:-2deg"><span class="sticker sticker--sm">{obj("pencil")}</span><span><b>Blog</b><small>{len(P)} histórias desde 2015</small></span></a>
            <a class="index-card" href="{root}br/apps.html" style="--r:1.5deg"><span class="sticker sticker--sm">{obj("laptop")}</span><span><b>Apps</b><small>Coisas que eu construí</small></span></a>
            <a class="index-card" href="{root}br/sobre.html" style="--r:-1deg"><span class="sticker sticker--sm">{obj("bulb")}</span><span><b>Sobre</b><small>A biografia autorizada</small></span></a>
          </nav>
          <span class="sticker collage__deco" style="--r:12deg">{obj("map")}</span>
        </div>
        <aside class="mockup-note" style="grid-column: 1 / -1">A foto e os itens do post-it vêm da página "Sobre o Gui" do blog atual e são provisórios até chegar o material novo.</aside>
      </section>

      <section class="container" aria-labelledby="apps-title">
        <div class="board-title">
          <span class="sticker" style="--r:8deg">{obj("laptop")}</span>
          <h2 id="apps-title">Coisas que eu construí</h2>
          <a class="section-heading__link" href="{root}br/apps.html">Ver todos os apps {arrow()}</a>
        </div>
        <div class="apps-shelf">
{apps}
        </div>
      </section>

      {home_section("pt", root, P, polaroid, sdate)}

      <section class="container" aria-labelledby="topics-title">
        <div class="board-title">
          <span class="sticker" style="--r:-4deg">{obj("pencil")}</span>
          <h2 id="topics-title">Sobre o que eu escrevo</h2>
          <div class="sticky-note topic-board__note" style="--r:3deg">Escolhe um assunto e puxa o adesivo. Quanto maior, mais eu já escrevi sobre ele.</div>
        </div>
        <div class="topic-board">
{topics}
        </div>
      </section>

      {newsletter()}
    </main>
''' + foot(root)

# ---------------------------------------------------------------- Blog
cat_nav = f'          <li data-state="tech-off"><a class="tag" href="{root}br/blog.html" aria-current="page">Todos<span class="category-nav__count">{len(P)}</span></a></li>\n' + f'          <li data-state="tech-on"><a class="tag" href="{root}br/blog.html" aria-current="page">Todos<span class="category-nav__count">{len(P) + len(tech_posts("pt"))}</span></a></li>\n' + "\n".join(f'          <li><a class="tag" href="{root}br/{c["slug"]}/">{e(c["name"])}<span class="category-nav__count">{c["count"]}</span></a></li>' for c in sorted(cats, key=lambda c: c["name"])) + "\n" + tech_nav_items("pt", root)
latest = P[0]
blog_wall = "\n".join("          " + polaroid(p, root) for p in P[1:13])
blog = head("Blog · gui carvalho", "Histórias, metas, idiomas, viagens e as presepadas da vida, desde 2015.", root) + f'''
    <site-header root="{root}" current="blog" alternate="{root}en/blog.html"></site-header>

    <main id="main" class="mockup-stateful">
      <section class="container blog-intro" aria-labelledby="blog-title">
        <div class="board-title" style="margin-block-start: var(--space-xl)">
          <span class="sticker" style="--r:-8deg">{obj("pencil")}</span>
          <div>
            <h1 id="blog-title" style="font-size: var(--text-3xl)">Blog</h1>
            <p class="text-muted" style="font-size: var(--text-md)"><span data-state="tech-off">{len(P)} histórias coladas aqui desde 2015.</span><span data-state="tech-on">{len(P) + len(tech_posts("pt"))} histórias coladas aqui desde 2015.</span></p>
          </div>
        </div>
        <div data-state="tech-on">{group_switch("pt", root, "all")}</div>
        <nav class="category-nav" aria-label="Categorias">
          <ul class="category-nav__list" role="list">
{cat_nav}
          </ul>
        </nav>
      </section>

      {blog_featured_on("pt", root, sdate)}

      <section class="container featured-entry" aria-label="Post mais recente" data-state="tech-off">
        {polaroid(latest, root, lazy=False, extra_cls="polaroid--wide featured-entry__photo", style="--r:-2deg")}
        <div class="sticky-note featured-entry__note" style="--r:3deg">
          <span class="sticky-note__title">Post mais recente</span>
          <h2 class="featured-entry__title"><a href="{link(latest, root)}">{e(latest["title"])}</a></h2>
          <p>{e(latest["excerpt"])}</p>
          <a class="featured-entry__more" href="{link(latest, root)}">Ler agora {arrow()}</a>
        </div>
      </section>

      <section class="container" aria-label="Todos os posts">
        <div class="wall" style="margin-block-start: var(--space-xl)" data-state="tech-off">
{blog_wall}
        </div>
        <div class="wall" style="margin-block-start: var(--space-xl)" data-state="tech-on">
{blog_wall_on("pt", root, P, polaroid, sdate)}
        </div>
        <nav class="pagination" aria-label="Paginação">
          <a class="pagination__page" href="{root}br/blog.html" aria-current="page">1</a>
          <a class="pagination__page" href="#">2</a>
          <a class="pagination__page" href="#">Próxima <svg width="16" height="16" aria-hidden="true" style="margin-inline-start:.3em"><use href="#icon-arrow-right"/></svg></a>
        </nav>
        <aside class="mockup-note" style="margin-block-start: var(--space-md)">Os filtros levam às páginas de categoria, que reaproveitam este layout. Só o post "O que te impede de aprender outro idioma?" tem página no mockup.</aside>
      </section>

      {newsletter()}
      <aside class="container mockup-note">{GT["pt"]["blog_note"]}</aside>
      {states("pt", floating=True)}
    </main>
''' + foot(root)

# ---------------------------------------------------------------- Post
proot = "../../../"
p = next(x for x in P if x["slug"] == "o-que-te-impede-de-aprender-outro-idioma")
words = len(re.sub(r"<[^>]+>", " ", article).split()); minutes = max(1, round(words / 200))
body = article.replace("IMGROOT", f"{proot}assets/images/posts/")
body = re.sub(r'(<figure><img[^>]*alt="Conhecimento nunca é demais"[^>]*>)</figure>\s*<p style="text-align: center;">Conhecimento nunca é demais</p>', r'\1<figcaption>Conhecimento nunca é demais</figcaption></figure>', body)
body = re.sub(r' style="[^"]*"', "", body)
body = "\n".join("            " + l for l in body.strip().splitlines())
related = [next(x for x in P if x["slug"] == s) for s in ["quem-e-mineiro-me-entende", "o-inicio-dos-sonhos", "aumentando-sua-auto-confianca-em-apenas-2-minutos"]]
rel = "\n".join("          " + polaroid(r, proot) for r in related)
comments = open(f"{M}/br/idiomas/o-que-te-impede-de-aprender-outro-idioma/index.html").read()
cstart = comments.find('<section class="container container--narrow comments')
if cstart < 0: cstart = comments.index('<section class="comments mockup-stateful')
cend = comments.index("</section>", cstart) + len("</section>")
csec = comments[cstart:cend].replace('class="container container--narrow comments mockup-stateful illo"', 'class="comments mockup-stateful illo"')
post = head(f"{p['title']} · gui carvalho", p["excerpt"], proot, extra=f'''
  <link rel="alternate" hreflang="pt-BR" href="https://guicarvalho.com.br{p['path']}">
  <link rel="alternate" hreflang="en" href="https://guicarvalho.com.br/en/languages/what-stops-you-from-learning-another-language/">''') + f'''
    <site-header root="{proot}" current="blog" alternate="{proot}en/languages/what-stops-you-from-learning-another-language/"></site-header>

    <main id="main">
      <article class="container container--narrow">
        <header class="post-header">
          <nav aria-label="Você está em">
            <ol class="breadcrumb" role="list">
              <li><a href="{proot}br/blog.html">Blog</a></li>
              <li><a href="{proot}br/{p['cat_slug']}/">{e(p['cat'])}</a></li>
            </ol>
          </nav>
          <h1 class="post-header__title">{e(p['title'])}</h1>
          <p class="post-header__lead">{e(p['excerpt'])}</p>
          <div class="post-meta">
            <span class="post-meta__author"><span class="avatar avatar--sm" aria-hidden="true"><img src="{proot}assets/images/about/gui-paris.jpg" alt=""></span>Gui Carvalho</span>
            <span class="post-meta__sep" aria-hidden="true">·</span>
            <time datetime="{p['date']}">{fdate(p['date'])}</time>
            <span class="post-meta__sep" aria-hidden="true">·</span>
            <span>{minutes} min de leitura</span>
            <span class="post-meta__sep" aria-hidden="true">·</span>
            <span class="post-languages" lang="en">Also in <a class="tag" href="{proot}en/languages/what-stops-you-from-learning-another-language/" hreflang="en">English</a></span>
          </div>
        </header>

        <figure class="polaroid polaroid--wide post-photo" style="--r:-1.5deg">
          <img src="{cover(p, proot)}" alt="{e(p['alt'] or p['title'])}" width="768" height="512">
        </figure>

        <div class="sheet">
          <div class="post-body">
{body}
          </div>

          <footer class="post-footer">
            <div class="cluster">
              <a class="tag" href="{proot}br/coaching/">Coaching</a>
              <a class="tag" href="{proot}br/idiomas/">Idiomas</a>
              <a class="tag" href="{proot}br/viagens/">Viagens</a>
            </div>
            <div class="share">
              <span>Compartilhar</span>
              <button class="icon-button" type="button" aria-label="Copiar link"><svg aria-hidden="true"><use href="#icon-link"/></svg></button>
              <a class="button button--ghost button--small" href="#">LinkedIn</a>
              <a class="button button--ghost button--small" href="#">WhatsApp</a>
            </div>
          </footer>

          <aside class="author-note" aria-label="Sobre o autor">
            <figure class="polaroid" style="--r:-4deg"><img src="{proot}assets/images/about/gui-paris.jpg" alt="" width="768" height="576"></figure>
            <div class="sticky-note" style="--r:2deg">
              <span class="sticky-note__title">Quem escreveu</span>
              <p>Gui Carvalho: mineiro, engenheiro front-end e curioso por natureza. Escreve sobre carreira, metas, idiomas e as presepadas da vida.</p>
              <a href="{proot}br/sobre.html"><b>Mais sobre mim →</b></a>
            </div>
          </aside>
        </div>
      </article>

      {newsletter("Gostou? Receba os próximos por e-mail ✉️", "1.2deg")}

      <section class="container" aria-labelledby="related-title">
        <div class="board-title">
          <span class="sticker" style="--r:6deg">{obj("plane")}</span>
          <h2 id="related-title">Leia também</h2>
        </div>
        <div class="wall">
{rel}
        </div>
      </section>

      <div class="container container--narrow" style="margin-block-start: var(--space-2xl)">
        <div class="sheet">
      {csec}
        </div>
      </div>
    </main>
''' + foot(proot)


# ---------------------------------------------------------------- Apps
def ext_icon(): return '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>'
def spread(a):
    hl = "".join(f"<li>{e(h)}</li>" for h in a["highlights"])
    tech = "".join(f'<span class="tag">{e(t)}</span>' for t in a["tech"])
    return f"""      <section class="app-spread" id="{a['id']}" aria-labelledby="{a['id']}-title">
        <a class="polaroid polaroid--wide app-spread__shot" href="{a['open'][1]}" style="--r:{a['r']}"><span class="polaroid__tag">{e(a['kind'])}</span><img src="{root}assets/images/apps/{a['img']}" alt="{e(a['alt'])}" width="1200" height="630" loading="lazy"></a>
        <div class="app-spread__card">
          <div class="app-spread__head">
            <span class="sticker">{obj(a['obj'])}</span>
            <div><h2 id="{a['id']}-title">{e(a['name'])}</h2><p>{e(a['tagline'])}</p></div>
          </div>
          <p>{e(a['desc'])}</p>
          <ul class="app-spread__highlights">{hl}</ul>
          <div class="cluster app-spread__tech">{tech}</div>
          <div class="cluster app-spread__actions">
            <a class="button" href="{a['open'][1]}">{e(a['open'][0])} {ext_icon()}</a>
            <a class="button button--secondary" href="{a['code']}">Código no GitHub</a>
          </div>
        </div>
      </section>"""
apps_html = head("Apps · gui carvalho", "Os apps que o Gui construiu: Tymebox, Bat Hunter, csv→ofx e Dialogs Valve.", root) + f"""
    <site-header root="{root}" current="apps" alternate="{root}en/apps.html"></site-header>

    <main id="main">
      <div class="container">
        <div class="board-title" style="margin-block-start: var(--space-xl)">
          <span class="sticker" style="--r:8deg">{obj("laptop")}</span>
          <div>
            <h1 style="font-size: var(--text-3xl)">Coisas que eu construí</h1>
            <p class="text-muted" style="font-size: var(--text-md)">Feitos para resolver algum problema meu, ou não. Mas sempre por diversão. Todos abertos para usar, e com o código no GitHub.</p>
          </div>
        </div>
        <nav class="cluster" aria-label="Apps nesta página" style="--cluster-gap: var(--space-sm)">
{"".join(f'          <a class="index-card" href="#{a["id"]}" style="--r:{("-2deg","1.5deg","-1deg","2deg")[i]}"><span class="sticker sticker--sm">{obj(a["obj"])}</span><span><b>{e(a["name"])}</b><small>{e(a["kind"])}</small></span></a>' + chr(10) for i, a in enumerate(APPS))}        </nav>
{chr(10).join(spread(a) for a in APPS)}
      </div>

      {newsletter("Quer saber quando sair coisa nova? ✉️")}
    </main>
""" + foot(root)
open(f"{M}/br/apps.html", "w").write(apps_html)


# ---------------------------------------------------------------- Sobre
BIO = [
    ("mountain", "Criado em Viçosa", ["Nascido em Ipatinga em 1987, o Guilherme Pereira de Carvalho é graduado em Ciência da Computação pela Universidade Federal de Viçosa. Ficou meros 9 anos por lá, que foram extremamente bem aproveitados."]),
    ("heart", "Família", ["Muitíssimo bem casado com a Joice e muito sortudo em ser pai da Elisa, que é a realização do maior sonho da sua vida: ser pai! Não perde uma festa de família por nada. E nessas festas, talvez não seja o primeiro a chegar, mas geralmente é um dos últimos a sair."]),
    ("map", "Lugar", ["Mineiro de coração, mora em Minas por enquanto, mas já viveu em Joinville e Navegantes, em Santa Catarina, e um dia volta para lá: gosta demais dos dois lugares. No caminho também passou por Belo Horizonte."]),
    ("laptop", "Trabalho", ["Engenheiro front-end, trabalha há mais de 5 anos para uma empresa americana, com React, TypeScript e Ruby on Rails. É apaixonado por desenvolvimento front-end, especialmente bibliotecas de componentes e por organização de código.",
                            f'Antes disso, foi voluntário por anos em empresa júnior e co-fundou uma empresa onde trabalhou por três anos. Nas horas vagas, usa a criatividade para estudar e criar os próprios aplicativos (<a href="{root}br/apps.html">dá uma olhada nos apps</a>).']),
    ("chip", "Gambiarras e invenções", ["É muito conhecido pelas habilidades de fazer gambiarras e consertar as coisas: se quebrou, ele dá um jeito. Adora eletrônica e criar coisas novas, do ferro de solda ao editor de código."]),
    ("clover", "Um ano em Dublin", ["Fez intercâmbio em Dublin, na Irlanda: trabalhou, estudou inglês e viajou muito. Por lá viveu algumas das experiências mais valiosas da sua vida, conhecendo pessoas ímpares e lugares fabulosos."]),
    ("suitcase", "Viagens", ["Viajar é muito importante pra ele. Inspirado pelo Amyr Klink, já conheceu 12 países e passou 3 meses viajando com a Joice como nômade digital. Ama conhecer novas culturas e pessoas diferentes e sonha em comprar um motor home para fazer muitas viagens com a própria família."]),
    ("note", "Música", ["Simplesmente não vive sem sua dose diária de música, na maior parte um velho e bom rock, mas o sertanejo raiz, um MPB e um forró para dançar têm seu lugar. Gosta de ouvir rádio e discos de vinil no seu receiver Gradiente, que tem a mesma idade que ele. Toca bateria por diversão, violão para a filha e faz aula de forró com a Joice."]),
    ("wave", "Esportista de fim de semana", ["Faz natação, já correu uma meia maratona e é faixa amarela de judô. Tem uma paixão adormecida por mountain bike e agora está aprendendo a surfar. E, para o futuro, seu sonho é se tornar competidor de triatlo."]),
    ("bulb", "Jeito de ser", ["Positivo, alegre, brincalhão e tem a capacidade de fazer amizades pra vida inteira em poucos minutos. No entanto, também é objetivo, preciso e direto quando necessário."]),
]
FACTS = [("Toca bateria por diversão.", ""), ("Toca violão para a filha.", " sticky-note--sage"),
         ("É faixa amarela em judô.", ""), ("Já correu uma meia maratona.", " sticky-note--sage"),
         ("Faz aula de forró com a Joice.", " sticky-note--sage"), ("Está aprendendo a surfar.", ""),
         ("Rei das gambiarras: se quebrou, ele conserta.", " sticky-note--sage"), ("Faz amizades pra vida inteira em poucos minutos.", "")]
SOCIAL = [("LinkedIn", "Carreira e trabalho", "https://www.linkedin.com/in/linkguicarvalho", "laptop"),
          ("GitHub", "O código dos meus apps", "https://github.com/guiooak", "window"),
          ("YouTube", "Vídeos de vez em quando", "http://youtube.com/c/GuilhermeCarvalhoOnline", "note"),
          ("Instagram", "Fotos e viagens", "https://www.instagram.com/guicarvalho.com.br", "plane")]
bio_html = "\n".join(f"""            <section class="bio-section" aria-labelledby="bio-{i}">
              <span class="sticker" style="--r:{("-6deg","5deg","-3deg","7deg","-5deg","4deg","-4deg","6deg","-2deg","3deg")[i % 10]}">{obj(o)}</span>
              <div><h2 id="bio-{i}">{e(t)}</h2>{"".join(f"<p>{p}</p>" for p in ps)}</div>
            </section>""" for i, (o, t, ps) in enumerate(BIO))
facts_html = "\n".join(f'          <div class="sticky-note{v}">{e(t)}</div>' for t, v in FACTS)
social_html = "\n".join(f'          <a class="index-card" href="{u}" target="_blank" rel="noopener" style="--r:{("-2deg","1.5deg","-1deg","2deg")[i]}"><span class="sticker sticker--sm">{obj(o)}</span><span><b>{n}</b><small>{d}</small></span><span class="visually-hidden"> (abre em nova aba)</span></a>' for i, (n, d, u, o) in enumerate(SOCIAL))
about_html = head("Sobre · gui carvalho", "A biografia autorizada do Gui: de Ipatinga a Viçosa, um ano em Dublin, rock, pedal e pão de queijo.", root) + f"""
    <site-header root="{root}" current="about" alternate="{root}en/about.html"></site-header>

    <main id="main">
      <div class="container">
        <div class="board-title" style="margin-block-start: var(--space-xl)">
          <span class="sticker" style="--r:-8deg">{obj("bulb")}</span>
          <div>
            <h1 style="font-size: var(--text-3xl)">Sobre o <span class="scribble">Gui</span></h1>
            <p class="text-muted" style="font-size: var(--text-md)">A biografia autorizada, colada aqui no caderno.</p>
          </div>
        </div>

        <section class="about-hero" aria-label="Ficha">
          <figure class="polaroid" style="--r:-4deg">
            <img src="{root}assets/images/about/gui-paris.jpg" alt="Gui sorrindo no alto de um mirante, com Paris ao fundo" width="768" height="576">
            <figcaption class="polaroid__caption"><span class="polaroid__title">Eu, em Paris</span><span class="polaroid__meta">2016</span></figcaption>
          </figure>
          <div class="sticky-note fact-sheet" style="--r:3deg">
            <span class="sticky-note__title">Ficha técnica</span>
            <dl>
              <div><dt>Nome</dt><dd>Guilherme Pereira de Carvalho</dd></div>
              <div><dt>Nasceu em</dt><dd>Ipatinga, MG, em 1987</dd></div>
              <div><dt>Profissão</dt><dd>Engenheiro front-end</dd></div>
              <div><dt>Família</dt><dd>Marido da Joice e pai da Elisa</dd></div>
              <div><dt>Já morou em</dt><dd>Viçosa, Dublin, Joinville, Navegantes e BH</dd></div>
              <div><dt>Não vive sem</dt><dd>Família, rock, um notebook e pão de queijo</dd></div>
            </dl>
          </div>
        </section>
      </div>

      <div class="container container--narrow">
        <div class="sheet">
{bio_html}
          <aside class="mockup-note" style="margin-block-start: var(--space-lg)">Biografia atualizada a partir da "Biografia Autorizada" de 2016 e das respostas do Gui (família, trabalho, Dublin, música e esportes).</aside>
        </div>
      </div>

      <section class="container" aria-labelledby="facts-title">
        <div class="board-title">
          <span class="sticker" style="--r:6deg">{obj("pencil")}</span>
          <h2 id="facts-title">Fatos aleatórios</h2>
        </div>
        <div class="fact-wall">
{facts_html}
        </div>
      </section>

      <section class="container" aria-labelledby="gift-title">
        <div class="sticky-note newsletter-note" style="--r:-1.5deg">
          <span class="sticker" style="--r:10deg; float: right; margin: 0 0 var(--space-xs) var(--space-sm)">{obj("mug")}</span>
          <h2 id="gift-title">Quer me dar um presente?</h2>
          <p>Compre um par de cervejas artesanais e se convide pra bebê-las comigo. Ou dê um disco de vinil de rock: vai direto pro Gradiente! :)</p>
        </div>
      </section>

      <section class="container" aria-labelledby="find-title">
        <div class="board-title">
          <span class="sticker" style="--r:-5deg">{obj("plane")}</span>
          <h2 id="find-title">Onde me encontrar</h2>
        </div>
        <nav class="cluster" style="--cluster-gap: var(--space-md)" aria-label="Redes">
{social_html}
        </nav>
      </section>

      {newsletter()}
    </main>
""" + foot(root)
open(f"{M}/br/sobre.html", "w").write(about_html)

open(f"{M}/br/index.html", "w").write(home)
open(f"{M}/br/blog.html", "w").write(blog)
open(f"{M}/br/idiomas/o-que-te-impede-de-aprender-outro-idioma/index.html", "w").write(post)
print("ok", minutes)
