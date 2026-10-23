import os, re
from common import posts as P, e, S
from en_data import posts as PE, cats_en, CAT_OBJ
from apps import APPS
from groups import home_section, group_switch, tech_nav_items, blog_featured_on, blog_wall_on, states, T as GT
from tech_data import posts as tech_posts

M = __import__("common").MOCKUP
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def sdate(d): y, m, dd = d.split("-"); return f"{MON[int(m)-1]} {int(dd)}, {y}"
def fdate(d): y, m, dd = d.split("-"); return f"{MONTHS[int(m)-1]} {int(dd)}, {y}"
def obj(name): return f'<svg aria-hidden="true"><use href="#obj-{name}"/></svg>'
def arrow(): return '<svg aria-hidden="true"><use href="#icon-arrow-right"/></svg>'

SRC = next(x for x in P if x["slug"] == "o-que-te-impede-de-aprender-outro-idioma")
POST = {"title": "What stops you from learning another language?", "cat": "Languages", "cat_slug": "languages",
        "slug": "what-stops-you-from-learning-another-language", "date": SRC["date"], "cover": SRC["cover"],
        "alt": "Puzzle pieces painted with flags from different countries",
        "excerpt": "Many of us dream of mastering a second language, but sometimes it takes lessons you won't find in any grammar book."}
POST_PATH = "en/languages/what-stops-you-from-learning-another-language/"
PT_POST = SRC["path"].lstrip("/")

def head(title, desc, root, extra=""):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">{extra}
  <link rel="icon" href="{root}assets/images/brand/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{root}assets/stylesheets/application.css?v=2026-10-23a">
  <link rel="stylesheet" href="{root}assets/stylesheets/mockup.css?v=2026-10-23a">
  <script src="{root}assets/javascripts/mockup.js?v=2026-10-23a"></script>
</head>
<body class="paper">
  <div class="site">'''

def foot(root):
    return f'''
    <site-footer root="{root}"></site-footer>
  </div>

  <div class="mockup-toolbar" aria-label="Mockup tools">
    <button type="button" data-notes-toggle>Mockup notes</button>
  </div>
