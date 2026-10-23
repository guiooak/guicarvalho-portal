import os
from common import *
P = posts
css = '''
.mast { padding-block:var(--space-xl) var(--space-md); border-bottom:3px solid var(--color-heading); display:flex; flex-wrap:wrap; justify-content:space-between; align-items:end; gap:1rem; }
.mast h1 { font-size:clamp(3rem, 1.5rem + 7vw, 7.5rem); line-height:.9; letter-spacing:-.05em; }
.mast h1 b { font-weight:900; } .mast h1 span { font-weight:300; }
.mast p { max-width:24ch; text-align:right; color:var(--color-text-muted); font-size:var(--text-sm); }
.edition { display:flex; flex-wrap:wrap; gap:.5rem 1.5rem; padding-block:.6rem; border-bottom:1px solid var(--color-border); font-size:var(--text-xs); font-weight:800; text-transform:uppercase; letter-spacing:.08em; color:var(--color-text-muted); }
.edition a { color:inherit; text-decoration:none; font-weight:800; } .edition a:hover { color:var(--color-accent); }
.front { display:grid; grid-template-columns: 2fr 1fr; gap:var(--space-xl); padding-block:var(--space-xl); border-bottom:1px solid var(--color-border); }
.lead-story { display:grid; gap:var(--space-sm); }
.lead-story img { aspect-ratio:3/2; object-fit:cover; width:100%; border-radius:var(--radius-card); }
.lead-story h2 { font-size:clamp(2.25rem, 1.5rem + 3vw, 4rem); line-height:1; letter-spacing:-.035em; }
.lead-story h2 a { color:inherit; text-decoration:none; font-weight:inherit; }
.lead-story h2 a:hover { text-decoration:underline; text-decoration-color:var(--color-accent); }
.lead-story p { font-size:var(--text-md); color:var(--color-text-muted); max-width:52ch; }
.side h3 { font-size:var(--text-xs); text-transform:uppercase; letter-spacing:.1em; color:var(--color-text-muted); padding-bottom:.6rem; border-bottom:3px solid var(--color-accent); }
.ranked { list-style:none; padding:0; counter-reset:r; }
.ranked li { counter-increment:r; display:grid; grid-template-columns:3rem 1fr; gap:.25rem 0; padding-block:var(--space-sm); border-bottom:1px solid var(--color-border); }
.ranked li::before { content:counter(r, decimal-leading-zero); font-size:2rem; font-weight:900; color:var(--color-accent); line-height:1; letter-spacing:-.04em; grid-row:span 2; }
.ranked a { color:var(--color-heading); text-decoration:none; font-weight:800; line-height:1.25; }
.ranked a:hover { color:var(--color-accent); }
.ranked small { color:var(--color-text-muted); font-size:var(--text-xs); }
.quote { padding-block:var(--space-2xl); text-align:center; border-bottom:1px solid var(--color-border); }
.quote blockquote { font-size:clamp(1.75rem, 1.2rem + 2.5vw, 3rem); font-style:italic; font-weight:300; line-height:1.2; letter-spacing:-.02em; color:var(--color-heading); max-width:28ch; margin-inline:auto; }
.quote blockquote b { font-weight:800; font-style:normal; color:var(--color-accent); }
.quote cite { display:block; margin-top:1rem; font-style:normal; font-size:var(--text-sm); color:var(--color-text-muted); }
.sections { display:grid; grid-template-columns:repeat(3, 1fr); gap:var(--space-xl); padding-block:var(--space-xl); border-bottom:1px solid var(--color-border); }
.sec h3 { display:flex; justify-content:space-between; align-items:center; font-size:var(--text-lg); padding-bottom:.5rem; border-bottom:3px solid var(--color-heading); margin-bottom:var(--space-sm); }
.sec h3 svg { width:36px; height:36px; }
.sec article { display:grid; grid-template-columns:1fr 5rem; gap:.75rem; padding-block:.75rem; border-bottom:1px dashed var(--color-border); }
.sec article img { width:5rem; aspect-ratio:1; object-fit:cover; border-radius:12px; }
.sec article a { color:var(--color-heading); text-decoration:none; font-weight:800; line-height:1.25; }
.sec article small { display:block; color:var(--color-text-muted); font-size:var(--text-xs); margin-top:.25rem; }
.archive { padding-block:var(--space-xl); }
.archive > h2 { font-size:var(--text-xs); text-transform:uppercase; letter-spacing:.1em; color:var(--color-text-muted); margin-bottom:var(--space-sm); }
.row { display:grid; grid-template-columns:7rem 1fr 9rem 6rem; gap:1rem; align-items:center; padding-block:var(--space-sm); border-top:1px solid var(--color-border); color:inherit; text-decoration:none; font-weight:inherit; transition: padding var(--duration-base) var(--ease-standard), background var(--duration-fast); }
.row:hover { padding-inline:var(--space-sm); background:var(--color-accent-soft); color:inherit; border-radius:12px; }
.row time { font-family:var(--font-mono); font-size:var(--text-xs); color:var(--color-text-muted); }
.row strong { font-size:var(--text-lg); color:var(--color-heading); letter-spacing:-.02em; line-height:1.2; }
.row img { width:6rem; aspect-ratio:3/2; object-fit:cover; border-radius:10px; }
.classifieds { display:grid; grid-template-columns:repeat(3,1fr); gap:0; border:3px solid var(--color-heading); border-radius:var(--radius-lg); overflow:hidden; margin-block:var(--space-xl); }
.classifieds > * { padding:var(--space-md); border-right:1px solid var(--color-border); }
.classifieds > *:last-child { border:0; }
.classifieds h4 { font-size:var(--text-md); letter-spacing:0; } .classifieds p { font-size:var(--text-sm); color:var(--color-text-muted); }
.classifieds .k { font-size:var(--text-xs); font-weight:800; text-transform:uppercase; letter-spacing:.08em; color:var(--color-accent); }
@media (max-width: 56rem) { .front, .sections, .classifieds { grid-template-columns:1fr; } .row { grid-template-columns:1fr 5rem; } .row time, .row .tag { grid-column:1; } .row img { grid-row:1 / span 3; grid-column:2; width:5rem; } .classifieds > * { border-right:0; border-bottom:1px solid var(--color-border); } .mast p { text-align:left; } }
'''
def ranked(ps): return "".join(f'<li><a href="{href(p)}">{e(p["title"])}</a><small>{e(p["cat"])} · {sdate(p["date"])}</small></li>' for p in ps)
def sec(name, o, ps): return f'<section class="sec"><h3>{e(name)} <span class="illo">{obj(o)}</span></h3>' + "".join(f'<article><div><a href="{href(p)}">{e(p["title"])}</a><small>{sdate(p["date"])}</small></div><img src="{cover(p)}" alt="" loading="lazy"></article>' for p in ps) + '</section>'
by = lambda c: [p for p in P if p["cat"] == c]
rows = "".join(f'<a class="row" href="{href(p)}"><time datetime="{p["date"]}">{sdate(p["date"])}</time><strong>{e(p["title"])}</strong><span class="tag">{e(p["cat"])}</span><img src="{cover(p)}" alt="" loading="lazy"></a>' for p in P[:10])
lead = next(p for p in P if p["slug"] == "o-que-te-impede-de-aprender-outro-idioma")
body = f'''
      <div class="container">
        <header class="mast">
          <h1><b>gui</b><span>carvalho</span></h1>
          <p>Histórias, metas, idiomas e os apps que eu construo. Desde 2015, direto de Minas.</p>
        </header>
        <nav class="edition" aria-label="Seções"><span>Nº 24 · Outubro 2026</span>{''.join(f'<a href="#">{e(c["name"])}</a>' for c in cats[:7])}</nav>

        <section class="front">
          <article class="lead-story">
            <span class="eyebrow">Idiomas · Matéria de capa</span>
            <h2><a href="{href(lead)}">{e(lead["title"])}</a></h2>
            <p>{e(lead["excerpt"])}</p>
            <img src="{cover(lead)}" alt="">
          </article>
          <aside class="side">
            <h3>Mais lidos</h3>
            <ol class="ranked">{ranked(P[:5])}</ol>
          </aside>
        </section>

        <section class="quote">
          <blockquote>"De nada vale muita boa vontade <b>sem atitude</b>."</blockquote>
          <cite>— do post "{e(lead["title"])}"</cite>
        </section>

        <div class="sections">
          {sec("Irlanda", "clover", by("Irlanda")[:3])}
          {sec("Viva", "bulb", by("Viva")[:3])}
          {sec("Homenagens", "note", by("Homenagens")[:3])}
        </div>

        <section class="classifieds" aria-label="Apps">
          <div><span class="k">Apps · classificados</span><h4>Coisas que eu construí</h4><p>Projetos que nasceram de problemas meus.</p></div>
          <div><span class="k">App</span><h4>Nome do app</h4><p>O que ele faz, em uma frase.</p></div>
          <div><span class="k">App</span><h4>Outro app</h4><p>O que ele faz, em uma frase.</p></div>
        </section>

        <section class="archive">
          <h2>Arquivo · todos os posts</h2>
          {rows}
        </section>
        <aside class="mockup-note">Conceito Revista: a home é uma "capa de revista" (marca gigante, matéria de capa, mais lidos, citação, seções por categoria) e o blog vira um arquivo em linhas, com data, título grande, categoria e miniatura. A "edição nº 24" e os "mais lidos" são ilustrativos.</aside>
      </div>
'''
open(f"{OUT}/revista.html", "w").write(page("Revista", "2 · Revista", "a home como capa de revista", body, css))
print("ok")
