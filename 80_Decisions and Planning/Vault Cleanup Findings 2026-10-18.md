# Vault Cleanup Findings 2026-10-18

Phase 1 of the vault cleanup: a read-only review of every folder and subfolder, recorded in the `## Folder review (2026-10-18)` section of each `README_<folder>` note. This note holds the cross-cutting findings (F-01 to F-17), the conflicts between documented and observed state, the decisions needed, and the proposed standard structure and Base views. Phase 2 starts from the decisions listed here.

## Challenges to the brief

1. **A MOC for every folder conflicts with the vault contract.** `MDSE Vault File and Folder Structure 0.8` section 6 limits README/Base/Canvas sets to primary domain folders unless a navigation need is shown. Resolved by your choice on 2026-10-18: extend the 22 existing READMEs and add `README_<folder>` (no Base, no Canvas) only to 30 subfolders that hold 10 or more notes or are category-level folders. Smaller folders are covered in their parent's Subfolders table.
2. **A standard note structure cannot be imposed by editing notes alone.** `AGENTS.md` and `AI_INSTRUCTIONS.md` fix template headings and properties; new properties or sections need a controlled schema or template release. Section "Proposed standard structure" separates what fits the current contract from what needs a release.
3. **Bases cannot read most of the evidence.** Bases `note.*` properties come only from Markdown frontmatter; `file.*` properties work for any file type (see Sources). Facts held in body prose, in tables inside notes, or in YAML decision records are therefore not queryable.
4. **The runtime handoff says not to start another broad reorganization.** This phase moves, renames and deletes nothing. Placement questions are listed as decisions only.

## What is healthy (do not break)

- All 2,101 typed notes have valid `id` and `uid` formats, matching id prefixes, correct common-property order and no properties outside the schema. No `id` is reused.
- Only 3 of 2,101 typed notes have no inbound link.
- All 509 concrete product notes in `10_Products` link a maker (`madeBy` or `offeredBy`); the 59 without one are all `abstract: true`.
- All 488 Source Documents carry `sourceClass` and `sourceUrl`; 471 carry `accessed`.
- Every Source Document has `describes` and at least one inbound link.
- 13,147 relationship-field values (forward and inverse) are in use; the repo's relationship checks passed on 2026-10-12 per the runtime handoff (not re-run here).

## Method and limits

- Read-only audit of 2,297 Markdown files (2,101 typed) plus file counts for other types, using ad hoc scripts run in this session. The scripts are not committed; `99_System` is controlled runtime. They can be added to `99_System/09_Tools` on request.
- Not done: semantic fact-checking of claims against sources, a live check of the 944 cited URLs (the workspace network is allow-listed), and a GitHub Actions status check (done after the push, see the handoff message).
- `99_System` was reviewed for conflicts only and not edited.
- Obsidian behavior claims were checked against the sources listed at the end.

## Findings

Fix class: **A** = fits the current contract, can be done now. **B** = needs a script, schema or template change through the controlled release. **C** = needs your decision first.

| ID | Finding | Evidence | Class | Where |
| --- | --- | --- | --- | --- |
| F-01 | Status carries no review signal | 2,100 notes Draft, 1 Superseded | C | all |
| F-02 | Evidence tier, source and retrieval date live in prose | `(T#)` text in 1,196 notes; tier tag on 386 of 488 Documents in two spellings; 203 concrete products link no Document note | C | 10, 20, 40, 50, 70 |
| F-03 | Aliases in body list; checker blind to YAML aliases | 604 notes use body `## Aliases`, 9 use YAML | B | 10, 60, 70, 30 |
| F-04 | Body structure drift | 220 notes with dated update blocks; 29 repeated labels; 8 empty blocks; two documented layouts conflict | C | all |
| F-05 | Classification properties unused; off-schema subtypes | `productClass` on 10 of 570 Objects; 59 off-schema subtypes | A and C | 10, 20 |
| F-06 | Metrics not comparable | 55 Metric notes hold values as prose; 0 of 318 Info notes set measure properties | A and C | 30 |
| F-07 | Conflicts are not queryable | One 213 KB prose register; `contradicts` on 4 notes | C | 70, 30 |
| F-08 | Databases stored as oversized notes | 7 notes over 100 KB | C | 70, 60, 80 |
| F-09 | Untyped content and hidden YAML records | 90 untyped notes outside 99; 107 YAML decision records hidden; 1 unparseable | C | 70, 80, 90 |
| F-10 | `Organization` class unused | 147 organizations are `Info`; 0 `Organization` notes | C | 60 |
| F-11 | Placement differs from the taxonomy | See conflicts table rows 6 to 8 | C | 20, 30, 70, 80 |
| F-12 | Tag vocabulary sprawl | 601 distinct tags, 238 used once | C | all |
| F-13 | Existing Bases use few properties | Columns limited to name, `subtypeOf`, `madeBy`, `offeredBy`, status | A | all |
| F-14 | Documentation and repo hygiene drift | Stale counts and versions; 33 tracked `.pyc` files | B | root, 99 |
| F-15 | Root folders outside the taxonomy | `Reference Files` 109 PDFs; `Downloads` 14 PDFs; public repo | C | root |
| F-16 | Thin or placeholder folders | Eight folders with 1 to 2 notes | C | 10 |
| F-17 | Property definitions out of step with usage | 36 used fields undefined; 22 defined fields unused | A | 90 |

