from common import *
P = posts
css = '''
body { background-color:var(--color-bg); background-image:radial-gradient(light-dark(var(--gray-300), var(--gray-800)) 1.2px, transparent 1.2px); background-size:22px 22px; }
.site-header { background:color-mix(in srgb, var(--color-bg) 92%, transparent); }
.desk { position:relative; display:grid; grid-template-columns:1.1fr 1fr; gap:var(--space-xl); align-items:center; padding-block:var(--space-2xl); }
.desk h1 { font-size:clamp(2.75rem, 2rem + 3vw, 4.75rem); line-height:1; }
.desk p { font-size:var(--text-md); color:var(--color-text-muted); max-width:36ch; margin-block:var(--space-sm) var(--space-md); }
.pile { position:relative; min-height:34rem; }
.polaroid { position:absolute; display:block; width:min(17rem, 60%); padding:12px 12px 16px; background:#fff; color:#262626; border-radius:6px; box-shadow:0 10px 30px rgb(0 0 0 / .14); rotate:var(--r); text-decoration:none; font-weight:inherit; transition: rotate var(--duration-base) var(--ease-bounce), scale var(--duration-base) var(--ease-bounce), z-index 0s; }
.polaroid:hover { rotate:0deg; scale:1.04; z-index:5; color:#262626; }
.polaroid img { aspect-ratio:1; object-fit:cover; width:100%; border-radius:2px; }
.polaroid strong { display:block; margin-top:.6rem; font-size:var(--text-sm); line-height:1.25; color:#0c0c0c; }
.polaroid small { font-size:var(--text-xs); color:#545454; }
.polaroid::before { content:""; position:absolute; top:-12px; left:50%; width:84px; height:26px; translate:-50% 0; rotate:-4deg; background:rgb(165 197 165 / .7); border-radius:2px; }
.sticky { position:absolute; width:12rem; aspect-ratio:1; padding:1rem; background:#fff3a8; color:#3b3200; rotate:5deg; box-shadow:0 8px 20px rgb(0 0 0 / .12); font-weight:800; line-height:1.3; clip-path:polygon(0 0, 100% 0, 100% 82%, 82% 100%, 0 100%); }
.sticky small { display:block; margin-top:.5rem; font-weight:600; }
.sticker { display:inline-grid; place-items:center; width:4.5rem; height:4.5rem; border-radius:50%; background:var(--color-accent-soft); outline:5px solid var(--color-bg); box-shadow:0 4px 12px rgb(0 0 0 / .12); rotate:var(--r, -8deg); }
.sticker svg { width:2.75rem; height:2.75rem; }
.board-title { display:flex; align-items:center; gap:1rem; margin-block:var(--space-xl) var(--space-lg); }
.board-title h2 { font-size:var(--text-2xl); }
.wall { display:grid; grid-template-columns:repeat(auto-fill, minmax(15rem, 1fr)); gap:var(--space-xl) var(--space-lg); padding-block:var(--space-md) var(--space-2xl); }
.wall .polaroid { position:relative; width:100%; }
.wall .polaroid:nth-child(3n+1) { --r:-2.5deg; } .wall .polaroid:nth-child(3n+2) { --r:1.8deg; } .wall .polaroid:nth-child(3n) { --r:-1deg; }
.cat-sticker { position:absolute; top:-14px; right:-10px; padding:.25em .7em; border-radius:999px; background:var(--color-accent); color:var(--color-on-accent); font-size:var(--text-xs); font-weight:800; rotate:6deg; box-shadow:0 3px 8px rgb(0 0 0 / .15); }
.apps-shelf { display:flex; flex-wrap:wrap; gap:var(--space-lg); align-items:center; padding:var(--space-lg); border-radius:var(--radius-lg); background:var(--color-bg); border:2px dashed var(--color-border-input); }
.apps-shelf .app { display:flex; align-items:center; gap:.75rem; color:var(--color-heading); font-weight:800; text-decoration:none; }
.apps-shelf .app small { display:block; font-weight:600; color:var(--color-text-muted); }
.note-news { position:relative; max-width:34rem; margin:var(--space-2xl) auto; padding:var(--space-lg); background:#fff3a8; color:#3b3200; rotate:-1.2deg; box-shadow:0 10px 30px rgb(0 0 0 / .12); }
.note-news h2 { color:#3b3200; font-size:var(--text-xl); }
.note-news form { display:flex; flex-wrap:wrap; gap:.5rem; margin-top:var(--space-sm); }
.note-news .input { flex:1 1 12rem; background:#fffbe0; color:#3b3200; border-color:#a08a2c; }
@media (max-width: 52rem) { .desk { grid-template-columns:1fr; } }
.pile .me { left:0; top:3rem; width:min(15rem, 44%); z-index:1; }
.pile .me figcaption { display:block; }
.pile .who { position:absolute; right:2%; top:0; width:min(15rem, 46%); aspect-ratio:auto; padding:1.1rem 1.1rem 1.6rem; rotate:4deg; font-weight:600; z-index:2; }
.who-title, .tabs-title { display:block; font-size:var(--text-xs); font-weight:900; text-transform:uppercase; letter-spacing:.08em; margin-bottom:.4rem; }
.who ul { margin:0; padding-left:1.1rem; font-size:var(--text-sm); line-height:1.45; }
.who li::marker { content:"✓  "; font-weight:900; }
.tabs { position:absolute; right:0; top:14rem; display:grid; gap:.6rem; width:min(16.5rem, 50%); z-index:3; }
.tabs-title { color:var(--color-text-muted); margin:0 0 .1rem .3rem; }
.tab-card { display:flex; align-items:center; gap:.75rem; padding:.6rem .9rem .6rem .6rem; border-radius:14px; background:var(--color-bg); border:1px solid var(--color-border); box-shadow:0 6px 16px rgb(0 0 0 / .08); rotate:var(--r); color:var(--color-heading); text-decoration:none; font-weight:inherit; transition: rotate var(--duration-base) var(--ease-bounce), translate var(--duration-base) var(--ease-bounce); }
.tab-card:hover { rotate:0deg; translate:-6px 0; color:var(--color-heading); }
.tab-card .sticker { width:2.75rem; height:2.75rem; outline-width:3px; rotate:0deg; box-shadow:none; }
.tab-card .sticker svg { width:1.7rem; height:1.7rem; }
.tab-card b { display:block; font-weight:900; }
.tab-card small { color:var(--color-text-muted); font-size:var(--text-xs); }
.pile .deco { position:absolute; left:18%; bottom:0; z-index:0; }
@media (max-width: 52rem) {
  .pile { min-height:0; display:grid; gap:var(--space-lg); justify-items:center; padding-top:var(--space-md); }
  .pile .me, .pile .who, .tabs { position:relative; inset:auto; width:min(20rem, 90%); }
  .pile .deco { display:none; }
}

'''
pile = f'''
            <figure class="polaroid me" style="--r:-5deg"><img src="{ROOT}assets/images/about/gui-paris.jpg" alt="Gui sorrindo em Paris"><figcaption><strong>Esse sou eu</strong><small>Paris, 2016</small></figcaption></figure>
            <div class="sticky who"><span class="who-title">Quem escreve aqui</span><ul><li>Mineiro de Ipatinga</li><li>Cientista da computação pela UFV</li><li>Morei um ano em Dublin</li><li>Rock, pedal e cerveja artesanal</li></ul></div>
            <nav class="tabs illo" aria-label="O que tem por aqui">
              <span class="tabs-title">O que tem por aqui</span>
              <a class="tab-card" href="#" style="--r:-2deg"><span class="sticker">{obj("pencil")}</span><span><b>Blog</b><small>23 histórias desde 2015</small></span></a>
              <a class="tab-card" href="#" style="--r:1.5deg"><span class="sticker">{obj("laptop")}</span><span><b>Apps</b><small>Coisas que eu construí</small></span></a>
              <a class="tab-card" href="#" style="--r:-1deg"><span class="sticker">{obj("bulb")}</span><span><b>Sobre</b><small>A biografia autorizada</small></span></a>
            </nav>
            <span class="sticker illo deco" style="--r:12deg">{obj("clover")}</span>'''
