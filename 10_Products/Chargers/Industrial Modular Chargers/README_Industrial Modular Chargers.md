# Industrial Modular Chargers

## Purpose

Industrial modular battery charger offerings.

Parent: [[README_Chargers|Chargers]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 41 / 41 |
| Typed model notes (incl. subfolders) | 41 (Object 41) |
| Status | Draft 41 of 41 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 24 / 20 of 41 |
| Tags | 12 distinct, 3 used once |
| Size | median 2,825 bytes; largest [[EnerSys NexSys+ Charger]] (9 KB) |

### Analysis

- 41 notes: 1 abstract category/family notes and 40 concrete offerings. 40 of 40 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 23 of 40 (58%) concrete offerings carry a `describedBy` link; 17 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 40 of 41 (98%) notes `performs` at least one Function; 31 of 41 (76%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 40 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 9 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 38 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 41 of 41 Objects (F-05).
- Vocabulary and size: 12 distinct tags (3 used once); median note 2,825 bytes, largest EnerSys NexSys+ Charger (9 KB).

### Key links

- [[Crown V-HFM3 Charger]] — 60 inbound links
- [[EnerSys NexSys+ Charger]] — 45 inbound links
- [[Industrial Modular Charger]] (abstract) — 44 inbound links
- [[Power Designers REVOLUTION X]] — 42 inbound links
- [[PosiCharge ProCore Edge]] — 41 inbound links
- [[ACT Quantum 2]] — 39 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 41 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 17 concrete offerings with no source link: [[ACT Quantum Outdoor]], [[AMETEK Prestolite Power Eclipse II]], [[AMETEK Prestolite Power ULTRA]], [[Crown Battery EVOLUTION Series]], [[Exide Motion+ Lithium Charger]], [[Fronius SelectION]] and 11 more.
3. **F-04** Consolidate the dated update blocks in 9 notes into the current-state sections once a note layout is chosen.
4. **F-03** Move 38 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