</body>
</html>
'''

def newsletter(title="Want the next post by email? ✉️", r="-1.2deg"):
    if not __import__("common").NEWSLETTER_INLINE:
        return ""
    return f'''<section class="container" aria-labelledby="newsletter-title">
        <div class="sticky-note newsletter-note" id="newsletter" style="--r:{r}">
          <h2 id="newsletter-title">{title}</h2>
          <p>Leave your email on this note. One email per new post, no spam, and you can leave anytime.</p>
          <form action="#" onsubmit="return false">
            <fieldset class="newsletter-topics">
              <legend>Send me</legend>
              <label class="tick"><input type="checkbox" name="groups" value="vida" checked><span class="tick__box" aria-hidden="true"></span><span><strong>Life</strong><small>stories, goals and travel</small></span></label>
              <label class="tick"><input type="checkbox" name="groups" value="tech" checked><span class="tick__box" aria-hidden="true"></span><span><strong>Tech</strong><small>code and front-end</small></span></label>
            </fieldset>
            <label class="visually-hidden" for="newsletter-email">Your email</label>
            <input class="input" id="newsletter-email" type="email" placeholder="you@email.com" autocomplete="email" required>
            <button class="button" type="submit">Stick my email here</button>
          </form>
          <small>You'll get an email to confirm your subscription.</small>
          <aside class="mockup-note" style="margin-block-start: var(--space-sm)">The tick boxes only show up with the Tech section on. Without it, everyone gets everything, and existing subscribers keep both ticked. At least one has to stay ticked.</aside>
        </div>
      </section>'''

def link(p, root): return f"{root}{p['path'].lstrip('/')}"
def cover(p, root): return f"{root}assets/images/covers/{p['cover']}"

def polaroid(p, root, tag=True, lazy=True, extra_cls="", style=""):
    t = f'<span class="polaroid__tag">{e(p["cat"])}</span>' if tag else ""
    return f'''<a class="polaroid {extra_cls}" href="{link(p, root)}"{f' style="{style}"' if style else ''}>{t}<img src="{cover(p, root)}" alt="{e(p['alt'] or p['title'])}" width="768" height="512"{' loading="lazy"' if lazy else ''}><span class="polaroid__caption"><span class="polaroid__title">{e(p['title'])}</span><time class="polaroid__meta" datetime="{p['date']}">{sdate(p['date'])}</time></span></a>'''

APPS_EN = {
    "tymebox": {"short": "Meetings that end on time", "kind": "Productivity", "img": "tymebox-en.png", "tagline": "Every event, inside its box.",
                "alt": "Tymebox share image: 'Every event, inside its box', with a countdown and meeting milestones",
                "desc": "Puts meetings and events in time boxes: plan the milestones, run the countdown, finish on time and then see exactly how it went.",
                "highlights": ["The countdown compares your pace with the plan and warns you when you fall behind", "Ready-made templates for planning, retros and 1:1s", "A report at the end to send to everyone who was there"],
                "open": ("Open Tymebox", "https://tymebox.web.app/")},
    "bat-hunter": {"short": "Aim game in the browser", "kind": "Game", "tagline": "Too many bats. Time to drop some.",
                   "alt": "Bat Hunter artwork: a crosshair on a bat against the moon, haunted houses and pumpkins",
                   "desc": "A browser shooting game born in a hackathon: the night sky is full of bats and your job is to drop as many as you can, with the best aim you can.",
                   "highlights": ["Free play, a 60-second challenge and 1v1 matches with chat", "On Hard: golden bats are worth 10, and the owl costs you points", "Works on desktop and phone"],
                   "open": ("Play now", "https://bat-hunter-game.web.app/")},
    "csv-to-ofx": {"short": "Sicredi bill from CSV to OFX", "kind": "Finance", "tagline": "Your Sicredi bill, ready for your finance app.",
                   "alt": "csv→ofx screen: 'Convert the bill from CSV to OFX', with the file drop area",
                   "desc": "Turns the CSV of a Sicredi credit card bill into an OFX file, ready to import into your personal finance app. The app itself is in Portuguese, for Brazilian users.",
                   "highlights": ["Puts each installment in the right month", "Shows a summary of the bill before the download", "Runs in the browser: no data leaves your computer"],
                   "open": ("Open the app", "https://guiooak.github.io/csv-to-ofx/")},
    "dialogs-valve": {"short": "React dialogs library", "kind": "Library", "tagline": "Modals and drawers driven by the URL.",
                      "alt": "@dialogs-valve/react demo page: 'URL-driven dialog management for React'",
                      "desc": "An open source React library that keeps the state of modals and drawers in the URL, so deep links, the back button and shareable URLs just work.",
                      "highlights": ["Works with any router: Next.js, React Router, TanStack…", "Stacked dialogs, with permission guards", "Strictly typed with TypeScript, published on npm"],
                      "open": ("See the demo", "https://guiooak.github.io/dialogs-valve-react/")},
}

# ---------------------------------------------------------------- Home
root = "../"
ROT = ["-6deg", "4deg", "-2deg", "7deg", "-4deg", "3deg", "-8deg", "5deg", "-3deg", "6deg", "-5deg", "2deg", "-7deg", "4deg", "-1deg"]
VAR = ["", "topic-sticker--paper", "topic-sticker--note", "topic-sticker--sage"]
def tsize(n): return " topic-sticker--lg" if n >= 7 else (" topic-sticker--md" if n >= 4 else "")
def tvar(i): return (" " + VAR[i % 4]) if VAR[i % 4] else ""
topics = "\n".join(f'          <a class="topic-sticker{tsize(c["count"])}{tvar(i)}" href="{root}en/{c["slug"]}/" style="--r:{ROT[i % len(ROT)]}">{obj(CAT_OBJ.get(c["name"], "bulb"))}{e(c["name"])}<span class="topic-sticker__count" aria-label="{c["count"]} posts">{c["count"]}</span></a>' for i, c in enumerate(sorted(cats_en, key=lambda c: c["name"])))
wall = "\n".join("          " + polaroid(p, root) for p in PE[:8])
SHELF_R = ["-6deg", "5deg", "-3deg", "7deg"]
shelf = "\n".join(f'''          <a class="apps-shelf__app" href="{root}en/apps.html#{a['id']}"><span class="sticker" style="--r:{SHELF_R[i]}">{obj(a['obj'])}</span><span>{e(a['name'])}<small>{e(APPS_EN[a['id']]['short'])}</small></span></a>''' for i, a in enumerate(APPS))
home = head("gui carvalho · Stories, goals, languages and apps", "Guilherme Carvalho's notebook: stories, goals, languages, travel and the apps he builds.", root, extra=f'''
  <link rel="alternate" hreflang="pt-BR" href="https://guicarvalho.com.br/br/">
  <link rel="alternate" hreflang="en" href="https://guicarvalho.com.br/en/">''') + f'''
    <site-header root="{root}" current="home" alternate="{root}br/index.html"></site-header>

    <main id="main">
      <section class="container desk" aria-labelledby="intro-title">
        <div>
          <h1 class="desk__title" id="intro-title">Hi, I'm <span class="scribble">Gui</span>.</h1>
          <p class="desk__lead">This is my notebook: stories, goals, languages, travel and the apps I build, pinned here since 2015.</p>
          <div class="cluster">
            <a class="button" href="{root}en/blog.html">Browse the blog</a>
            <a class="button button--secondary" href="{root}en/apps.html">My apps</a>
          </div>
        </div>
        <div class="collage">
          <figure class="polaroid collage__photo" style="--r:-5deg">
            <img src="{root}assets/images/about/gui-paris.jpg" alt="Gui smiling on a viewpoint with Paris in the background" width="768" height="576">
            <figcaption class="polaroid__caption"><span class="polaroid__title">That's me</span><span class="polaroid__meta">Paris, 2016</span></figcaption>
          </figure>
          <div class="sticky-note collage__note" style="--r:4deg">
            <span class="sticky-note__title">Who writes here</span>
            <ul>
              <li>From Ipatinga, Minas Gerais</li>
              <li>Front-end engineer</li>
              <li>Joice's husband</li>
              <li>Elisa's daddy</li>
              <li>Drums, forró and surfing</li>
            </ul>
          </div>
          <nav class="collage__cards" aria-label="What's in here">
            <span class="collage__cards-title">What's in here</span>
            <a class="index-card" href="{root}en/blog.html" style="--r:-2deg"><span class="sticker sticker--sm">{obj("pencil")}</span><span><b>Blog</b><small>{len(PE)} stories since 2015</small></span></a>
            <a class="index-card" href="{root}en/apps.html" style="--r:1.5deg"><span class="sticker sticker--sm">{obj("laptop")}</span><span><b>Apps</b><small>Things I've built</small></span></a>
            <a class="index-card" href="{root}en/about.html" style="--r:-1deg"><span class="sticker sticker--sm">{obj("bulb")}</span><span><b>About</b><small>The authorized biography</small></span></a>
          </nav>
          <span class="sticker collage__deco" style="--r:12deg">{obj("map")}</span>
        </div>
        <aside class="mockup-note" style="grid-column: 1 / -1">The photo and the post-it items come from the "About Gui" page on the current blog and are placeholders until the new material arrives.</aside>
      </section>

      <section class="container" aria-labelledby="apps-title">
        <div class="board-title">
          <span class="sticker" style="--r:8deg">{obj("laptop")}</span>
          <h2 id="apps-title">Things I've built</h2>
          <a class="section-heading__link" href="{root}en/apps.html">See all apps {arrow()}</a>
        </div>
        <div class="apps-shelf">
{shelf}
        </div>
      </section>

      {home_section("en", root, PE, polaroid, sdate)}

      <section class="container" aria-labelledby="topics-title">
        <div class="board-title">
          <span class="sticker" style="--r:-4deg">{obj("pencil")}</span>
          <h2 id="topics-title">What I write about</h2>
          <div class="sticky-note topic-board__note" style="--r:3deg">Pick a topic and peel off the sticker. The bigger it is, the more I've written about it.</div>
        </div>
        <div class="topic-board">
{topics}
        </div>
      </section>

      {newsletter()}
    </main>