wall = "".join(f'<a class="polaroid" href="{href(p)}"><span class="cat-sticker">{e(p["cat"])}</span><img src="{cover(p)}" alt="" loading="lazy"><strong>{e(p["title"])}</strong><small>{sdate(p["date"])}</small></a>' for p in P[:9])
body = f'''
      <div class="container">
        <section class="desk">
          <div>
            <h1>Oi, eu sou o <span class="scribble">Gui</span>.</h1>
            <p>Este é o meu caderno: histórias, metas, idiomas, viagens e os apps que eu construo, colados aqui desde 2015.</p>
            <div class="cluster"><a class="button" href="#">Folhear o blog</a><a class="button button--secondary" href="#">Meus apps</a></div>
          </div>
          <div class="pile">{pile}
          </div>
        </section>

        <div class="board-title"><span class="sticker illo" style="--r:8deg">{obj("laptop")}</span><h2>Coisas que eu construí</h2></div>
        <div class="apps-shelf illo">
          <a class="app" href="#"><span class="sticker" style="--r:-6deg">{obj("clock")}</span><span>Nome do app<small>O que ele faz</small></span></a>
          <a class="app" href="#"><span class="sticker" style="--r:5deg">{obj("bulb")}</span><span>Outro app<small>O que ele faz</small></span></a>
          <a class="app" href="#"><span class="sticker" style="--r:-3deg">{obj("note")}</span><span>Mais um app<small>O que ele faz</small></span></a>
        </div>

        <div class="board-title"><span class="sticker illo" style="--r:-6deg">{obj("plane")}</span><h2>Do blog</h2></div>
        <div class="wall">{wall}</div>

        <div class="note-news">
          <h2>Quer receber o próximo post? ✉️</h2>
          <p>Deixa seu e-mail aqui no bilhete. Sem spam, prometo.</p>
          <form onsubmit="return false"><input class="input" type="email" placeholder="seu@email.com" aria-label="Seu e-mail"><button class="button">Colar meu e-mail</button></form>
        </div>
        <aside class="mockup-note">Conceito Caderno: o portal parece um caderno pessoal em papel pontilhado, com posts como polaroids coladas com fita, adesivos com as ilustrações, post-its e um bilhete para a newsletter. As fotos se endireitam ao passar o mouse.</aside>
      </div>
'''
open(f"{OUT}/caderno.html", "w").write(page("Caderno", "4 · Caderno", "um caderno pessoal com polaroids e adesivos", body, css))
print("ok")
