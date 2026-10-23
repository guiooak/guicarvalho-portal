"""Admin screens: dashboard, posts, editor, comments, subscribers, newsletter."""
import os, re
from common import posts as P, cats, e, S
import pages as pt

OUT = f"{pt.M}/admin"
R = "../"
obj = pt.obj
SRC = next(x for x in P if x["slug"] == "o-que-te-impede-de-aprender-outro-idioma")

NAV = [("index.html", "Painel", "window", None), ("posts.html", "Posts", "pencil", None), ("comentarios.html", "Comentários", "chat", 2),
       ("inscritos.html", "Inscritos", "bulb", None), ("newsletter.html", "Newsletter", "envelope", None)]

def shell(file, title, head_html, main):
    nav = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{obj(o)}{t}{f"<span class=\"admin-nav__count\">{n}</span>" if n else ""}</a>' for f, t, o, n in NAV)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>{e(title)} · Admin · gui carvalho</title>
  <link rel="icon" href="{R}assets/images/brand/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{R}assets/stylesheets/application.css?v=2026-10-23a">
  <link rel="stylesheet" href="{R}assets/stylesheets/mockup.css?v=2026-10-23a">
  <script src="{R}assets/javascripts/mockup.js?v=2026-10-23a"></script>
</head>
<body>
  <div class="admin">
    <aside class="admin-sidebar">
      <a class="brand" href="index.html" style="--brand-size: 1.1rem"><svg class="brand__symbol" aria-hidden="true"><use href="#logo-acorn"/></svg><span><span class="brand__first">gui</span><span class="brand__last">admin</span></span></a>
      <nav class="admin-nav illo" aria-label="Admin">{nav}</nav>
      <a class="button button--small button--secondary" href="{R}br/index.html">Ver o site ↗</a>
      <div class="admin-sidebar__foot"><span class="avatar avatar--sm"><img src="{R}assets/images/about/gui-paris.jpg" alt=""></span><div><strong>Gui Carvalho</strong>Admin · <a href="#">sair</a></div></div>
    </aside>
    <main class="admin-main" id="main">
      <header class="admin-head">{head_html}</header>
{main}
    </main>
  </div>
  <div class="mockup-toolbar" aria-label="Ferramentas do mockup">
    <button type="button" data-theme-toggle><svg width="16" height="16" aria-hidden="true"><use href="#icon-moon"/></svg></button>
    <button type="button" data-notes-toggle>Notas do mockup</button>
  </div>
