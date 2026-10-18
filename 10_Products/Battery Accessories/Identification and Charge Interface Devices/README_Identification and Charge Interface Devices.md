# Identification and Charge Interface Devices

## Purpose

Devices that identify a battery to a charger or carry charge-relevant battery information.

Parent: [[README_Battery Accessories|Battery Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 10 / 10 |
| Typed model notes (incl. subfolders) | 10 (Object 10) |
| Status | Draft 10 of 10 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 8 / 4 of 10 |
| Tags | 12 distinct, 4 used once |
| Size | median 6,780 bytes; largest [[PosiCharge PosiGuard]] (12 KB) |

### Analysis

- 10 notes: 2 abstract category/family notes and 8 concrete offerings. 8 of 8 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 6 of 8 (75%) concrete offerings carry a `describedBy` link; 2 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 7 of 10 (70%) notes `performs` at least one Function; 8 of 10 (80%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 7 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 1 notes carry dated update blocks, 0 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 5 notes list aliases in a body `## Aliases` section and 5 in YAML (F-03).
- Classification: `productClass` is blank on 5 of 10 Objects (F-05).
- Vocabulary and size: 12 distinct tags (4 used once); median note 6,780 bytes, largest PosiCharge PosiGuard (12 KB).

### Key links

- [[PosiCharge PosiGuard]] — 81 inbound links
- [[PosiCharge BMID]] (abstract) — 68 inbound links
- [[PosiCharge Battery Rx]] — 54 inbound links
- [[Crown V-Force BMID]] — 44 inbound links
- [[AMETEK Prestolite Power BID with Ah Accumulator]] — 31 inbound links
- [[Fronius TagID]] — 30 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 5 Objects (the 2 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 2 concrete offerings with no source link: [[Crown V-Force BMID]], [[Fronius TagID]].
3. **F-04** Consolidate the dated update blocks in 1 notes into the current-state sections once a note layout is chosen.
4. **F-03** Move 5 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
5. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
