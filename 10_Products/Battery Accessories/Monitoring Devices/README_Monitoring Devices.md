# Monitoring Devices

## Purpose

Battery monitors, data collectors and similar battery-mounted sensing and reporting devices.

Parent: [[README_Battery Accessories|Battery Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 35 / 35 |
| Typed model notes (incl. subfolders) | 35 (Object 35) |
| Status | Draft 35 of 35 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 20 / 12 of 35 |
| Tags | 26 distinct, 9 used once |
| Size | median 5,046 bytes; largest [[EnerSys Wi-iQ]] (27 KB) |

### Analysis

- 35 notes: 1 abstract category/family notes and 34 concrete offerings. 34 of 34 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 19 of 34 (56%) concrete offerings carry a `describedBy` link; 15 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 29 of 35 (83%) notes `performs` at least one Function; 24 of 35 (69%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 32 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 7 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 30 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 35 of 35 Objects; 4 notes use a subtype outside the schema list (F-05).
- Vocabulary and size: 26 distinct tags (9 used once); median note 5,046 bytes, largest EnerSys Wi-iQ (27 KB).

### Key links

- [[EnerSys Wi-iQ]] — 110 inbound links
- [[HOPPECKE trak collect]] — 87 inbound links
- [[Power Designers PowerTrac 3]] — 63 inbound links
- [[Exide Motion+ EasyMonitor]] — 53 inbound links
- [[Philadelphia Scientific eGO!pro]] — 53 inbound links
- [[Power Designers PowerTrac DT3]] — 49 inbound links

### Improvement steps

1. **F-05** Give a schema subtype to 4 notes now using {'unknown': 4}: [[Amaron DIY Rx]], [[Banner Traction Bull Battery Controller]], [[Deka Ready Power BDI]], [[Midac MB2 Battery Brain]].
2. **F-05** Backfill `productClass` on 35 Objects (the 1 abstract notes are the category/family candidates; classify them first).
3. **F-02** Add a `describedBy` link (or create the Source Document first) for 15 concrete offerings with no source link: [[AMETEK Prestolite Power Site Probe]], [[AMETEK Prestolite Power WBID]], [[Access Control Group CellTrac]], [[Access Control Group CellVue]], [[Crown Battery Health Monitor]], [[Energywith withBMS BMU]] and 9 more.
4. **F-04** Consolidate the dated update blocks in 7 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 30 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
