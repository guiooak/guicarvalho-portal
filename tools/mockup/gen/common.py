import json, os, html as H
# tools/mockup/gen -> tools/mockup -> repo root. MOCKUP_OUT lets a dry run write elsewhere.
TOOLS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(TOOLS, "data")
MOCKUP = os.environ.get("MOCKUP_OUT") or os.path.join(os.path.dirname(os.path.dirname(TOOLS)), "mockup")
OUT = f"{MOCKUP}/explorations"
# The newsletter note is not part of the pages: the header, footer and phone-menu
# buttons drop it in as a popover (mockup.js). True brings back the inline note.
NEWSLETTER_INLINE = False
posts = json.load(open(f"{S}/wp/data.json"))
cats = sorted([c for c in json.load(open(f"{S}/wp/cats.json")) if c["count"] > 0], key=lambda c: -c["count"])
MONTHS = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
MON = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
e = H.escape
ROOT = "../"
def fdate(d):
    y, m, dd = d.split("-"); return f"{int(dd)} de {MONTHS[int(m)-1]} de {y}"
def sdate(d):
    y, m, dd = d.split("-"); return f"{int(dd)} {MON[int(m)-1]} {y}"
def cover(p): return f"{ROOT}assets/images/covers/{p['cover']}"
def href(p): return f"{ROOT}br/idiomas/o-que-te-impede-de-aprender-outro-idioma/" if p["slug"] == "o-que-te-impede-de-aprender-outro-idioma" else "#"
def obj(name, cls="", style=""):
    return f'<svg class="{cls}" style="{style}" aria-hidden="true"><use href="#obj-{name}"/></svg>'
def page(title, concept, desc, body, css):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)} · conceito de layout</title>
  <link rel="icon" href="{ROOT}assets/images/brand/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{ROOT}assets/stylesheets/application.css?v=2026-10-23a">
  <link rel="stylesheet" href="{ROOT}assets/stylesheets/mockup.css?v=2026-10-23a">
  <script src="{ROOT}assets/javascripts/mockup.js?v=2026-10-23a"></script>
  <style>
    @layer mockup {{
      .concept-bar {{ display:flex; flex-wrap:wrap; gap:.5rem 1rem; align-items:center; justify-content:space-between; padding:.6rem var(--gutter); background:#d4a017; color:#1a1400; font-size:var(--text-xs); font-weight:800; }}
      .concept-bar a {{ color:inherit; }}
{css}
    }}
  </style>
</head>
<body>
  <div class="concept-bar"><span>Conceito {concept}: {e(desc)}</span><a href="index.html">← todos os conceitos</a></div>
  <div class="site">
    <site-header root="{ROOT}"></site-header>
    <main id="main">
{body}
    </main>
    <site-footer root="{ROOT}"></site-footer>
  </div>
</body>
</html>
'''
