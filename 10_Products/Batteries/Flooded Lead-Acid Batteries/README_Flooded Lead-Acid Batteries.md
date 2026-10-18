# Flooded Lead-Acid Batteries

## Purpose

Concrete flooded lead-acid traction battery offerings and variants.

Parent: [[README_Batteries|Batteries]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 33 / 33 |
| Typed model notes (incl. subfolders) | 33 (Object 33) |
| Status | Draft 33 of 33 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 32 / 32 of 33 |
| Tags | 9 distinct, 2 used once |
| Size | median 1,954 bytes; largest [[HAWKER Perfect Plus Battery]] (5 KB) |

### Analysis

- 33 notes: 1 abstract category/family notes and 32 concrete offerings. 32 of 32 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 32 of 32 (100%) concrete offerings carry a `describedBy` link.
- Function and design links: 17 of 33 (52%) notes `performs` at least one Function; 22 of 33 (67%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 28 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 19 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 30 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 33 of 33 Objects (F-05).
- Vocabulary and size: 9 distinct tags (2 used once); median note 1,954 bytes, largest HAWKER Perfect Plus Battery (5 KB).

### Key links

- [[Flooded Lead-Acid Traction Battery]] (abstract) — 33 inbound links
- [[HAWKER Perfect Plus Battery]] — 28 inbound links
- [[EnerSys IRONCLAD Battery]] — 27 inbound links
- [[Stryten M-Series T310 Battery]] — 25 inbound links
- [[Stryten M-Series T330 Battery]] — 25 inbound links
- [[Midac PzS Traction Battery]] — 24 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 33 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-04** Consolidate the dated update blocks in 19 notes into the current-state sections once a note layout is chosen.
3. **F-03** Move 30 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
4. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
