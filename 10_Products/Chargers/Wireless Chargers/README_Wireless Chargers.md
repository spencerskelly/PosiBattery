# Wireless Chargers

## Purpose

Wireless charging offerings for industrial vehicles and batteries.

Parent: [[README_Chargers|Chargers]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 11 / 11 |
| Typed model notes (incl. subfolders) | 11 (Object 11) |
| Status | Draft 11 of 11 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 10 / 10 of 11 |
| Tags | 9 distinct, 4 used once |
| Size | median 1,046 bytes; largest [[EnerSys NexSys AIR Wireless Charger]] (6 KB) |

### Analysis

- 11 notes: 1 abstract category/family notes and 10 concrete offerings. 10 of 10 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 10 of 10 (100%) concrete offerings carry a `describedBy` link.
- Function and design links: 10 of 11 (91%) notes `performs` at least one Function; 10 of 11 (91%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 10 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 2 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 9 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 11 of 11 Objects (F-05).
- Vocabulary and size: 9 distinct tags (4 used once); median note 1,046 bytes, largest EnerSys NexSys AIR Wireless Charger (6 KB).

### Key links

- [[EnerSys NexSys AIR Wireless Charger]] — 38 inbound links
- [[Delta MOOVair Wireless Charging Series]] — 22 inbound links
- [[Resonant Link Wireless Lift Truck Charger]] — 17 inbound links
- [[Wiferion etaLINK 3000 Wireless Charging System]] — 11 inbound links
- [[Wireless Charger]] (abstract) — 11 inbound links
- [[Lindig L.inductive Charging Offer]] — 10 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 11 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-04** Consolidate the dated update blocks in 2 notes into the current-state sections once a note layout is chosen.
3. **F-03** Move 9 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
4. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
