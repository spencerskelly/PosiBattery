# Battery Accessories

## Purpose

Devices added to batteries during or after production: battery management systems, monitoring, identification and charge-interface devices, connectors, watering, electrolyte circulation, thermal management, protection and telematics.

Parent: [[README_Products|10_Products]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 4 / 107 |
| Typed model notes (incl. subfolders) | 107 (Object 107) |
| Status | Draft 107 of 107 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 64 / 50 of 107 |
| Tags | 44 distinct, 13 used once |
| Size | median 2,254 bytes; largest [[EnerSys Wi-iQ]] (27 KB) |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Battery Management Systems|Battery Management Systems]] | 10 | 1 | source-linked 1/9; 2 body-alias; 1 update-log |
| [[README_Connector Assemblies|Connector Assemblies]] | 12 | 1 | source-linked 9/11; 9 body-alias; 5 update-log |
| Electrolyte Circulation Systems | 9 | 1 | source-linked 5/8; 6 body-alias; 3 update-log; 2 off-schema subtype |
| [[README_Identification and Charge Interface Devices|Identification and Charge Interface Devices]] | 10 | 2 | source-linked 6/8; 5 body-alias; 1 update-log |
| [[README_Monitoring Devices|Monitoring Devices]] | 35 | 1 | source-linked 19/34; 30 body-alias; 7 update-log; 4 off-schema subtype |
| Protection and Disconnect Units | 1 | 1 | source-linked 1/1; 1 body-alias; thin |
| Telematics and Connectivity Devices | 3 | 1 | source-linked 1/2; 3 body-alias |
| Thermal Management Devices | 1 | 1 | source-linked 1/1; 1 body-alias; thin |
| Water Level Monitors | 9 | 1 | source-linked 4/8; 7 body-alias; 1 update-log; 1 off-schema subtype |
| [[README_Watering Systems|Watering Systems]] | 13 | 1 | source-linked 6/12; 7 body-alias; 1 update-log; 3 off-schema subtype |

### Analysis

- 107 notes: 14 abstract category/family notes and 93 concrete offerings. 93 of 93 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 52 of 93 (56%) concrete offerings carry a `describedBy` link; 33 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 82 of 107 (77%) notes `performs` at least one Function; 64 of 107 (60%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 86 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 20 notes carry dated update blocks, 1 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 73 notes list aliases in a body `## Aliases` section and 5 in YAML (F-03).
- Classification: `productClass` is blank on 102 of 107 Objects; 11 notes use a subtype outside the schema list (F-05).
- Vocabulary and size: 44 distinct tags (13 used once); median note 2,254 bytes, largest EnerSys Wi-iQ (27 KB).

### Key links

- [[EnerSys Wi-iQ]] — 110 inbound links
- [[HOPPECKE trak collect]] — 87 inbound links
- [[PosiCharge PosiGuard]] — 81 inbound links
- [[PosiCharge BMID]] (abstract) — 68 inbound links
- [[Power Designers PowerTrac 3]] — 63 inbound links
- [[PosiCharge Battery Rx]] — 54 inbound links

### Improvement steps

1. **F-05** Give a schema subtype to 11 notes now using {'unknown': 11}: [[Amaron AFS System]], [[Amaron DIY Rx]], [[Banner Traction Bull Battery Controller]], [[Banner Traction Bull Electrolyte Circulation Pump Module]], [[Banner Traction Bull Filling System]], [[Deka Ready Power BDI]] and 5 more.
2. **F-05** Backfill `productClass` on 102 Objects (the 14 abstract notes are the category/family candidates; classify them first).
3. **F-02** Add a `describedBy` link (or create the Source Document first) for 33 concrete offerings with no source link: [[AMETEK Prestolite Power Site Probe]], [[AMETEK Prestolite Power WBID]], [[Access Control Group CellTrac]], [[Access Control Group CellVue]], [[Crown Battery Acid Indicators]], [[Crown Battery Cables and Connectors]] and 27 more.
4. **F-04** Merge repeated or empty label blocks in [[Crown Battery Acid Indicators]].
5. **F-04** Consolidate the dated update blocks in 20 notes into the current-state sections once a note layout is chosen.
6. **F-03** Move 73 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
7. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
