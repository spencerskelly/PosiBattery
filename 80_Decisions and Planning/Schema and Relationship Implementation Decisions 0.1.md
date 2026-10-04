---
title: Schema and Relationship Implementation Decisions 0.1
document_type: Decision Record
status: Proposed
version: 0.1
date: 2026-10-04
scope: Documentation-only; no schema, template, taxonomy, or legacy-content changes are authorized by this record.
related:
  - "[[99_System/10_Docs/Schema Reconciliation Matrix 0.1]]"
  - "[[99_System/10_Docs/Schema Reconciliation Plan 0.1]]"
  - "[[99_System/10_Docs/Relationship Vocabulary Usage Guide 0.1]]"
  - "[[99_System/10_Docs/Common Element Metadata Standard 0.1]]"
  - "[[99_System/10_Docs/MDSE Modeling Ruleset 1.23]]"
  - "[[99_System/10_Docs/Canonical Vault Top-Level Taxonomy 0.1]]"
  - "[[99_System/10_Docs/MDSE Vault File and Folder Structure 0.8]]"
  - "[[80_Decisions and Planning/Knowledge Base Backlog]]"
  - "[[80_Decisions and Planning/Legacy Content Inventory and Migration Map 0.1]]"
approval_required_before:
  - Schema updates
  - Template updates
  - Bulk metadata normalization
  - Legacy-content migration
  - Automated relationship rewrites
---

# Schema and Relationship Implementation Decisions 0.1

## Purpose

This record converts the findings in the Schema Reconciliation Matrix 0.1 into an implementation decision framework. It establishes what is approved in principle, what remains deliberately unresolved, the sequencing of later work, and the controls required before any schema, template, or content change is made.

This is a documentation-only record. It does not modify the current vault schema, templates, folder taxonomy, note metadata, relationship fields, or legacy-content placement.

## Decision Summary

| ID | Decision | Status | Implementation Effect |
|---|---|---:|---|
| D-01 | Preserve the canonical top-level taxonomy as the governing location model for new and migrated content | Proposed | No folder moves are authorized by this record |
| D-02 | Use the Common Element Metadata Standard as the baseline for shared metadata fields | Proposed | No metadata fields are added, renamed, or normalized by this record |
| D-03 | Use the Relationship Vocabulary Usage Guide as the authoritative semantic source for relationship predicates | Proposed | No link field conversion or relationship rewrite is authorized |
| D-04 | Treat the Schema Reconciliation Matrix as the controlled source for mapping legacy concepts to canonical concepts | Proposed | No migration mapping is executed |
| D-05 | Separate semantic decisions from mechanical migration work | Proposed | Schema decisions must be approved before template or bulk-content changes |
| D-06 | Preserve legacy notes and evidence until their mapped destination, provenance, and disposition are verified | Proposed | No deletion or silent replacement of legacy content is permitted |
| D-07 | Implement changes through reviewable, reversible batches with validation evidence | Proposed | No implementation batch begins without an approved change specification |
| D-08 | Record unresolved relationship ambiguity as an explicit decision or backlog item rather than inferring a predicate | Proposed | Ambiguous links remain unchanged until resolved |

## Governing Principles

### 1. Canonical model before migration

The canonical taxonomy, metadata standard, modeling ruleset, and relationship vocabulary govern future-state design. Legacy note structures do not become canonical merely because they already exist.

Where a legacy construct conflicts with the canonical model, the conflict must be recorded and resolved explicitly. Existing content may be retained as historical evidence, but it must not silently establish a parallel schema.

### 2. Semantic stability before mechanical change

No bulk rename, metadata normalization, link rewrite, template update, or folder migration should occur until the intended meaning is approved.

The implementation sequence is therefore:

1. Approve the decision record and any linked unresolved decisions.
2. Publish controlled schema and relationship specifications.
3. Update templates and creation guidance.
4. Pilot metadata and relationship migration on a limited, representative set.
5. Validate results against the matrix and methodology rules.
6. Execute reviewed migration batches.
7. Retire or archive superseded structures only after traceability is confirmed.

### 3. Controlled relationship vocabulary

Relationships must use the approved vocabulary and direction rules defined in the Relationship Vocabulary Usage Guide. A relationship is not sufficiently defined by a generic wiki-link alone when its meaning is material to traceability, decision-making, or model interpretation.

