import os
from common import *
P = posts
css = '''
.bento { display:grid; gap:var(--space-sm); grid-template-columns:repeat(4, 1fr); grid-auto-rows:minmax(11rem, auto); grid-auto-flow:dense; padding-block:var(--space-lg) var(--space-2xl); }
.tile { position:relative; overflow:hidden; display:flex; flex-direction:column; gap:var(--space-2xs); padding:var(--space-md); border-radius:28px; background:var(--color-surface); border:1px solid var(--color-border); color:var(--color-text); text-decoration:none; font-weight:inherit; transition: translate var(--duration-base) var(--ease-bounce), rotate var(--duration-base) var(--ease-bounce), box-shadow var(--duration-base); }
a.tile:hover { translate:0 -4px; rotate:-.6deg; box-shadow:var(--shadow-card-hover); color:var(--color-text); }
.tile h2, .tile h3 { letter-spacing:var(--tracking-tight); }
.t-intro { grid-column:span 2; grid-row:span 2; justify-content:flex-end; background:var(--color-accent-soft); border-color:transparent; }
.t-intro h1 { font-size:clamp(2.5rem, 2rem + 2.5vw, 4rem); line-height:1.02; }
.t-intro p { font-size:var(--text-md); color:var(--color-accent-soft-text); max-width:30ch; }
.t-intro .illo svg { position:absolute; width:64px; height:64px; }
.t-photo { grid-column:span 2; grid-row:span 2; padding:0; justify-content:flex-end; border:0; }
.t-photo img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; transition: scale var(--duration-base) var(--ease-standard); }
a.t-photo:hover img { scale:1.04; }
.t-photo .shade { position:relative; padding:var(--space-md); padding-top:5rem; background:linear-gradient(transparent, rgb(0 0 0 / .78)); color:#fff; }
.t-photo .shade h3 { color:#fff; font-size:var(--text-xl); }
.t-photo .chip { display:inline-block; margin-bottom:.5rem; padding:.2em .7em; border-radius:999px; background:rgb(255 255 255 / .9); color:#0c0c0c; font-size:var(--text-xs); font-weight:800; }
.t-small-photo { grid-column:span 1; grid-row:span 2; }
.t-small-photo h3 { font-size:var(--text-md) !important; }
.t-stat { justify-content:space-between; background:var(--cover-bg); color:var(--cover-fg); border:0; }
.t-stat strong { font-size:4.5rem; line-height:1; font-weight:900; letter-spacing:-.04em; color:var(--cover-fg); }
.t-now { gap:var(--space-xs); }
.t-now dl { display:grid; gap:.5rem; font-size:var(--text-sm); }
.t-now dt { font-size:var(--text-xs); font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--color-accent); }
.t-now dd { margin:0; color:var(--color-heading); font-weight:700; }
.t-map { background:var(--color-bg); justify-content:space-between; }
.t-map .route { display:flex; align-items:center; gap:.5rem; font-weight:800; color:var(--color-heading); font-size:var(--text-md); }
.t-map .route i { flex:1; border-top:3px dashed var(--color-accent); }
.t-map .illo { display:flex; justify-content:space-between; }
.t-map .illo svg { width:52px; height:52px; }
.t-app { background:var(--color-bg); }
.t-app .icon { width:3.25rem; height:3.25rem; border-radius:16px; display:grid; place-items:center; background:var(--color-accent-soft); }
.t-app .icon svg { width:2.2rem; height:2.2rem; }
.t-app h3 { font-size:var(--text-md); letter-spacing:0; margin-top:auto; }
.t-app p { font-size:var(--text-sm); color:var(--color-text-muted); }
.t-topics { grid-column:span 2; }
.t-topics .cluster { --cluster-gap:.4rem; }
.t-news { grid-column:span 2; background:var(--color-heading); color:var(--color-bg); border:0; justify-content:space-between; }
.t-news h3 { color:var(--color-bg); font-size:var(--text-xl); }
.t-news form { display:flex; gap:.5rem; flex-wrap:wrap; }
.t-news .input { flex:1 1 12rem; background:transparent; color:var(--color-bg); border-color:var(--gray-500); }
.t-news .button { --button-bg:var(--color-accent); }
.label { font-size:var(--text-xs); font-weight:800; text-transform:uppercase; letter-spacing:.06em; color:var(--color-text-muted); }
.t-stat .label { color:var(--cover-fg); opacity:.85; }
.blog-head { display:flex; flex-wrap:wrap; align-items:end; justify-content:space-between; gap:1rem; margin-top:var(--space-xl); }
@media (max-width: 60rem) { .bento { grid-template-columns:repeat(2, 1fr); } }
@media (max-width: 36rem) { .bento { grid-template-columns:1fr; } .bento > * { grid-column:auto !important; grid-row:auto !important; } .t-photo { min-height:20rem; } .t-intro { min-height:24rem; } }
'''
def photo(p, cls="t-photo"):
    return f'''<a class="tile t-photo {cls}" href="{href(p)}"><img src="{cover(p)}" alt="" loading="lazy"><div class="shade"><span class="chip">{e(p['cat'])}</span><h3>{e(p['title'])}</h3><span class="text-sm" style="opacity:.85">{fdate(p['date'])}</span></div></a>'''
