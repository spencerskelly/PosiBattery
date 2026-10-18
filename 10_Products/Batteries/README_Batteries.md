# Batteries

## Purpose

Industrial traction battery offerings by chemistry: flooded lead-acid, valve-regulated lead-acid and lithium-ion.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 1 / 92 |
| Typed model notes (incl. subfolders) | 92 (Object 92) |
| Status | Draft 92 of 92 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 88 / 87 of 92 |
| Tags | 28 distinct, 6 used once |
| Size | median 1,954 bytes; largest [[Green Cubes SAFEFlex PLUS Battery]] (8 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Flooded Lead-Acid Batteries|Flooded Lead-Acid Batteries]] | 33 | 1 | source-linked 32/32; 30 body-alias; 19 update-log |
| [[README_Lithium-Ion Batteries|Lithium-Ion Batteries]] | 41 | 2 | source-linked 39/39; 33 body-alias; 24 update-log |
| [[README_Valve-Regulated Lead-Acid Batteries|Valve-Regulated Lead-Acid Batteries]] | 17 | 1 | source-linked 15/16; 16 body-alias; 8 update-log |

### Analysis

- 92 notes: 5 abstract category/family notes and 87 concrete offerings. 87 of 87 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 86 of 87 (99%) concrete offerings carry a `describedBy` link; 1 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 58 of 92 (63%) notes `performs` at least one Function; 57 of 92 (62%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 82 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 51 notes carry dated update blocks, 4 repeat a bold label inside the note and 3 contain an empty label block (F-04).
- Aliases: 79 notes list aliases in a body `## Aliases` section and 4 in YAML (F-03).
- Classification: `productClass` is blank on 87 of 92 Objects (F-05).
- Vocabulary and size: 28 distinct tags (6 used once); median note 1,954 bytes, largest Green Cubes SAFEFlex PLUS Battery (8 KB).

### Key links

- [[Industrial Traction Battery]] (abstract) — 44 inbound links
- [[Lithium-Ion Traction Battery]] (abstract) — 37 inbound links
- [[Exide Sonnenschein Lithium Battery]] — 33 inbound links
- [[Flooded Lead-Acid Traction Battery]] (abstract) — 33 inbound links
- [[Stryten M-Series Li610 Battery]] — 33 inbound links
- [[Green Cubes SAFEFlex PLUS Battery]] — 32 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 87 Objects (the 5 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 1 concrete offerings with no source link: [[Exide Element VRLA Battery]].
3. **F-04** Merge repeated or empty label blocks in [[Crown V-Force Lithium-Ion ESS]], [[Deka PowrMate Battery]], [[Hangcha Lithium Iron Phosphate Battery Pack]], [[Raymond 8250 Lithium-Ion Battery]], [[Toyota Lithium-Ion 5-35 Battery Series]], [[Triathlon Lithium-Ion Battery for UniCarriers]].
4. **F-04** Consolidate the dated update blocks in 51 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 79 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
