"""Email templates (table-based, inline styles) and a preview page."""
import os
from common import posts as P, e
import pages_en as en

OUT = __import__("common").MOCKUP + "/emails"
A = "../assets"
FONT = "'Nunito Sans', Helvetica, Arial, sans-serif"
INK, TEXT, MUTED, LINE = "#0c0c0c", "#262626", "#545454", "#e6e6e6"
SAGE, SAGE_DARK, SAGE_SOFT, NOTE, NOTE_FG = "#527752", "#2d472e", "#eef9ee", "#fff3a8", "#3b3200"
SRC = next(x for x in P if x["slug"] == "o-que-te-impede-de-aprender-outro-idioma")

def button(label, href="#", primary=True):
    bg, fg, border = (SAGE, "#ffffff", SAGE) if primary else ("#ffffff", SAGE, SAGE)
    return f'''<table role="presentation" cellspacing="0" cellpadding="0" border="0" style="display:inline-table;margin:4px 6px 4px 0"><tr>
                  <td bgcolor="{bg}" style="border-radius:999px;border:2px solid {border}">
                    <a href="{href}" style="display:inline-block;padding:12px 26px;font-family:{FONT};font-size:16px;font-weight:800;line-height:1.2;color:{fg};text-decoration:none;border-radius:999px">{label}</a>
                  </td></tr></table>'''

def p(text, size=17, color=TEXT, weight=400, extra=""):
    return f'<p style="margin:0 0 16px;font-family:{FONT};font-size:{size}px;line-height:1.6;color:{color};font-weight:{weight};{extra}">{text}</p>'

def h1(text):
    return f'<h1 style="margin:0 0 12px;font-family:{FONT};font-size:30px;line-height:1.15;font-weight:800;letter-spacing:-0.5px;color:{INK}">{text}</h1>'

def eyebrow(text):
    return f'<p style="margin:0 0 8px;font-family:{FONT};font-size:12px;line-height:1.4;font-weight:800;letter-spacing:1px;text-transform:uppercase;color:{SAGE}">{text}</p>'

def note(inner):
    return f'''<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin:8px 0 4px"><tr>
                <td bgcolor="{NOTE}" style="padding:18px 20px;font-family:{FONT};font-size:15px;line-height:1.55;color:{NOTE_FG}">{inner}</td></tr></table>'''

def email(lang, title, preheader, body, footer):
    return f'''<!doctype html>
<html lang="{lang}" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <meta name="color-scheme" content="light">
  <meta name="supported-color-schemes" content="light">
  <title>{e(title)}</title>
  <!-- Clients that support web fonts (Apple Mail, iOS) get Nunito Sans; the rest fall back to Helvetica/Arial. Self-hosted in production. -->
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;700;800&display=swap" rel="stylesheet">
  <style>
    body {{ margin: 0; padding: 0; }}
    a {{ color: {SAGE}; }}
    @media (max-width: 620px) {{
      .container {{ width: 100% !important; }}
      .px {{ padding-left: 20px !important; padding-right: 20px !important; }}
    }}
  </style>
</head>
<body style="margin:0;padding:0;background:#f4f4f4">
  <div style="display:none;max-height:0;overflow:hidden;mso-hide:all">{e(preheader)}&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;</div>
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#f4f4f4" style="background-color:#f4f4f4;background-image:radial-gradient(#e4e4e4 1.2px, transparent 1.2px);background-size:22px 22px">
    <tr><td align="center" style="padding:32px 12px">
      <table role="presentation" class="container" width="600" cellspacing="0" cellpadding="0" border="0" style="width:600px;max-width:600px">
        <tr><td class="px" style="padding:0 8px 20px">
          <a href="#"><img src="{A}/images/brand/email-logo.png" width="198" height="48" alt="gui carvalho" style="display:block;border:0;width:198px;height:48px"></a>
        </td></tr>
        <tr><td class="px" bgcolor="#ffffff" style="background:#ffffff;border-radius:18px;padding:36px 40px;box-shadow:0 10px 30px rgba(0,0,0,0.08)">
{body}
        </td></tr>
        <tr><td class="px" style="padding:24px 8px 8px;font-family:{FONT};font-size:12px;line-height:1.6;color:{MUTED}">
{footer}
        </td></tr>
      </table>
    </td></tr>
  </table>
</body>
</html>
'''

