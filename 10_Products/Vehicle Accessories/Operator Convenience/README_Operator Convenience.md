# Operator Convenience

## Purpose

Operator convenience features offered with trucks.

Parent: [[README_Vehicle Accessories|Vehicle Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 12 / 12 |
| Typed model notes (incl. subfolders) | 12 (Object 12) |
| Status | Draft 12 of 12 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 6 / 6 of 12 |
| Tags | 8 distinct, 2 used once |
| Size | median 1,430 bytes; largest [[Jungheinrich easyPILOT]] (2 KB) |

### Analysis

- 12 notes: 1 abstract category/family notes and 11 concrete offerings. 11 of 11 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 6 of 11 (55%) concrete offerings carry a `describedBy` link; 5 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 7 of 12 (58%) notes `performs` at least one Function; 2 of 12 (17%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 11 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 3 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 4 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 12 of 12 Objects (F-05).
- Vocabulary and size: 8 distinct tags (2 used once); median note 1,430 bytes, largest Jungheinrich easyPILOT (2 KB).

### Key links

- [[STILL EasyBelt]] — 14 inbound links
- [[Jungheinrich easyPILOT]] — 13 inbound links
- [[Operator Convenience Accessory]] (abstract) — 12 inbound links
- [[UniCarriers In-Cab Accessories]] — 12 inbound links
- [[Linde Rotating Operator Workstation]] — 10 inbound links
- [[Linde Smartphone Holder]] — 10 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 12 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 5 concrete offerings with no source link: [[Jungheinrich easyPILOT]], [[Linde Rotating Operator Workstation]], [[Linde Smartphone Holder]], [[STILL EasyBelt]], [[UniCarriers In-Cab Accessories]].
3. **F-04** Consolidate the dated update blocks in 3 notes into the current-state sections once a note layout is chosen.
4. **F-03** Move 4 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