Relationship entries should be explicit enough to identify:

- Subject element.
- Approved predicate.
- Object element.
- Directionality.
- Any role, qualifier, or source context necessary to avoid ambiguity.

Where inverse relationships are represented, they must remain semantically compatible with the authoritative direction rule rather than creating competing interpretations.

### 4. Metadata is shared infrastructure

Shared metadata fields serve retrieval, traceability, lifecycle control, and automation. Metadata changes therefore require more care than local note-formatting changes.

New common fields, field renames, controlled values, cardinality changes, or changes to requiredness must be treated as schema changes and require approval before application.

### 5. Preserve evidence and provenance

Legacy content remains intact until all of the following are verified:

- A canonical destination or retained-status decision exists.
- The migration map identifies the content's treatment.
- Source provenance is retained.
- Any transformation is traceable to the prior content.
- Review confirms that no required information or decision context was lost.

Conflicts, duplicates, and uncertainty must be retained as explicit migration findings. They are not to be silently deleted or merged.

## Proposed Schema Decisions

| Area | Proposed decision | Rationale | Deferred implementation work |
|---|---|---|---|
| Top-level organization | Retain the canonical numbered taxonomy as the future-state vault organization | Maintains stable navigation and separates products, architecture, capabilities, operations, needs, ecosystem, evidence, decisions, reusable reference, and system governance | Folder alignment and legacy relocation |
| Common metadata | Adopt the Common Element Metadata Standard as the baseline shared-field model | Enables consistent discovery, lifecycle control, and automation across element types | Template changes, metadata backfill, controlled-value normalization |
| Element-specific properties | Keep specialized fields local to the relevant element type unless repeated cross-domain use justifies elevation to common metadata | Prevents the common schema from becoming a dumping ground for type-specific attributes | Field inventory and promotion criteria |
| Relationship representation | Use the relationship vocabulary as the semantic authority; use links as references, not as a substitute for an undefined predicate | Preserves interpretable model semantics and traceability | Relationship-field structure, inverse-link policy, existing-link conversion |
| Source and evidence links | Maintain provenance links between assertions, evidence, and source material where decisions or claims depend on evidence | Supports auditability and avoids detaching conclusions from their basis | Evidence-link normalization and legacy-source migration |
| Status and lifecycle | Apply lifecycle/status handling according to the metadata standard and modeling ruleset | Separates active canonical content from draft, deprecated, legacy, or archival material | Status vocabulary rollout and legacy classification |
| Templates | Templates must reflect only approved canonical schema decisions | Avoids creating new notes using an unapproved or unstable model | Template redesign and validation tests |

## Relationship Implementation Decisions

| Topic | Proposed decision | Control |
|---|---|---|
| Predicate selection | Select the narrowest approved predicate that expresses the intended meaning | Do not use a generic relation when a defined predicate exists |
| Directionality | Record relationships in the vocabulary's authoritative direction | Do not create both directions unless the model explicitly requires reciprocal representation |
| Inverses | Derive or display inverses only where the relationship guide defines an unambiguous inverse | Avoid manually maintained duplicate assertions where synchronization risk exists |
| Multiplicity | Do not infer cardinality from a single existing note or example | Capture cardinality only when supported by the applicable model rule or explicit decision |
| Relationship evidence | Link decision-critical relationships to the supporting source, decision, or rationale | Preserve traceability for high-impact claims |
| Ambiguity | Leave ambiguous legacy links unchanged and create a backlog/decision item | No automated predicate assignment based solely on note titles or folder placement |
| Cross-domain links | Use approved predicates across taxonomy areas rather than duplicating facts into multiple notes | Maintain a single authoritative assertion with navigable references |

## Reconciliation Outcomes by Category

| Category | Current treatment | Future-state decision | Approval needed before action |
|---|---|---|---|
| Canonical structures already aligned | Retain | No structural change unless an identified defect is approved | Only for any corrective change |
| Legacy content with clear canonical mapping | Preserve pending migration | Migrate in reviewed batches with provenance retained | Migration batch specification |
| Legacy content with partial mapping | Preserve and classify as unresolved | Resolve semantic mismatch before migration | Specific decision record or matrix update |
| Duplicate or overlapping content | Preserve both until authority is determined | Identify authoritative record and retain conflict history | Consolidation decision |
| Undefined metadata fields | Do not normalize | Evaluate against common metadata standard | Schema change decision |
| Undefined relationship semantics | Do not rewrite | Map to approved predicate or create a vocabulary proposal | Relationship decision |
| Deprecated structures | Do not delete | Mark/retain until replacement and traceability are confirmed | Retirement decision |

