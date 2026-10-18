# Warning Lights and Alerts

## Purpose

Warning lights and alert devices.

Parent: [[README_Vehicle Accessories|Vehicle Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 16 / 16 |
| Typed model notes (incl. subfolders) | 16 (Object 16) |
| Status | Draft 16 of 16 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 2 / 2 of 16 |
| Tags | 13 distinct, 4 used once |
| Size | median 2,316 bytes; largest [[Toyota Forklift Lighting Options]] (3 KB) |

### Analysis

- 16 notes: 1 abstract category/family notes and 15 concrete offerings. 15 of 15 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 2 of 15 (13%) concrete offerings carry a `describedBy` link; 13 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 15 of 16 (94%) notes `performs` at least one Function; 10 of 16 (62%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 15 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 0 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 12 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 16 of 16 Objects (F-05).
- Vocabulary and size: 13 distinct tags (4 used once); median note 2,316 bytes, largest Toyota Forklift Lighting Options (3 KB).

### Key links

- [[Warning Light and Alert]] (abstract) — 16 inbound links
- [[Cat Safety Lighting Options]] — 15 inbound links
- [[STILL Warning Zone Light]] — 15 inbound links
- [[Linde Safety Guard Static Unit]] — 14 inbound links
- [[STILL SafetyLight 4Plus]] — 14 inbound links
- [[UniCarriers Lighting Packages]] — 14 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 16 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 13 concrete offerings with no source link: [[Cat Safety Lighting Options]], [[Larson Explosion-Proof Blue LED Forklift Light]], [[Linde BlueSpot]], [[Linde Safety Guard Portable Unit]], [[Linde Safety Guard Static Unit]], [[Oshkosh AeroTech Ramp Visibility Lights]] and 7 more.
3. **F-03** Move 12 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
4. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