def polaroid_img(src, alt):
    return f'''<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin:8px 0 24px"><tr>
                <td bgcolor="#ffffff" style="padding:12px 12px 18px;border:1px solid {LINE};border-radius:6px;box-shadow:0 8px 20px rgba(0,0,0,0.12)">
                  <img src="{src}" width="496" alt="{e(alt)}" style="display:block;width:100%;max-width:496px;height:auto;border:0;border-radius:2px">
                </td></tr></table>'''

T = []

# 1. Subscription confirmation -------------------------------------------------
for lang, f, d in [("pt-BR", "confirmacao-inscricao.html", dict(
        subject="Confirma que é você? ✉️", pre="Falta só um clique para receber os posts do Gui por e-mail.",
        eb="Newsletter", h="Confirma que é você?",
        b1="Alguém (tomara que você!) pediu para receber os posts do caderno do Gui neste endereço: <strong>seu@email.com</strong>.",
        b2="Para começar, é só confirmar:", cta="Confirmar inscrição",
        fine="Se não foi você, é só ignorar este e-mail. Sem a confirmação, você não recebe nada.",
        note="<strong>O que vem por aí:</strong> um e-mail quando sair post novo, com histórias, metas, idiomas e as presepadas da vida. Sem spam.",
        foot="Você recebeu este e-mail porque alguém digitou este endereço em <a href=\"#\" style=\"color:#545454\">guicarvalho.com.br</a>. O link de confirmação vale por 7 dias.")),
    ("en", "en/subscription-confirmation.html", dict(
        subject="Is this you? ✉️", pre="One click away from getting Gui's posts by email.",
        eb="Newsletter", h="Is this you?",
        b1="Someone (hopefully you!) asked to get the posts from Gui's notebook at this address: <strong>you@email.com</strong>.",
        b2="To start, just confirm:", cta="Confirm subscription",
        fine="If it wasn't you, just ignore this email. Without confirmation you won't get anything.",
        note="<strong>What's coming:</strong> one email per new post, with stories, goals, languages and life's shenanigans. Most posts are in Portuguese. No spam.",
        foot="You got this email because someone typed this address at <a href=\"#\" style=\"color:#545454\">guicarvalho.com.br</a>. The confirmation link is valid for 7 days."))]:
    body = "\n".join([eyebrow(d["eb"]), h1(d["h"]), p(d["b1"]), p(d["b2"]), f'<div style="margin:8px 0 24px">{button(d["cta"])}</div>',
                      p(d["fine"], 14, MUTED), note(d["note"])])
    T.append((f, lang, d["subject"], d["pre"], email(lang, d["subject"], d["pre"], body, p(d["foot"], 12, MUTED, extra="margin:0"))))

