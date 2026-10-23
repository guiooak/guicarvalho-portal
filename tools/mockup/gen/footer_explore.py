"""Exploration: three footer options. Writes mockup/explorations/rodape.html (pt only)."""
from common import MOCKUP

ROOT = "../"
YEAR = "2026"

# Small single-color social glyphs (24x24, currentColor).
ICON = {
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="4" fill="currentColor"/><path d="M7 10v7M7 7v.01M11 17v-4.2c0-1.6 1-2.8 2.5-2.8S16 11.2 16 12.8V17M11 10v7" stroke="var(--icon-cut, #fff)" stroke-width="2" stroke-linecap="round" fill="none"/></svg>',
    "github": '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-3.2 19.5c.5.1.7-.2.7-.5v-1.8c-2.8.6-3.4-1.2-3.4-1.2-.5-1.2-1.1-1.5-1.1-1.5-.9-.6.1-.6.1-.6 1 .1 1.6 1 1.6 1 .9 1.6 2.4 1.1 3 .9.1-.7.4-1.1.6-1.4-2.2-.3-4.6-1.1-4.6-5 0-1.1.4-2 1-2.7-.1-.3-.4-1.3.1-2.7 0 0 .8-.3 2.8 1a9.6 9.6 0 0 1 5 0c1.9-1.3 2.8-1 2.8-1 .5 1.4.2 2.4.1 2.7.6.7 1 1.6 1 2.7 0 3.9-2.4 4.7-4.6 5 .4.3.7.9.7 1.9V21c0 .3.2.6.7.5A10 10 0 0 0 12 2Z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="1.5" y="5" width="21" height="14" rx="4.5" fill="currentColor"/><path d="M10 9v6l5-3Z" fill="var(--icon-cut, #fff)"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5.5" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="17.3" cy="6.7" r="1.3" fill="currentColor"/></svg>',
    "rss": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 11a8 8 0 0 1 8 8M5 5a14 14 0 0 1 14 14" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/><circle cx="6" cy="18" r="1.8" fill="currentColor"/></svg>',
}
SOCIAL = [("LinkedIn", "linkedin", "https://www.linkedin.com/in/linkguicarvalho"), ("GitHub", "github", "https://github.com/guiooak"),
          ("YouTube", "youtube", "https://youtube.com/c/GuilhermeCarvalhoOnline"), ("Instagram", "instagram", "https://www.instagram.com/guicarvalho.com.br")]


def obj(n):
    return f'<svg aria-hidden="true"><use href="#obj-{n}"/></svg>'


def brand(cls=""):
    return (f'<a class="brand {cls}" href="{ROOT}br/index.html"><svg class="brand__symbol" aria-hidden="true"><use href="#logo-acorn"/></svg>'
            '<span><span class="brand__first">gui</span><span class="brand__last">carvalho</span></span></a>')


def links(items):
    return "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in items)


PORTAL = [("Início", f"{ROOT}br/index.html"), ("Blog", f"{ROOT}br/blog.html"), ("Apps", f"{ROOT}br/apps.html"), ("Sobre", f"{ROOT}br/sobre.html")]
BLOG = [("Vida", f"{ROOT}br/vida/"), ("Tech", f"{ROOT}br/tech/"), ("Buscar", f"{ROOT}br/busca.html"), ("RSS", "#")]
social_icons = "".join(f'<a class="social-dot" href="{h}" aria-label="{n}">{ICON[i]}</a>' for n, i, h in SOCIAL)
social_list = "".join(f'<li><a href="{h}">{ICON[i]}{n}</a></li>' for n, i, h in SOCIAL)

# ---------------------------------------------------------------- A: back cover
A = f'''
    <footer class="fa">
      <div class="container fa__inner">
        <div class="fa__sign">
          {brand("fa__brand")}
          <p class="fa__line">Obrigado por folhear o caderno.</p>
          <p class="fa__sub">Histórias, metas, idiomas e os apps que eu construo, colados aqui desde 2015.</p>
          <a class="fa__cta" href="#">✉️ Receber os próximos posts</a>
        </div>
        <nav class="fa__cols" aria-label="Rodapé">
          <div><h3>Portal</h3><ul role="list">{links(PORTAL)}</ul></div>
          <div><h3>Blog</h3><ul role="list">{links(BLOG)}</ul></div>
          <div><h3>Redes</h3><ul role="list" class="fa__social">{social_list}</ul></div>
        </nav>
      </div>
      <div class="container fa__bottom">
        <span>© {YEAR} Guilherme Carvalho</span>
        <a href="{ROOT}en/index.html" hreflang="en" lang="en">English version</a>
        <span class="legal"><a href="#">Política de privacidade</a> · <a href="#">Política de cookies</a></span>
        <span>Feito com Rails, CSS puro e um pouco de café ☕</span>
      </div>
      <svg class="fa__acorn" aria-hidden="true"><use href="#logo-acorn"/></svg>
    </footer>'''

