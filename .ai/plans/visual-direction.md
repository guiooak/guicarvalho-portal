# Gui Carvalho Portal — Visual Direction

The visual brief for the mockup (see [mockup.md](mockup.md)), agreed during the design brainstorm. It defines the look and feel; exact values (fonts, shades, scales) are settled in the style guide.

## In one sentence

A clean, calm base with a **subtle, light sense of fun**: the playfulness comes from a few deliberate touches, never from the layout itself.

## References

### Liked

- **[Kent C. Dodds](https://kentcdodds.com)**: the main reference.
  - Clean white base, black text and system-like sans-serif type.
  - Large headings in a medium (not bold) weight, which reads soft and friendly.
  - Pill-shaped buttons (one solid, one outlined), round icon buttons, rounded gray tags and softly rounded images.
  - All the fun lives in the illustrations, with objects floating around the hero; everything else stays sober.
  - Blog index with a tag cloud for filtering, a highlighted "featured article" card and colorful cover images per post.
- **[Ali Abdaal](https://aliabdaal.com)**: a secondary reference for warmth.
  - Friendly first-person tone ("Hey Friends 👋").
  - Hand-drawn underline on a heading word.
  - Generously rounded cards.
  - Newsletter call to action always visible in the header.

### Not liked

- Too sober or too editorial: [James Clear](https://jamesclear.com), [Maggie Appleton](https://maggieappleton.com).
- Too playful: [Josh W. Comeau](https://www.joshwcomeau.com).
- Too dark or technical: [Brittany Chiang](https://brittanychiang.com).
- Creator and coaching sites felt too boxy and corporate, e.g. [Thomas Frank](https://www.thomasjfrank.com), [Marie Forleo](https://www.marieforleo.com).

## Decisions

### Identity

- **Start fresh.** Nothing is carried over from the current blog's visual identity: no stick-figure logo, no motto ("E se tiver com medo, vai com medo mesmo!"), no full-width photo hero.
  - Content, categories and URLs still migrate as described in [architecture.md](architecture.md).
- **No mascot or character.** The site does not revolve around an illustrated figure.

### Where the fun comes from

1. **Illustrated objects and shapes**: loose elements floating around hero areas, themed per section (e.g. objects related to writing on the blog, to building things on the apps page).
2. **Color**: a green accent, used with intent on links, buttons, highlights and illustrations.
3. **Small hand-drawn touches**: a drawn underline or scribble on a key heading word, and an occasional emoji such as 👋.
4. **Micro-interactions in pure CSS**: cards that lift or tilt slightly on hover, buttons with a small bounce, smooth focus states. All of them respect `prefers-reduced-motion`.

### Color and theme

- **Background**: pure white in the light theme.
- **Accent**: green. The exact shade is chosen in the style guide and must pass WCAG AA contrast for text and buttons in both themes.
- **Dark mode**: automatic via `prefers-color-scheme`, with a manual toggle that writes `data-theme` on `<html>`. Every color is a semantic token with light and dark values.

### Shape and type

- Rounded language throughout: pill buttons, round icon buttons, rounded tags, generously rounded cards and images.
- Clean sans-serif, with large headings in a medium weight. Specific typefaces are chosen in the style guide and self-hosted.

### Home page

- Opens with a personal, first-person introduction (e.g. "Oi, eu sou o Gui 👋") and a short line about what I do and write, framed by floating illustrated objects.
- **No intro video.**

## Open items for the style guide

- [ ] Typefaces for headings and body.
- [ ] Exact green shade(s) and the neutral scale, for light and dark.
- [ ] Illustration style for the floating objects (3D, flat or hand-drawn) and their source (placeholders or AI-generated for the mockup, commissioned later if needed).
- [ ] Wordmark/logo and favicon.
- [ ] Cover image style for blog posts.
