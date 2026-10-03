---
type: Info
subtype:
id: INFO-00237
uid: 20261003145706704skellyspencer
status: Draft
tags:
  - provenance
  - context
  - conventions
describes:
  - "[[Battery-Connected Product]]"
---

# External Context and Provenance

## Definition

Register of what was added to the vault outside the AI working sessions (by the owner or another tool), when, what each item is, and how it was handled.

## Notes

- **Why this note exists (owner request, 2026-10-03):** the vault now holds material that was not produced in the AI sessions that built the Products, Functions, Designs, Metrics and Research notes. Readers need to know which is which, and what each is based on.
- **How to read the history:** all commits are authored under the owner's account (`spencerskelly`); the repository history does not say which tool wrote a given note. The notes' own wording and the commit messages are the only attribution available, so the table says 'added outside the AI sessions' where the notes show it and does not guess the tool.
- **Handling rule:** external material is left as written. Changes made to it are limited to: converting layout to model notes, moving files to a folder, relinking, and adding dated update lines; each change is logged in [[Note Reuse Audit]] and [[Research Change and Decision Tracker]]. Owner statements are kept as 'vault owner statement' with their date and never turned into facts about the market.

| Date | Commit | What was added | Where | Basis stated in the material | Handling |
|---|---|---|---|---|---|
| 2026-10-03 | bbb7fa9 | Navigation README notes for top-level folders (Definitions and Downloads created) | `Definitions`, `Downloads`, folder READMEs | owner navigation request | kept as written; `README_Products` is owner-maintained and is no longer regenerated |
| 2026-10-03 | 0e0b952 | PosiCharge business analysis framework: scope, segments, competitive landscape, comparison matrix, capability gaps, opportunity backlog, change tracker | [[PosiCharge Business Scope and Portfolio]] and siblings in `Research/Business Analysis` | 'vault owner direction' | converted to model notes and filed in round 19 |
| 2026-10-03 | 42bd222 | Ampure group context; Ampure and Ampure Automotive and Aftermarket EVSE organization notes; PosiCharge and Power Designers edits; ledger rows | [[Ampure]], [[Ampure Automotive and Aftermarket EVSE]], [[Ampure Group Portfolio Context]] | 'vault owner statement, 2026-10-03', Ampure press releases | kept; Ampure notes were already model notes |
| 2026-10-03 | e41eac2 | Knowledge Base Next Steps | [[Knowledge Base Next Steps]] | planning note | converted in round 19 |
| 2026-10-03 | 2bd9b3d | Public evidence baseline, evidence register and gaps note for PosiCharge and Power Designers | [[PosiCharge and Power Designers Current Portfolio Baseline]], [[PosiCharge and Power Designers Public Evidence Register]], [[PosiCharge and Power Designers Evidence Gaps and Conflicts]] | official PosiCharge pages and press releases, accessed 2026-10-03 | converted in round 19; product facts moved to product notes |
| 2026-10-03 | 16b63f1, 09dd52a, a20079c and others | Uploaded documents (about 70 files: manufacturer sheets, brochures, manuals, reports) | `Downloads` | owner downloads | wishlist rows marked in repo; read documents are absorbed as noted in [[Document Wishlist]] |

**Owner statements recorded in the notes (second-hand: these were relayed in notes written outside the AI sessions)**

- Ampure has three business units: PosiCharge (primary improvement focus), Power Designers Sibex (internal industrial portfolio and shared-team capability) and Automotive and Aftermarket EVSE (contextual capability source) - vault owner statement, 2026-10-03, recorded in [[Ampure]].
- Some teams serve more than one Ampure business - vault owner statement, 2026-10-03, recorded in [[Ampure]] and [[Power Designers]]; which teams is not recorded.
- 'Automotive and Aftermarket EVSE' is the owner's working name, not an official unit name - recorded in [[Ampure Automotive and Aftermarket EVSE]].
- Power Designers Sibex is analyzed as internal, not as a competitor; EVSE offers are capability references, not comparators - modeling decisions recorded in [[Research Change and Decision Tracker]].

**Owner statements given in the AI sessions (first-hand)**

- Q11 keep light-duty chargers in scope; Q12 batteries and electric forklifts use subtype electrical; Q13 stay with electric trucks but note ICE and fuel-cell features that electric may lack; Q14 ICE trucks are electrical; Q15 model all accessories, a key focus; Q16 functions depend on designs. The owner also directed: folders by product type then category with owners as relationships; no two notes share a name; direct-file links only in the wishlist URL column; truck-side devices matter more than lifting power. See [[Research Change and Decision Tracker]] and [[Note Reuse Audit]].

**What is not known:** which tool or person authored each externally added note; the review status of the business analysis notes (they say 'draft-for-internal-review', reviewer 'Director of Engineering'); the internal documents referred to by the evidence register as 'controlled' (not in the repository).

## Aliases

- Context provenance

## Former ids
