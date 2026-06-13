# Design

Visual system for this repo's communication surfaces (currently `docs/index.html`;
the review-pack templates share the accent family). Voice: a bank's appraisal
dossier re-typeset by a meticulous print shop — trustworthy, precise, composed.

## Theme
Light. Color strategy: **Committed** — deep ink-blue carries the hero and the
concepts band (~35% of the page); everything else is blue-tinted off-white.
No warm/cream neutrals.

## Color (OKLCH)
| Token | Value | Use |
| --- | --- | --- |
| `--bg` | `oklch(98.6% .004 262)` | body background (blue-tinted off-white) |
| `--surface` | `oklch(96.4% .009 262)` | alternate sections, code chips |
| `--ink` | `oklch(23% .032 262)` | body text |
| `--muted` | `oklch(43% .03 262)` | secondary text (≥4.5:1 on bg) |
| `--line` | `oklch(89% .012 262)` | hairlines, table borders |
| `--accent` | `oklch(50% .21 262)` | brand blue (#2b59ff family) |
| `--accent-ink` | `oklch(38% .16 262)` | links, emphasized labels |
| `--deep` / `--deep-2` | `oklch(25% .06 262)` / `oklch(30% .075 262)` | hero, concepts band, footer, pre blocks |
| `--on-deep` / `--on-deep-2` | `oklch(97% .008 262)` / `oklch(81% .035 262)` | text on deep |
| `--ok` / `--warn` / `--bad` | 155 / 70 / 25 hue | S / A / Q tag families |

## Typography
- **Display/headings:** Literata 600–700 (Google Fonts, Vietnamese subset),
  fallback Georgia. `letter-spacing: -0.015em`, `text-wrap: balance`.
- **Body/UI:** Be Vietnam Pro 400–700, fallback system-ui.
- **Mono:** `ui-monospace` stack (no webfont; offline-safe).
- Fluid body `clamp(1rem … 1.0625rem)`; h2 `clamp(1.7rem … 2.4rem)`; hero h1
  `clamp(2.1rem … 3.7rem)`. The page must remain complete with fonts unloaded
  (`display=swap`).

## Components & patterns
- **Section cadence:** serif h2 + one-line standfirst. No uppercase eyebrows, no
  numbered section markers (numbers only where a real sequence exists: pipeline,
  journey).
- **Panels:** full 1px tinted border + tinted bg, radius 12px. Never side-stripe
  borders.
- **Tables:** wrap in `.tscroll` (own horizontal scroll, `min-width` on wide
  tables); the page never scrolls horizontally.
- **Pipeline:** 6-col grid with connector lines on desktop; vertical left-rail
  timeline ≤860px. Optional steps use dashed number circles.
- **Journey steps:** grid `[number-circle | content]`; the circle is the
  `::before` — content is a single div (no placeholder div).
- **Doc facsimile / wireframe demo:** the product's own artifacts as imagery
  (Answer Sheet card, grayscale phone frames with trace footers). No stock
  photos, no sketchy SVG scenes.
- **Tags:** `A#/Q#/S#/V#` pill tags in warn/bad/ok/accent families.
- Radii: 8/12/16px (`--r-s/m/l`). Phone frames 18px (mimetic). No 24px+ cards.

## Motion
Enhance-only reveal (`.rv` → `.in` via IntersectionObserver): content visible
without JS; `html.js` gates the animation; `prefers-reduced-motion` disables.
Ease `cubic-bezier(.16,1,.3,1)`, 600–800ms, hero children staggered 90ms.

## Layout
Container 1060px. Sections `clamp(56px…104px)` vertical. Breakpoints: 920px
(hero/split collapse), 860px (pipeline vertical), 560px (CTA full-width).
Body measure ≤ ~68ch (`.maxw`).

## Copy rules
Vietnamese; no em dashes; machine labels (ASSUMPTION/IDs) stay English.
Button/link labels are verb + object.
