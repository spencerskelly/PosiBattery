# Source Documents

## Purpose

This folder contains curated metadata notes for authoritative external documents used as evidence in the vault. A source-document note identifies a specific brochure, data sheet, guide, flyer, or similar primary document and provides a stable link target for product, organization, and research claims.

## Current source records

- [[Document - ACT Battview Sheet (2023)]]
- [[Document - ACT Quantum 3 Sheet (2024)]]
- [[Document - ACT Quantum Charger Sheet (2023)]]
- [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]]
- [[Document - EnerSys iQ Mini Flyer (GLOB-EN-FLY-IQM 0924)]]
- [[Document - Lester Summit Series II 1425 W Data Sheet (06-2023)]]
- [[Document - Power Designers PowerTrac 3 Specification (PDS-PT3 11-2025)]]
- [[Document - Prestolite BID and BID with Ah Accumulator Data Sheet 1336 (08-18)]]

## Navigation

- `BASE_all_Source Documents.base` — view across all curated source records.
- `BASE_local_Source Documents.base` — locally scoped source-record view.

## Related areas

- [[README_Reference Files|Reference Files]] — kept copies of source files with no recoverable web address.
- [[README_Organizations|Organizations]] — entities referenced by source documents.
- [[README_Products|Products]] — products and categories supported by the evidence.
- [[README_Research|Research]] — synthesis, matrices, audits, conflicts, and future work derived from sources.
- [[README_Definitions|Definitions]] — rules for note structure, source sections, and traceability properties.

## Maintenance

Create a source-document note when an external item becomes evidence for a durable claim. Capture enough provenance to distinguish document version, publisher, date, and identity. Keep original files in Downloads or their approved storage location; use this folder for the curated record and its links.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 503 / 503 |
| Typed model notes (incl. subfolders) | 502 (Document 488, Info 14) |
| Status | Draft 502 of 502 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 0 / 32 of 502 |
| Tags | 166 distinct, 79 used once |
| Size | median 1,667 bytes; largest [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]] (8 KB) |
| Non-markdown files | .base 2, .canvas 1 |

### Analysis

- 502 typed notes: 488 Document and 14 Info.
- YAML provenance is strong: `sourceClass` and `sourceUrl` on 488 of 488, `accessed` on 471, `sourceRevision` on 60. The 2026-10-12 runtime handoff still carries the 2026-10-05 line that 8 curated Source Documents lack structured provenance; the observed state supersedes it (F-14).
- Evidence tier is stored twice: every Document has an 'Evidence tier' line in the body and 386 also carry a tag. The tag has two spellings (`tier-T1` style on 356 Documents, `tier-1` style on 30), so a Base filter on one spelling misses the other. No tag disagrees numerically with its body line (383 checked); 102 Documents have the body line only (F-02, F-12).
- 153 of 488 Document names embed the retrieval date (for example '(retrieved 2026-10-14)'), so a re-fetch produces a new name, while `accessed` already holds the date.
- 14 Info notes sit among the Documents.
- Source Documents are the evidence layer for the whole vault: every Document has `describes` and an inbound link.

### Key links

- [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]] — 21 inbound links
- [[Document - Midac Motive Power Integrated Solutions Catalogue (01-2022)]] — 21 inbound links
- [[Document - CARB LCFS Guidance 25-01 Forklift Fueling Reporting (2025-10)]] — 17 inbound links
- [[Document - PosiCharge BMID FAQ]] — 16 inbound links
- [[Document - GNB Motive Power Overview (2021-08)]] — 14 inbound links
- [[Document - Stryten M-Series Lineup Sheet (09-2024)]] — 14 inbound links

### Improvement steps

1. **F-02** Choose one home for tier and one tag spelling, then backfill the 102 Documents with the body line only and normalize the 30 `tier-#` tags.
2. **F-13** Base: Documents by `sourceClass`, tier, `accessed` age, and number of notes each supports.
3. **F-14** Run `check-links.py` from a machine with internet access to verify the cited URLs (the workspace network is allow-listed).