''' + foot(root)

# ---------------------------------------------------------------- Blog
cat_nav = f'          <li data-state="tech-off"><a class="tag" href="{root}en/blog.html" aria-current="page">All<span class="category-nav__count">{len(PE)}</span></a></li>\n' + f'          <li data-state="tech-on"><a class="tag" href="{root}en/blog.html" aria-current="page">All<span class="category-nav__count">{len(PE) + len(tech_posts("en"))}</span></a></li>\n' + "\n".join(f'          <li><a class="tag" href="{root}en/{c["slug"]}/">{e(c["name"])}<span class="category-nav__count">{c["count"]}</span></a></li>' for c in sorted(cats_en, key=lambda c: c["name"])) + "\n" + tech_nav_items("en", root)
latest = PE[0]
blog_wall = "\n".join("          " + polaroid(p, root) for p in PE[1:13])
blog = head("Blog · gui carvalho", "Stories about goals, languages, travel and life's shenanigans, since 2015.", root) + f'''
    <site-header root="{root}" current="blog" alternate="{root}br/blog.html"></site-header>

    <main id="main" class="mockup-stateful">
      <section class="container blog-intro" aria-labelledby="blog-title">
        <div class="board-title" style="margin-block-start: var(--space-xl)">
          <span class="sticker" style="--r:-8deg">{obj("pencil")}</span>
          <div>
            <h1 id="blog-title" style="font-size: var(--text-3xl)">Blog</h1>
            <p class="text-muted" style="font-size: var(--text-md)"><span data-state="tech-off">{len(PE)} stories pinned here since 2015.</span><span data-state="tech-on">{len(PE) + len(tech_posts("en"))} stories pinned here since 2015.</span></p>
          </div>
        </div>
        <div data-state="tech-on">{group_switch("en", root, "all")}</div>
        <nav class="category-nav" aria-label="Categories">
          <ul class="category-nav__list" role="list">
{cat_nav}
          </ul>
        </nav>
      </section>

      {blog_featured_on("en", root, sdate)}

      <section class="container featured-entry" aria-label="Latest post" data-state="tech-off">
        {polaroid(latest, root, lazy=False, extra_cls="polaroid--wide featured-entry__photo", style="--r:-2deg")}
        <div class="sticky-note featured-entry__note" style="--r:3deg">
          <span class="sticky-note__title">Latest post</span>
          <h2 class="featured-entry__title"><a href="{link(latest, root)}">{e(latest["title"])}</a></h2>
          <p>{e(latest["excerpt"])}</p>
          <a class="featured-entry__more" href="{link(latest, root)}">Read it now {arrow()}</a>
        </div>
      </section>

      <section class="container" aria-label="All posts">
        <div class="wall" style="margin-block-start: var(--space-xl)" data-state="tech-off">
{blog_wall}
        </div>
        <div class="wall" style="margin-block-start: var(--space-xl)" data-state="tech-on">
{blog_wall_on("en", root, PE, polaroid, sdate)}
        </div>
        <nav class="pagination" aria-label="Pagination">
          <a class="pagination__page" href="{root}en/blog.html" aria-current="page">1</a>
          <a class="pagination__page" href="#">2</a>
          <a class="pagination__page" href="#">Next <svg width="16" height="16" aria-hidden="true" style="margin-inline-start:.3em"><use href="#icon-arrow-right"/></svg></a>
        </nav>
        <aside class="mockup-note" style="margin-block-start: var(--space-md)">The filters lead to the category pages, which reuse this layout. Only the post "What stops you from learning another language?" has a page in the mockup.</aside>
      </section>

      {newsletter()}
      <aside class="container mockup-note">{GT["en"]["blog_note"]}</aside>
      {states("en", floating=True)}
    </main>