# ---------------------------------------------------------------- B: farewell note
B = f'''
    <footer class="fb">
      <div class="container">
        <div class="fb__desk">
          <figure class="polaroid fb__photo" style="--r:-5deg">
            <img src="{ROOT}assets/images/about/gui-paris.jpg" alt="" width="768" height="576" loading="lazy">
            <figcaption class="polaroid__caption"><span class="polaroid__title">Até a próxima!</span></figcaption>
          </figure>
          <div class="sticky-note fb__note" style="--r:2deg">
            <span class="sticky-note__title">Um bilhete antes de você ir</span>
            <p>Obrigado pela visita! Se quiser conversar, me acha por aqui:</p>
            <div class="fb__social">{social_icons}</div>
          </div>
          <nav class="fb__cards" aria-label="Rodapé">
            <div class="index-card fb__card" style="--r:-1.5deg"><h3>Portal</h3><ul role="list">{links(PORTAL)}</ul></div>
            <div class="index-card fb__card" style="--r:1.5deg"><h3>Blog</h3><ul role="list">{links(BLOG)}</ul></div>
          </nav>
        </div>
        <div class="fb__bottom">
          {brand()}
          <span>© {YEAR} Guilherme Carvalho · <a href="{ROOT}en/index.html" hreflang="en" lang="en">English</a></span>
          <span class="legal"><a href="#">Política de privacidade</a> · <a href="#">Política de cookies</a></span>
          <span>Feito com Rails, CSS puro e um pouco de café ☕</span>
        </div>
      </div>
    </footer>'''

# ---------------------------------------------------------------- C: big wordmark
C = f'''
    <footer class="fc">
      <div class="container">
        <div class="fc__top">
          <p class="fc__lead">Histórias, metas, idiomas e os apps que eu construo, colados aqui desde 2015.</p>
          <nav class="fc__cols" aria-label="Rodapé">
            <div><h3>Portal</h3><ul role="list">{links(PORTAL)}</ul></div>
            <div><h3>Blog</h3><ul role="list">{links(BLOG)}</ul></div>
            <div><h3>Redes</h3><ul role="list">{links([(n, h) for n, i, h in SOCIAL])}</ul></div>
          </nav>
        </div>
        <a class="fc__word" href="{ROOT}br/index.html" aria-label="gui carvalho, página inicial"><svg class="fc__acorn" aria-hidden="true"><use href="#logo-acorn"/></svg><span class="brand__first">gui</span><span class="brand__last">carvalho</span></a>
        <div class="fc__bottom">
          <span>© {YEAR} Guilherme Carvalho</span>
          <span class="legal"><a href="#">Política de privacidade</a> · <a href="#">Política de cookies</a></span>
          <span class="fc__langs"><a href="{ROOT}br/index.html" aria-current="true">Português</a> · <a href="{ROOT}en/index.html" hreflang="en" lang="en">English</a></span>
          <span>Feito com Rails, CSS puro e um pouco de café ☕</span>
        </div>
      </div>
    </footer>'''