# 2. New post --------------------------------------------------------------------
for lang, f, d in [("pt-BR", "novo-post.html", dict(
        subject=SRC["title"], pre=SRC["excerpt"], eb="Post novo no caderno", title=SRC["title"],
        meta="Idiomas · 7 min de leitura", excerpt=SRC["excerpt"], alt=SRC["alt"] or SRC["title"], cta="Ler o post completo",
        note="<strong>Um bilhete:</strong> esse é um dos posts mais antigos do blog, agora de casa nova. Se você também já travou numa conversa em outro idioma, me responde este e-mail contando como foi!",
        foot="Você recebe este e-mail porque se inscreveu na newsletter de <a href=\"#\" style=\"color:#545454\">guicarvalho.com.br</a>.<br><a href=\"#\" style=\"color:#545454\">Ver no navegador</a> · <a href=\"#\" style=\"color:#545454\">Descadastrar</a>")),
    ("en", "en/new-post.html", dict(
        subject=en.POST["title"], pre=en.POST["excerpt"], eb="New post in the notebook", title=en.POST["title"],
        meta="Languages · 6 min read", excerpt=en.POST["excerpt"], alt=en.POST["alt"], cta="Read the full post",
        note="<strong>A note:</strong> this is one of the oldest posts on the blog, now in its new home and in English. If you've ever frozen mid-conversation in another language, reply and tell me how it went!",
        foot="You get this email because you subscribed to the newsletter at <a href=\"#\" style=\"color:#545454\">guicarvalho.com.br</a>.<br><a href=\"#\" style=\"color:#545454\">View in browser</a> · <a href=\"#\" style=\"color:#545454\">Unsubscribe</a>"))]:
    body = "\n".join([eyebrow(d["eb"]), h1(d["title"]), p(d["meta"], 14, MUTED), polaroid_img(f"{A}/images/covers/{SRC['cover']}", d["alt"]),
                      p(d["excerpt"], 18), f'<div style="margin:8px 0 28px">{button(d["cta"])}</div>', note(d["note"])])
    T.append((f, lang, d["subject"], d["pre"], email(lang, d["subject"], d["pre"], body, p(d["foot"], 12, MUTED, extra="margin:0"))))

# 3. New comment, for the admin ------------------------------------------------
comment = f'''<table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="margin:4px 0 24px;border:1px solid {LINE};border-radius:14px"><tr>
                <td width="56" valign="top" style="padding:18px 0 18px 18px">
                  <table role="presentation" cellspacing="0" cellpadding="0" border="0"><tr><td width="40" height="40" align="center" bgcolor="{SAGE_SOFT}" style="border-radius:999px;font-family:{FONT};font-size:16px;font-weight:800;color:{SAGE_DARK}">A</td></tr></table>
                </td>
                <td valign="top" style="padding:18px 18px 18px 8px;font-family:{FONT}">
                  <p style="margin:0 0 4px;font-size:15px;color:{INK};font-weight:800">Ana Ribeiro <span style="font-weight:400;color:{MUTED};font-size:13px">· primeiro comentário · ana@email.com</span></p>
                  <p style="margin:0;font-size:16px;line-height:1.6;color:{TEXT}">A dica de contar uma piada no idioma é ótima, vou testar no meu próximo call em inglês!</p>
                </td></tr></table>'''
body = "\n".join([eyebrow("Moderação"), h1("Novo comentário esperando você"),
                  p(f'Em <a href="../br/idiomas/o-que-te-impede-de-aprender-outro-idioma/" style="color:{SAGE};font-weight:700">{e(SRC["title"])}</a>:'),
                  comment, f'<div style="margin:0 0 20px">{button("Aprovar")}{button("Rejeitar", primary=False)}</div>',
                  p(f'Ou <a href="#" style="color:{SAGE};font-weight:700">abra a fila de moderação no admin</a> para ver todos os pendentes.', 14, MUTED)])
T.append(("comentario-para-moderar.html", "pt-BR", "Novo comentário em “O que te impede de aprender outro idioma?”", "Ana Ribeiro comentou e está esperando moderação.",
          email("pt-BR", "Novo comentário", "Ana Ribeiro comentou e está esperando moderação.", body,
                p("Notificação do admin de guicarvalho.com.br. Só você recebe este e-mail.", 12, MUTED, extra="margin:0"))))

os.makedirs(f"{OUT}/en", exist_ok=True)
for f, lang, subj, pre, html in T:
    html = html.replace('src="../assets', 'src="../../assets').replace('href="../br/', 'href="../../br/') if f.startswith("en/") else html
    open(f"{OUT}/{f}", "w").write(html)
