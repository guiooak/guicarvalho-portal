"""Made-up Tech posts, only to validate the two-group layout. Every current
WordPress post belongs to the Vida group; Tech starts empty and stays hidden
until Gui publishes the first one and turns it on in the admin."""
from html import escape as e

GROUPS = {
    "pt": {"vida": ("Vida", "vida", "mountain", "Histórias, metas, viagens e as presepadas da vida."),
           "tech": ("Tech", "tech", "chip", "Código, front-end e as ferramentas que eu construo.")},
    "en": {"vida": ("Life", "life", "mountain", "Stories, goals, travel and life's shenanigans."),
           "tech": ("Tech", "tech", "chip", "Code, front-end and the tools I build.")},
}

# (pt name, pt slug, en name, en slug, sticker)
TECH_CATS = [("Front-end", "front-end", "Front-end", "front-end", "window"),
             ("React", "react", "React", "react", "chip"),
             ("Rails", "rails", "Rails", "rails", "laptop"),
             ("Ferramentas", "ferramentas", "Tools", "tools", "clock")]
CAT_BY_PT = {c[0]: c for c in TECH_CATS}

# (pt title, pt slug, pt excerpt, en title, en slug, en excerpt, pt category, date)
RAW = [
    ("Como o Tymebox sabe que sua reunião vai atrasar", "como-o-tymebox-sabe-que-sua-reuniao-vai-atrasar",
     "O cronômetro compara o seu ritmo com o plano em tempo real. Conto como fiz essa conta e por que ela mudou minhas reuniões.",
     "How Tymebox knows your meeting is running late", "how-tymebox-knows-your-meeting-is-running-late",
     "The countdown compares your pace with the plan in real time. Here's how I did that math and why it changed my meetings.",
     "Ferramentas", "2026-09-28"),
    ("Diálogos na URL: por que criei o dialogs-valve", "dialogos-na-url-por-que-criei-o-dialogs-valve",
     "Modais que somem no botão voltar e links que não abrem o diálogo certo. A biblioteca nasceu dessa irritação.",
     "Dialogs in the URL: why I built dialogs-valve", "dialogs-in-the-url-why-i-built-dialogs-valve",
     "Modals that vanish on the back button and links that don't open the right dialog. The library was born from that annoyance.",
     "React", "2026-08-30"),
    ("Tokens de design só com CSS e light-dark()", "tokens-de-design-so-com-css-e-light-dark",
     "Tema claro e escuro sem uma linha de JavaScript: como organizei as cores deste site em camadas e tokens.",
     "Design tokens with plain CSS and light-dark()", "design-tokens-with-plain-css-and-light-dark",
     "Light and dark themes without a line of JavaScript: how I organized this site's colors in layers and tokens.",
     "Front-end", "2026-07-19"),
    ("Rails 8 sem build de JavaScript, um ano depois", "rails-8-sem-build-de-javascript-um-ano-depois",
     "Importmaps, Hotwire e zero bundler. O que ficou mais simples, o que deu trabalho e se eu faria de novo.",
     "Rails 8 without a JavaScript build, one year later", "rails-8-without-a-javascript-build-one-year-later",
     "Importmaps, Hotwire and zero bundler. What got simpler, what took work and whether I'd do it again.",
     "Rails", "2026-06-07"),
    ("Meu setup de 2026: terminal, editor e atalhos", "meu-setup-de-2026-terminal-editor-e-atalhos",
     "Os aliases, atalhos e pequenos scripts que mais me poupam tempo no dia a dia de front-end.",
     "My 2026 setup: terminal, editor and shortcuts", "my-2026-setup-terminal-editor-and-shortcuts",
     "The aliases, shortcuts and small scripts that save me the most time in my front-end day.",
     "Ferramentas", "2026-05-10"),
]

def posts(lang):
    out = []
    for pt_t, pt_s, pt_x, en_t, en_s, en_x, cat, date in RAW:
        c = CAT_BY_PT[cat]
        if lang == "pt":
            out.append(dict(title=pt_t, slug=pt_s, excerpt=pt_x, cat=c[0], cat_slug=c[1], date=date, obj=c[4], path=f"/br/{c[1]}/{pt_s}/", code=pt_s))
        else:
            out.append(dict(title=en_t, slug=en_s, excerpt=en_x, cat=c[2], cat_slug=c[3], date=date, obj=c[4], path=f"/en/{c[3]}/{en_s}/", code=pt_s))
    return out

