# Mockup generator

Python scripts that build the static HTML in `/mockup`. The CSS, JS and images
in `mockup/assets` are hand-written; the pages are generated. Edit the scripts,
then regenerate. Don't hand-edit generated HTML, or the next run overwrites it.

Standard library only, Python 3.12+.

## Run

From the repo root:

```bash
cd tools/mockup/gen && for f in bento revista timeline caderno indice pages pages_en pages_m4 emails admin; do python3 $f.py; done && python3 post_links.py
```

`post_links.py` runs last. The mockup has one real post page per locale, so it
points every other post link at that sample post.

To try a change without touching `/mockup`, set `MOCKUP_OUT` to a copy:

```bash
MOCKUP_OUT=/tmp/mockup-copy python3 pages.py
```

## Serve

```bash
python3 tools/mockup/serve.py
```

Serves `/mockup` on http://localhost:8000 with caching off, so the browser
always picks up regenerated pages and edited CSS without a hard reload.

## Publish

Every push to `main` that changes `mockup/` deploys it to GitHub Pages
(`.github/workflows/mockup-pages.yml`): https://guiooak.github.io/guicarvalho-portal/

## Files

| Script | Writes |
| --- | --- |
| `common.py` | Shared data and helpers; paths (`S` = `data/`, `MOCKUP`) |
| `pages.py` | `br/` home, blog, sample post, apps, about |
| `pages_en.py` | `en/` home, blog, sample post, apps, about |
| `en_data.py` | English titles, slugs and excerpts for every post and category |
| `pages_m4.py` | Category and tag pages (both locales), sign-in, newsletter pages, 404; runs `search_a.py` |
| `search_a.py` | `br/busca.html`, `en/search.html` |
| `apps.py` | Data for the four apps |
| `emails.py` | `emails/` |
| `admin.py` | `admin/` |
| `bento.py`, `revista.py`, `timeline.py`, `caderno.py`, `indice.py` | The five layout concepts in `explorations/` |
| `tech_data.py`, `groups.py` | Made-up Tech posts and the Vida / Tech group building blocks |
| `blog_groups_explore.py`, `newsletter_choice_explore.py` | Exploration pages in `explorations/` |
| `../validate.py` | Light HTML checks: `python3 validate.py ../../mockup/**/*.html` |

`data/wp/` holds what came from the WordPress API: posts, categories, tags and
the sample post's article HTML (plus its English translation).