## Implementation Gates

No implementation work is authorized until the relevant gate is satisfied.

| Gate | Required evidence | Permitted outcome |
|---|---|---|
| G1: Decision approval | Approval of this record and any linked unresolved decisions | Prepare controlled implementation specifications |
| G2: Schema specification approval | Field definitions, ownership, type, cardinality, requiredness, controlled values, migration rules | Update schemas and templates in a reviewable change |
| G3: Relationship specification approval | Predicate definitions, directionality, inverse handling, examples, and migration rules | Update relationship guidance and pilot relationship conversion |
| G4: Pilot approval | Representative sample, before/after traceability, validation findings, rollback method | Execute limited migration batch |
| G5: Batch approval | Scoped inventory, conflict log, verification checklist, and rollback/retention plan | Execute production migration batch |
| G6: Closure approval | Reconciliation matrix updated with final disposition and residual exceptions | Mark a migration work package complete |

## Required Change Artifacts

Each later schema or migration change must include:

- A unique change identifier and clearly bounded scope.
- The affected element types, files, templates, and relationship predicates.
- Before-and-after definitions or examples.
- Migration logic, including treatment of missing, conflicting, and multi-valued data.
- Validation criteria and expected evidence.
- Rollback or preservation method.
- Explicit handling for conflicts and exceptions.
- Links to the applicable matrix rows, backlog item, and decision record.

## Conflict Handling

The following conditions must be recorded rather than silently resolved:

- Two or more notes assert incompatible values, definitions, ownership, or relationships.
- Legacy terminology maps to more than one canonical concept.
- A canonical concept requires information that is absent from the legacy source.
- A relationship can plausibly use multiple approved predicates.
- A proposed common metadata field duplicates or conflicts with an existing field.
- A note's folder location, metadata type, and semantic content imply different classifications.

For each conflict, record the source notes, the competing interpretations, the decision owner, the selected disposition, and the rationale. Preserve non-authoritative material when it has historical, evidentiary, or traceability value.

## Deferred Work

The following work is intentionally deferred until approval:

- Update or creation of schema definitions.
- Changes to note templates.
- Common metadata field additions, renames, removals, or backfill.
- Controlled-value normalization.
- Relationship predicate migration or inverse-link generation.
- Folder moves or canonical-path migration.
- Legacy-note consolidation, replacement, archival, or deletion.
- Automated scripts or bulk operations affecting documentation content.

## Backlog Additions

The following work items should be maintained in the Knowledge Base Backlog:

| ID | Proposed backlog item | Priority | Dependency |
|---|---|---:|---|
| KB-SR-01 | Approve canonical common-metadata field catalog and field governance | High | D-02 approval |
| KB-SR-02 | Publish controlled relationship predicate catalog with direction and inverse rules | High | D-03 approval |
| KB-SR-03 | Define element-type schema specifications and template mapping | High | KB-SR-01 |
| KB-SR-04 | Build legacy-to-canonical migration work packages from the migration map | High | D-04 approval |
| KB-SR-05 | Create a representative migration pilot and validation checklist | Medium | KB-SR-03, KB-SR-04 |
| KB-SR-06 | Define duplicate/conflict-resolution register and authority-selection criteria | Medium | D-06, D-08 approval |
| KB-SR-07 | Define automated validation rules for required metadata, controlled values, and relationship predicates | Medium | KB-SR-01, KB-SR-02 |
| KB-SR-08 | Define retirement criteria for deprecated templates, structures, and legacy notes | Low | Successful pilot and migration evidence |

## Approval Request

Approval of this record authorizes documentation planning and the preparation of controlled implementation specifications only.

It does not authorize any change to:

- The canonical schema.
- Metadata field definitions or values.
- Templates.
- Relationship data.
- Folder placement.
- Legacy-content disposition.
- Automated migration tooling.

A separate approved change specification is required before each implementation category proceeds.