tags = "".join(f'<a class="tag" href="#">{e(c["name"])}</a>' for c in cats)
body = f'''
      <div class="container">
        <section class="bento" aria-label="Destaques">
          <div class="tile t-intro">
            <div class="illo" aria-hidden="true">{obj("laptop", style="top:8%;right:10%;rotate:-10deg")}{obj("mug", style="top:30%;right:32%;rotate:8deg;width:48px;height:48px")}{obj("plane", style="top:12%;left:8%;rotate:-6deg;width:52px;height:52px")}</div>
            <span class="label">Oi! 👋</span>
            <h1>Eu sou o <span class="scribble">Gui</span>.</h1>
            <p>Mineiro, dev e curioso. Escrevo sobre a vida e construo apps.</p>
            <div class="cluster"><a class="button" href="#">Ler o blog</a><a class="button button--secondary" href="#">Meus apps</a></div>
          </div>
          {photo(P[0])}
          <div class="tile t-stat"><span class="label">No blog</span><strong>23</strong><span>posts desde 2015</span></div>
          <div class="tile t-now"><span class="label">Agora</span><dl><div><dt>Construindo</dt><dd>Este portal novo</dd></div><div><dt>Lendo</dt><dd>Um livro bacana</dd></div><div><dt>Ouvindo</dt><dd>Foo Fighters, sempre</dd></div></dl></div>
          <div class="tile t-map"><span class="label">De onde escrevo</span><div class="illo">{obj("clover")}{obj("plane")}{obj("mug")}</div><div class="route">Minas <i></i> Irlanda</div></div>
          <a class="tile t-app" href="#"><span class="icon illo">{obj("clock")}</span><h3>Nome do app</h3><p>O que ele faz, em uma frase.</p></a>
          {photo(P[1], "t-photo t-small-photo")}
          {photo(P[3], "t-photo t-small-photo")}
          <a class="tile t-app" href="#"><span class="icon illo">{obj("bulb")}</span><h3>Outro app</h3><p>O que ele faz, em uma frase.</p></a>
          <div class="tile t-topics"><span class="label">Sobre o que eu escrevo</span><div class="cluster">{tags}</div></div>
          <div class="tile t-news"><span class="label" style="color:inherit;opacity:.7">Newsletter</span><h3>Um e-mail quando sair post novo ✉️</h3><form onsubmit="return false"><input class="input" type="email" placeholder="seu@email.com" aria-label="Seu e-mail"><button class="button">Inscrever</button></form></div>
        </section>
        <aside class="mockup-note">Conceito Bento: a home vira um painel de blocos de tamanhos diferentes, cada um com um tipo de conteúdo (apresentação, post em destaque, números, "agora", origem, apps, temas, newsletter). Os blocos "Agora", "De onde escrevo" e os apps têm conteúdo provisório.</aside>
      </div>
'''
os.makedirs(OUT, exist_ok=True)
open(f"{OUT}/bento.html", "w").write(page("Bento", "1 · Bento", "a home como um painel de blocos", body, css))
print("ok")
