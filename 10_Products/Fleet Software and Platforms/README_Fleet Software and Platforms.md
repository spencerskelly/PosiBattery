# Fleet Software and Platforms

## Purpose

Customer-facing fleet, battery and charger management, telematics and reporting software and platforms.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 17 / 68 |
| Typed model notes (incl. subfolders) | 68 (Object 68) |
| Status | Draft 68 of 68 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 50 / 43 of 68 |
| Tags | 22 distinct, 4 used once |
| Size | median 1,329 bytes; largest [[Powerfleet Forklift Gateway]] (4 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Battery and Charger Management|Battery and Charger Management]] | 26 | 1 | source-linked 23/25; 15 body-alias; 4 update-log; 2 off-schema subtype |
| [[README_Truck Telematics|Truck Telematics]] | 25 | 1 | source-linked 10/24; 23 body-alias; 2 update-log; 1 off-schema subtype |

### Analysis

- 68 notes: 6 abstract category/family notes and 62 concrete offerings. 62 of 62 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 46 of 62 (74%) concrete offerings carry a `describedBy` link; 16 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 56 of 68 (82%) notes `performs` at least one Function; 35 of 68 (51%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 60 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 7 notes carry dated update blocks, 4 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 39 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 68 of 68 Objects; 3 notes use a subtype outside the schema list (F-05).
- Vocabulary and size: 22 distinct tags (4 used once); median note 1,329 bytes, largest Powerfleet Forklift Gateway (4 KB).

### Key links

- [[Crown InfoLink]] — 29 inbound links
- [[Battery and Charger Management Software]] (abstract) — 25 inbound links
- [[Logisnext Lift Link]] — 25 inbound links
- [[PosiCharge PosiLink]] — 25 inbound links
- [[Truck Telematics Software]] (abstract) — 25 inbound links
- [[Linde connect]] — 24 inbound links

### Improvement steps

1. **F-05** Give a schema subtype to 3 notes now using {'hardware': 1, 'hardware and software': 1, 'unknown': 1}: [[EnerSys BSI40]], [[EnerSys EZSelect Lite]], [[Raymond iWAREHOUSE GATEWAY]].
2. **F-05** Backfill `productClass` on 68 Objects (the 6 abstract notes are the category/family candidates; classify them first).
3. **F-02** Add a `describedBy` link (or create the Source Document first) for 16 concrete offerings with no source link: [[Adveez Asset and Operations Monitoring System]], [[Doosan Lin-Q]], [[Fronius Charge & Connect]], [[Hangcha FIMS]], [[Heli Fleet Management System]], [[Hyster Tracker Telemetry]] and 10 more.
4. **F-04** Merge repeated or empty label blocks in [[Crown InfoLink]], [[Hyster Tracker Telemetry]], [[Logisnext Lift Link]], [[Powerfleet Forklift Gateway]].
5. **F-04** Consolidate the dated update blocks in 7 notes into the current-state sections once a note layout is chosen.
6. **F-03** Move 39 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
7. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
