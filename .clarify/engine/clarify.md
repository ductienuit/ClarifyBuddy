# Engine: clarify

Purpose: extract what is unknown and either resolve it live or proceed with
labeled assumptions. Do NOT hard-block.

## Do
0. **Establish the Document Profile first** (drives every later engine and the
   final `finalize` export). The **target document standard is always URD** (User
   Requirements Document) — there is no PRD/BRD choice. Determine, by asking live or
   reading the input:
   - **Audience role:** is the requester a **BA** (Business Analyst) or **PO**
     (Product Owner)? This shapes tone and depth — BA → business/process and
     compliance emphasis; PO → product/value and delivery emphasis.
   Record the Role plus `Standard: URD` as a **Document Profile** block at the top of
   the output so every later engine and `finalize` know the target.
0b. **Detect the domain** (Principle 12) and pick the mode: if a pack under
   `domain-packs/` matches, load it (`domain pack: <name>`); otherwise proceed
   with labeled inference (`domain: <inferred> (no pack — inferences labeled)`).
   Never force-fit a wrong pack or stop because no pack exists. Record the mode in
   the Document Profile.
0c. **Set the output Language**: default to the language the user is writing in
   (record `ASSUMPTION` if inferred rather than stated). Record
   `Language: <vi | en | …>` in the Document Profile. All downstream output
   (headings + content) renders in this language, **except** the machine-readable
   anchors which always stay in English: the labels `ASSUMPTION:` /
   `OPEN QUESTION:` / `SUGGESTION:`, all IDs (`A#/Q#/S#/V#/F#/S#/BR#/CR#`,
   error codes), and file names.
1. Read the input. List every gap: missing actor, trigger, outcome, scope,
   business rule, success metric, data owner, permission. Also probe the
   **product/operational lenses** that user-flow specs routinely miss — do not
   stay only in the "user acts → system responds" frame:
   - non-user / back-office actors — admin/configurator, operations, accounting,
     external systems, scheduled jobs (`missing-system-actor`, completeness).
   - tunable parameters with no config owner — rates, fees, limits, thresholds:
     where configured, by whom, validation, propagation
     (`missing-configuration-ownership`, business-rule-quality).
   - rules/config that change over time with no effective date or version
     (`missing-effective-dating`, business-rule-quality).
   - existing-vs-new treatment when a rule changes — grandfather vs apply-forward,
     migration/backfill (`missing-cohort-treatment`, completeness).
   - scheduled/batch jobs with no schedule, idempotency, outputs, or downstream
     consumers such as reconciliation/accounting (`missing-batch-job-spec`,
     risk-control).
1b. **Walk every stakeholder class** (Principle 10): end user, operations,
   accounting/finance, reconciliation, partners/external, risk/compliance,
   maintenance/engineering, data/analytics, security. For each, note what it needs
   from this feature; a stakeholder with no stated need is a gap
   (`missing-system-actor`). If a domain pack is selected, read its
   `back-office-flows.md` for the non-user stakeholders.
1c. **Propose completeness** (Principle 11): based on the feature + domain, list
   `SUGGESTION:` items for capabilities a complete product needs but the input
   omits (config/admin side, reconciliation, reporting, notifications, audit,
   migration, serving jobs). Ground them in the domain pack's common flows; never
   write them as confirmed requirements.
1d. **Offer a Variant / Options Matrix** instead of only asking. When the feature
   implies multiple product types, channels, customer segments, or configuration
   options, generate a small table of plausible options with their key
   differentiators so the user can pick. Mark it `for selection` (a SUGGESTION
   set), never an assumed choice. (Example axes for a banking deposit: term vs
   non-term vs goal-savings; channel; segment; lifecycle ops included.)
2. Group gaps into **clarifying questions** (cap ~7). **For thin input, lead with
   the 5 highest-impact, scope-blocking questions** before any detail question —
   the unknowns that most change the whole document. Typically: (1) role + scope
   (Document Profile), (2) which channel(s)/platform, (3) which product
   variant/type(s), (4) which customer segment, (5) which lifecycle operations are
   in scope (and the depth/altitude wanted: BRD high-level vs PRD detailed).
   Adapt these axes to the feature/domain. Tag each question with its dimension
   **and an elicitation owner** — `→ ask: <stakeholder>` (PO, accounting/finance,
   operations, risk/legal/compliance, design, dev/architecture, customer service,
   partner…) inferred from the lens that raised it; if no owner can be inferred,
   tag `ask: OPEN QUESTION`. Owners tell the BA **whom to interview**, not just
   what is missing.
3. If the user is interacting live, ask the questions and wait for answers.
4. If not live (batch) OR the user declines, proceed: convert each open gap to
   an `ASSUMPTION:` (a reasonable default) or `OPEN QUESTION:` (only a human can
   decide). Never invent a business rule silently.
5. Output two lists: **Clarifying Questions** and **Assumptions in effect**.
6. When the output contains an Answer Sheet, tell the user the immediate next
   step is to fill it and run `/clarify:improve answers`, then `/clarify:finalize`
   to produce the URD.

## Rules
- Prefer a small number of decision-changing questions over many trivial ones.
- Every assumption must be explicit and revisitable downstream.
- Tag the questions by the dimension they affect (clarity, business-rule, etc.).

## Output
Number every decidable item with a stable ID and end with a copyable **Answer
Sheet** (see `output-conventions.md` → "Labeled items & answer sheet"):
- `## Document Profile` — `Role: BA | PO`, `Standard: URD`,
  `Domain: <pack name | inferred (no pack)>`, and `Language: <vi | en | …>`
  (default `vi`).
- `## Clarifying / Open Questions` — `Q1, Q2, …`, each tagged with dimension AND
  `→ ask: <stakeholder>`; thin input → the 5 highest-impact, scope-blocking
  questions first.
- `## Variant / Options Matrix` — a table with an `ID` column (`V1, V2, …`) for the
  user to select, when the feature implies more than one variant.
- `## Assumptions` — `A1, A2, …` (ASSUMPTION: …; in effect unless overridden).
- `## Suggested Additional Capabilities` — `S1, S2, …` (SUGGESTION: … — for
  confirmation, not yet in scope).
- `## Answer Sheet` — one fenced ```text block listing every `V/A/Q/S` ID with a
  blank to fill (each line carries its `ask:` owner as a hint), so the user can
  copy, answer in-place, and send back.
- An **Open items** block in the draft REGROUPING the questions **by stakeholder
  owner** (one sub-list per owner, each question with one line of context: why it
  matters + the related section), so the BA can take it straight into a
  workshop/interview. This lives **inside the draft**, not a separate
  `elicitation-pack.md` file (Principle 13.11); `templates/elicitation-pack-template.md`
  is the working structure.
- `## Recommended next step` — "Fill the Answer Sheet, then run
  `/clarify:improve answers` to resolve the draft, then `/clarify:finalize` to
  produce the URD (`urd.md` + `urd.html`; add `word` for `urd.docx`)."
