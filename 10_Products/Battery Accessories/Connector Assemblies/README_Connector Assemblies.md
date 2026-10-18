# Connector Assemblies

## Purpose

Battery and charger connector, cable and lead assemblies.

Parent: [[README_Battery Accessories|Battery Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 12 / 12 |
| Typed model notes (incl. subfolders) | 12 (Object 12) |
| Status | Draft 12 of 12 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 10 / 9 of 12 |
| Tags | 12 distinct, 5 used once |
| Size | median 1,797 bytes; largest [[Anderson SB Connector Series]] (5 KB) |

### Analysis

- 12 notes: 1 abstract category/family notes and 11 concrete offerings. 11 of 11 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 9 of 11 (82%) concrete offerings carry a `describedBy` link; 2 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 11 of 12 (92%) notes `performs` at least one Function; 8 of 12 (67%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 12 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 5 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 9 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 12 of 12 Objects (F-05).
- Vocabulary and size: 12 distinct tags (5 used once); median note 1,797 bytes, largest Anderson SB Connector Series (5 KB).

### Key links

- [[Anderson SB Connector Series]] — 21 inbound links
- [[Battery Connector Assembly]] (abstract) — 14 inbound links
- [[Anderson IBC Industrial Battery Connector]] — 12 inbound links
- [[Anderson SBE SBX SBO Connector Series]] — 12 inbound links
- [[Anderson Double Stack Manual Assist Brackets]] — 11 inbound links
- [[Anderson EBC Euro Battery Connector]] — 11 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 12 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 2 concrete offerings with no source link: [[Crown Battery Cables and Connectors]], [[Midac End Leads]].
3. **F-04** Consolidate the dated update blocks in 5 notes into the current-state sections once a note layout is chosen.
4. **F-03** Move 9 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
