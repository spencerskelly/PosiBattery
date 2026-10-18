# Research and Evidence

## Purpose

This is the canonical PosiBattery domain for evidence provenance and research synthesis. It separates acquired source artifacts, curated Source Document records, and analytical research so evidence can be traced without confusing files, source identity, and interpretation.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[PosiBattery Model Organization and Handoff]].

## Evidence layers

### Raw or acquired source artifacts

`Downloads` is the temporary intake area for externally acquired files; [[README_Reference Files|Reference Files]] holds the copies kept long term.

A downloaded file is not, by itself, the canonical evidence record. Files may be duplicated, renamed, superseded, incomplete, or awaiting identity review.

### Source Document records

[[README_Source Documents|Source Documents]] contains curated Document records for specific external sources used as evidence.

These notes preserve source identity and provenance such as publisher, document title, revision/date, URL or file reference, and relevant evidence context. Model and research claims should link to the curated source record when one exists.

### Research synthesis

[[README_Research|Research]] contains analysis, comparison work, evidence registers, landscapes, conflicts, audits, market synthesis, open questions, and prioritized investigation.

Research may interpret multiple sources, but interpretation must remain distinguishable from the underlying evidence.

## Navigation

- `BASE_local_Research and Evidence.base` — direct Markdown contents of this root domain.
- `BASE_all_Research and Evidence.base` — recursive Markdown contents across Source Documents and Research.
- [[CANVAS_Research and Evidence]] — map of the evidence flow.

## Reusable-reference evidence support

When evidence supports a reusable definition, preserve the separation between semantic meaning and source interpretation:

- the reusable definition remains under [[README_Definitions and Reusable Reference|Definitions and Reusable Reference]];
- the curated external-source identity remains in [[README_Source Documents|Source Documents]];
- source comparison, extraction, conflicts, and dated analysis remain in [[README_Research|Research]];
- definitions may link here for provenance, but evidence text should not be copied into the definition merely to make the claim self-contained.

This keeps reusable vocabulary stable while allowing the supporting evidence to evolve independently as sources change.

## Working rule

Use the evidence chain:

`acquired artifact → curated Source Document record → research/model claim`

Do not silently convert vendor language into fact. Preserve conflicting evidence, uncertainty, document identity, and source provenance.

The `Downloads` folder and the root research islands remain transitional inputs governed by later migration/cleanup steps; this step does not move or delete them.

## Related areas

- [[README_Products|Products]] — product claims supported by evidence.
- [[README_Organizations|Organizations]] — organization claims and business relationships.
- [[README_Product Capabilities|Product Capabilities]] — functions, designs, metrics, and other modeled claims.
- [[PosiBattery Architecture Improvement Plan]] — controlled migration and evidence-cleanup sequence.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 1 / 627 |
| Typed model notes (incl. subfolders) | 599 (Document 488, Info 111) |
| Status | Draft 599 of 599 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 33 / 69 of 599 |
| Tags | 290 distinct, 150 used once |
| Size | median 1,882 bytes; largest [[Battery Product Landscape Conflicts and Open Questions]] (213 KB) |
| Untyped notes (no model `type`, excluding READMEs) | 22 |
| Non-markdown files | .base 6, .canvas 3 |

### Subfolders

| Folder | Notes | Abstract | Flags |
| --- | --- | --- | --- |
| [[README_Research|Research]] | 97 | 0 | source-linked 33/97; 67 body-alias; 34 update-log |
| [[README_Source Documents|Source Documents]] | 502 | 0 | source-linked 0/502; 1 body-alias; 14 update-log |

### Analysis

- Typed notes: 488 Document, 111 Info. Untyped notes: 22 raw research files without frontmatter (Cost Drivers 12, EMS 4, Power Conversion 4, SysML v2 2), about 500 KB (F-09).
- Hubs by inbound links: [[Landscape Evidence and Modeling Conventions]] (176), [[Truck Part Connection Register]] (172), [[Battery Product Landscape Conflicts and Open Questions]] (167).
- Five notes in this domain exceed 100 KB; the conflict register alone is 213 KB (F-07, F-08).
- The taxonomy places backlog, open questions, conflicts and model-quality findings in `80_Decisions and Planning`; this domain holds the Document Wishlist, Investigation Backlog, three conflict logs and several triage registers (F-11).

### Key links

- [[Landscape Evidence and Modeling Conventions]] — 176 inbound links
- [[Truck Part Connection Register]] — 172 inbound links
- [[Battery Product Landscape Conflicts and Open Questions]] — 167 inbound links
- [[Extra Functions Register]] — 62 inbound links
- [[Function and Design Levels]] — 58 inbound links
- [[California Forklift Electrification Regulations Register]] — 54 inbound links

### Improvement steps

1. **F-09** Convert the 22 untyped research files to Info notes or mark them as raw source; decide per file.
2. **F-08** Split or restructure the oversized registers (decision needed).
3. **F-11** Decide whether work-control registers move to 80.