### F-01 Status carries no review signal

All typed notes are `Draft` except one `Superseded` note ([[Battery Sensor Element Design]]). `AGENTS.md` forbids an AI from advancing status, so nothing has been reviewed in the data. A Base cannot build a review queue or show coverage of reviewed content. Decision: who reviews, in what order, and whether review state is `status` alone or needs a sparse property (class B).

### F-02 Evidence tier, source and retrieval date live in prose

- Product, need and use-case notes cite sources as bullets inside `## Notes` with `(T1)` to `(T4)` and `retrieved <date>` in text: 1,196 notes carry tier marks (499 in `10_Products`).
- Source Documents hold provenance in YAML (`sourceClass`, `sourceUrl`, `accessed`) and tier in a body line (all 488) and a tag (386). The tag uses two spellings: `tier-T1` style on 356 Documents and `tier-1` style on 30. No tag disagrees numerically with its body line (383 compared). 102 Documents have the body line only; 14 Info notes also carry a tier tag.
- 203 of 509 concrete products have no `describedBy` and link no Document note; 202 of them cite a URL inline. The curated chain `acquired artifact → Source Document → claim` is therefore skipped for these.
- Architecture notes (20) are analyst-derived: 6 of 196 have `describedBy`. For example [[Battery Current Measurement Circuit]] is `partOf` ten products with no source on the circuit-level claim and no marker that it is inferred.

Options: (a) keep per-claim prose and add one note-level property for best tier and an `inferred` marker (needs a release); (b) one evidence-table block per note with fixed columns (claim, source link, tier, date), still prose to Bases; (c) one Document-linked claim record per claim (heavy). Recommendation: (a) plus normalizing the tag spelling now.

### F-03 Aliases in a body list; checker blind to YAML aliases

Schema `element-types` 1.18 says YAML `aliases` replaces the body alias list when a note is migrated. 604 typed notes still use the body list and 9 use YAML. `check-names.py` reads only the body `## Aliases` block, so the 9 YAML-alias notes are already invisible to its alias-collision checks; migrating the rest would blind it entirely. Obsidian resolves alias links from the frontmatter `aliases` property, not from a body list (see Sources). Order of work: update `check-names.py` first (class B), then migrate in batches.

### F-04 Body structure drift

- Two documented layouts conflict. `Note Layout` (INFO-00022) says the body starts with the note text and `## Notes` is an empty user section. The templates and 99% of notes (2,081 of 2,101) use `# Title`, `## Definition`, and a populated `## Notes`.
- `## Notes` is the evidence log: dated "Update", "Solution link added" and "Customer-side evidence added" blocks (220 notes), repeated bold labels such as "Design characteristics, with citations" (29 notes), and empty label blocks (8 notes). Example: [[Crown V-Force Lithium-Ion ESS]].
- 356 notes have more than 2,000 characters in `## Notes`.

Decision: pick the standard layout (see proposal), then consolidate in batches. History belongs in git and in a dated log, not in the current-state text.

### F-05 Classification properties unused; off-schema subtypes

