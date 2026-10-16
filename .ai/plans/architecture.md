# Gui Carvalho Portal — Architecture

Living document with the architecture decisions for the portal that will replace the WordPress blog at `guicarvalho.com.br`.

## Goal

A personal portal with three public, server-rendered, indexable sections:

- **Blog** — every article from the current WordPress blog ported here.
- **Apps** — a showcase of the apps I have built.
- **About** — a page about me.

## Conventions

- All code, documentation, commit messages and identifiers are written in **English**.
- User-facing content is translated through I18n (see below).

## Stack

| Layer | Choice |
|---|---|
| Framework | Rails 8 (native SSR) + Hotwire (Turbo + Stimulus) |
| Database | PostgreSQL |
| Jobs / cache | Solid Queue, Solid Cache (backed by Postgres) |
| JS | importmap (no Node) |
| Assets | Propshaft |
| CSS | Plain modern CSS + Open Props (vendored), no Tailwind, no build step |
| Rich content | ActionText (Trix editor) |
| Files | ActiveStorage → Cloudflare R2 (S3-compatible) |
| Authentication | Google OAuth (OmniAuth) |
| Email | SendGrid (ActionMailer transport + Mail Send API) |
| Deploy | Kamal 2 on a VPS (e.g. Hetzner), kamal-proxy with automatic SSL |
| DNS / CDN | Cloudflare |

## Internationalization

Initial languages: **Portuguese (pt-BR)** and **English (en)**. Adding a new language must not require code changes beyond configuration and translations.

### URLs

The locale is always the first URL segment. The segment → locale mapping lives in a single configuration place:

```ruby
# config/initializers/locales.rb
LOCALES = {
  "br" => :"pt-BR", # keeps the current WordPress URLs
  "en" => :en
}.freeze
```

Examples:

- `/br/viva/psicologo-e-so-para-doidos` (identical to the current URL → no SEO loss)
- `/en/live/psychologist-is-only-for-crazy-people`
- `/br/apps`, `/en/apps`, `/br/sobre`, `/en/about`

`/` renders the home page in the default locale (pt-BR), with no automatic redirect based on `Accept-Language` (Google recommends against redirecting). A subtle notice offers the other version when the browser prefers another language.

### Translatable content

Translatable entities follow a **base record + one translation record per locale** pattern:

- `Post` (shared data: category, cover image, status, author) → `PostTranslation` (`locale`, `title`, `slug`, `excerpt`, ActionText `body`, `seo_title`, `seo_description`, `published_at`).
- `Category` → `CategoryTranslation` (`locale`, `name`, `slug`).
- `Tag` → `TagTranslation` (`locale`, `name`, `slug`).
- `App` → `AppTranslation` (`locale`, `name`, `tagline`, ActionText `description`).
- `Page` (About, etc.) → `PageTranslation`.

A post may exist in a single language (the old articles will be pt-BR only at first). Each locale's listings only show content with a published translation in that locale.

Interface strings live in `config/locales/<locale>.yml` (standard Rails I18n).

### Multilingual SEO

- `<link rel="alternate" hreflang="...">` between existing translations, plus `x-default`.
- Correct `<html lang>` on every page.
- Sitemap with every URL in every locale, including alternates.
- RSS per locale: `/br/rss`, `/en/rss` (and `/rss` → pt-BR, compatible with the current feed).

## Authentication and roles

- **Google-only** sign-in (`omniauth-google-oauth2` + `omniauth-rails_csrf_protection`).
- Database-backed sessions (`Session` model, in the style of the Rails 8 authentication generator).
- `User`: `email`, `name`, `avatar_url`, `google_uid`, `role` (`reader` | `admin`).
- Admins are defined by an email allowlist in the credentials. No passwords are stored.

## Comments

- Only users signed in with Google can comment.
- `Comment`: `post_id`, `user_id`, `parent_id` (one level of replies), `body` (plain text, no HTML), `status` (`pending` | `approved` | `rejected`), `locale`.
- Moderation in the admin area. A user's first comment is held as pending; later comments from already-approved users may be published directly (configurable).
- Rails 8 `rate_limit` on the create endpoint.
- Email to the admin for every new comment.
- Authors can delete their own comments.

