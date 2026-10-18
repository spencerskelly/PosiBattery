# Valve-Regulated Lead-Acid Batteries

## Purpose

Concrete valve-regulated lead-acid (VRLA) traction battery offerings.

Parent: [[README_Batteries|Batteries]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 17 / 17 |
| Typed model notes (incl. subfolders) | 17 (Object 17) |
| Status | Draft 17 of 17 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 15 / 15 of 17 |
| Tags | 9 distinct, 3 used once |
| Size | median 1,431 bytes; largest [[Stryten M-Series AGM200 Battery]] (4 KB) |

### Analysis

- 17 notes: 1 abstract category/family notes and 16 concrete offerings. 16 of 16 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 15 of 16 (94%) concrete offerings carry a `describedBy` link; 1 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 9 of 17 (53%) notes `performs` at least one Function; 11 of 17 (65%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 16 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 8 notes carry dated update blocks, 1 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 16 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 17 of 17 Objects (F-05).
- Vocabulary and size: 9 distinct tags (3 used once); median note 1,431 bytes, largest Stryten M-Series AGM200 Battery (4 KB).

### Key links

- [[EnerSys NexSys TPPL Battery]] — 26 inbound links
- [[Stryten M-Series AGM200 Battery]] — 25 inbound links
- [[Stryten M-Series AGM220 Battery]] — 24 inbound links
- [[Deka Dominator Battery]] — 18 inbound links
- [[Valve-Regulated Lead-Acid Traction Battery]] (abstract) — 17 inbound links
- [[Banner Traction Bull PzV Gel]] — 15 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 17 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 1 concrete offerings with no source link: [[Exide Element VRLA Battery]].
3. **F-04** Merge repeated or empty label blocks in [[Deka PowrMate Battery]].
4. **F-04** Consolidate the dated update blocks in 8 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 16 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
