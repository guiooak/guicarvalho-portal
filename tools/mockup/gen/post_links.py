"""Point every link to a post page that the mockup doesn't have at the one
sample post of the same locale, so any post opens while testing.
Run after the page generators."""
import os, re, sys
from urllib.parse import urlsplit

M = __import__("common").MOCKUP
SAMPLE = {"br": "br/idiomas/o-que-te-impede-de-aprender-outro-idioma/",
          "en": "en/languages/what-stops-you-from-learning-another-language/"}
POST = re.compile(r"^(br|en)/[^/]+/[^/]+/(index\.html)?$")
HREF = re.compile(r'href="([^"#?]+)([#?][^"]*)?"')

def exists(rel):
    p = os.path.join(M, rel)
    return os.path.isfile(p) or os.path.isfile(os.path.join(p, "index.html"))

changed, broken = 0, set()
for dirpath, _, files in os.walk(M):
    for f in files:
        if not f.endswith(".html"): continue
        path = os.path.join(dirpath, f); here = os.path.relpath(dirpath, M)
        html = open(path).read()
        def fix(m):
            global changed
            url, suffix = m.group(1), m.group(2) or ""
            if urlsplit(url).scheme or url.startswith(("/", "mailto:")): return m.group(0)
            rel = os.path.normpath(os.path.join(here, url)).replace(os.sep, "/") + ("/" if url.endswith("/") else "")
            if exists(rel): return m.group(0)
            mm = POST.match(rel)
            if not mm: broken.add(f"{os.path.relpath(path, M)} -> {url}"); return m.group(0)
            changed += 1
            target = os.path.relpath(os.path.join(M, SAMPLE[mm.group(1)]), dirpath) + "/"
            return f'href="{target}{suffix}"'
        new = HREF.sub(fix, html)
        if new != html: open(path, "w").write(new)

print(f"post links rewritten: {changed}")
for b in sorted(broken): print("other broken link:", b)