CSS = '''
    @layer mockup {
      .intro { margin-block: var(--space-xl) var(--space-lg); max-width: 46rem; }
      .intro h1 { font-size: var(--text-3xl); }
      .intro p { margin-block-start: var(--space-sm); color: var(--color-text-muted); font-size: var(--text-md); }
      .option-label { display: flex; gap: var(--space-sm); align-items: flex-start; max-width: 48rem; margin-block: calc(var(--space-2xl) * 1.5) var(--space-lg); }
      .option-label > span { flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%; background: #d4a017; color: #1a1400; font-weight: var(--weight-black); }
      .option-label h2 { font-size: var(--text-xl); }
      .option-label p { margin-block-start: 0.25rem; color: var(--color-text-muted); }
      footer h3 { font-size: var(--text-xs); font-weight: var(--weight-black); letter-spacing: var(--tracking-wide); text-transform: uppercase; }
      footer ul { display: grid; gap: 0.45rem; margin: 0; padding: 0; list-style: none; }
      footer svg { flex: none; }

      .legal a { color: inherit; text-decoration: underline; text-decoration-color: currentColor; text-decoration-thickness: 1px; text-underline-offset: 0.2em; font-weight: inherit; }
      .legal a:hover { text-decoration-thickness: 2px; }
      .fa .fa__bottom a { color: var(--sage-100); }

      /* A: back cover. */
      .fa { --icon-cut: var(--sage-800); position: relative; overflow: hidden; padding-block: var(--space-2xl) var(--space-lg); border-radius: 2.5rem 2.5rem 0 0; background-color: var(--sage-800); background-image: radial-gradient(rgb(255 255 255 / 0.06) 1.2px, transparent 1.2px); background-size: 22px 22px; color: var(--sage-100); }
      .fa__inner { position: relative; z-index: 1; display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1.5fr); gap: var(--space-2xl); }
      .fa__brand { --logo-cap: var(--sage-100); --logo-nut: var(--sage-300); color: #ffffff; }
      .fa__brand .brand__first, .fa__brand .brand__last { color: #ffffff; }
      .fa__line { margin-block: var(--space-md) var(--space-xs); color: #ffffff; font-size: var(--text-2xl); font-weight: var(--weight-black); line-height: 1.1; letter-spacing: var(--tracking-tight); text-wrap: balance; }
      .fa__sub { max-width: 34ch; color: var(--sage-200); }
      .fa__cta { display: inline-flex; margin-block-start: var(--space-md); padding: 0.6em 1.2em; border-radius: var(--radius-pill); background: var(--note-bg); color: var(--note-fg); font-weight: var(--weight-black); text-decoration: none; rotate: -1.5deg; box-shadow: 0 6px 16px rgb(0 0 0 / 0.25); transition: rotate var(--duration-base) var(--ease-bounce); }
      .fa__cta:hover { rotate: 0deg; color: var(--note-fg); }
      .fa__cols { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-lg); padding-block-start: var(--space-xs); }
      .fa h3 { margin-block-end: var(--space-sm); color: var(--sage-300); }
      .fa a:not(.fa__cta, .brand) { color: var(--sage-50); font-weight: var(--weight-medium); text-decoration: none; }
      .fa a:not(.fa__cta, .brand):hover { color: #ffffff; text-decoration: underline; text-decoration-color: var(--note-bg); text-underline-offset: 0.25em; }
      .fa__social a { display: inline-flex; align-items: center; gap: 0.5rem; }
      .fa__social svg { width: 1.1rem; height: 1.1rem; color: var(--sage-300); }
      .fa__bottom { position: relative; z-index: 1; display: flex; flex-wrap: wrap; justify-content: space-between; gap: var(--space-sm); margin-block-start: var(--space-2xl); padding-block-start: var(--space-md); border-block-start: 1px solid rgb(255 255 255 / 0.12); color: var(--sage-300); font-size: var(--text-xs); }
      .fa__acorn { --logo-cap: rgb(255 255 255 / 0.05); --logo-nut: rgb(255 255 255 / 0.04); position: absolute; inset-block-end: -3rem; inset-inline-end: -2rem; width: 22rem; height: 22rem; rotate: -14deg; }

      /* B: farewell note on the desk. */
      .fb { position: relative; padding-block: var(--space-2xl) var(--space-lg); }
      .fb::before { content: ""; position: absolute; inset-block-start: 0; inset-inline: 0; height: 14px; background: radial-gradient(circle at 7px 0, transparent 6px, var(--color-border) 6.5px, transparent 7.5px) 0 0 / 22px 14px repeat-x; }
      .fb__desk { display: grid; grid-template-columns: 13rem minmax(0, 1.3fr) minmax(0, 1fr); gap: var(--space-xl); align-items: center; }
      .fb__photo { width: 13rem; }
      .fb__photo img { aspect-ratio: 4 / 5; }
      .fb__note { padding: var(--space-md) var(--space-md) var(--space-lg); }
      .fb__note p { margin-block: var(--space-2xs) var(--space-sm); }
      .fb__social { display: flex; flex-wrap: wrap; gap: var(--space-xs); }
      .social-dot { --icon-cut: #ffffff; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%; background: #ffffff; color: var(--sage-700); box-shadow: 0 3px 8px rgb(0 0 0 / 0.12); transition: translate var(--duration-fast) var(--ease-standard), rotate var(--duration-base) var(--ease-bounce); }
      .social-dot:nth-child(odd) { rotate: -6deg; } .social-dot:nth-child(even) { rotate: 5deg; }
      .social-dot:hover { translate: 0 -3px; rotate: 0deg; color: var(--sage-800); }
      .social-dot svg { width: 1.3rem; height: 1.3rem; }
      .social-dot:has(svg rect[fill="currentColor"]) { --icon-cut: #ffffff; }
      .fb__cards { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-md); }
      .fb__card { display: block; padding: var(--space-sm) var(--space-md); rotate: var(--r, 0deg); }
      .fb__card h3 { margin-block-end: var(--space-xs); padding-block-end: var(--space-2xs); border-block-end: 2px solid var(--color-accent-soft); color: var(--color-accent); }
      .fb__card a { color: var(--color-heading); font-weight: var(--weight-bold); text-decoration: none; }
      .fb__card a:hover { color: var(--color-accent); }
      .fb__bottom { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: var(--space-sm); margin-block-start: var(--space-2xl); padding-block-start: var(--space-md); border-block-start: 1px dashed var(--color-border-input); color: var(--color-text-muted); font-size: var(--text-xs); }

      /* C: big wordmark. */
      .fc { padding-block: var(--space-2xl) var(--space-lg); border-block-start: 1px solid var(--color-border); background: var(--color-bg); }
      .fc__top { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.4fr); gap: var(--space-2xl); align-items: start; }
      .fc__lead { max-width: 26ch; color: var(--color-heading); font-size: var(--text-xl); font-weight: var(--weight-bold); line-height: 1.3; text-wrap: balance; }
      .fc__cols { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-lg); }
      .fc h3 { margin-block-end: var(--space-sm); color: var(--color-text-muted); }
      .fc__cols a { color: var(--color-heading); font-weight: var(--weight-bold); text-decoration: none; }
      .fc__cols a:hover { color: var(--color-accent); }
      .fc__word { display: flex; align-items: center; margin-block: var(--space-2xl) var(--space-md); color: var(--color-heading); font-size: clamp(3rem, 13.5vw, 11.5rem); line-height: 0.9; letter-spacing: -0.045em; text-decoration: none; white-space: nowrap; }
      .fc__word .brand__first { font-weight: var(--weight-black); }
      .fc__word .brand__last { font-weight: 300; }
      .fc__acorn { width: 0.8em; height: 0.8em; margin-inline-end: 0.12em; rotate: -8deg; transition: rotate var(--duration-base) var(--ease-bounce); }
      .fc__word:hover .fc__acorn { rotate: 8deg; }
      .fc__bottom { display: flex; flex-wrap: wrap; justify-content: space-between; gap: var(--space-sm); padding-block-start: var(--space-md); border-block-start: 1px solid var(--color-border); color: var(--color-text-muted); font-size: var(--text-xs); }
      .fc__langs a { color: inherit; text-decoration: none; }
      .fc__langs a[aria-current] { color: var(--color-heading); font-weight: var(--weight-black); }

      @media (max-width: 60rem) {
        .fa__inner, .fc__top { grid-template-columns: minmax(0, 1fr); gap: var(--space-xl); }
        .fb__desk { grid-template-columns: 10rem minmax(0, 1fr); }
        .fb__photo { width: 10rem; }
        .fb__cards { grid-column: 1 / -1; }
      }
      @media (max-width: 36rem) {
        .fa__cols, .fc__cols { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .fb__desk { grid-template-columns: minmax(0, 1fr); }
        .fb__photo { display: none; }
        .fa__acorn { width: 14rem; height: 14rem; }
      }
    }'''


