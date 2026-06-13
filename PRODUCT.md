# Product

## Register
brand — the design surfaces of this repo are communication surfaces: the user
guide landing page (`docs/index.html`) and the generated HTML BRD + wireframe
HTML templates. Design IS the deliverable for these pages. (The skill pack itself
is markdown/prompt engineering, out of scope for visual design work.)

## Users & Purpose
- **Who:** Vietnamese Business Analysts and Product Owners (banking/fintech
  heavy), mid-to-senior, reading at a desk in normal office light, usually with
  10–15 minutes before a meeting.
- **Job:** understand what the Clarify skill does, how to install it, and how to
  run the from-idea → answers → finalize → export journey, with one worked
  example (savings deposit).
- **Emotion to evoke:** confidence and calm competence. "This tool was made by
  someone who does my job seriously." Never hype.

## Brand personality
Tin cậy · chính xác · điềm tĩnh (trustworthy · precise · composed).
Physical-object voice: a bank's appraisal dossier re-typeset by a meticulous
print shop. Authority from typography and structure, not decoration.

## Anti-references (explicitly NOT)
- Template SaaS landing pages: purple gradients, glitter badges, hype copy.
- Dry developer docs: walls of text with no rhythm, no visual guidance.
- Corporate PowerPoint: clipart icons above every heading, dense bullets.

## Visual identity anchors
- Committed color strategy around the existing brand blue (#2b59ff family,
  already shipped in the HTML BRD templates); deep ink-blue may carry large
  surfaces (hero). Body background stays true off-white tinted toward the brand
  hue, never warm cream.
- Typography pairs on a serif/sans contrast axis with full Vietnamese diacritic
  support; the page must remain readable offline via system fallbacks.
- Product imagery is the product itself: document facsimiles (Answer Sheet,
  BRD snippets), pipeline diagrams, and the skill's own low-fi phone wireframe
  language. No stock photography needed.

## Accessibility
WCAG AA: body contrast ≥ 4.5:1, focus-visible on all interactive elements,
`prefers-reduced-motion` honored (content never gated on animation), semantic
landmarks/headings, single-file page must work with no network and no JS.

## Strategic design principles
1. Content was approved; redesigns keep the information architecture.
2. Self-contained single file: no build step, no external JS; web fonts may load
   with `font-display: swap` but the page must be complete without them.
3. The savings-deposit worked example is the narrative spine of the guide.
4. Tables are data-dense by nature here; on small screens they scroll within
   their own container, never the page.
