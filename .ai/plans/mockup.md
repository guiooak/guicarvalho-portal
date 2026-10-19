# Gui Carvalho Portal — High-Fidelity Mockup

Plan for phase 1: a high-fidelity, static prototype of the portal. Its purpose is to settle the visual design, information architecture, content structure and page states **before** any application code is written. Once approved, its HTML and CSS are carried into phase 2 (the Rails application) with minimal rework.

See [architecture.md](architecture.md) for the application decisions this mockup must respect.

## Principles

- **Plain HTML + CSS.** No backend, no build step, no package manager, no framework.
- **As little JavaScript as possible.** Interactivity uses native HTML first: `<details>`, the `popover` attribute, `<dialog>`, `:target`, `:has()`. JavaScript is allowed only where listed under [JavaScript budget](#javascript-budget).
- **Production-grade CSS.** The stylesheets are written exactly as they will live in the Rails app (`app/assets/stylesheets/`), using the same layers, tokens and naming. They are copied over, not rewritten.
- **Easy to change.** Design decisions live in tokens (CSS custom properties). Changing a color, font or spacing scale is a one-line edit.
- **Realistic content.** Real post titles, categories and excerpts from the current blog, and at least one full real article, so typography and layout are validated against actual content rather than lorem ipsum.
- **Mirrors the final information architecture.** Every page in the mockup corresponds to a route in the app, in both locales where relevant.

## How to run

Open `mockup/index.html` directly in a browser (works over `file://`), or serve the folder:

```bash
ruby -run -e httpd mockup -p 8000
```

`mockup/index.html` is a **page directory**: a hub linking to every page and state in the prototype, used for reviews.

## Folder structure

```
mockup/
  index.html                  # page directory for reviewers
  styleguide/                 # the style guide, in its own folder
    index.html                # tokens and every component in isolation
    styleguide.css            # layout of the style guide page; NOT ported
  assets/
    stylesheets/
      application.css         # @layer order + imports (same file as in Rails)
      vendor/open-props/      # vendored Open Props modules actually used
      tokens.css              # portal tokens built on top of Open Props
      reset.css
      base.css                # elements: typography, links, forms, media
      layout.css              # page shell, containers, grids
      components/             # one file per component
        site-header.css
        site-footer.css
        post-card.css
        post-body.css         # article typography (ActionText output)
        app-card.css
        comment.css
        newsletter-form.css
        button.css
        ...
      utilities.css
      mockup.css              # mockup-only helpers (annotations); NOT ported
    javascripts/
      mockup.js               # the whole JavaScript budget; NOT ported as-is
    images/                   # placeholder images and real covers
    fonts/                    # self-hosted fonts (no third-party requests)
  br/                         # pt-BR pages
  en/                         # en pages
  emails/                     # email templates
  admin/                      # admin area screens
```

## CSS architecture

- Layer order declared once in `application.css`:

  ```css
  @layer reset, vendor, tokens, base, layout, components, utilities, mockup;
  ```

- **Open Props** is vendored (downloaded once into `vendor/`) and only the modules in use are imported.
- **Portal tokens** (`tokens.css`) give semantic names on top of Open Props, e.g. `--color-surface`, `--color-text`, `--color-accent`, `--font-body`, `--font-heading`, `--measure-reading`, `--space-section`. Components use only semantic tokens, never raw Open Props values, so the theme can be swapped from a single file.
- **Dark mode** via `prefers-color-scheme`, overridable with `[data-theme]` on `<html>`.
- **Naming**: one root class per component (`.post-card`), child elements as `.post-card__title`, variants as `.post-card--featured`. Each component maps to one Rails partial.
- **Native CSS only**: nesting, custom properties, `@layer`, container queries, `:has()`, `clamp()` for fluid type. No preprocessor.
- **Mobile-first**, with container queries for components and few global breakpoints.

## JavaScript budget

Only `mockup.js`, a classic script (so `file://` keeps working), containing:

1. **Shared chrome**: `<site-header>` and `<site-footer>` custom elements that render the header and footer markup from one place, so a navigation change is a single edit across every page. In phase 2 these become Rails partials; the markup is copied out of the template strings.
2. **Theme switch** for reviewing light/dark (writes `data-theme` on `<html>`).
3. **Annotations switch** that shows or hides `.mockup-note` callouts.
4. **SVG sprite**: injects the shared symbols (logo, UI icons, flat illustrations) once per page, so every page can `<use>` them without an external sprite file, which `file://` would block. In phase 2 the sprite becomes a Rails partial rendered in the layout.

Everything else (mobile menu, language switcher, share menu, dialogs) uses native HTML (`popover`, `<details>`, `<dialog>`). If a page ever needs more, it is discussed first and implemented as a future Stimulus controller.

## Annotations

Reviewer notes live in the markup as `<aside class="mockup-note">…</aside>` next to the element they describe (e.g. "list shows only posts with a published translation in this locale"). They are styled in `mockup.css`, toggled by the annotations switch, and are never ported.

## Pages and states

Pages are listed with their future route. **P1** pages are needed for the first review; **P2** come after the visual direction is approved.

### Public (pt-BR in `br/`, en in `en/`)

| Page | Future route | Priority | Notes |
|---|---|---|---|
| Home | `/br`, `/en` | P1 | Intro/hero, latest posts, featured apps, newsletter CTA |
| Blog index | `/br/blog` | P1 | Paginated list, category navigation |
| Post | `/br/<category>/<slug>` | P1 | Full real article; see post states below |
| Apps | `/br/apps` | P1 | Showcase grid |
| About | `/br/sobre`, `/en/about` | P1 | Bio, photo, links, social profiles |
| Category | `/br/<category>` | P2 | Reuses blog index layout |
| Tag | `/br/tag/<slug>` | P2 | Reuses blog index layout |
| Search results | `/br/busca?q=` | P2 | Results + empty state |
| Sign in | `/br/entrar` | P2 | Google button only |
| Newsletter: check your inbox | — | P2 | After sign-up |
| Newsletter: confirmed | — | P2 | |
| Newsletter: unsubscribed | — | P2 | |
| 404 | — | P2 | |

The English folder needs at least Home, Post (a translated article), Apps and About to validate the language switcher, hreflang behavior and a post that exists in only one language.

### Post page states

- Post with cover image, headings, quote, list, inline images, a code block and a YouTube embed.
- Post without a cover image.
- Language switcher with a translation available, and with no translation.
- Comments: signed out (call to sign in with Google), signed in (form), list with one level of replies, a comment pending moderation (visible only to its author), empty state.
- Related posts and newsletter CTA at the end.

### Emails (`emails/`)

Table-based HTML with inline-friendly CSS, as real email clients require. Preview-only here; production versions become ActionMailer views.

- Subscription confirmation (double opt-in).
- New post newsletter.
- New comment notification for the admin.

### Admin (`admin/`, P2)

Lightweight, functional screens to validate content workflows, not polished design:

- Dashboard.
- Posts list and post editor (title, slug, excerpt, ActionText-like body area, translations tabs per locale, SEO fields, cover, category, tags, status).
- Comments moderation queue.
- Subscribers list.
- Send newsletter (broadcast preview and confirmation).

## Visual direction

The agreed brief lives in [visual-direction.md](visual-direction.md): a clean white base, a green accent, automatic dark mode, no mascot, and subtle fun from floating illustrated objects, hand-drawn touches and CSS micro-interactions.

Before building every page, settle the details within that brief:

1. Build the style guide (`styleguide/index.html`) with the token scales (color, type, spacing, radius, shadow) and base components.
2. Produce **two variations** applied to the same two screens (Home and Post header), differing in typography pairing, green shade and density.
3. The user picks one (or a mix); its values go into `tokens.css` and the other is deleted.

Decisions to make during this step are the open items listed in [visual-direction.md](visual-direction.md), plus the reading width (target ~65ch).

## Quality bar

- **Responsive**: verified at 360px, 768px, 1280px and 1600px widths; no horizontal scroll.
- **Accessibility**: semantic landmarks, skip link, visible focus states, WCAG AA contrast in both themes, alt text, `lang` attributes.
- **Performance**: no third-party requests; fonts self-hosted and subset; images sized and lazy-loaded.
- **Validity**: HTML passes the W3C validator.

## Milestones

1. **Foundations** — folder structure, layers, vendored Open Props, reset/base, `mockup.js`, page directory.
2. **Visual direction** — style guide and two directions for Home and Post header; user chooses.
3. **Core pages (P1)** — Home, Blog index, Post (all states), Apps, About in pt-BR; English Home, Post, Apps, About.
4. **Secondary pages (P2)** — Category, Tag, Search, Sign in, newsletter pages, 404.
5. **Emails** — the three templates.
6. **Admin** — the lightweight admin screens.
7. **Review and approval** — responsive and accessibility pass, annotations reviewed, mockup frozen and tagged (`mockup-v1`).

Each milestone ends with a review by the user before the next one starts.

**Status (2026-10-19)**: milestones 1–2 done. In milestone 3, the first card-grid version of Home, Blog and Post was rejected as too plain; after prototyping five layout concepts in `mockup/explorations/`, the pages were rebuilt with the chosen "Caderno" layout (see [visual-direction.md](visual-direction.md)). Apps and About wait for the user's material.

## Handover to phase 2

When the Rails app is created:

- `assets/stylesheets/**` (except `mockup.css`) is copied into `app/assets/stylesheets/` unchanged.
- `fonts/` and real images move to `app/assets/`.
- Each page becomes a view, and each component becomes a partial, following this mapping:

  | Mockup | Rails |
  |---|---|
  | `<site-header>` template | `app/views/layouts/_site_header.html.erb` |
  | `<site-footer>` template | `app/views/layouts/_site_footer.html.erb` |
  | `.post-card` markup | `app/views/posts/_post_card.html.erb` |
  | `br/post.html` | `app/views/posts/show.html.erb` |
  | `emails/*.html` | `app/views/*_mailer/*.html.erb` |

- Static text becomes I18n keys in `config/locales/pt-BR.yml` and `en.yml`.
- Any interaction that needs JavaScript becomes a Stimulus controller.
- The `mockup/` folder stays in the repository as the design reference until the app reaches parity, then it is removed.
