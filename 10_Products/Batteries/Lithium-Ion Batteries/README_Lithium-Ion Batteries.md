# Lithium-Ion Batteries

## Purpose

Concrete lithium-ion traction battery and energy-storage-system offerings, including packs sold with an integrated BMS or charger.

Parent: [[README_Batteries|Batteries]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 41 / 41 |
| Typed model notes (incl. subfolders) | 41 (Object 41) |
| Status | Draft 41 of 41 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 40 / 40 of 41 |
| Tags | 21 distinct, 8 used once |
| Size | median 2,410 bytes; largest [[Green Cubes SAFEFlex PLUS Battery]] (8 KB) |

### Analysis

- 41 notes: 2 abstract category/family notes and 39 concrete offerings. 39 of 39 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 39 of 39 (100%) concrete offerings carry a `describedBy` link.
- Function and design links: 32 of 41 (78%) notes `performs` at least one Function; 24 of 41 (59%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 38 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 24 notes carry dated update blocks, 3 repeat a bold label inside the note and 3 contain an empty label block (F-04).
- Aliases: 33 notes list aliases in a body `## Aliases` section and 4 in YAML (F-03).
- Classification: `productClass` is blank on 36 of 41 Objects (F-05).
- Vocabulary and size: 21 distinct tags (8 used once); median note 2,410 bytes, largest Green Cubes SAFEFlex PLUS Battery (8 KB).

### Key links

- [[Lithium-Ion Traction Battery]] (abstract) — 37 inbound links
- [[Exide Sonnenschein Lithium Battery]] — 33 inbound links
- [[Stryten M-Series Li610 Battery]] — 33 inbound links
- [[Green Cubes SAFEFlex PLUS Battery]] — 32 inbound links
- [[Raymond Energy Essentials Lithium-Ion Battery]] — 32 inbound links
- [[Flux Power GSE Pack]] (abstract) — 31 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 36 Objects (the 2 abstract notes are the category/family candidates; classify them first).
2. **F-04** Merge repeated or empty label blocks in [[Crown V-Force Lithium-Ion ESS]], [[Hangcha Lithium Iron Phosphate Battery Pack]], [[Raymond 8250 Lithium-Ion Battery]], [[Toyota Lithium-Ion 5-35 Battery Series]], [[Triathlon Lithium-Ion Battery for UniCarriers]].
3. **F-04** Consolidate the dated update blocks in 24 notes into the current-state sections once a note layout is chosen.
4. **F-03** Move 33 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