- `productClass` (enum: product-category, product-type, product-family, product-variant, specific-offering) is set on 10 of 570 Objects, so Bases cannot group the product hierarchy. All 59 abstract notes are the likely category and family set. `reuseScope` is set on 153 of 196 architecture notes but on 2 of 570 products.
- Subtype values outside `element-types` 1.18: 24 `component` and 19 `assembly` Objects in `20_Product Architecture`; 12 `unknown`, 1 `hardware` and 1 `hardware and software` in `10_Products`; 2 Port notes with blank subtype (schema: proxy, full). The repo audit does not check subtypes.

Class A: classify the 59 abstract notes; set Port subtype; give the 14 product Objects a schema subtype. Class C: whether `component` and `assembly` are added to the schema or the 43 notes are changed.

### F-06 Metrics not comparable

The 55 Metric notes copy per-product values as prose bullets and state that the product note wins on disagreement, so each value is stored twice and cannot be sorted, filtered or compared in a Base. None of the schema's Info measure properties (`measureClass`, `valueType`, `unit`, `measurementMethod`) is set on any of the 318 Info notes. This blocks the stated goal of comparing products on established metrics.

Class A: set the four properties on the 55 Metrics. Class C: where the per-product values live (keep in Metric notes; generate from product notes; one record per product-metric value). A one-record-per-value design makes Bases work fully but adds notes; a generated table keeps one source of truth.

### F-07 Conflicts are not queryable

- `conflictsWith` is reserved for compatibility conflicts and unused by design (schema: "kept though nothing writes it yet"). `contradicts` (source: Document, Info or Result) is the evidence-conflict relationship and is on 4 notes. No relationship lets one Requirement contradict another.
- Conflicts live in prose: [[Battery Product Landscape Conflicts and Open Questions]] (213 KB, 167 notes link to it), [[Demand Evidence Conflict Log]] and [[PosiCharge and Power Designers Evidence Gaps and Conflicts]]. More than 270 notes say "the conflict register", and no note has that name.
- A conflict in a 213 KB note cannot be filtered by product, claim, status or date.

Options: (a) one Info note per conflict, linked with `contradicts` to the disagreeing Documents, with tags for status; (b) keep the logs and add a structured table per log; (c) add a conflict relationship usable by Requirements (release). Recommendation: (a), which also satisfies the project rule that conflicts stay visible.

### F-08 Databases stored as oversized notes

Seven notes exceed 100 KB: [[PosiBattery Architecture Improvement Plan]] (265 KB), [[Battery Product Landscape Conflicts and Open Questions]] (213 KB), [[Product to Customer Need Map]] (141 KB), [[Investigation Backlog]] (119 KB), [[Document Wishlist]] (106 KB), [[Business Relationship Ledger]] (106 KB) and [[SOC and Health Estimation Literature Review]] (103 KB). Ten typed notes exceed 30 KB. They are databases in prose: slow to open, hard to edit, and invisible to Bases. The Document Wishlist and Investigation Backlog are the working registers you maintain; a status column inside a table cannot be filtered.

Decision per register: one note per record with properties, or keep as a register with a generated summary note.

### F-09 Untyped content and hidden YAML records

- 90 non-README Markdown files have no model `type`: 22 research files in `70` (Cost Drivers 12, EMS 4, Power Conversion 4, SysML v2 2, about 500 KB, none with frontmatter), 18 in `80` (15 without frontmatter), 48 in `90` (45 Property Definitions plus 3 methodology notes, which are expected), and two root files. Names such as "Chat 1" and "EMS 1" say nothing about content.
- 107 YAML decision records in `80`. `showUnsupportedFiles` is false, so they are hidden in the file explorer, and Bases give `file.*` properties only for non-Markdown files, not record content. One record does not parse: `Reusable Definition vs Contextual Architecture Review Step 44 0.1.yaml`.
- Two READMEs link YAML or `.base` files with wikilinks that the repo audit's resolver may treat differently from Obsidian: [[README_Definitions]] (`Properties/Property Dictionary`) and [[README_Properties]] (`Property Definition Quality Inventory Step 71 0.1`). Not changed.

### F-10 `Organization` class unused

The schema defines `Organization` (prefix ORG) and `relationships.yaml` marks the Info endpoints `legacyInfoOrganizationEndpoint`, with the retired provisional file noting migration is incremental. 147 organizations remain `Info`. Decision: when and how to migrate (a controlled batch with id allocation and relationship endpoint checks).

