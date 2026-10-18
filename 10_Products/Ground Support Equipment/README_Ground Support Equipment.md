# Ground Support Equipment

## Purpose

Airport ground support vehicles: baggage and tow tractors, belt loaders, cargo loaders and pushback tractors.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 1 / 21 |
| Typed model notes (incl. subfolders) | 21 (Object 21) |
| Status | Draft 21 of 21 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 0 / 0 of 21 |
| Tags | 6 distinct, 0 used once |
| Size | median 1,183 bytes; largest [[TUG ALPHA 1 Pushback]] (3 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| Baggage and Tow Tractors | 7 | 1 | source-linked 0/6; 6 body-alias |
| Belt Loaders | 6 | 1 | source-linked 0/5; 5 body-alias |
| Cargo Loaders | 3 | 1 | source-linked 0/2; 2 body-alias |
| Pushback Tractors | 4 | 1 | source-linked 0/3; 3 body-alias |

### Analysis

- 21 notes: 5 abstract category/family notes and 16 concrete offerings. 16 of 16 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 0 of 16 (0%) concrete offerings carry a `describedBy` link; 16 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 5 of 21 (24%) notes `performs` at least one Function; 6 of 21 (29%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 17 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 0 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 16 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 21 of 21 Objects (F-05).
- Vocabulary and size: 6 distinct tags (0 used once); median note 1,183 bytes, largest TUG ALPHA 1 Pushback (3 KB).

### Key links

- [[TUG ALPHA 1 Pushback]] — 20 inbound links
- [[TUG Endurance Baggage Tractor]] — 20 inbound links
- [[Mallaghan SkyBelt]] — 15 inbound links
- [[Oshkosh AeroTech Commander 30i Cargo Loader]] — 13 inbound links
- [[TLD NBL-E Belt Loader]] — 12 inbound links
- [[Charlatte T135 Neo 25T]] — 10 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 21 Objects (the 5 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 16 concrete offerings with no source link: [[Charlatte Belt Loaders]], [[Charlatte CBT350 AC Tow Tractor]], [[Charlatte CPB35E Pushback Tractor]], [[Charlatte T135 Neo 25T]], [[Charlatte T137-V3]], [[Linde P250 Electric Baggage Tractor]] and 10 more.
3. **F-03** Move 16 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
4. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