def label(letter, title, desc):
    return f'''
    <div class="container option-label"><span>{letter}</span><div><h2>{title}</h2><p>{desc}</p></div></div>'''


html = f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Rodapé · exploração · gui carvalho</title>
  <link rel="icon" href="{ROOT}assets/images/brand/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{ROOT}assets/stylesheets/application.css?v=2026-10-23a">
  <link rel="stylesheet" href="{ROOT}assets/stylesheets/mockup.css?v=2026-10-23a">
  <script src="{ROOT}assets/javascripts/mockup.js?v=2026-10-23c"></script>
  <style>{CSS}
  </style>
</head>
<body class="paper">
  <div class="site">
    <site-header root="{ROOT}"></site-header>
    <main id="main">
      <div class="container intro">
        <span class="eyebrow">Exploração</span>
        <h1>Três rodapés</h1>
        <p>Todos levam o mesmo conteúdo: marca, uma frase, links do portal e do blog (Vida, Tech, busca, RSS), redes, idioma, as políticas de privacidade e de cookies e o © no fim. Muda o jeito de fechar a página. As duas políticas ainda não têm página.</p>
      </div>
{label("A", "Contracapa", "A página termina na contracapa do caderno: um bloco verde-escuro de ponta a ponta, uma frase de despedida grande, um botão-bilhete para a newsletter e uma bolota enorme e quase invisível no canto.")}
{A}
{label("B", "Bilhete de despedida", "Continua no papel pontilhado, separado por uma linha picotada. Uma polaroid, um post-it com as redes em adesivos redondos e duas fichas com os links.")}
{B}
{label("C", "Assinatura grande", "Limpo e tipográfico: frase e colunas de links em cima, e o nome gui carvalho gigante atravessando a página, como uma assinatura no fim do caderno.")}
{C}
    </main>
  </div>
</body>
</html>
'''
open(f"{MOCKUP}/explorations/rodape.html", "w").write(html)
print("ok")
