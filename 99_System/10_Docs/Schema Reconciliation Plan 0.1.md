---
element_type: document
status: active
scope:
  kind: cross-product
created: 2026-10-04
related_backlog:
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-003]]
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-004]]
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-009]]
---

# Schema Reconciliation Plan 0.1

## Purpose

This plan defines how to reconcile the existing PosiBattery model controls with the approved documentation standards before modifying schemas, templates, scripts, or canonical elements. It is a planning artifact only.

The following existing controls remain authoritative until a later approved implementation change updates them:

- `99_System/03_Schemas/element-types.yaml`
- `99_System/03_Schemas/local-model.yaml`
- `99_System/03_Schemas/relationships.yaml`
- `99_System/03_Schemas/authors.yaml`
- `99_System/03_Schemas/business-relationships.provisional.yaml`
- `Definitions/Properties/` property vocabulary
- `99_System/05_Templates/` templates
- `99_System/check-dependencies.py` and `99_System/check-names.py`

This document does not change those controls.

## Inputs

| Input | Role in reconciliation |
| --- | --- |
| [[99_System/10_Docs/Canonical Vault Top-Level Taxonomy 0.1]] | Target folder architecture and scope/placement principles |
| [[99_System/10_Docs/Common Element Metadata Standard 0.1]] | Proposed common element metadata, lifecycle, evidence, uncertainty, and type extensions |
| [[99_System/10_Docs/Relationship Vocabulary Usage Guide 0.1]] | Proposed relationship usage, directionality, traceability, and ambiguity register |
| `element-types.yaml` | Existing controlled element-type definitions |
| `local-model.yaml` | Existing frontmatter and local-model conventions |
| `relationships.yaml` | Existing controlled relationship definitions |
| `Definitions/Properties/` | Legacy property definitions and relationship documentation |
| `99_System/05_Templates/` | Authoring starting points for current element types |
| Integrity scripts | Existing automated dependency and naming controls |

## Reconciliation principles

- Preserve current controls and existing content until an approved migration/implementation batch changes them.
- Prefer extension, aliasing, or explicit deprecation over silent replacement of fields, types, or relationships.
- Do not create parallel vocabularies for the same concept. Resolve synonyms by selecting one canonical name and recording any accepted legacy alias.
- Treat relationship direction and endpoint constraints as controlled semantics, not author preference.
- Keep schema requirements proportional to element maturity; legacy elements must not be made invalid merely because a newly introduced field is absent.
- Support incremental adoption: new canonical notes first, then controlled legacy migration.
- Preserve source traceability, model links, and history through every change.

## Proposed canonical metadata groups

The following groups from the metadata standard must be compared with the existing `local-model.yaml` and element-type definitions before implementation.

| Group | Candidate fields | Reconciliation question |
| --- | --- | --- |
| Identity | `id`, `element_type`, `title`, `aliases` | Which existing fields already serve each purpose, and what is the migration/alias rule? |
| Lifecycle | `status`, `created`, `updated` | Are controlled values, timestamps, and legacy status semantics aligned? |
| Scope | `scope.kind`, `scope.applies_to` | Can scope be represented as nested YAML, or must the local model use flat fields? |
| Discovery | `tags` | How do existing tags interact with controlled element types and file classes? |
| Evidence | `evidence.basis`, `confidence`, `source_records`, `last_reviewed` | What fields/relationship records already capture provenance, and which are missing? |
| Uncertainty | `assumptions`, `open_questions`, `conflicts` | Should these be lists of links, IDs, or plain text with optional links? |
| Relationships | typed relationship records | Can the current schema validate relationship arrays, target links, direction, maturity, and evidence? |

## Element-type reconciliation

The repository currently includes templates for actors, artifacts, designs, diagrams, documents, failure modes, functions, flows, info, issues, item flows, objects, people, plans, ports, procedures, property definitions, requirements, results, setups, state machines, states, steps, use cases, and verification.

The existing element-type schema must be reviewed against the following target classification dimensions:

