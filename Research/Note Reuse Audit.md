---
type: Info
subtype:
id: INFO-00203
uid: 20261003093855193skellyspencer
status: Draft
tags:
  - review
  - conventions
  - quality
describes:
  - "[[Battery-Connected Product]]"
---

# Note Reuse Audit

## Definition

Record of where notes covered the same thing, what was merged or renamed, and the rules that keep one note per thing.

## Notes

- **Rules (owner, 2026-10-03):** (1) one note per thing: one organization note per owner, one product note per product, one metric note per metric; (2) products link to the owner by relationship, and the owner is never a folder; (3) check titles and aliases before creating a note; (4) when notes are merged, the survivor keeps its id and the retired ids go in Former ids; (5) notes that might be the same but are unproven stay separate and are cross-referenced; (6) no two notes share a name, and a colliding name gets an identifier after it (brand or application), checked by `99_System/check-names.py`.
- **Folder rule:** `Products/<Type>/<Category>/` where the type is Batteries, Chargers, Forklifts, Battery Accessories, Charger Accessories, Vehicle Accessories, Fleet Software and Platforms, Fuel Cell Power Units or Ground Support Equipment, and the category folders sit under the type (for example `Products/Batteries/Lithium-Ion Batteries`).

| Area | What overlapped | Decision |
|---|---|---|
| Folders | Crown vs Crown Equipment, East Penn vs East Penn Manufacturing, Stryten vs Stryten Energy, Exide vs Exide Technologies, Fronius vs Fronius International were separate folders for the same owner, and owners had folders under both Battery Products and Forklifts | Folders are now product type then category; no owner folders; the owner is the makes, offers or other relationship on the product note |
| Metrics | Certifications, Size and Mass, Voltage, Operating Temperature, Warranty and Price, Power Consumption and Ingress Protection were separate notes for monitors, chargers and batteries | Merged into 7 shared metric notes (original ids in Former ids); the other metric notes renamed 'Metric - ...' with the class kept as a tag |
| Maps | Truck Device Feature Map repeated part of the Function Map and Design Map | Merged; Function Map and Design Map now cover every function and design |
| Comparisons | Battery Monitoring Performance Comparison overlapped Monitor Comparison Matrix | Merged into the matrix; original kept as a section and its id in Former ids |
| Aliases | 'GNB Industrial Power' was an alias of Exide Technologies and also its own note; 'Triathlon' was an alias of two notes; two notes listed an alias twice | Aliases removed or made specific; duplicates dropped |
| Organization notes | Round 5 offered-with lists repeated products that now have notes | Relabeled as superseded and kept as written for items not yet modeled; owners link to products by relationship |
| Kept separate until evidence | Hyster Tracker Telemetry vs Hyster Battery Tracker (C60); Yale Vision Telemetry vs Yale Battery Vision (C60); Triathlon USA vs Triathlon Battery Solutions (C62); eGO!c vs eGO!core (C23); WBID vs WBID Pro; Lester Summit II 650 W vs Delta-Q IC650 (C58) | Not merged because no source says they are the same thing; each pair is cross-referenced in the conflicts register |
| Boundary kept | Alert on Abnormal Condition (battery) vs Alert Operator of Hazards (truck); Log Battery Events and Usage vs Report Truck Telemetry | Different objects of the behavior; kept separate with the boundary stated in each note |
- **Round 18:** vault-wide name check added; the vault had no duplicate note names. Eleven Research working notes from the PosiCharge business analysis use a different layout (no model frontmatter or standard headings); they are left as written (owner decision pending).

**Business analysis notes: where each was stored and why (round 19, 2026-10-03)**

| Note | Decision | Reason |
|---|---|---|
| Knowledge Base Next Steps | Converted to a model note; stays in Research (vault-wide plan) | Different job from the Investigation Backlog: this note orders the work (P0/P1/P2), the backlog lists the work items; each now points to the other |
| Research Change and Decision Tracker | Converted; stays in Research; now also logs the vault-structure decisions | One decision log instead of decisions scattered across registers; owner decisions Q13 to Q16, folder layout and naming rule added |
| PosiCharge and Power Designers Current Portfolio Baseline | Converted; moved to Research/Business Analysis; product facts moved to product notes | Facts stored once on product notes; the baseline keeps confidence, still-needed evidence, the connected-product architecture and review limits |
| PosiCharge and Power Designers Public Evidence Register | Converted; moved to Research/Business Analysis | Register of public sources for the baseline; acquisition queue now points to Document Wishlist |
| PosiCharge and Power Designers Evidence Gaps and Conflicts | Converted; moved; conflicts moved to the central register | PC-PUB-001 to 003 are now C77 to C79 in the single conflict register; the gaps (PC-GAP-001 to 013) stay here because they are PosiCharge internal-evidence questions |
| PosiCharge Opportunity Backlog | Converted; moved; kept separate | Business opportunities are not research tasks; kept apart from the Investigation Backlog on purpose and cross-linked |
| PosiCharge Business Scope and Portfolio, Market Segments and Jobs-to-Be-Done, Competitive and Partner Landscape, Product Comparison Matrix, Capability Gap Assessment | Converted; moved to Research/Business Analysis | Analysis frameworks for the PosiCharge business; the comparison matrix note defines cohorts and eligibility, while the data stays in the Monitor, Charger and Battery Comparison Matrices |
| Ampure Group Portfolio Context, Ampure Industrial Portfolio Overlap and Synergy Map | Already model notes; moved to Research/Business Analysis | Group-level analysis guidance; the organizations themselves stay in Organizations |

- **Folder:** `Research/Business Analysis` is named for the category of work, not for an owner, following the folder rule above. Notes keep their original titles so the owner's links still resolve.
- **Links:** path-style links (a folder name, a slash and the note name inside double brackets) were rewritten to name-only links for the moved notes; folder-level links to a bare folder name now point to that folder's README note. Pipes inside links in table rows were escaped so the tables render (one table in the Opportunity Backlog was broken).

## Aliases

- Reuse audit

## Former ids
