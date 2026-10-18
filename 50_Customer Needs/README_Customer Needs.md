# Customer Needs

## Purpose

Customer and user outcomes, needs, pain points, constraints, and demand signals are organized here. Current need records are modeled as Use Case notes (subtype why); each need is realized by specific Functions, which products perform, and lists the Actors who have the need.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[Knowledge Base Backlog]].

## Contents

- Use Case notes (why). All needs are hypotheses until customer-side evidence is added. The route from products is in [[Product to Customer Need Map]].

## Navigation

- `BASE_all_Customer Needs.base` and `BASE_local_Customer Needs.base` — views of the notes in this folder.
- [[Product to Customer Need Map]] — product to need to role route.
- [[Battery Product Landscape Conflicts and Open Questions|Conflicts and open questions]] — C101 to C106 cover the evidence behind these notes.

## Operational traceability

All current Customer Need notes identify the Actors who have the need through `participants` and the Functions that address the need through `realizedBy`.

Where a stable operational scenario or context now exists, the Need note also includes an **Operational traceability** section with ordinary wikilinks to that Use Case/context. These links are intentionally navigational rather than `tracesTo`: the current relationship vocabulary has no dedicated Need-to-operational-Use-Case relationship, and `tracesTo` is provisional/review-generating.

Do not force every Need into an operational Use Case. Some Needs currently map only to operating contexts, and others remain ahead of the operational model.

## Related areas

- [[README_Product Functions|Product Functions]] — the functions that realize needs.
- [[README_Products|Products]] — offerings that perform those functions.

## Maintenance

New need or role notes follow `99_System/02_AI/AI_INSTRUCTIONS.md`. Do not state a need without a source; keep vendor statements separate from customer evidence.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 32 / 32 |
| Typed model notes (incl. subfolders) | 31 (Use Case 31) |
| Status | Draft 31 of 31 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 8 / 10 of 31 |
| Tags | 7 distinct, 3 used once |
| Size | median 4,230 bytes; largest [[Prevent Tip-Overs and Overloads]] (6 KB) |
| Non-markdown files | .base 2, .canvas 1 |

### Analysis

- 31 Use Case notes, all subtype `why`, all with `participants` and `realizedBy`. Needs follow the agreed model (Use Case, subtype why).
- Evidence status is carried by tags (`need-hypothesis`, `vendor-stated`) and by prose ('Evidence status: need hypothesis'); 27 of 31 notes also mark source tier (T1 to T4) in prose only (F-02).
- 8 of 31 have `describedBy`; 10 link any Source Document. Notes cite Documents inline, so most evidence links are not in YAML.
- Several notes accumulate dated 'Customer-side evidence added' bullets in `## Notes` (13 notes carry update stamps, F-04).
- No customer-side source confirms any need; all remain hypotheses, as the notes themselves say. This is consistent with the ruleset, but status is not queryable.

### Key links

- [[Prevent Battery Abuse and Premature Replacement]] — 29 inbound links
- [[Know Battery State Before and During the Shift]] — 21 inbound links
- [[Charge Each Battery Correctly for Its Chemistry and Condition]] — 20 inbound links
- [[Return Trucks to Service Quickly After a Low Charge]] — 19 inbound links
- [[Connect Chargers and Batteries Safely at the Site]] — 18 inbound links
- [[Integrate the Battery with Truck and Charger Controls]] — 18 inbound links

### Improvement steps

1. **F-02** Promote evidence status (hypothesis, vendor-stated, customer-confirmed) to a controlled tag vocabulary now; propose a property later.
2. **F-02** Move inline Document citations into `describedBy` or `supportedBy`/`contradicts` so a Base can show evidence per need.
3. **F-13** Base: needs by evidence status with count of linked Documents and realizing Functions.