''' + foot(root)

# ---------------------------------------------------------------- Post
proot = "../../../"
article = open(f"{S}/wp/article-en.html").read().replace("IMGROOT", f"{proot}assets/images/posts/")
words = len(re.sub(r"<[^>]+>", " ", article).split()); minutes = max(1, round(words / 220))
body = "\n".join("            " + l for l in article.strip().splitlines())
comments = f'''<section class="comments mockup-stateful illo" id="comments" aria-labelledby="comments-title">
        <fieldset class="mockup-states">
          <legend class="visually-hidden">Comment state in the mockup</legend>
          <span>State:</span>
          <label><input type="radio" name="comments-state" value="signed-out" checked>Visitor</label>
          <label><input type="radio" name="comments-state" value="signed-in">Signed in</label>
          <label><input type="radio" name="comments-state" value="empty">No comments</label>
        </fieldset>

        <h2 class="comments__title" id="comments-title"><span data-state="signed-out signed-in">Comments <span class="comments__count">(3)</span></span><span data-state="empty">Comments</span></h2>

        <div class="comments__signin" data-state="signed-out empty">
          <p>Sign in with your Google account to comment. We only use your name and photo, and never publish your email.</p>
          <a class="button button--google" href="#"><svg aria-hidden="true"><use href="#icon-google"/></svg>Sign in with Google</a>
        </div>

        <form class="comment-form" action="#" onsubmit="return false" data-state="signed-in">
          <div class="comment-form__who"><span class="avatar avatar--sm" aria-hidden="true">E</span>Commenting as <strong>Emma Walsh</strong> · <a href="#">sign out</a></div>
          <label class="visually-hidden" for="comment-body">Your comment</label>
          <textarea class="input" id="comment-body" placeholder="What did you think of the post?"></textarea>
          <div class="comment-form__actions">
            <span>Your first comment is reviewed before everyone can see it.</span>
            <button class="button" type="submit">Post comment</button>
          </div>
        </form>

        <div class="comments__empty" data-state="empty">
          <svg aria-hidden="true"><use href="#obj-chat"/></svg>
          <strong>No comments yet.</strong>
          <span>How about being the first?</span>
        </div>

        <ol class="comment-list" role="list" data-state="signed-out signed-in">
          <li class="comment comment--pending" data-state="signed-in">
            <span class="avatar" aria-hidden="true">E</span>
            <div class="comment__body">
              <div class="comment__meta"><strong>Emma Walsh</strong><time datetime="2026-10-19">just now</time></div>
              <span class="comment__status">Awaiting moderation · only you can see this</span>
              <p>The joke test is brilliant. I'll try it in my next Portuguese class!</p>
            </div>
          </li>
          <li class="comment">
            <span class="avatar" aria-hidden="true">L</span>
            <div class="comment__body">
              <div class="comment__meta"><strong>Liam Byrne</strong><time datetime="2017-01-10">January 10, 2017</time></div>
              <p>Switching my phone to Spanish was painful for a week and then it just clicked. Great tips.</p>
              <div class="comment__actions"><button type="button">Reply</button></div>
            </div>
            <ol class="comment__replies" role="list">
              <li class="comment comment--author">
                <span class="avatar avatar--sm" aria-hidden="true">G</span>
                <div class="comment__body">
                  <div class="comment__meta"><strong>Gui Carvalho</strong><time datetime="2017-01-11">January 11, 2017</time></div>
                  <p>That first week is the worst part. After that the GPS in Spanish becomes pure fun!</p>
                </div>
              </li>
            </ol>
          </li>
          <li class="comment">
            <span class="avatar" aria-hidden="true">S</span>
            <div class="comment__body">
              <div class="comment__meta"><strong>Sean Murphy</strong><time datetime="2017-01-04">January 4, 2017</time></div>
              <p>Comparing hours of classes with living abroad made me rethink everything. Thanks for the post!</p>
              <div class="comment__actions"><button type="button">Reply</button></div>
            </div>
          </li>
        </ol>
        <aside class="mockup-note">The comments and names are made up, just to illustrate. Use the state buttons above to see the post for visitors, for signed-in readers (with a comment awaiting moderation) and with no comments.</aside>
      </section>'''
post = head(f"{POST['title']} · gui carvalho", POST["excerpt"], proot, extra=f'''
  <link rel="alternate" hreflang="pt-BR" href="https://guicarvalho.com.br{SRC['path']}">
  <link rel="alternate" hreflang="en" href="https://guicarvalho.com.br/{POST_PATH}">''') + f'''
    <site-header root="{proot}" current="blog" alternate="{proot}{PT_POST}"></site-header>

    <main id="main">
      <article class="container container--narrow">
        <header class="post-header">
          <nav aria-label="You are here">
            <ol class="breadcrumb" role="list">
              <li><a href="{proot}en/blog.html">Blog</a></li>
              <li><a href="{proot}en/{POST['cat_slug']}/">{POST['cat']}</a></li>
            </ol>
          </nav>
          <h1 class="post-header__title">{e(POST['title'])}</h1>
          <p class="post-header__lead">{e(POST['excerpt'])}</p>
          <div class="post-meta">
            <span class="post-meta__author"><span class="avatar avatar--sm" aria-hidden="true"><img src="{proot}assets/images/about/gui-paris.jpg" alt=""></span>Gui Carvalho</span>
            <span class="post-meta__sep" aria-hidden="true">·</span>
            <time datetime="{POST['date']}">{fdate(POST['date'])}</time>
            <span class="post-meta__sep" aria-hidden="true">·</span>
            <span>{minutes} min read</span>
            <span class="post-meta__sep" aria-hidden="true">·</span>
            <span class="post-languages" lang="pt-BR">Também em <a class="tag" href="{proot}{PT_POST}" hreflang="pt-BR">Português</a></span>
          </div>
        </header>

        <figure class="polaroid polaroid--wide post-photo" style="--r:-1.5deg">
          <img src="{proot}assets/images/covers/{POST['cover']}" alt="{e(POST['alt'])}" width="768" height="512">
        </figure>

        <div class="sheet">
          <div class="post-body">
{body}
          </div>

          <footer class="post-footer">
            <div class="cluster">
              <a class="tag" href="{proot}en/productivity/">Productivity</a>
              <a class="tag" href="{proot}en/languages/">Languages</a>
              <a class="tag" href="{proot}en/travel/">Travel</a>
            </div>
            <div class="share">
              <span>Share</span>
              <button class="icon-button" type="button" aria-label="Copy link"><svg aria-hidden="true"><use href="#icon-link"/></svg></button>
              <a class="button button--ghost button--small" href="#">LinkedIn</a>
              <a class="button button--ghost button--small" href="#">WhatsApp</a>
            </div>
          </footer>

          <aside class="author-note" aria-label="About the author">
            <figure class="polaroid" style="--r:-4deg"><img src="{proot}assets/images/about/gui-paris.jpg" alt="" width="768" height="576"></figure>
            <div class="sticky-note" style="--r:2deg">
              <span class="sticky-note__title">Written by</span>
              <p>Gui Carvalho: from Minas Gerais, front-end engineer and curious by nature. Writes about career, goals, languages and life's shenanigans.</p>
              <a href="{proot}en/about.html"><b>More about me →</b></a>
            </div>
          </aside>
        </div>
      </article>

      {newsletter("Liked it? Get the next one by email ✉️", "1.2deg")}

      <section class="container" aria-labelledby="related-title">
        <div class="board-title">
          <span class="sticker" style="--r:6deg">{obj("plane")}</span>
          <h2 id="related-title">Keep reading</h2>
        </div>
        <div class="wall">
{chr(10).join("          " + polaroid(r, proot) for r in [next(x for x in PE if x["pt_slug"] == s) for s in ["quem-e-mineiro-me-entende", "o-inicio-dos-sonhos", "aumentando-sua-auto-confianca-em-apenas-2-minutos"]])}
        </div>
      </section>

      <div class="container container--narrow" style="margin-block-start: var(--space-2xl)">
        <div class="sheet">
      {comments}
        </div>
      </div>
    </main>
