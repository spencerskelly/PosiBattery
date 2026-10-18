# Decisions and Planning

## Purpose

This is the canonical PosiBattery domain for work control, decisions, assumptions, open questions, conflicts, model-quality findings, migration records, and improvement plans.

Use this area to make unresolved work and governance visible without mixing it into product, architecture, capability, evidence, or reusable-reference content.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[PosiBattery Model Organization and Handoff]].

## Start here

- [[PosiBattery Project Chat to GitHub Traceability Audit 2026-10-08]] — chronological chat-to-commit/model evidence and documented verification limits.
- [[PosiBattery GitHub Capture and Reconciliation Audit 2026-10-08]] — current remote capture, validation, branch/PR reconciliation, and recovery status; see [[PosiBattery Runtime Handoff State]] and [issue #2](https://github.com/spencerskelly/PosiBattery/issues/2).
- [[PosiBattery Architecture Improvement Plan]] — historical 100/100 completed vault-improvement roadmap (2026-10-05), retained for evidence.
- [[Knowledge Base Backlog]] — repository-native backlog for taxonomy, model, evidence, integrity, migration, and validation work.
- [[Schema and Relationship Implementation Decisions 0.1]] — decision framework for schema and relationship changes; currently documentation-only unless later approvals authorize implementation.
- [[Legacy Content Inventory and Migration Map 0.1]] — preserved historical migration baseline; useful for rationale, not current placement authority.
- `PosiBattery Folder Inventory.yaml` — machine-readable folder inventory and architectural-role classification.
- `PosiBattery Navigation Artifact Inventory.yaml` — machine-readable record of transitional, duplicate, stale, and intentional navigation artifacts.

## What belongs here

Examples include:

- active roadmaps and execution plans;
- backlog items and work queues;
- explicit decisions and decision records;
- assumptions requiring validation;
- unresolved classification questions;
- conflicts that must remain visible;
- model-quality findings and integrity follow-up;
- migration inventories and mappings;
- temporary planning artifacts that govern later controlled changes.

Do not use this domain as a substitute for evidence. Claims and source provenance remain under [[README_Research and Evidence|Research and Evidence]].

Do not use planning notes to silently change schema, relationships, or canonical placement. Implementation occurs only through the applicable controlled roadmap or approved change process.

## Navigation

- `BASE_local_Decisions and Planning.base` — direct Markdown planning and decision records.
- `BASE_all_Decisions and Planning.base` — recursive Markdown planning and decision records.
- [[CANVAS_Decisions and Planning]] — curated map of the primary planning and governance records.

## Lifecycle guidance

Keep current plans clearly distinguishable from historical baselines. When a decision or plan is superseded, preserve enough context to recover why it existed and point readers to the newer authority rather than silently deleting the record.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 19 / 19 |
| Untyped notes (no model `type`, excluding READMEs) | 18 |
| Non-markdown files | .yaml 107, .base 2, .canvas 1 |

### Analysis

- 19 markdown notes (18 without a model `type`, 15 of them without any frontmatter), 107 YAML decision records, 2 Bases and 1 Canvas.
- [[PosiBattery Architecture Improvement Plan]] is 265 KB and [[PosiBattery Semantic Linking Completion Plan]] 63 KB, both without frontmatter.
- `showUnsupportedFiles` is false, so the YAML records do not appear in the file explorer; Bases offer only `file.*` properties for non-markdown files, not the content of a record (F-09).
- One YAML record does not parse: `Reusable Definition vs Contextual Architecture Review Step 44 0.1.yaml` (already known in the runtime handoff).
- Work-control content that the taxonomy assigns here (backlog, wishlist, conflicts) mostly lives in `70_Research and Evidence/Research` (F-11).

### Improvement steps

1. **F-09** Decide whether decision records become notes (one per decision, with properties) or stay YAML with a generated index note.
2. **F-11** Decide the home of backlog, wishlist and conflict logs.
3. **F-08** Split the 265 KB plan into a summary plus per-step records.
