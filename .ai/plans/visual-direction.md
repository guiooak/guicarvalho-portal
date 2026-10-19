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
- **Accent: sage green**, a calm, slightly gray, natural green. Scale (sRGB approximations of `oklch(L 0.07 145)`, chroma tapered at the ends):

  | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 |
  |---|---|---|---|---|---|---|---|---|
  | `#eef9ee` | `#ddeddd` | `#c4dcc4` | `#a5c5a5` | `#85aa85` | `#6c926c` | `#527752` | `#3e5f3f` | `#2d472e` |

  - Light theme: accent `600` (`#527752`) for links and buttons (contrast 5.1:1 on white), `50` for soft highlights and tags, `800` for text on soft green.
  - Dark theme: accent `300` (`#a5c5a5`) on `#0f1311` (contrast 9.9:1), with `#1f2d1f` for soft highlights.
- **Dark mode**: automatic via `prefers-color-scheme`, with a manual toggle that writes `data-theme` on `<html>`. Every color is a semantic token with light and dark values.

### Shape and type

- Rounded language throughout: pill buttons, round icon buttons, rounded tags, generously rounded cards and images.
- **Typeface: [Nunito Sans](https://fonts.google.com/specimen/Nunito+Sans)**, a single family for everything (navigation, headings, article body, buttons, UI), self-hosted.
  - Chosen for comfortable long-form reading while keeping the friendly tone of Nunito.
  - It covers every scenario without a second family: real weights from 200 to 1000, true italics, full Portuguese accents and an OFL license.
  - Fonts proposed for the portal must meet these same requirements; display-only families (single weight or no italics) are ruled out.

### Logo

- **Symbol: an acorn with a small leaf on its stem.** "Carvalho" means oak in Portuguese, so the oak's fruit is a playful nod to the surname without being a mascot.
  - Two-tone: dark sage cap and stem (`800` in light, `100` in dark), sage nut and leaf (`600` in light, `300` in dark).
  - Source: [`mockup/assets/images/brand/symbol.svg`](../../mockup/assets/images/brand/symbol.svg).
- **Favicon**: a version of the same symbol drawn for 16–32 px, with a thicker stem, a chunkier leaf and a more compact body, so the leaf stays visible at small sizes. It is used only at small sizes.
  - Source: [`mockup/assets/images/brand/favicon.svg`](../../mockup/assets/images/brand/favicon.svg).
  - Both SVGs switch to their dark colors with `prefers-color-scheme`.
- **Lockup: horizontal, mixed weight.** Symbol to the left of the name, all lowercase, written as one word: **gui** in Nunito Sans 800 and carvalho in Nunito Sans 400, tight letter-spacing (`-0.02em`), symbol about 1.45× the text size.
  - The lockup is built in HTML/CSS (symbol SVG + live text) rather than a text-in-SVG file, so it always uses the self-hosted font and can be translated or scaled freely.

### Home page

- Opens with a personal, first-person introduction (e.g. "Oi, eu sou o Gui 👋") and a short line about what I do and write, framed by floating illustrated objects.
- **No intro video.**

## Open items for the style guide

- [x] Typeface: Nunito Sans.
- [x] Green: sage.
- [ ] Neutral scale for light and dark.
- [ ] Illustration style for the floating objects (3D, flat or hand-drawn) and their source (placeholders or AI-generated for the mockup, commissioned later if needed).
- [x] Logo and favicon: acorn with a leaf, mixed-weight lowercase lockup.
- [ ] Cover image style for blog posts.
