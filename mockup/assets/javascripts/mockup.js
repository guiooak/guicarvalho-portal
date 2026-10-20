/*
 * Mockup-only JavaScript. Everything here becomes Rails partials or
 * Stimulus controllers in phase 2; this file itself is not ported.
 *
 * 1. Theme: applies the saved theme before first paint and wires the toggle.
 * 2. Sprite: injects the shared SVG symbols (logo, icons, illustrations).
 * 3. Shared chrome: <site-header> and <site-footer> custom elements.
 * 4. Annotations: shows or hides .mockup-note callouts.
 */
(() => {
  const storage = {
    get(key) { try { return localStorage.getItem(key); } catch { return null; } },
    set(key, value) { try { localStorage.setItem(key, value); } catch { /* storage unavailable */ } }
  };

  // 1. Theme --------------------------------------------------------------
  const savedTheme = storage.get("theme");
  if (savedTheme === "light" || savedTheme === "dark") {
    document.documentElement.dataset.theme = savedTheme;
  }

  const currentTheme = () =>
    document.documentElement.dataset.theme ||
    (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

  const toggleTheme = () => {
    const next = currentTheme() === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    storage.set("theme", next);
    syncThemeButtons();
  };

  const syncThemeButtons = () => {
    const dark = currentTheme() === "dark";
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      const en = (document.documentElement.lang || "").startsWith("en");
      button.setAttribute("aria-label", dark ? (en ? "Use light theme" : "Usar tema claro") : (en ? "Use dark theme" : "Usar tema escuro"));
      button.querySelector("use")?.setAttribute("href", dark ? "#icon-sun" : "#icon-moon");
    });
  };

  document.addEventListener("click", (event) => {
    if (event.target.closest("[data-theme-toggle]")) toggleTheme();
    if (event.target.closest("[data-notes-toggle]")) toggleNotes();
  });

  // 2. Sprite -------------------------------------------------------------
  const SPRITE = `
<svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="position:absolute;width:0;height:0;overflow:hidden">
  <symbol id="logo-acorn" viewBox="0 0 64 64">
    <path d="M32 13V6c0-1.5 1-2.5 2.5-2.5" stroke="var(--logo-cap)" stroke-width="4" stroke-linecap="round" fill="none"/>
    <path d="M35 8c6-6 14-6 18-3-3 6-10 9-18 3Z" fill="var(--logo-nut)"/>
    <path d="M9 27c0-9 11-14 23-14s23 5 23 14c0 2.2-1.8 4-4 4H13c-2.2 0-4-1.8-4-4Z" fill="var(--logo-cap)"/>
    <path d="M13 33h38c0 14-8 25-19 25S13 47 13 33Z" fill="var(--logo-nut)"/>
  </symbol>
  <symbol id="icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></symbol>
  <symbol id="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z"/></symbol>
  <symbol id="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
  <symbol id="icon-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>
  <symbol id="icon-arrow-right" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="icon-link" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/></symbol>
  <symbol id="icon-google" viewBox="0 0 24 24"><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.4h6.5a5.6 5.6 0 0 1-2.4 3.6v3h3.9c2.2-2.1 3.5-5.1 3.5-8.7Z"/><path fill="#34A853" d="M12 24c3.2 0 6-1.1 7.9-2.9l-3.9-3a7.2 7.2 0 0 1-10.8-3.8h-4v3.1A12 12 0 0 0 12 24Z"/><path fill="#FBBC05" d="M5.2 14.3a7.2 7.2 0 0 1 0-4.6V6.6h-4a12 12 0 0 0 0 10.8l4-3.1Z"/><path fill="#EA4335" d="M12 4.8c1.8 0 3.4.6 4.6 1.8l3.4-3.4A12 12 0 0 0 1.2 6.6l4 3.1A7.2 7.2 0 0 1 12 4.8Z"/></symbol>
  <symbol id="obj-envelope" viewBox="0 0 64 64">
    <rect x="7" y="15" width="50" height="36" rx="6" fill="var(--f)"/>
    <path d="M10 19 32 35 54 19" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <circle cx="32" cy="36" r="4.5" fill="var(--f2)"/>
  </symbol>
  <symbol id="obj-bat" viewBox="0 0 64 64">
    <path d="M32 24c-3 0-5 2-6 5-5-6-13-8-21-5 3 3 4 7 3 11 4-2 8-1 11 2 2-2 5-2 8 0 1 4 3 7 5 9 2-2 4-5 5-9 3-2 6-2 8 0 3-3 7-4 11-2-1-4 0-8 3-11-8-3-16-1-21 5-1-3-3-5-6-5Z" fill="var(--f)"/>
    <path d="M27 26l-2-7 5 4M37 26l2-7-5 4" fill="var(--f)"/>
    <circle cx="29.5" cy="31" r="2" fill="var(--f2)"/><circle cx="34.5" cy="31" r="2" fill="var(--f2)"/>
  </symbol>
  <symbol id="obj-doc" viewBox="0 0 64 64">
    <path d="M19 7h19l12 12v33a5 5 0 0 1-5 5H19a5 5 0 0 1-5-5V12a5 5 0 0 1 5-5Z" fill="var(--f)"/>
    <path d="M38 7l12 12h-8a4 4 0 0 1-4-4Z" fill="var(--f2)"/>
    <path d="M22 31h20M22 38h20M22 45h12" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-window" viewBox="0 0 64 64">
    <rect x="17" y="7" width="40" height="30" rx="5" fill="var(--f2)"/>
    <rect x="7" y="20" width="42" height="36" rx="5" fill="var(--f)"/>
    <circle cx="14" cy="27" r="2.2" fill="var(--f2)"/><circle cx="21" cy="27" r="2.2" fill="var(--f2)"/>
    <path d="M14 38h28M14 46h18" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-mountain" viewBox="0 0 64 64">
    <circle cx="49" cy="15" r="6" fill="var(--f2)"/>
    <path d="M4 52 23 20l10 15 8-11 19 28Z" fill="var(--f)"/>
    <path d="M23 20l-5 8.5 5-2 5 3Z" fill="var(--f2)"/>
    <path d="M10 56h44" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-bike" viewBox="0 0 64 64">
    <circle cx="16" cy="42" r="10" stroke="var(--f)" stroke-width="5" fill="none"/>
    <circle cx="48" cy="42" r="10" stroke="var(--f)" stroke-width="5" fill="none"/>
    <path d="M16 42 27 25h15l6 17M27 25l9 17h12M24 20h8M42 25l-2-6h5" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
    <circle cx="36" cy="42" r="3" fill="var(--f2)"/>
  </symbol>
  <symbol id="obj-map" viewBox="0 0 64 64">
    <path d="M6 14 22 8l20 6 16-6v42l-16 6-20-6-16 6Z" fill="var(--f)"/>
    <path d="M22 8v42M42 14v42" stroke="var(--f2)" stroke-width="3" fill="none"/>
    <path d="M12 42c6-5 10 2 16-4s9-12 17-8" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" stroke-dasharray="2 5" fill="none"/>
    <circle cx="47" cy="29" r="4.5" fill="var(--f2)"/>
  </symbol>
  <symbol id="obj-magnifier" viewBox="0 0 64 64">
    <path d="M38 38l15 15" stroke="var(--f)" stroke-width="9" stroke-linecap="round" fill="none"/>
    <circle cx="26" cy="26" r="16" fill="var(--f2)" stroke="var(--f)" stroke-width="6"/>
    <path d="M18 22a9 9 0 0 1 8-6" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-heart" viewBox="0 0 64 64">
    <path d="M32 55C14 43 6 33 6 22.5A12.5 12.5 0 0 1 32 16a12.5 12.5 0 0 1 26 6.5C58 33 50 43 32 55Z" fill="var(--f)"/>
    <path d="M15 21a6 6 0 0 1 6-5" stroke="var(--f2)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-wave" viewBox="0 0 64 64">
    <circle cx="48" cy="15" r="7" fill="var(--f2)"/>
    <path d="M4 42c6-10 14-16 24-16 9 0 14 6 12 12-1 4-6 5-8 2 6-1 4-8-3-8-8 0-12 6-15 12 8 2 14 2 22-2 7-3 13-3 22 1v15H4Z" fill="var(--f)"/>
    <path d="M10 50c6 2 12 2 18 0s12-2 18 0" stroke="var(--f2)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-wrench" viewBox="0 0 64 64">
    <g transform="rotate(-40 32 32)">
      <rect x="27.5" y="24" width="9" height="36" rx="4.5" fill="var(--f)"/>
      <path d="M32 3a13 13 0 0 0-13 13 13 13 0 0 0 8.5 12.2V18h9v10.2A13 13 0 0 0 45 16 13 13 0 0 0 32 3Z" fill="var(--f)"/>
      <circle cx="32" cy="53" r="2.6" fill="var(--f2)"/>
    </g>
    <path d="M47 40l4-7 2 5 5-1-6 9 0-5Z" fill="var(--f2)"/>
  </symbol>
  <symbol id="obj-chat" viewBox="0 0 64 64">
    <path d="M13 11h38a7 7 0 0 1 7 7v20a7 7 0 0 1-7 7H31l-11 9v-9h-7a7 7 0 0 1-7-7V18a7 7 0 0 1 7-7Z" fill="var(--f)"/>
    <circle cx="22" cy="28" r="3.2" fill="var(--f2)"/><circle cx="32" cy="28" r="3.2" fill="var(--f2)"/><circle cx="42" cy="28" r="3.2" fill="var(--f2)"/>
  </symbol>
  <symbol id="obj-laptop" viewBox="0 0 64 64">
    <rect x="12" y="13" width="40" height="29" rx="4" fill="var(--f)"/>
    <rect x="17" y="18" width="30" height="19" rx="2" fill="var(--f2)"/>
    <path d="M6 46h52l-3.5 6.5a3 3 0 0 1-2.6 1.5H12.1a3 3 0 0 1-2.6-1.5Z" fill="var(--f)"/>
    <path d="M22 26h12M22 31h18" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-mug" viewBox="0 0 64 64">
    <path d="M43 28h4a7 7 0 0 1 0 14h-4" stroke="var(--f)" stroke-width="5" fill="none" stroke-linecap="round"/>
    <rect x="13" y="22" width="31" height="32" rx="7" fill="var(--f)"/>
    <rect x="13" y="30" width="31" height="7" fill="var(--f2)"/>
    <path d="M22 6c-3 4 3 6 0 10M31 6c-3 4 3 6 0 10" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-plane" viewBox="0 0 64 64">
    <path d="M6 30 58 8 45 55 30 39Z" fill="var(--f)"/>
    <path d="M30 39 26 54l8-10" fill="var(--f2)"/>
    <path d="M30 39 58 8" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-pencil" viewBox="0 0 64 64">
    <g transform="rotate(40 32 32)">
    <rect x="26" y="4" width="12" height="7" rx="3" fill="var(--f2)"/>
    <rect x="26" y="11" width="12" height="35" fill="var(--f)"/>
    <path d="M26 46h12l-6 13Z" fill="var(--f2)"/>
    <path d="M32 15v26" stroke="var(--dt)" stroke-width="2.5" stroke-linecap="round" fill="none"/>
    </g>
  </symbol>
  <symbol id="obj-note" viewBox="0 0 64 64">
    <path d="M24 16 54 9v11l-30 7Z" fill="var(--f)"/>
    <rect x="22" y="16" width="5" height="32" fill="var(--f)"/>
    <rect x="50" y="10" width="5" height="32" fill="var(--f)"/>
    <ellipse cx="17" cy="49" rx="9" ry="7" fill="var(--f)"/>
    <ellipse cx="45" cy="43" rx="9" ry="7" fill="var(--f)"/>
    <path d="M13 47.5a4 3 0 0 1 4-2.5" stroke="var(--f2)" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-clock" viewBox="0 0 64 64">
    <circle cx="17" cy="14" r="7" fill="var(--f)"/>
    <circle cx="47" cy="14" r="7" fill="var(--f)"/>
    <circle cx="32" cy="35" r="22" fill="var(--f)"/>
    <circle cx="32" cy="35" r="16" fill="var(--f2)"/>
    <path d="M32 35V25M32 35l7 5" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="obj-clover" viewBox="0 0 64 64">
    <path d="M32 36c1 10 5 17 11 21" stroke="var(--dt)" stroke-width="4" stroke-linecap="round" fill="none"/>
    <path d="M32 34c-9-4-12-16-4-19 3-1 4 1 4 3 0-2 1-4 4-3 8 3 5 15-4 19Z" fill="var(--f)"/>
    <path d="M32 34c-6 8-18 9-19 1 0-3 2-4 4-4-2-1-3-3-1-5 5-6 14 1 16 8Z" fill="var(--f)"/>
    <path d="M32 34c6 8 18 9 19 1 0-3-2-4-4-4 2-1 3-3 1-5-5-6-14 1-16 8Z" fill="var(--f)"/>
  </symbol>
  <symbol id="obj-bulb" viewBox="0 0 64 64">
    <path d="M32 7a17 17 0 0 0-10 31c2 2 3 4 3 7h14c0-3 1-5 3-7A17 17 0 0 0 32 7Z" fill="var(--f2)"/>
    <rect x="24" y="45" width="16" height="11" rx="3" fill="var(--f)"/>
    <path d="M26 26l3 6 3-6 3 6 3-6" stroke="var(--dt)" stroke-width="2.5" stroke-linecap="round" fill="none"/>
    <path d="M6 22h-3M61 22h-3M11 6l2 2M53 6l-2 2" stroke="var(--dt)" stroke-width="3" stroke-linecap="round" fill="none"/>
  </symbol>
</svg>`;

  const injectSprite = () => {
    if (!document.getElementById("logo-acorn")) {
      document.body.insertAdjacentHTML("afterbegin", SPRITE);
    }
  };

  // 3. Shared chrome ------------------------------------------------------
  // Attributes: `root` is the relative path from the page to the mockup
  // folder, `current` marks the active section, `alternate` is the same page
  // in the other language. The locale comes from <html lang>.
  const STRINGS = {
    pt: {
      dir: "br/",
      nav: [["blog", "Blog", "br/blog.html"], ["apps", "Apps", "br/apps.html"], ["about", "Sobre", "br/sobre.html"]],
      skip: "Pular para o conteúdo",
      home: "gui carvalho, página inicial",
      main: "Principal",
      search: "Buscar",
      searchHref: "br/busca.html",
      menu: "Abrir menu",
      subscribe: "Assinar a newsletter",
      other: { code: "EN", name: "English", lang: "en", home: "en/index.html" },
      tagline: "Histórias, metas, idiomas e os apps que eu construo.",
      portal: "Portal",
      social: "Redes",
      madeWith: "Feito com Rails, CSS puro e um pouco de café ☕"
    },
    en: {
      dir: "en/",
      nav: [["blog", "Blog", "en/blog.html"], ["apps", "Apps", "en/apps.html"], ["about", "About", "en/about.html"]],
      skip: "Skip to content",
      home: "gui carvalho, home page",
      main: "Main",
      search: "Search",
      searchHref: "en/search.html",
      menu: "Open menu",
      subscribe: "Subscribe to the newsletter",
      other: { code: "PT", name: "Português", lang: "pt-BR", home: "br/index.html" },
      tagline: "Stories, goals, languages and the apps I build.",
      portal: "Portal",
      social: "Social",
      madeWith: "Made with Rails, plain CSS and a bit of coffee ☕"
    }
  };

  const locale = () => (document.documentElement.lang || "pt").toLowerCase().startsWith("en") ? "en" : "pt";
  const t = () => STRINGS[locale()];

  const navLinks = (root, current) =>
    t().nav.map(([key, label, href]) => `
      <li><a class="site-nav__link" href="${root}${href}"${key === current ? ' aria-current="page"' : ""}>${label}</a></li>`).join("");

  class SiteHeader extends HTMLElement {
    connectedCallback() {
      injectSprite();
      const s = t();
      const root = this.getAttribute("root") || "";
      const current = this.getAttribute("current") || "";
      const alternate = this.getAttribute("alternate") || `${root}${s.other.home}`;
      this.innerHTML = `
        <a class="skip-link" href="#main">${s.skip}</a>
        <header class="site-header">
          <div class="container site-header__inner">
            <a class="brand site-header__brand" href="${root}${s.dir}index.html" aria-label="${s.home}">
              <svg class="brand__symbol" aria-hidden="true"><use href="#logo-acorn"/></svg>
              <span><span class="brand__first">gui</span><span class="brand__last">carvalho</span></span>
            </a>
            <nav class="site-nav" aria-label="${s.main}">
              <ul class="site-nav__list" role="list">${navLinks(root, current)}</ul>
            </nav>
            <div class="site-header__actions">
              <a class="lang-switch" href="${alternate}" hreflang="${s.other.lang}" lang="${s.other.lang}" title="${s.other.name}">${s.other.code}</a>
              <a class="icon-button" href="${root}${s.searchHref}" aria-label="${s.search}"><svg aria-hidden="true"><use href="#icon-search"/></svg></a>
              <button class="icon-button" type="button" data-theme-toggle><svg aria-hidden="true"><use href="#icon-moon"/></svg></button>
              <a class="button button--small site-header__newsletter" href="#newsletter">Newsletter</a>
              <button class="icon-button site-header__menu-button" type="button" popovertarget="site-menu" aria-label="${s.menu}"><svg aria-hidden="true"><use href="#icon-menu"/></svg></button>
            </div>
          </div>
          <div class="site-menu" id="site-menu" popover>
            <nav aria-label="${s.main}">
              <ul class="site-nav__list" role="list">${navLinks(root, current)}
                <li><a class="site-nav__link" href="${alternate}" hreflang="${s.other.lang}" lang="${s.other.lang}">${s.other.name}</a></li>
              </ul>
            </nav>
            <a class="button" href="#newsletter" style="width:100%;margin-top:var(--space-xs)">${s.subscribe}</a>
          </div>
        </header>`;
      syncThemeButtons();
    }
  }

  class SiteFooter extends HTMLElement {
    connectedCallback() {
      injectSprite();
      const s = t();
      const root = this.getAttribute("root") || "";
      this.innerHTML = `
        <footer class="site-footer">
          <div class="container">
            <div class="site-footer__grid">
              <div class="stack" style="--stack-gap: var(--space-xs)">
                <a class="brand" href="${root}${s.dir}index.html" style="--brand-size: 1.125rem">
                  <svg class="brand__symbol" aria-hidden="true"><use href="#logo-acorn"/></svg>
                  <span><span class="brand__first">gui</span><span class="brand__last">carvalho</span></span>
                </a>
                <p>${s.tagline}</p>
              </div>
              <div>
                <h2 class="site-footer__title">${s.portal}</h2>
                <ul class="site-footer__links" role="list">
                  ${s.nav.map(([, label, href]) => `<li><a href="${root}${href}">${label}</a></li>`).join("")}
                  <li><a href="#">RSS</a></li>
                </ul>
              </div>
              <div>
                <h2 class="site-footer__title">${s.social}</h2>
                <ul class="site-footer__links" role="list">
                  <li><a href="https://www.linkedin.com/in/linkguicarvalho">LinkedIn</a></li>
                  <li><a href="https://github.com/guiooak">GitHub</a></li>
                  <li><a href="https://youtube.com/c/GuilhermeCarvalhoOnline">YouTube</a></li>
                  <li><a href="https://www.instagram.com/guicarvalho.com.br">Instagram</a></li>
                </ul>
              </div>
            </div>
            <div class="site-footer__bottom">
              <span>© ${new Date().getFullYear()} Guilherme Carvalho</span>
              <span>${s.madeWith}</span>
            </div>
          </div>
        </footer>`;
    }
  }

  customElements.define("site-header", SiteHeader);
  customElements.define("site-footer", SiteFooter);

  // 4. Annotations --------------------------------------------------------
  const toggleNotes = () => {
    const on = document.documentElement.toggleAttribute("data-show-notes");
    storage.set("notes", on ? "on" : "off");
  };
  if (storage.get("notes") === "on") {
    document.documentElement.setAttribute("data-show-notes", "");
  }

  document.addEventListener("DOMContentLoaded", () => {
    injectSprite();
    syncThemeButtons();
  });
})();
