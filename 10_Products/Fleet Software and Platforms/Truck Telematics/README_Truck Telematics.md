# Truck Telematics

## Purpose

Truck telematics and fleet-data platforms.

Parent: [[README_Fleet Software and Platforms|Fleet Software and Platforms]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 25 / 25 |
| Typed model notes (incl. subfolders) | 25 (Object 25) |
| Status | Draft 25 of 25 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 10 / 10 of 25 |
| Tags | 14 distinct, 2 used once |
| Size | median 1,851 bytes; largest [[Powerfleet Forklift Gateway]] (4 KB) |

### Analysis

- 25 notes: 1 abstract category/family notes and 24 concrete offerings. 24 of 24 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 10 of 24 (42%) concrete offerings carry a `describedBy` link; 14 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 22 of 25 (88%) notes `performs` at least one Function; 9 of 25 (36%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 24 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 2 notes carry dated update blocks, 4 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 23 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 25 of 25 Objects; 1 notes use a subtype outside the schema list (F-05).
- Vocabulary and size: 14 distinct tags (2 used once); median note 1,851 bytes, largest Powerfleet Forklift Gateway (4 KB).

### Key links

- [[Crown InfoLink]] — 29 inbound links
- [[Logisnext Lift Link]] — 25 inbound links
- [[Truck Telematics Software]] (abstract) — 25 inbound links
- [[Linde connect]] — 24 inbound links
- [[Powerfleet Forklift Gateway]] — 24 inbound links
- [[Raymond iWAREHOUSE]] — 23 inbound links

### Improvement steps

1. **F-05** Give a schema subtype to 1 notes now using {'unknown': 1}: [[Raymond iWAREHOUSE GATEWAY]].
2. **F-05** Backfill `productClass` on 25 Objects (the 1 abstract notes are the category/family candidates; classify them first).
3. **F-02** Add a `describedBy` link (or create the Source Document first) for 14 concrete offerings with no source link: [[Adveez Asset and Operations Monitoring System]], [[Doosan Lin-Q]], [[Hangcha FIMS]], [[Heli Fleet Management System]], [[Hyster Tracker Telemetry]], [[Jungheinrich ISM Online]] and 8 more.
4. **F-04** Merge repeated or empty label blocks in [[Crown InfoLink]], [[Hyster Tracker Telemetry]], [[Logisnext Lift Link]], [[Powerfleet Forklift Gateway]].
5. **F-04** Consolidate the dated update blocks in 2 notes into the current-state sections once a note layout is chosen.
6. **F-03** Move 23 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
7. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
