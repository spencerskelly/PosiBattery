# Operator Assist and Stability

## Purpose

Operator-assist and stability features offered with trucks.

Parent: [[README_Vehicle Accessories|Vehicle Accessories]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 43 / 43 |
| Typed model notes (incl. subfolders) | 43 (Object 43) |
| Status | Draft 43 of 43 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 6 / 6 of 43 |
| Tags | 17 distinct, 5 used once |
| Size | median 2,200 bytes; largest [[Toyota Assist]] (7 KB) |

### Analysis

- 43 notes: 1 abstract category/family notes and 42 concrete offerings. 42 of 42 (100%) concrete offerings link a maker (`madeBy` or `offeredBy`).
- Source links: 6 of 42 (14%) concrete offerings carry a `describedBy` link; 36 have no `describedBy` and link no Document note anywhere (0 of those cite no URL in the body either).
- Function and design links: 39 of 43 (91%) notes `performs` at least one Function; 15 of 43 (35%) have a `hasDesign` link.
- Evidence tier appears only as `(T#)` text in 42 notes; no tier tag or property exists on product notes (F-02).
- `## Notes` works as an append log: 1 notes carry dated update blocks, 2 repeat a bold label inside the note and 0 contain an empty label block (F-04).
- Aliases: 27 notes list aliases in a body `## Aliases` section and 0 in YAML (F-03).
- Classification: `productClass` is blank on 43 of 43 Objects (F-05).
- Vocabulary and size: 17 distinct tags (5 used once); median note 2,200 bytes, largest Toyota Assist (7 KB).

### Key links

- [[Operator Assist and Stability System]] (abstract) — 43 inbound links
- [[Toyota Assist]] — 32 inbound links
- [[STILL Safety Assist]] — 22 inbound links
- [[Yale Reliant Portfolio]] — 21 inbound links
- [[Mitsubishi Integrated Presence System]] — 17 inbound links
- [[STILL Curve Speed Control]] — 16 inbound links

### Improvement steps

1. **F-05** Backfill `productClass` on 43 Objects (the 1 abstract notes are the category/family candidates; classify them first).
2. **F-02** Add a `describedBy` link (or create the Source Document first) for 36 concrete offerings with no source link: [[Cat Presence Detection System]], [[Crown Capacity Data Monitor]], [[Doosan Bobcat Mast Sway Control]], [[Heli Operator Presence Sensing System]], [[Hyster Dynamic Stability System]], [[Jungheinrich curveCONTROL]] and 30 more.
3. **F-04** Merge repeated or empty label blocks in [[Linde Safety Pilot]], [[STILL Safety Assist]].
4. **F-04** Consolidate the dated update blocks in 1 notes into the current-state sections once a note layout is chosen.
5. **F-03** Move 27 body alias lists to YAML `aliases` after `check-names.py` reads YAML aliases.
6. **F-13** Add Base views for this folder: concrete offerings missing a source, by maker, by `productClass`.