</body>
</html>
'''

def badge(kind, text): return f'<span class="badge badge--{kind}">{text}</span>'

DRAFT = {"title": "Um ano de portal novo", "date": "2026-10-19", "status": ("wait", "Rascunho"), "cat": "Geral", "cover": None}
pages = {}

# ---------------------------------------------------------------- Dashboard
recent_rows = "".join(f'<tr><td><a href="post-editar.html">{e(p["title"])}</a></td><td class="cell-muted">{pt.sdate(p["date"])}</td><td>{badge("ok", "Publicado")}</td></tr>' for p in P[:4])
pages["index.html"] = shell("index.html", "Painel", '''<div><h1>Bom dia, Gui</h1><p>Um resumo do caderno hoje.</p></div>
        <a class="button" href="post-editar.html">+ Novo post</a>''', f'''      <div class="stats">
        <a class="stat" href="posts.html"><strong>{len(P)}</strong><span>posts publicados</span></a>
        <a class="stat" href="posts.html"><strong>1</strong><span>rascunho</span></a>
        <a class="stat stat--alert" href="comentarios.html"><strong>2</strong><span>comentários para moderar</span></a>
        <a class="stat" href="inscritos.html"><strong>38</strong><span>inscritos confirmados</span></a>
      </div>
      <div class="editor" style="grid-template-columns: minmax(0, 1fr) minmax(0, 22rem)">
        <section class="panel" aria-labelledby="recent">
          <h2 id="recent">Posts recentes</h2>
          <div class="table-wrap"><table class="data-table"><thead><tr><th>Título</th><th>Data</th><th>Status</th></tr></thead><tbody>
            <tr><td><a href="post-editar.html">{DRAFT["title"]}</a></td><td class="cell-muted">editado hoje</td><td>{badge("wait", "Rascunho")}</td></tr>
            {recent_rows}</tbody></table></div>
        </section>
        <div class="stack" style="--stack-gap: var(--space-md)">
          <section class="panel mockup-stateful" aria-labelledby="groups">
            <h2 id="groups">Grupos do blog</h2>
            <fieldset class="mockup-states"><legend class="visually-hidden">Seção Tech no mockup</legend><span>Estado:</span><label><input type="radio" name="tech-admin" value="tech-off" checked>Sem posts tech</label><label><input type="radio" name="tech-admin" value="tech-on">Com post publicado</label></fieldset>
            <div class="group-row">
              <div><strong>Vida</strong><span class="text-muted">23 posts publicados · sempre visível</span></div>
              <label class="switch"><input type="checkbox" checked disabled><span class="visually-hidden">Vida visível no site</span></label>
            </div>
            <div class="group-row" data-state="tech-off">
              <div><strong>Tech</strong><span class="text-muted">0 publicados · 5 rascunhos</span></div>
              <label class="switch"><input type="checkbox" disabled><span class="visually-hidden">Mostrar Tech no site</span></label>
            </div>
            <p class="text-sm text-muted" data-state="tech-off">A seção Tech fica oculta na home e no blog. Dá para ligar assim que o primeiro post tech for publicado.</p>
            <div class="group-row" data-state="tech-on">
              <div><strong>Tech</strong><span class="text-muted">1 publicado · 4 rascunhos</span></div>
              <label class="switch"><input type="checkbox"><span class="visually-hidden">Mostrar Tech no site</span></label>
            </div>
            <p class="text-sm text-muted" data-state="tech-on">Ligue para mostrar a faixa Tech na home, o seletor Tudo · Vida · Tech no blog e as categorias tech.</p>
          </section>
          <section class="panel" aria-labelledby="todo">
            <h2 id="todo">Para fazer</h2>
            <div class="sticky-note" style="--r:-1deg"><ul><li>Moderar 2 comentários</li><li>Terminar “{DRAFT["title"]}”</li><li>Traduzir mais posts para o inglês (1 de {len(P)})</li></ul></div>
          </section>
          <section class="panel" aria-labelledby="last-send">
            <h2 id="last-send">Última newsletter</h2>
            <p class="text-sm"><strong>{e(SRC["title"])}</strong><br><span class="text-muted">Enviada para 36 pessoas · 61% abriram · 0 descadastros</span></p>
            <a class="section-heading__link" href="newsletter.html">Enviar outra {pt.arrow()}</a>
          </section>
        </div>
      </div>
      <aside class="mockup-note">Números e listas ilustrativos. O admin é funcional e simples de propósito: o caderno fica para o site público.</aside>''')

# ---------------------------------------------------------------- Posts list
rows = [f'<tr><td><span class="thumb" style="display:inline-grid;place-items:center;background:var(--color-subtle);font-size:.7rem">—</span></td><td><a href="post-editar.html">{DRAFT["title"]}</a><br><span class="cell-muted">sem capa ainda</span></td><td>Geral</td><td>{badge("ok", "PT")}</td><td class="cell-muted">—</td><td>{badge("wait", "Rascunho")}</td></tr>']
for p in P:
    en_ok = p["slug"] == SRC["slug"]
    rows.append(f'<tr><td><img class="thumb" src="{R}assets/images/covers/{p["cover"]}" alt=""></td><td><a href="post-editar.html">{e(p["title"])}</a></td><td>{e(p["cat"])}</td>'
                f'<td>{badge("ok", "PT")} {badge("ok", "EN") if en_ok else badge("", "EN")}</td><td class="cell-muted">{pt.sdate(p["date"])}</td><td>{badge("ok", "Publicado")}</td></tr>')
pages["posts.html"] = shell("posts.html", "Posts", '''<div><h1>Posts</h1><p>24 posts · 23 publicados · 1 rascunho</p></div>
        <a class="button" href="post-editar.html">+ Novo post</a>''', f'''      <div class="toolbar">
        <input class="input" type="search" placeholder="Buscar posts…" aria-label="Buscar posts">
        <nav class="segmented" aria-label="Filtrar por status"><a href="#" aria-current="true">Todos</a><a href="#">Publicados</a><a href="#">Rascunhos</a><a href="#">Sem tradução</a></nav>
        <select class="input" style="max-width: 13rem" aria-label="Categoria"><option>Todas as categorias</option>{"".join(f"<option>{e(c['name'])}</option>" for c in sorted(cats, key=lambda c: c["name"]))}</select>
      </div>
      <div class="table-wrap"><table class="data-table">
        <thead><tr><th></th><th>Título</th><th>Categoria</th><th>Idiomas</th><th>Publicado em</th><th>Status</th></tr></thead>
        <tbody>{"".join(rows)}</tbody>
      </table></div>
      <aside class="mockup-note">A coluna Idiomas mostra em quais línguas o post tem tradução publicada; o filtro “Sem tradução” ajuda a escolher o próximo para traduzir.</aside>''')

# ---------------------------------------------------------------- Editor
article = open(f"{S}/wp/article-clean.html").read()
paras = re.findall(r"<(?:h2|p)[^>]*>.*?</(?:h2|p)>", article, flags=re.S)[:7]
body_pt = "\n".join(paras).replace("IMGROOT", f"{R}assets/images/posts/")
article_en = open(f"{S}/wp/article-en.html").read()
body_en = "\n".join(re.findall(r"<(?:h2|p)[^>]*>.*?</(?:h2|p)>", article_en, flags=re.S)[:7])
TOOLBAR = '<div class="rich-editor__toolbar" role="toolbar" aria-label="Formatação"><button type="button" aria-label="Negrito">B</button><button type="button" aria-label="Itálico"><i>I</i></button><button type="button" aria-label="Link">🔗</button><span class="sep"></span><button type="button">H2</button><button type="button" aria-label="Citação">❝</button><button type="button" aria-label="Lista">•</button><button type="button" aria-label="Código">&lt;/&gt;</button><span class="sep"></span><button type="button" aria-label="Imagem">🖼</button><button type="button" aria-label="Desfazer">↶</button></div>'
def panel(lang, title, slug_prefix, slug, excerpt, body, seo_t, seo_d):
    return f'''        <div class="stack" data-locale="{lang}" style="--stack-gap: var(--space-sm)">
          <textarea class="title-input" rows="2" aria-label="Título">{e(title)}</textarea>
          <p class="slug">guicarvalho.com.br/{slug_prefix}<b>{slug}</b>/ · <a href="#">editar endereço</a></p>
          <div class="field"><label class="field__label" for="ex-{lang}">Resumo</label><textarea class="input" id="ex-{lang}" style="min-height: 5rem">{e(excerpt)}</textarea><span class="char-count">{len(excerpt)}/200</span></div>
          <div class="rich-editor">{TOOLBAR}<div class="rich-editor__body post-body" contenteditable="true" style="max-width:none">{body}</div></div>
          <details class="panel"><summary class="field__label" style="cursor:pointer">SEO e compartilhamento</summary>
            <div class="field"><label class="field__label" for="st-{lang}">Título para buscadores</label><input class="input" id="st-{lang}" value="{e(seo_t)}"><span class="char-count">{len(seo_t)}/60</span></div>
            <div class="field"><label class="field__label" for="sd-{lang}">Descrição</label><textarea class="input" id="sd-{lang}" style="min-height: 4rem">{e(seo_d)}</textarea><span class="char-count">{len(seo_d)}/160</span></div>
          </details>
        </div>'''
side = f'''        <aside class="editor__side">
          <section class="panel" aria-label="Publicação">
            <div class="field"><label class="field__label" for="status">Status</label><select class="input" id="status"><option>Publicado</option><option>Rascunho</option><option>Agendado</option></select></div>
            <div class="field"><label class="field__label" for="pub">Publicado em</label><input class="input" id="pub" type="date" value="{SRC["date"]}"></div>
            <div class="cluster"><button class="button" type="button">Salvar</button><a class="button button--ghost" href="{R}br/idiomas/o-que-te-impede-de-aprender-outro-idioma/">Ver ↗</a></div>
          </section>
          <section class="panel" aria-label="Capa">
            <h2>Capa</h2>
            <div class="cover-pick"><span class="polaroid polaroid--wide"><img src="{R}assets/images/covers/{SRC["cover"]}" alt=""></span>
            <div class="cluster" style="--cluster-gap:.4rem"><button class="button button--small button--secondary" type="button">Trocar</button><button class="button button--small button--ghost" type="button">Ajustar foco</button></div>
            <span class="field__hint">Sem foto, o post ganha a capa tipográfica automática.</span></div>
          </section>
          <section class="panel" aria-label="Organização">
            <div class="field"><label class="field__label" for="group">Grupo</label><select class="input" id="group"><option selected>Vida</option><option>Tech</option></select><span class="text-sm text-muted">As categorias mudam conforme o grupo.</span></div>
            <div class="field"><label class="field__label" for="cat">Categoria principal</label><select class="input" id="cat">{"".join(f"<option{' selected' if c['slug'] == 'idiomas' else ''}>{e(c['name'])}</option>" for c in sorted(cats, key=lambda c: c["name"]))}</select></div>
            <div class="field"><span class="field__label">Tags</span><div class="chip-input"><span class="tag">coaching ×</span><span class="tag">viagens ×</span><input placeholder="Adicionar…" aria-label="Adicionar tag"></div></div>
          </section>
          <section class="panel" aria-label="Newsletter">
            <h2>Newsletter</h2>
            <p class="text-sm text-muted">Enviado para 36 pessoas em 12/02/2015 (no blog antigo).</p>
            <a class="button button--small button--secondary" href="newsletter.html">Enviar este post</a>
          </section>
        </aside>'''
pages["post-editar.html"] = shell("posts.html", "Editar post", f'''<div><p><a href="posts.html">← Posts</a></p><h1>Editar post</h1></div>
        <div class="cluster">{badge("ok", "Publicado")}<span class="cell-muted">salvo há 2 min</span></div>''', f'''      <div class="editor">
        <div class="stack locale-panels" style="--stack-gap: var(--space-md)">
          <div class="locale-tabs" role="tablist" aria-label="Idioma">
            <label><input type="radio" name="locale" id="tab-pt" checked>Português</label>
            <label><input type="radio" name="locale" id="tab-en">English {badge("ok", "publicado")}</label>
            <label style="color: var(--color-text-muted)">+ Adicionar idioma</label>
          </div>
{panel("pt", SRC["title"], "br/idiomas/", SRC["slug"], SRC["excerpt"], body_pt, SRC["title"] + " · gui carvalho", SRC["excerpt"])}
{panel("en", "What stops you from learning another language?", "en/languages/", "what-stops-you-from-learning-another-language", "Many of us dream of mastering a second language, but sometimes it takes lessons you won't find in any grammar book.", body_en, "What stops you from learning another language?", "Many of us dream of mastering a second language, but sometimes it takes lessons you won't find in any grammar book.")}
          <aside class="mockup-note">Cada idioma é uma tradução com título, endereço, resumo, texto e SEO próprios. Capa, categoria, tags e status valem para todas. O editor de texto é o Trix, do ActionText.</aside>
        </div>
{side}
      </div>''')

# ---------------------------------------------------------------- Comments
QUEUE = [("A", "Ana Ribeiro", "ana@email.com", "primeiro comentário", SRC["title"], "agora mesmo", "A dica de contar uma piada no idioma é ótima, vou testar no meu próximo call em inglês!"),
         ("J", "João Pedro", "jp@email.com", "primeiro comentário", "Quem é mineiro me entende", "há 3 horas", "Uai, sô! Faltou o “trem” na lista, que serve pra tudo.")]
qitems = "".join(f'''      <article class="queue-item">
        <span class="avatar" aria-hidden="true">{i}</span>
        <div><p class="text-sm"><strong>{n}</strong> <span class="cell-muted">· {m} · {em} · {t}</span></p><p class="text-sm text-muted">em <a href="#">{e(post)}</a></p><blockquote>{e(c)}</blockquote></div>
        <div class="actions"><button class="button button--small" type="button">Aprovar</button><button class="button button--small button--secondary" type="button">Responder</button><button class="button button--small button--danger" type="button">Rejeitar</button></div>
      </article>''' for i, n, em, m, post, t, c in QUEUE)
pages["comentarios.html"] = shell("comentarios.html", "Comentários", '''<div><h1>Comentários</h1><p>2 esperando moderação · 3 aprovados</p></div>''', f'''      <nav class="segmented" aria-label="Filtrar comentários"><a href="#" aria-current="true">Pendentes (2)</a><a href="#">Aprovados</a><a href="#">Rejeitados</a></nav>
{qitems}
      <section class="panel" aria-labelledby="rule">
        <h2 id="rule">Regra de moderação</h2>
        <label class="cluster text-sm"><input type="checkbox" checked style="accent-color: var(--sage-700); width:1.1rem; height:1.1rem"> Publicar direto comentários de quem já teve um comentário aprovado</label>
      </section>
      <aside class="mockup-note">Nomes e comentários fictícios. Aprovar publica no post; Responder abre um campo aqui mesmo, e a resposta sai com o selo “autor”.</aside>''')

# ---------------------------------------------------------------- Subscribers
SUBS = [("ana@email.com", "pt-BR", "ok", "Confirmado", "18 out 2026", "rodapé do post"), ("liam@email.com", "en", "ok", "Confirmado", "12 out 2026", "home"),
        ("mariana@email.com", "pt-BR", "ok", "Confirmado", "02 out 2026", "importado do WordPress"), ("rafael@email.com", "pt-BR", "wait", "Aguardando confirmação", "19 out 2026", "home"),
        ("camila@email.com", "pt-BR", "off", "Descadastrado", "28 set 2026", "rodapé do post"), ("bounce@exemplo.com", "pt-BR", "off", "E-mail inválido", "15 set 2026", "importado do WordPress"),
        ("emma@email.com", "en", "ok", "Confirmado", "09 set 2026", "post em inglês")]
GROUP_OF = {"liam@email.com": "Só Tech", "rafael@email.com": "Só Vida", "mariana@email.com": "Só Vida"}
srows = "".join(f'<tr><td><a href="#">{em}</a></td><td>{badge(k, st)}</td><td>{badge("", loc)}</td><td>{badge("", GROUP_OF.get(em, "Tudo"))}</td><td class="cell-muted">{d}</td><td class="cell-muted">{src}</td></tr>' for em, loc, k, st, d, src in SUBS)
pages["inscritos.html"] = shell("inscritos.html", "Inscritos", '''<div><h1>Inscritos</h1><p>38 confirmados · 1 aguardando · 3 saíram</p></div>
        <div class="cluster"><button class="button button--secondary button--small" type="button">Importar CSV</button><button class="button button--secondary button--small" type="button">Exportar</button></div>''', f'''      <div class="stats">
        <div class="stat"><strong>36</strong><span>em português</span></div>
        <div class="stat"><strong>2</strong><span>em inglês</span></div>
        <div class="stat"><strong>61%</strong><span>abertura média</span></div>
      </div>
      <p class="text-sm text-muted">Recebem: <strong>31</strong> Tudo · <strong>5</strong> só Vida · <strong>2</strong> só Tech</p>
      <div class="toolbar">
        <input class="input" type="search" placeholder="Buscar por e-mail…" aria-label="Buscar inscritos">
        <nav class="segmented" aria-label="Filtrar por status"><a href="#" aria-current="true">Todos</a><a href="#">Confirmados</a><a href="#">Aguardando</a><a href="#">Saíram</a></nav>
        <nav class="segmented" aria-label="Filtrar pelo que recebem"><a href="#" aria-current="true">Qualquer grupo</a><a href="#">Tudo</a><a href="#">Só Vida</a><a href="#">Só Tech</a></nav>
      </div>
      <div class="table-wrap"><table class="data-table">
        <thead><tr><th>E-mail</th><th>Status</th><th>Idioma</th><th>Recebe</th><th>Desde</th><th>Origem</th></tr></thead>
        <tbody>{srows}</tbody>
      </table></div>
      <aside class="mockup-note">E-mails fictícios. A lista real (menos de 50 pessoas) vem do WordPress depois; quem não tiver consentimento registrado recebe um pedido de reconfirmação. Bounces e marcações de spam chegam pelo webhook do SendGrid e mudam o status sozinhos.</aside>''')

# ---------------------------------------------------------------- Newsletter
hist = "".join(f'<tr><td>{t}</td><td>{badge("", l)}</td><td class="cell-muted">{d}</td><td>{n}</td><td>{o}</td></tr>' for t, l, d, n, o in [
    (e(SRC["title"]), "pt-BR", "19 out 2026", "36", "61%"), ("What stops you from learning another language?", "en", "19 out 2026", "2", "50%")])
pages["newsletter.html"] = shell("newsletter.html", "Newsletter", '''<div><h1>Enviar newsletter</h1><p>Escolha o post, confira o e-mail e envie. Nada sai sem você confirmar.</p></div>''', f'''      <div class="send-layout">
        <section class="panel" aria-label="Envio">
          <div class="field"><label class="field__label" for="np">Post</label><select class="input" id="np"><option>{e(SRC["title"])}</option>{"".join(f"<option>{e(p['title'])}</option>" for p in P[:5])}</select></div>
          <div class="field"><label class="field__label" for="nl">Para</label><select class="input" id="nl"><option>Português · Tudo e só Vida (34)</option><option>Inglês · Tudo e só Vida (2)</option></select><span class="field__hint">O post é do grupo Vida, então vai para quem assina Tudo ou só Vida. Só aparece um idioma se o post tiver tradução nele.</span></div>
          <div class="field"><label class="field__label" for="ns">Assunto</label><input class="input" id="ns" value="{e(SRC["title"])}"></div>
          <div class="field"><label class="field__label" for="nn">Bilhete (opcional)</label><textarea class="input" id="nn">Esse é um dos posts mais antigos do blog, agora de casa nova. Se você também já travou numa conversa em outro idioma, me responde contando como foi!</textarea><span class="field__hint">Aparece num post-it amarelo no e-mail.</span></div>
          <div class="cluster"><button class="button button--secondary" type="button">Enviar teste para mim</button><button class="button" type="button" popovertarget="confirm-send">Enviar para 34 pessoas</button></div>
        </section>
        <section aria-label="Prévia do e-mail">
          <iframe src="{R}emails/novo-post.html" title="Prévia do e-mail"></iframe>
        </section>
      </div>
      <section class="panel" aria-labelledby="hist">
        <h2 id="hist">Envios anteriores</h2>
        <div class="table-wrap"><table class="data-table"><thead><tr><th>Post</th><th>Idioma</th><th>Enviado em</th><th>Pessoas</th><th>Abriram</th></tr></thead><tbody>{hist}</tbody></table></div>
      </section>
      <div class="confirm-pop" id="confirm-send" popover>
        <div class="stack" style="--stack-gap: var(--space-sm)">
          <h2>Enviar para 34 pessoas?</h2>
          <p class="text-muted">“{e(SRC["title"])}” vai para os inscritos em português que recebem Tudo ou só Vida. Depois de enviado, não dá para desfazer.</p>
          <div class="cluster"><button class="button" type="button" popovertarget="confirm-send" popovertargetaction="hide">Sim, enviar agora</button><button class="button button--ghost" type="button" popovertarget="confirm-send" popovertargetaction="hide">Cancelar</button></div>
        </div>
      </div>
      <aside class="mockup-note">O botão de envio abre uma confirmação (atributo popover do HTML, sem JavaScript). Os envios são feitos em lotes pelo SendGrid, e as aberturas chegam pelo webhook.</aside>''')

os.makedirs(OUT, exist_ok=True)
for f, html in pages.items():
    open(f"{OUT}/{f}", "w").write(html)
print("ok", list(pages))