| Target classification | Existing likely coverage | Reconciliation action |
| --- | --- | --- |
| Product category/type/family/variant/offering | May be represented through object/info/artifact or local conventions | Decide whether `product` becomes a controlled type, subtype, or type-extension field |
| Stakeholder/actor/organization/organization type | Actor, person, object, and business relationship concepts exist | Align actor/person/organization boundaries and role fields |
| Customer need | Existing local conventions may use requirement, issue, or info | Decide whether need is a first-class controlled type or a type extension |
| Function/capability | Function, requirement, property definition, state, failure mode, verification exist | Align `capability_class` with current formal types; avoid duplicates |
| Architecture/design | Design, artifact, port, item flow, functional flow, diagram exist | Define architecture/subsystem/interface/component extensions and endpoint constraints |
| Metric/property/comparison criterion | Property definition and result exist; metric likely has local conventions | Define controlled distinction among measured metrics, property definitions, and comparison criteria |
| Source record/research synthesis | Document and info types exist | Define source/research subtypes and provenance requirements |
| Decision/planning item | Plan and issue types exist | Define decision, assumption, conflict, backlog-item extensions without duplicating issue semantics |

## Relationship reconciliation

The relationship guide uses a focused core, while the existing schema/property vocabulary contains a broader set of terms. Reconciliation must build a controlled matrix with the following columns before editing `relationships.yaml`:

| Field | Purpose |
| --- | --- |
| Canonical relationship name | One authoritative spelling |
| Legacy aliases/synonyms | Existing names that map to the canonical term, if any |
| Direction | Required source → target meaning |
| Allowed source element types | Permitted origin types |
| Allowed target element types | Permitted target types |
| Inverse/query label | Readable inverse for views/documentation |
| Cardinality | One-to-one, one-to-many, many-to-many, or constrained |
| Evidence expectation | Required, recommended, optional, or prohibited |
| Status support | Whether relationship maturity/status applies |
| Scope/applicability support | Whether a contextual qualifier is allowed/required |
| Migration handling | Keep, normalize, deprecate with alias, split, or merge |

### High-priority relationship decisions

| Topic | Terms involved | Required decision |
| --- | --- | --- |
| Need traceability | `hasNeed`, `arisesIn`, `drives`, `satisfies` | Endpoint types, direction, and relationship between needs, requirements, functions, and products |
| Design realization | `hasDesign`, `realizedBy`, `satisfies`, `hasPart` | Product/design/function semantics and permitted nesting |
| Interface/flow modeling | `interfaces`, `exchanges`, `transmits`, `receives`, `hasPort`, `hasFlow` | When to use direct interaction versus port and flow elements |
| Hierarchy | `hasChild`, `hasPart`, `subtypeOf`, `optionOf` | Structural, taxonomic, and configuration rules |
| Evidence/provenance | `supports`, `contradicts`, `describes`, `derivedFrom`, `references` | Claim-level evidence pattern and source-record requirements |
| Governance/lifecycle | `supersedes`, `copyOf`, `equals`, `conflictsWith` | Identity, duplication, revision, archival, and conflict behavior |
| Requirement/verification | `drives`, `refines`, `tracesTo`, `satisfies`, `verifies` | Formal traceability and verification-result direction |

## Template reconciliation

Templates should be updated only after common fields and controlled values are approved in schemas. For each existing template, determine:

1. Applicable common-core fields.
2. Required type-specific extension fields.
3. Minimum body sections.
4. Permitted relationship types and common relationship examples.
5. Evidence and uncertainty expectations.
6. Legacy/template compatibility and migration behavior.

### Initial template priority

| Priority | Templates | Reason |
| --- | --- | --- |
| P0 | Actor, Function, Design, Requirement, Property Definition, Document, Plan, Verification | Directly support early migration and traceability chain |
| P1 | Artifact, Object, Person, Procedure, Use Case, Result, State, Failure Mode, Port, flows | Needed for richer model development |
| P2 | Diagram, Setup, Step, State Machine, Info, Freestyle, modelCheck | Supporting/modeling utility templates |

