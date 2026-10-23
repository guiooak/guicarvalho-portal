"""Lightweight HTML checks: tag nesting, duplicate ids, nested interactive
elements, missing alt/lang/title, labels for form fields, heading order."""
import sys, os, re
from html.parser import HTMLParser

VOID = {"area","base","br","col","embed","hr","img","input","link","meta","source","track","wbr"}
OPTIONAL_CLOSE = {"p","li","dt","dd","option","tr","td","th","thead","tbody"}
INTERACTIVE = {"a","button","select","textarea","label"}
SVG_INNER = {"svg","use","path","circle","rect","ellipse","g","symbol","defs","line","polygon","polyline","filter","clippath","pattern"}

class V(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.ids, self.issues, self.labels_for, self.fields, self.headings = [], {}, [], set(), [], []
        self.has_lang = self.has_title = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html" and a.get("lang"): self.has_lang = True
        if tag == "title": self.has_title = True
        if "id" in a:
            self.ids[a["id"]] = self.ids.get(a["id"], 0) + 1
        if tag == "img" and "alt" not in a: self.issues.append(f"img without alt: {a.get('src','')[:60]}")
        if tag in ("a", "button") and any(t in ("a", "button") for t in self.stack): self.issues.append(f"<{tag}> nested inside {[t for t in self.stack if t in ('a','button')]}")
        if tag == "label" and a.get("for"): self.labels_for.add(a["for"])
        if tag in ("input", "textarea", "select") and a.get("type") not in ("hidden", "radio", "checkbox", "submit"):
            inside_label = "label" in self.stack
            self.fields.append((a.get("id"), bool(a.get("aria-label")), inside_label, a.get("name") or a.get("placeholder") or tag))
        if re.fullmatch(r"h[1-6]", tag): self.headings.append(int(tag[1]))
        if tag not in VOID and tag not in SVG_INNER or tag == "svg":
            self.stack.append(tag)
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1] == tag: self.stack.pop()
    def handle_endtag(self, tag):
        if tag in VOID or (tag in SVG_INNER and tag != "svg"): return
        if tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                t = self.stack.pop()
                if t not in OPTIONAL_CLOSE: self.issues.append(f"unclosed <{t}> before </{tag}>")
            self.stack.pop()
        else:
            self.issues.append(f"stray </{tag}>")

root = sys.argv[1]
total = 0
for dp, _, fs in os.walk(root):
    if "/explorations" in dp: continue
    for f in fs:
        if not f.endswith(".html"): continue
        path = os.path.join(dp, f)
        v = V(); v.feed(open(path, encoding="utf-8").read()); v.close()
        issues = list(v.issues)
        issues += [f"duplicate id '{k}' ×{n}" for k, n in v.ids.items() if n > 1]
        if not v.has_lang: issues.append("missing <html lang>")
        if not v.has_title: issues.append("missing <title>")
        for fid, aria, in_label, name in v.fields:
            if not (aria or in_label or (fid and fid in v.labels_for)): issues.append(f"form field without label: {name}")
        hs = v.headings
        if hs and hs.count(1) != 1 and "/emails/" not in path or (hs and hs.count(1) > 1): issues.append(f"h1 count = {hs.count(1)}")
        for a, b in zip(hs, hs[1:]):
            if b > a + 1: issues.append(f"heading jump h{a} → h{b}"); break
        if issues:
            total += len(issues)
            print(path.replace(root, ""), "\n   - " + "\n   - ".join(dict.fromkeys(issues)))
print("TOTAL", total)
