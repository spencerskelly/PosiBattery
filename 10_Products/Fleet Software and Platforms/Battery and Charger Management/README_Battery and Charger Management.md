# Battery and Charger Management

## Purpose

Software that manages batteries and chargers at fleet or site level.

Parent: [[README_Fleet Software and Platforms|Fleet Software and Platforms]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 26 / 26 |
| Typed model notes (incl. subfolders) | 26 (Object 26) |
| Status | Draft 26 of 26 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 23 / 20 of 26 |
| Tags | 14 distinct, 7 used once |
| Size | median 1,369 bytes; largest [[Exide GNB Fleet]] (3 KB) |

### Analysis

- 26 notes: 1 abstract category/family notes and 25 concrete offerings. 25 of 25 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 23 of 25 (92%) concrete offerings carry a `describedBy` link; 2 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 22 of 26 (85%) notes `performs` at least one Function; 15 of 26 (58%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 24 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 4 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 15 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 26 of 26 Objects; 2 notes use a subtype outside the schema list (F-05).
- Vocabulary and size: 14 distinct tags (7 used once); median note 1,369 bytes, largest Exide GNB Fleet (3 KB).

### Key links

- [[Battery and Charger Management Software]] (abstract) — 25 inbound links
- [[PosiCharge PosiLink]] — 25 inbound links
- [[PosiCharge E-Meter]] — 23 inbound links
- [[PosiCharge SkyLink]] — 20 inbound links
- [[ACT ACTview]] — 18 inbound links
- [[Exide GNB Fleet]] — 18 inbound links

### Improvement steps

1. **F-05** Give a schema subtype to 2 notes now using {'hardware': 1, 'hardware and software': 1}: [[EnerSys BSI40]], [[EnerSys EZSelect Lite]].
2. **F-05** Backfill `productClass` on 26 Objects (the 1 abstract notes are the category/family candidates; classify them first).
3. **F-02** Add a `describedBy` link (or create the Source Document first) for 2 concrete offerings with no source link: [[Fronius Charge & Connect]], [[Stryten inCOMMAND]].
4. **F-04** Consolidate the dated update blocks in 4 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 15 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