## Validation and script impacts

Existing integrity scripts currently check names and dependencies. Before extending them, define a compatibility-aware validation profile.

| Check category | Initial intent | Legacy handling |
| --- | --- | --- |
| File naming | Verify canonical names and naming rules | Report-only first; do not fail legacy names without an approved migration rule |
| Dependencies/links | Detect broken links and missing referenced targets | Preserve existing behavior; add path-move checks for migration batches |
| Required metadata | Verify common core on newly created/adopted notes | Exempt legacy notes until a migration/adoption marker is present |
| Controlled values | Validate element type, scope, status, and relationship types | Warn first; enforce only after templates/schema are updated |
| Relationship endpoints | Validate allowed source/target types and required qualifiers | Introduce after relationship matrix approval |
| Evidence completeness | Identify material claims/relationships lacking source support | Report-only quality signal, not a hard failure initially |
| View artifacts | Identify Bases/Canvases that reference moved or missing paths | Add before direct migration batches |

No script should silently rewrite notes, relationships, IDs, or links. Automated changes require separate reviewable write actions.

## Phased implementation

### Phase 1 — Analysis and decision capture

- Read current schema files, selected property notes, and P0 templates in detail.
- Produce the field and relationship reconciliation matrix.
- Record every conflict, duplicate term, uncertain mapping, and proposed decision in a review document.
- Do not alter controls.

### Phase 2 — Controlled schema proposal

- Draft versioned schema changes for new fields, controlled values, aliases/deprecations, and relationship endpoint rules.
- Draft matching template changes.
- Identify validation-script changes as report-only versus enforceable.
- Review exact diffs before approval.

### Phase 3 — Pilot implementation

- Apply approved schema/template updates.
- Create or adopt a small representative set of notes: one actor, one need, one function, one design, one metric, and one source record.
- Run checks and evaluate usability in Obsidian views/Bases.
- Record exceptions and revise the proposal before broad rollout.

### Phase 4 — Controlled migration

- Migrate direct-candidate domains in small batches using the approved metadata and relationship rules.
- Update Bases, Canvases, README navigation, and path-sensitive links within the same batch.
- Run dependency, name, metadata, and view checks.
- Record batch results, regressions, and deferred work.

### Phase 5 — Classification-first domains and cleanup

- Classify and migrate Product Designs, Organizations, Research, Definitions, and complex Product hierarchy content.
- Process downloaded sources individually; delete only in separately approved cleanup batches after provenance capture.
- Add relationship-quality and evidence-completeness reporting.

## Deliverables before schema modification

The following must be available and reviewed before changing system controls:

- Field reconciliation matrix: current field → target field → disposition.
- Element-type reconciliation matrix: current type → target type/extension → disposition.
- Relationship reconciliation matrix with endpoint/direction rules.
- Template change matrix for P0 templates.
- Validation impact matrix, including compatibility/exemption rules.
- Pilot-element selection and acceptance criteria.
- Explicit conflict and decision register.

## Risks and controls

| Risk | Control |
| --- | --- |
| Breaking legacy Notes, Bases, or Canvases | Documentation-first, controlled batches, view/path validation, and no bulk rewrites |
| Creating parallel metadata vocabulary | Reconciliation matrices, canonical naming decision, alias/deprecation policy |
| Treating external evidence as validated internal fact | Separate status/evidence fields and explicit source linkage |
| Over-modeling simple notes | Common core remains small; type-specific fields are applied only when useful |
| Making legacy content appear invalid | Compatibility profile and migration/adoption markers |
| Losing relationship meaning during moves | Preserve links, record direction/endpoint rules, and run post-migration checks |
| Premature source deletion | Separate source-record/provenance capture and explicit cleanup approval |

## Change history

| Version | Date | Change |
| --- | --- |
| 0.1 | 2026-10-04 | Initial reconciliation scope, matrices, implementation phases, and compatibility controls |