### F-11 Placement differs from the taxonomy

The taxonomy table assigns backlog, open questions and conflicts to `80`, verification records to `30`, and concepts, protocols and units to `90`. Observed: those registers are in `70/Research`; 8 Verification notes are in `20`; `90` holds only property definitions and methodology notes; and the folder `California Regulatory Requirements` holds 6 other-jurisdiction rules and 5 derived reporting requirements. Folder placement is navigation, so these are deviations to decide on, not errors. Any move is a controlled batch with inventory and link checks.

### F-12 Tag vocabulary sprawl

601 distinct tags, 238 used once. `70/Research` has 163 tags with 107 used once. Tiers use two spellings (F-02). There is no controlled tag list. Class C: choose which tags carry meaning (evidence status, product line, lifecycle) and publish a short controlled list; singleton tags become properties or are removed.

### F-13 Existing Bases use few properties

`BASE_all_Products` shows name, `subtypeOf`, `madeBy`, `offeredBy`, folder and status; `BASE_offerings` swaps in `offeredWith`. No Base uses `abstract`, `productClass`, `describedBy`, `performs`, `hasDesign`, tags or `reuseScope`. See "Proposed Base views".

### F-14 Documentation and repo hygiene drift

See conflicts table rows 1 to 5. In addition, 33 compiled `.pyc` files under `99_System` are tracked in git, and `.gitignore` (generated by `build-base.py`) does not exclude them.

### F-15 Root folders outside the taxonomy

`Reference Files` (109 PDFs, README present) holds copies of cited files that cannot be re-fetched; `Downloads` still holds 14 government PDFs that the README says were left as deletable. The repository is public (your note of 2026-10-12) and the runtime handoff already flags third-party PDFs and the missing LICENSE as a separate owner decision. Nothing was changed.

### F-16 Thin or placeholder folders

One note: Class IV, V, VI and VII Forklifts, Protection and Disconnect Units, Thermal Management Devices. Two notes: Cable Management, Thermal Accessories. Consistent with the broad-first plan; decide whether to keep as placeholders.

### F-17 Property definitions out of step with usage

45 Property Definition notes exist. 36 fields used by notes have no definition and are not mentioned in any definition, including the sparse properties `productClass`, `reuseScope`, `aliases`, `sourceClass`, `sourceUrl`, `accessed`, `sourceRevision` and the business-relationship fields (`madeBy`, `makes`, `offeredBy`, `offeredWith`, `playsRole`, `integratesWith` and others). A further 14 inverse fields are mentioned only inside other definitions. 22 defined properties are used by no note (`conflictsWith`, `supersedes`, `tracesTo`, `refines`, `includes`, `precedes`, `optionOf` and 15 more). Class A: add the missing definitions from the `Property Definition` template.

## Documented versus observed

Nothing here has been edited; the documented text stays so both sides are visible.

| # | Documented (where) | Observed 2026-10-18 | Status |
| --- | --- | --- | --- |
| 1 | `README.md` and runtime handoff: 1,391 Markdown files, 1,196 model notes (2026-10-12) | 2,297 Markdown files, 2,101 typed notes | stale, counts to refresh |
| 2 | Runtime handoff provenance line (2026-10-05 text): 8 curated Source Documents, all lacking structured provenance | 488 Documents; `sourceClass` and `sourceUrl` 488, `accessed` 471, `sourceRevision` 60 | superseded, not marked |
| 3 | `MDSE Vault File and Folder Structure 0.8` header: release 0.8.0, relationships 1.35, element 1.17 | `.vault.yaml` 0.8.1, `relationships.yaml` 1.36, `element-types.yaml` 1.18 (the doc says a later release governs) | header stale |
| 4 | Same doc, section 3 layout: `00 - Folder Map.canvas` in `02_AI` and `08_Scripts`; `09_Tools` with three files | No Folder Map canvases; `09_Tools` has about 40 scripts and tracked `__pycache__` | layout stale |
| 5 | Same doc, section 6: navigation artifacts only at primary domain level unless a need is shown | Lower-level sets exist in 30 (3 folders), 60 (2) and 70 (2); this review adds README-only notes to 30 more folders | extended with your approval 2026-10-18 |
| 6 | Taxonomy: verification records belong in `30` | 8 Verification notes in `20` | open (F-11) |
| 7 | Taxonomy: backlog, open questions, conflicts, findings belong in `80` | Wishlist, backlog, conflict logs and triage registers in `70/Research` | open (F-11) |
| 8 | Taxonomy: `90` holds concepts, technologies, protocols, units | Property definitions and three methodology notes only | open (F-11) |
| 9 | `Note Layout`: `## Notes` is an empty user section; body starts with note text | 2,081 of 2,101 notes populate `## Notes`; templates use `## Definition` | conflict (F-04) |
| 10 | `element-types` 1.18 subtype lists | 59 off-schema subtypes (F-05) | conflict |
| 11 | Collision naming in three places: `check-names.py` (identifier in parentheses), structure doc section 8 (`~2`, `~a`), `Note Layout` W-289 (`_1`, `_r`) | Three conventions documented | conflict, needs one rule |
| 12 | `relationships.yaml`: `conflictsWith` kept for compatibility conflicts | Unused; evidence conflicts recorded in prose | gap (F-07) |
| 13 | 270-plus notes: "disagreements are logged in the conflict register" | No note of that name; three separate logs | broken reference (F-07) |
| 14 | Reference Files README: URL-backed files left in `Downloads` as deletable | 14 PDFs still in `Downloads` | pending your decision (F-15) |