print("ok", len(T))

# Preview page ---------------------------------------------------------------
import pages as pt
INFO = {
    "confirmacao-inscricao.html": ("Confirmação de inscrição", "Enviado logo depois que alguém se inscreve (double opt-in)."),
    "en/subscription-confirmation.html": ("Subscription confirmation (EN)", "Same, for subscribers who signed up on the English pages."),
    "novo-post.html": ("Post novo", "Enviado quando você clica em “Enviar newsletter” no admin."),
    "en/new-post.html": ("New post (EN)", "Sent to English subscribers when a post has an English version."),
    "comentario-para-moderar.html": ("Comentário para moderar", "Só para você: chega a cada comentário novo pendente."),
}
rows = []
for f, lang, subj, pre, _ in T:
    name, why = INFO[f]
    rows.append(f'''      <section class="stack" style="--stack-gap: var(--space-sm); margin-block-end: var(--space-2xl)" aria-label="{e(name)}">
        <div class="board-title" style="margin-block: 0">
          <span class="sticker sticker--sm">{pt.obj("envelope")}</span>
          <div><h2 style="font-size: var(--text-xl)">{e(name)}</h2><p class="text-muted text-sm">{e(why)}</p></div>
        </div>
        <div class="index-card" style="--r:0deg; display:grid; gap:.15rem; max-width: 46rem">
          <small>De: Gui Carvalho &lt;ola@guicarvalho.com.br&gt;</small>
          <b>{e(subj)}</b>
          <small>{e(pre)}</small>
        </div>
        <div class="email-previews">
          <figure><figcaption class="sg-label">Computador · 640 px</figcaption><iframe src="{f}" title="{e(name)}, computador" width="640" height="980" loading="lazy"></iframe></figure>
          <figure><figcaption class="sg-label">Celular · 375 px</figcaption><iframe src="{f}" title="{e(name)}, celular" width="375" height="980" loading="lazy"></iframe></figure>
        </div>
        <a class="section-heading__link" href="{f}">Abrir o e-mail sozinho {pt.arrow()}</a>
      </section>''')
preview = pt.head("E-mails · mockup · gui carvalho", "Templates de e-mail do portal.", "../").replace("</head>", '''  <link rel="stylesheet" href="../styleguide/styleguide.css">
  <style>
    @layer mockup {
      .email-previews { display: flex; flex-wrap: wrap; gap: var(--space-lg); align-items: start; }
      .email-previews figure { display: grid; gap: var(--space-2xs); max-width: 100%; }
      .email-previews iframe { max-width: 100%; border: 1px solid var(--color-border); border-radius: var(--radius-lg); background: #f4f4f4; box-shadow: var(--paper-shadow-sm); }
    }
  </style>
</head>''') + f'''
    <site-header root="../"></site-header>

    <main id="main" class="container">
      <div class="board-title" style="margin-block-start: var(--space-xl)">
        <span class="sticker" style="--r:-8deg">{pt.obj("envelope")}</span>
        <div>
          <h1 style="font-size: var(--text-3xl)">E-mails</h1>
          <p class="text-muted" style="font-size: var(--text-md)">Os e-mails que o portal envia, em HTML de e-mail: tabelas e estilos inline, para funcionar no Gmail, Outlook e Apple Mail.</p>
        </div>
      </div>
      <aside class="mockup-note" style="margin-block-end: var(--space-xl)">Nos e-mails, o logo é PNG (o Gmail não mostra SVG), as fotos usam endereço completo em produção e a fonte cai para Helvetica/Arial onde a Nunito Sans não carrega. O descadastro em um clique também vai no cabeçalho List-Unsubscribe, que não aparece aqui.</aside>
{chr(10).join(rows)}
    </main>
''' + pt.foot("../")
open(f"{OUT}/index.html", "w").write(preview)
print("preview ok")