## Newsletter

Subscribers live in the **portal's Postgres**. SendGrid is only the transport, so switching providers never requires migrating the list.

### Models

- `Subscriber`: `email`, `locale`, `status` (`pending` | `confirmed` | `unsubscribed` | `bounced` | `spam_reported`), `confirmation_token`, `confirmed_at`, `unsubscribed_at`, `source`, `consent_ip`.
- `Broadcast`: `post_id`, `locale`, `subject`, `status` (`draft` | `sending` | `sent`), `sent_at`, `recipients_count`.
- `EmailEvent`: `subscriber_id`, `broadcast_id`, `sg_message_id`, `event`, `occurred_at`, `payload` (jsonb).

### Flow

1. Sign-up form in the footer → confirmation email → confirmation (double opt-in, LGPD compliance).
2. The admin publishes a post and clicks **Send newsletter** (manual send, never automatic).
3. A job creates the `Broadcast`, splits the confirmed subscribers of that locale into batches of up to 1000 and calls the Mail Send API.
4. SendGrid's Event Webhook (`POST /webhooks/sendgrid`, signature verified) records events and updates the subscriber status on bounce, spam report and unsubscribe.

### Requirements

- Domain authentication in SendGrid (SPF/DKIM via CNAME) and a DMARC policy.
- `List-Unsubscribe` and `List-Unsubscribe-Post` headers (one-click unsubscribe) plus a footer link.
- API key restricted to Mail Send, stored in `Rails.application.credentials`.

### Pending

- Import the current WordPress subscribers (fewer than 50). Deferred; the list will be provided manually later.

## Apps (portfolio)

A simple showcase to start with: `App` with translations (`name`, `tagline`, `description`), icon/logo, screenshots (ActiveStorage), links (website, App Store, Play Store, GitHub), `position` for ordering and a publication `status`.

## WordPress migration

Source: the public WordPress REST API (`/wp-json/wp/v2/`). Current volume: 23 posts, 6 pages, 147 media files.

An idempotent rake task (`wordpress:import`) that:

1. Imports categories and tags (pt-BR).
2. Imports posts as `Post` + pt-BR `PostTranslation`, preserving `slug`, category and publication date.
3. Downloads images, attaches them via ActiveStorage and rewrites the references in the body for ActionText.
4. Imports the relevant pages (e.g. "Sobre o Gui").
5. Produces an old × new URL report. Any old URL that does not match the new one exactly gets a 301 redirect (`Redirect` table: `from_path`, `to_path`).

## Infrastructure

- **VPS** (e.g. Hetzner) deployed with **Kamal 2**: web app, Solid Queue worker and **Postgres as an accessory** on the same server.
- **kamal-proxy** with automatic Let's Encrypt certificates.
- **Backups**: daily `pg_dump` uploaded to R2, with retention.
- **Cloudflare** in front: DNS, asset caching and protection.
- Secrets via `.kamal/secrets` + Rails credentials.

## Local environment

- Ruby 3.4 (via asdf) and Rails 8. The machine currently has Ruby 3.2.2 and Rails 7.1 installed globally, so an upgrade is needed.
- PostgreSQL locally (Homebrew) or via Docker.

## Suggested phases

1. **Foundation**: `rails new`, base CSS with Open Props, layout, route i18n, minimal Kamal deploy.
2. **Blog**: translatable models, public pages, SEO (meta tags, hreflang, sitemap, RSS).
3. **Admin**: Google sign-in, CRUD for posts, categories, tags, apps and pages with ActionText.
4. **Migration**: WordPress import, redirects and URL verification.
5. **Apps and About**: showcase and about page.
6. **Comments**: model, moderation and notifications.
7. **Newsletter**: sign-up, double opt-in, SendGrid sending and webhook.
8. **DNS switch**: point `guicarvalho.com.br` to the new portal and monitor Search Console.