def cats(lang):
    ps = posts(lang)
    i = 0 if lang == "pt" else 2
    return [dict(name=c[i], slug=c[i + 1], obj=c[4], count=sum(1 for p in ps if p["cat"] == c[i])) for c in TECH_CATS]

def shot(p, root, sdate, lang, extra_cls="", style=""):
    """A Tech post: a printed code screenshot taped into the notebook, built
    like a .polaroid so it sits in the same walls as the Vida photos."""
    name, lines = CODE[p["code"]]
    body = "\n".join(lines)
    if lang == "en":
        for a, b in EN_CODE.items():
            body = body.replace(a, b)
    return (f'<a class="polaroid tech-shot {extra_cls}" href="{root}{p["path"].lstrip("/")}"{f" style=\"{style}\"" if style else ""}>'
            f'<span class="polaroid__tag">{e(p["cat"])}</span>'
            f'<span class="code-shot"><span class="code-shot__bar"><span class="code-shot__dots"></span>{e(name)}</span>'
            f'<pre class="code-shot__code"><code>{body}</code></pre></span>'
            f'<span class="polaroid__caption"><span class="polaroid__title">{e(p["title"])}</span>'
            f'<time class="polaroid__meta" datetime="{p["date"]}">{sdate(p["date"])}</time></span></a>')

# A short, real-looking snippet per post for its "code screenshot" cover.
# Spans: k keyword, s string, c comment, f function, n number, p property, t tag.
CODE = {
    "como-o-tymebox-sabe-que-sua-reuniao-vai-atrasar": ("pace.ts", [
        '<span class="c">// já devia ter acabado?</span>',
        '<span class="k">const</span> pace = spent / <span class="f">plan</span>();',
        '',
        '<span class="k">if</span> (pace &gt; <span class="n">1.1</span>) {',
        '  <span class="f">warn</span>(<span class="s">"Vai atrasar"</span>);',
        '}']),
    "dialogos-na-url-por-que-criei-o-dialogs-valve": ("ShareButton.tsx", [
        '<span class="k">const</span> d = <span class="f">useDialog</span>(<span class="s">"share"</span>);',
        '',
        '<span class="k">return</span> (',
        '  &lt;<span class="t">Button</span> <span class="p">onClick</span>={d.open}&gt;',
        '    Compartilhar',
        '  &lt;/<span class="t">Button</span>&gt;',
        ');']),
    "tokens-de-design-so-com-css-e-light-dark": ("tokens.css", [
        '<span class="t">:root</span> {',
        '  <span class="p">color-scheme</span>: light dark;',
        '  <span class="p">--accent</span>: <span class="f">light-dark</span>(',
        '    <span class="n">#527752</span>,',
        '    <span class="n">#a5c5a5</span>',
        '  );',
        '}']),
    "rails-8-sem-build-de-javascript-um-ano-depois": ("importmap.rb", [
        '<span class="c"># config/importmap.rb</span>',
        '<span class="f">pin</span> <span class="s">"application"</span>',
        '<span class="f">pin</span> <span class="s">"@hotwired/turbo"</span>',
        '<span class="f">pin_all_from</span> <span class="s">"app/js"</span>,',
        '  <span class="p">under:</span> <span class="s">"controllers"</span>']),
    "meu-setup-de-2026-terminal-editor-e-atalhos": (".zshrc", [
        '<span class="c"># atalhos que uso todo dia</span>',
        '<span class="k">alias</span> gs=<span class="s">"git status -sb"</span>',
        '<span class="k">alias</span> dev=<span class="s">"bin/dev"</span>',
        '',
        '<span class="f">mkcd</span>() {',
        '  mkdir -p <span class="p">"$1"</span> &amp;&amp; cd <span class="p">"$1"</span>',
        '}']),
}

# The Portuguese bits inside the snippets, for the English covers.
EN_CODE = {"// já devia ter acabado?": "// should it be over by now?", '"Vai atrasar"': '"Running late"',
           "    Compartilhar": "    Share", "# atalhos que uso todo dia": "# shortcuts I use every day"}
