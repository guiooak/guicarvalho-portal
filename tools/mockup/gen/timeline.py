from common import *
from collections import OrderedDict
P = posts
css = '''
.intro { display:grid; grid-template-columns: 1.3fr 1fr; gap:var(--space-xl); align-items:center; padding-block:var(--space-2xl) var(--space-xl); }
.intro h1 { font-size:clamp(2.5rem, 1.8rem + 3vw, 4.5rem); line-height:1.02; }
.intro p { font-size:var(--text-md); color:var(--color-text-muted); max-width:40ch; margin-top:var(--space-sm); }
.chapters { display:grid; gap:.25rem; padding:var(--space-md); border-radius:var(--radius-lg); background:var(--color-surface); border:1px solid var(--color-border); }
.chapters h2 { font-size:var(--text-xs); text-transform:uppercase; letter-spacing:.1em; color:var(--color-text-muted); margin-bottom:.5rem; }
.chapters a { display:grid; grid-template-columns:4rem 1fr; gap:.5rem; padding:.5rem .6rem; border-radius:12px; color:var(--color-heading); text-decoration:none; font-weight:700; }
.chapters a:hover { background:var(--color-accent-soft); }
.chapters a span { font-family:var(--font-mono); color:var(--color-accent); font-weight:800; }
.filters { display:flex; flex-wrap:wrap; gap:.4rem; justify-content:center; padding-block:var(--space-md); position:sticky; top:4.5rem; z-index:2; background:color-mix(in srgb, var(--color-bg) 92%, transparent); backdrop-filter:blur(8px); }
.tl { position:relative; padding-block:var(--space-lg) var(--space-2xl); }
.tl::before { content:""; position:absolute; left:50%; top:0; bottom:0; width:4px; translate:-50% 0; border-radius:4px; background:repeating-linear-gradient(var(--color-accent) 0 14px, transparent 14px 22px); opacity:.6; }
.year { position:relative; display:grid; place-items:center; margin-block:var(--space-xl) var(--space-md); }
.year span { padding:.35em 1.1em; border-radius:999px; background:var(--color-accent); color:var(--color-on-accent); font-size:var(--text-lg); font-weight:900; letter-spacing:-.02em; }
.item { position:relative; display:grid; grid-template-columns:1fr 1fr; gap:3.5rem; margin-block:var(--space-md); }
.item::after { content:""; position:absolute; left:50%; top:1.75rem; width:18px; height:18px; translate:-50% 0; border-radius:50%; background:var(--color-bg); border:4px solid var(--color-accent); }
.card { display:grid; grid-template-columns:7rem 1fr; gap:var(--space-sm); align-items:center; padding:var(--space-sm); border-radius:22px; background:var(--color-surface); border:1px solid var(--color-border); color:inherit; text-decoration:none; font-weight:inherit; transition: translate var(--duration-base) var(--ease-bounce), box-shadow var(--duration-base); }
.card:hover { translate:0 -3px; box-shadow:var(--shadow-card-hover); color:inherit; }
.card img { width:7rem; aspect-ratio:1; object-fit:cover; border-radius:16px; }
.card strong { display:block; color:var(--color-heading); font-size:var(--text-md); line-height:1.2; letter-spacing:-.01em; }
.card small { color:var(--color-text-muted); font-size:var(--text-xs); }
.item.l .card { grid-column:1; } .item.r .card { grid-column:2; }
.milestone { position:relative; display:grid; place-items:center; margin-block:var(--space-lg); }
.milestone div { display:flex; align-items:center; gap:.75rem; padding:.75rem 1.25rem; border-radius:20px; background:var(--color-accent-soft); color:var(--color-accent-soft-text); font-weight:800; border:2px dashed var(--color-accent); }
.milestone svg { width:40px; height:40px; }
.milestone.app div { background:var(--cover-bg); color:var(--cover-fg); border-style:solid; }
@media (max-width: 52rem) {
  .intro { grid-template-columns:1fr; }
  .tl::before { left:14px; }
  .item { grid-template-columns:1fr; gap:0; padding-left:2.5rem; }
  .item::after { left:14px; }
  .item.l .card, .item.r .card { grid-column:1; }
  .year, .milestone { justify-items:start; padding-left:0; }
  .card { grid-template-columns:5rem 1fr; } .card img { width:5rem; }
}
'''
years = OrderedDict()
for p in sorted(P, key=lambda p: p["date"], reverse=True):
    years.setdefault(p["date"][:4], []).append(p)
milestones = {"2021": ("app", "clock", "Lancei o app de metas pessoais"), "2016": ("life", "plane", "De volta ao Brasil"), "2015": ("life", "clover", "Mudança para a Irlanda")}
parts = []
i = 0
for y, ps in years.items():
    parts.append(f'<div class="year" id="y{y}"><span>{y}</span></div>')
    for p in ps:
        i += 1
        parts.append(f'<div class="item {"l" if i % 2 else "r"}"><a class="card" href="{href(p)}"><img src="{cover(p)}" alt="" loading="lazy"><div><span class="eyebrow">{e(p["cat"])}</span><strong>{e(p["title"])}</strong><small>{fdate(p["date"])}</small></div></a></div>')
    if y in milestones:
        kind, o, label = milestones[y]
        parts.append(f'<div class="milestone {"app" if kind=="app" else ""} illo"><div>{obj(o)}{e(label)}</div></div>')
chap = "".join(f'<a href="#y{y}"><span>{y}</span>{len(ps)} post{"s" if len(ps)>1 else ""}</a>' for y, ps in years.items())
filters = '<a class="tag" aria-current="page" href="#">Tudo</a>' + "".join(f'<a class="tag" href="#">{e(c["name"])}</a>' for c in cats[:8])
body = f'''
      <div class="container">
        <section class="intro">
          <div>
            <span class="eyebrow">Oi, eu sou o Gui 👋</span>
            <h1>Uma vida contada em <span class="scribble">posts</span>.</h1>
            <p>Da faculdade em Viçosa à Irlanda e de volta, com metas, idiomas, presepadas e os apps que fui construindo pelo caminho.</p>
          </div>
          <nav class="chapters" aria-label="Anos"><h2>Capítulos</h2>{chap}</nav>
        </section>
        <nav class="filters" aria-label="Filtrar por tema">{filters}</nav>
        <section class="tl" aria-label="Linha do tempo">
          {"".join(parts)}
        </section>
        <aside class="mockup-note">Conceito Linha do tempo: home e blog são a mesma história contada por ano, com os posts alternando dos dois lados e marcos de vida e de apps no meio. Os marcos ("Mudança para a Irlanda", "De volta ao Brasil", o app) são ilustrativos e precisam dos fatos reais.</aside>
      </div>
'''
open(f"{OUT}/linha-do-tempo.html", "w").write(page("Linha do tempo", "3 · Linha do tempo", "a vida contada em posts, por ano", body, css))
print("ok")
