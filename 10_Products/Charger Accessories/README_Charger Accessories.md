# Charger Accessories

## Purpose

Accessories for chargers: cable management, connector accessories, remote controls and indicators, stands and mounting, and thermal accessories.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 3 / 21 |
| Typed model notes (incl. subfolders) | 21 (Object 21) |
| Status | Draft 21 of 21 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 6 / 6 of 21 |
| Tags | 13 distinct, 2 used once |
| Size | median 1,303 bytes; largest [[Crown V-HFM3 Wired Remote Control Kit]] (2 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| Cable Management | 2 | 1 | source-linked 0/1; 1 body-alias; thin |
| Connector Accessories | 7 | 1 | source-linked 5/6; 3 body-alias; 1 update-log |
| Remote Controls and Indicators | 4 | 1 | source-linked 0/3; 3 body-alias |
| Stands and Mounting | 3 | 1 | source-linked 0/2 |
| Thermal Accessories | 2 | 1 | source-linked 0/1; 1 body-alias; thin |

### Analysis

- 21 notes: 6 abstract category/family notes and 15 concrete offerings. 15 of 15 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 6 of 15 (40%) concrete offerings carry a `describedBy` link; 9 have no `describedBy` and link no Document note anywhere (1 of those cite no URL in the body either).
- Function and design links: 13 of 21 (62%) notes `performs` at least one Function; 9 of 21 (43%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 14 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 2 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 9 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 21 of 21 Objects (F-05).
- Vocabulary and size: 13 distinct tags (2 used once); median note 1,303 bytes, largest Crown V-HFM3 Wired Remote Control Kit (2 KB).

### Key links

- [[Crown V-HFM3 Tower Light Kit]] — 16 inbound links
- [[Crown V-HFM3 Wired Remote Control Kit]] — 16 inbound links
- [[PosiCharge Three-Color Stack Light]] — 13 inbound links
- [[PosiCharge Cooling Fan Box]] — 12 inbound links
- [[Raymond Courier AutoCharge System]] — 11 inbound links
- [[Crown Cable Management Accessories]] — 10 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 21 Objects (the 6 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 9 concrete offerings with no source link: [[Crown Cable Management Accessories]], [[Crown V-HFM3 Charger Stand]], [[Crown V-HFM3 Tower Light Kit]], [[Crown V-HFM3 Wired Remote Control Kit]], [[HVPS Communications Kit]], [[PosiCharge Charger Stand Kit and Cable Handler]] and 3 more.
3. **F-04** Consolidate the dated update blocks in 2 notes into the current-state sections once a note layout is chosen.
4. **F-03** Move 9 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