''' + foot(proot)

# ---------------------------------------------------------------- Apps
def ext_icon(): return '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></svg>'
def spread(a):
    x = APPS_EN[a["id"]]
    hl = "".join(f"<li>{e(h)}</li>" for h in x["highlights"])
    tech = "".join(f'<span class="tag">{e(t)}</span>' for t in a["tech"]).replace("Open source", "Open source")
    img = x.get("img", a["img"])
    return f"""      <section class="app-spread" id="{a['id']}" aria-labelledby="{a['id']}-title">
        <a class="polaroid polaroid--wide app-spread__shot" href="{x['open'][1]}" style="--r:{a['r']}"><span class="polaroid__tag">{e(x['kind'])}</span><img src="{root}assets/images/apps/{img}" alt="{e(x['alt'])}" width="1200" height="630" loading="lazy"></a>
        <div class="app-spread__card">
          <div class="app-spread__head">
            <span class="sticker">{obj(a['obj'])}</span>
            <div><h2 id="{a['id']}-title">{e(a['name'])}</h2><p>{e(x['tagline'])}</p></div>
          </div>
          <p>{e(x['desc'])}</p>
          <ul class="app-spread__highlights">{hl}</ul>
          <div class="cluster app-spread__tech">{tech}</div>
          <div class="cluster app-spread__actions">
            <a class="button" href="{x['open'][1]}">{e(x['open'][0])} {ext_icon()}</a>
            <a class="button button--secondary" href="{a['code']}">Code on GitHub</a>
          </div>
        </div>
      </section>"""
cards = "".join(f'          <a class="index-card" href="#{a["id"]}" style="--r:{("-2deg","1.5deg","-1deg","2deg")[i]}"><span class="sticker sticker--sm">{obj(a["obj"])}</span><span><b>{e(a["name"])}</b><small>{e(APPS_EN[a["id"]]["kind"])}</small></span></a>\n' for i, a in enumerate(APPS))
apps_html = head("Apps · gui carvalho", "The apps Gui has built: Tymebox, Bat Hunter, csv→ofx and Dialogs Valve.", root) + f"""
    <site-header root="{root}" current="apps" alternate="{root}br/apps.html"></site-header>

    <main id="main">
      <div class="container">
        <div class="board-title" style="margin-block-start: var(--space-xl)">
          <span class="sticker" style="--r:8deg">{obj("laptop")}</span>
          <div>
            <h1 style="font-size: var(--text-3xl)">Things I've built</h1>
            <p class="text-muted" style="font-size: var(--text-md)">Built to solve a problem of my own, or not. But always for fun. All free to use, with the code on GitHub.</p>
          </div>
        </div>
        <nav class="cluster" aria-label="Apps on this page" style="--cluster-gap: var(--space-sm)">
{cards}        </nav>
{chr(10).join(spread(a) for a in APPS)}
      </div>

      {newsletter("Want to know when there's something new? ✉️")}
    </main>
""" + foot(root)

# ---------------------------------------------------------------- About
BIO = [
    ("mountain", "Raised in Viçosa", ["Born in Ipatinga, Brazil, in 1987, Guilherme Pereira de Carvalho holds a degree in Computer Science from the Federal University of Viçosa. He spent a mere 9 years there, and made the most of every one of them."]),
    ("heart", "Family", ["Very, very happily married to Joice and very lucky to be Elisa's dad, the biggest dream of his life come true: being a father! He never misses a family party. He may not be the first to arrive, but he's usually one of the last to leave."]),
    ("map", "Home", ["From Minas Gerais at heart, he lives there for now, but he has also lived in Joinville and Navegantes, in Santa Catarina, and will go back someday: he loves both places. Along the way he also lived in Belo Horizonte."]),
    ("laptop", "Work", ["A front-end engineer, he has worked for an American company for more than 5 years, with React, TypeScript and Ruby on Rails. He is passionate about front-end development, especially component libraries and code organization.",
                        f'Before that, he volunteered for years at a student-run consulting company and co-founded a company where he worked for three years. In his spare time he uses his creativity to study and build his own apps (<a href="{root}en/apps.html">take a look at them</a>).']),
    ("chip", "Fixes and inventions", ["He is well known for his gambiarras, the Brazilian word for clever improvised fixes, and for repairing just about anything: if it broke, he'll find a way. He loves electronics and making new things, from the soldering iron to the code editor."]),
    ("clover", "A year in Dublin", ["He went on an exchange to Dublin, Ireland: he worked, studied English and travelled a lot. There he had some of the most valuable experiences of his life, meeting one-of-a-kind people and fabulous places."]),
    ("suitcase", "Travel", ["Travel matters a lot to him. Inspired by Amyr Klink, the Brazilian sailor and explorer, he has been to 12 countries and spent 3 months travelling with Joice as a digital nomad. He loves getting to know new cultures and different people, and dreams of buying a motorhome to take many trips with his own family."]),
    ("note", "Music", ["He can't live without his daily dose of music, mostly good old rock, but old-school Brazilian country, some MPB and a good forró to dance to have their place too. He likes listening to the radio and to vinyl records on his vintage Gradiente receiver, a Brazilian classic exactly as old as he is. He plays the drums for fun, plays the guitar for his daughter and takes forró dance classes with Joice."]),
    ("wave", "Weekend athlete", ["He swims, has run a half marathon and has a yellow belt in judo. He has a dormant passion for mountain biking and is now learning to surf. And for the future, his dream is to become a triathlon competitor."]),
    ("bulb", "Who he is", ["Positive, cheerful and playful, he can make lifelong friends in a few minutes. Still, he's objective, precise and direct when he needs to be."]),
]
FACTS = [("Plays the drums for fun.", ""), ("Plays the guitar for his daughter.", " sticky-note--sage"),
         ("Has a yellow belt in judo.", ""), ("Has run a half marathon.", " sticky-note--sage"),
         ("Takes forró dance classes with Joice.", " sticky-note--sage"), ("Is learning to surf.", ""),
         ("King of improvised fixes: if it broke, he fixes it.", " sticky-note--sage"), ("Makes lifelong friends in a few minutes.", "")]
SOCIAL = [("LinkedIn", "Career and work", "https://www.linkedin.com/in/linkguicarvalho", "laptop"), ("GitHub", "The code of my apps", "https://github.com/guiooak", "window"),
          ("YouTube", "Videos now and then", "http://youtube.com/c/GuilhermeCarvalhoOnline", "note"), ("Instagram", "Photos and travel", "https://www.instagram.com/guicarvalho.com.br", "plane")]
bio_html = "\n".join(f"""            <section class="bio-section" aria-labelledby="bio-{i}">
              <span class="sticker" style="--r:{("-6deg","5deg","-3deg","7deg","-5deg","4deg","-4deg","6deg","-2deg","3deg")[i % 10]}">{obj(o)}</span>
              <div><h2 id="bio-{i}">{e(t)}</h2>{"".join(f"<p>{p}</p>" for p in ps)}</div>
            </section>""" for i, (o, t, ps) in enumerate(BIO))
facts_html = "\n".join(f'          <div class="sticky-note{v}">{e(t)}</div>' for t, v in FACTS)
social_html = "\n".join(f'          <a class="index-card" href="{u}" target="_blank" rel="noopener" style="--r:{("-2deg","1.5deg","-1deg","2deg")[i]}"><span class="sticker sticker--sm">{obj(o)}</span><span><b>{n}</b><small>{d}</small></span><span class="visually-hidden"> (opens in a new tab)</span></a>' for i, (n, d, u, o) in enumerate(SOCIAL))
about = head("About · gui carvalho", "Gui's authorized biography: from Ipatinga to Viçosa, a year in Dublin, rock, cycling and pão de queijo.", root) + f"""
    <site-header root="{root}" current="about" alternate="{root}br/sobre.html"></site-header>

    <main id="main">
      <div class="container">
        <div class="board-title" style="margin-block-start: var(--space-xl)">
          <span class="sticker" style="--r:-8deg">{obj("bulb")}</span>
          <div>
            <h1 style="font-size: var(--text-3xl)">About <span class="scribble">Gui</span></h1>
            <p class="text-muted" style="font-size: var(--text-md)">The authorized biography, pinned to the notebook.</p>
          </div>
        </div>

        <section class="about-hero" aria-label="Fact sheet">
          <figure class="polaroid" style="--r:-4deg">
            <img src="{root}assets/images/about/gui-paris.jpg" alt="Gui smiling on a viewpoint with Paris in the background" width="768" height="576">
            <figcaption class="polaroid__caption"><span class="polaroid__title">Me, in Paris</span><span class="polaroid__meta">2016</span></figcaption>
          </figure>
          <div class="sticky-note fact-sheet" style="--r:3deg">
            <span class="sticky-note__title">Fact sheet</span>
            <dl>
              <div><dt>Name</dt><dd>Guilherme Pereira de Carvalho</dd></div>
              <div><dt>Born in</dt><dd>Ipatinga, Brazil, in 1987</dd></div>
              <div><dt>Work</dt><dd>Front-end engineer</dd></div>
              <div><dt>Family</dt><dd>Joice's husband and Elisa's dad</dd></div>
              <div><dt>Has lived in</dt><dd>Viçosa, Dublin, Joinville, Navegantes and Belo Horizonte</dd></div>
              <div><dt>Can't live without</dt><dd>Family, rock, a laptop and pão de queijo</dd></div>
            </dl>
          </div>
        </section>
      </div>

      <div class="container container--narrow">
        <div class="sheet">
{bio_html}
          <aside class="mockup-note" style="margin-block-start: var(--space-lg)">Biography updated from the 2016 "Authorized Biography" and Gui's answers (family, work, Dublin, music and sports).</aside>
        </div>
      </div>

      <section class="container" aria-labelledby="facts-title">
        <div class="board-title">
          <span class="sticker" style="--r:6deg">{obj("pencil")}</span>
          <h2 id="facts-title">Random facts</h2>
        </div>
        <div class="fact-wall">
{facts_html}
        </div>
      </section>

      <section class="container" aria-labelledby="gift-title">
        <div class="sticky-note newsletter-note" style="--r:-1.5deg">
          <span class="sticker" style="--r:10deg; float: right; margin: 0 0 var(--space-xs) var(--space-sm)">{obj("mug")}</span>
          <h2 id="gift-title">Want to give me a present?</h2>
          <p>Buy a couple of craft beers and invite yourself over to drink them with me. Or give me a rock vinyl record: it goes straight onto the Gradiente! :)</p>
        </div>
      </section>

      <section class="container" aria-labelledby="find-title">
        <div class="board-title">
          <span class="sticker" style="--r:-5deg">{obj("plane")}</span>
          <h2 id="find-title">Where to find me</h2>
        </div>
        <nav class="cluster" style="--cluster-gap: var(--space-md)" aria-label="Social">
{social_html}
        </nav>
      </section>

      {newsletter()}
    </main>
""" + foot(root)

os.makedirs(f"{M}/{POST_PATH}", exist_ok=True)
open(f"{M}/en/index.html", "w").write(home)
open(f"{M}/en/blog.html", "w").write(blog)
open(f"{M}/en/apps.html", "w").write(apps_html)
open(f"{M}/en/about.html", "w").write(about)
open(f"{M}/{POST_PATH}index.html", "w").write(post)
print("ok", minutes)