## Decisions needed

In suggested order. Phase 2 asks one at a time.

1. **Note layout (F-04).** Keep templates (`## Definition`, `## Notes`) and amend `Note Layout`, or switch to `Note Layout`. Blocks F-03, F-04 and the evidence design.
2. **Evidence home (F-02).** Which of options (a), (b), (c); tag spelling.
3. **Conflict mechanism (F-07).** Option (a), (b) or (c).
4. **Metric values (F-06).** Where per-product values live.
5. **Review state (F-01).** Who reviews and how it is recorded.
6. **Organizations (F-10)** and **registers as databases (F-08).**
7. **Subtype vocabulary and placement (F-05, F-11).**
8. **Root folders and public third-party files (F-15).**
9. **Tag policy (F-12).**

Class A work that needs no decision and can start immediately: classify the 59 abstract notes with `productClass`; set Port subtype; set measure properties on the 55 Metrics; give 14 product Objects a schema subtype; normalize the 30 `tier-#` tags; write the 36 missing Property Definitions; build the Bases below.

## Proposed standard structure (for decision)

Fits the current contract (existing sparse properties and the template headings):

| Class and scope | Properties expected | Body | Evidence rule |
| --- | --- | --- | --- |
| Object, concrete product | common set, `productClass`, `reuseScope`, `subtypeOf`, `madeBy` or `offeredBy`, `describedBy` (at least one), `performs`, `hasDesign`, YAML `aliases` | H1, `## Definition` (at least 8 words), `## Notes`, `## Former ids` | every claim bullet carries source link, tier, date |
| Object, abstract | adds `abstract: true`, `productClass` category or family | same | none required |
| Document | `sourceClass`, `sourceUrl`, `accessed`, `sourceRevision` when known, one tier tag spelling | `## Definition`, `## Provenance`, `## Traceability` as in current Documents | n/a |
| Info, Metric | `measureClass`, `valueType`, `unit`, `measurementMethod`, `describes` | `## Definition`, comparison rule | per-product values by decision F-06 |
| Use Case, need | `subtype: why`, `participants`, `realizedBy`, `describedBy` | `## Definition`, evidence status | customer-side source for validated needs |
| Requirement | `subtype`, `appliesTo`, `references` | `## Definition` | regulation or standard cited |

Needs a controlled release: a note-level best-tier property and an inferred marker; any extra body section such as a fixed `## Evidence` block or a `## Conflicts` block.

## Proposed Base views

Use existing properties only; Bases support table, list, cards and kanban views, filters, formulas, summaries and `groupBy` (see Sources). Each view answers a question; none is built yet.

