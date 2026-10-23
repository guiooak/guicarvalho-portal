from common import *
P = posts
css = '''
.book { display:grid; grid-template-columns: 22rem 1fr; gap:var(--space-2xl); padding-block:var(--space-2xl); align-items:start; }
.cover-page { position:sticky; top:6rem; display:grid; gap:var(--space-md); padding:var(--space-lg); border-radius:var(--radius-lg); background:var(--cover-bg); color:var(--cover-fg); min-height:30rem; align-content:space-between; }
.cover-page h1 { color:var(--cover-fg); font-size:2.75rem; line-height:1; }
.cover-page h1 b { font-weight:900; } .cover-page h1 span { font-weight:300; }
.cover-page p { opacity:.9; }
.cover-page .illo { --illo-main:var(--cover-illo-main); --illo-soft:var(--cover-illo-soft); --illo-detail:var(--cover-illo-detail); display:flex; gap:.75rem; }
.cover-page .illo svg { width:46px; height:46px; }
.cover-page .button { --button-bg:var(--cover-fg); --button-fg:var(--cover-bg); --button-border:var(--cover-fg); }
.toc h2 { font-size:var(--text-xs); text-transform:uppercase; letter-spacing:.12em; color:var(--color-text-muted); margin-bottom:var(--space-sm); }
.chapter { margin-bottom:var(--space-xl); }
.chapter > h3 { display:flex; align-items:baseline; gap:.75rem; font-size:var(--text-xl); padding-bottom:.4rem; border-bottom:3px solid var(--color-heading); margin-bottom:.5rem; }
.chapter > h3 em { font-style:normal; font-family:var(--font-mono); font-size:var(--text-sm); color:var(--color-accent); }
.entry { position:relative; display:flex; align-items:baseline; gap:.5rem; padding-block:.55rem; color:var(--color-heading); text-decoration:none; font-weight:700; }
.entry .t { flex:none; max-width:75%; }
.entry .dots { flex:1; border-bottom:2px dotted var(--color-border-input); translate:0 -4px; }
.entry .pg { flex:none; font-family:var(--font-mono); font-size:var(--text-xs); color:var(--color-text-muted); }
.entry:hover { color:var(--color-accent); }
.entry .peek { position:absolute; right:6rem; top:50%; width:11rem; aspect-ratio:3/2; object-fit:cover; border-radius:12px; box-shadow:var(--shadow-card-hover); opacity:0; translate:0 -50%; scale:.9; rotate:-3deg; pointer-events:none; transition: opacity var(--duration-fast), scale var(--duration-base) var(--ease-bounce); z-index:3; }
.entry:hover .peek { opacity:1; scale:1; }
@media (max-width: 56rem) { .book { grid-template-columns:1fr; } .cover-page { position:static; min-height:auto; } .entry .peek { display:none; } .entry .t { max-width:80%; } }
'''
chapters = [("I", "Vida", ["Viva", "Homenagens", "Presepadas"]), ("II", "Mundo afora", ["Irlanda", "Viagens", "Idiomas", "Músicas"]), ("III", "Crescer", ["Coaching", "Inspiração", "Liderança", "Gestão de tempo", "Empreendedorismo", "Casos de Sucesso", "Princípios Básicos", "Geral"])]
seen = set(); out = []; page_no = 1
for num, name, cs in chapters:
    items = [p for p in P if p["cat"] in cs and p["slug"] not in seen]
    for p in items: seen.add(p["slug"])
    rows = []
    for p in items:
        rows.append(f'<a class="entry" href="{href(p)}"><span class="t">{e(p["title"])}</span><span class="dots"></span><span class="pg">{p["date"][:4]}</span><img class="peek" src="{cover(p)}" alt="" loading="lazy"></a>')
    out.append(f'<section class="chapter"><h3><em>{num}</em>{name}</h3>{"".join(rows)}</section>')
apps = '<section class="chapter"><h3><em>IV</em>Apps</h3>' + "".join(f'<a class="entry" href="#"><span class="t">{n}</span><span class="dots"></span><span class="pg">app</span></a>' for n in ["Nome do app", "Outro app", "Mais um app"]) + '</section>'
about = '<section class="chapter"><h3><em>V</em>Sobre o autor</h3><a class="entry" href="#"><span class="t">Quem é o Gui</span><span class="dots"></span><span class="pg">sobre</span></a><a class="entry" href="#newsletter"><span class="t">Receber os próximos capítulos por e-mail</span><span class="dots"></span><span class="pg">✉️</span></a></section>'
body = f'''
      <div class="container">
        <div class="book">
          <aside class="cover-page">
            <div class="illo">{obj("pencil")}{obj("mug")}{obj("clover")}</div>
            <div class="stack" style="--stack-gap: var(--space-sm)">
              <h1><b>gui</b><span>carvalho</span></h1>
              <p>Um livro em construção desde 2015: histórias, metas, idiomas e os apps que eu faço. Escolha um capítulo.</p>
            </div>
            <a class="button" href="#">Começar pelo último post</a>
          </aside>
          <nav class="toc" aria-label="Sumário">
            <h2>Sumário</h2>
            {"".join(out)}{apps}{about}
          </nav>
        </div>
        <aside class="mockup-note">Conceito Índice: o portal é um livro. A home é o sumário, com capítulos que agrupam as categorias, linhas pontilhadas e o ano no lugar da página. Passe o mouse num título para "espiar" a capa do post.</aside>
      </div>
'''
open(f"{OUT}/indice.html", "w").write(page("Índice", "5 · Índice", "o portal como o sumário de um livro", body, css))
print("ok")