| Base | Filter | Columns | Question |
| --- | --- | --- | --- |
| Product coverage | `10_Products`, not abstract | maker, `productClass`, count of `describedBy`, `performs`, `hasDesign` | which products lack a source, Function or Design |
| Product hierarchy | `10_Products` | grouped by `productClass` then `subtypeOf` | what categories and variants exist |
| Evidence register | Documents | `sourceClass`, tier tag, `accessed`, count of notes described | which sources are old or unused |
| Function coverage | Functions | performer count, `realizes`, `realizedBy` | Functions with no performer, need or Design |
| Need coverage | Use Cases subtype why | `realizedBy` count, `describedBy` count, tags | needs without source or realizing Function |
| Design coverage | Designs | `designOf`, `realizes`, `describedBy` | Designs that realize nothing |
| Requirement coverage | Requirements | `appliesTo`, `references`, satisfier count | Requirements nobody satisfies |
| Organization roles | `60/Organizations` | `playsRole`, `makes` count, `describedBy` | organizations without products or sources |
| Metric comparison | Metrics | after F-06 | compare products on one metric |
| Review queue | any | after F-01 | what a reviewer should open next |

## Phase 2 plan

1. Decide items 1 to 4 above.
2. Do the class A work.
3. Build the Bases.
4. Update `check-names.py` (F-03), refresh counts (F-14).
5. Convert and consolidate in batches per folder, using each folder README's steps.
6. Re-run the audit and record the new baseline here.

## Sources

- Obsidian Help, Introduction to Bases: https://obsidian.md/help/bases (view types; filters and formulas).
- Obsidian Help, Bases syntax: https://obsidian.md/help/bases/syntax (`note.*` properties come from Markdown frontmatter; `file.*` properties work for all file types; formulas, summaries and `groupBy`).
- Obsidian Forum, How do aliases in front matter work: https://forum.obsidian.md/t/how-do-aliases-in-front-matter-work/8852 (community source; frontmatter `aliases` drive link suggestions and resolution). The official aliases help page was not retrieved.
- Vault documents cited: `99_System/10_Docs/MDSE Vault File and Folder Structure 0.8.md`, `Canonical Vault Top-Level Taxonomy 0.1.md`, `PosiBattery Runtime Handoff State.md`, `99_System/02_AI/AI_INSTRUCTIONS.md`, `99_System/03_Schemas/element-types.yaml` and `relationships.yaml`, `README.md`, `AGENTS.md`.

## Follow-up 2026-10-18: productCategory and category facets

Done after the review, at your direction:
- `productCategory` is on 569 of 570 Objects in `10_Products` (the root class note *Battery-Connected Product* has none). Schema 1.19 declares 29 category facet properties; lists are now allowed for declared facets. See [[README_Products]].
- Facets are populated on 212 Objects from figures the notes state: battery 87, charger 43, industrial-truck 40, and connectivity or range facets on 42 accessory, software and GSE notes. No body text, source, id, uid, type, subtype or relationship was changed (each write was checked against a body hash).
- Findings partly addressed: F-05 (category now queryable; `productClass` still on 10 of 570), F-06 (product-level figures queryable; the 55 Metric notes are unchanged), F-13 (`BASE_product_specs.base` added; untested in Obsidian).
- Left open: the 4 dual-parent products keep the first-listed parent for `productCategory`; categories with no repeated numbers (gse, fuel-cell, charger-accessory) have no numeric facets; coverage is partial by design (charger 43 of 64, vehicle-accessory 8 of 120).
- Checks: `check-product-facets.py` and its workflow were added. A first push of the `interfaces` facet failed `check-relationships.py` because `interfaces` is a governed Port relationship field; it was renamed `commInterfaces` and the new check now rejects any facet name that collides with a relationship field.
- Lesson recorded for later extraction: a case-insensitive match on "CAN" hit the ordinary word "can", and most "CAN bus" mentions in accessory and software notes are inferred boilerplate. Interface facets use only sentences that state the interface for the product itself.


## Follow-up 2026-10-18: company property

- Facet data review: 564 values compared with note text; 546 matched, 18 were word-form misses or class-derived chemistry. One change: chemistry removed from Midac MBS Traction Battery because the note lists VLA and VRLA.
- `madeBy` audit: of 91 targets, several are brands or divisions (Linde, STILL, Rocla, Triathlon USA, PosiCharge, Power Designers, Textron GSE, Oshkosh AeroTech, Nuvera) and four are sellers recorded as makers (Liftow, Panacea Aftermarket, BlitzNXT, Lithium Battery Solutions). Left unchanged by decision; the new `company` property gives every concrete product an organization for filtering. See [[README_Products]].
