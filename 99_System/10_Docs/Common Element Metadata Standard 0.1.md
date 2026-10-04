---
element_type: document
status: active
scope:
  kind: cross-product
created: 2026-10-04
related_backlog:
  - [[80_Decisions and Planning/Knowledge Base Backlog#KB-003]]
  - [[80_Decisions and Planning/Legacy Content Inventory and Migration Map 0.1#MIG-002]]
  - [[80_Decisions and Planning/Legacy Content Inventory and Migration Map 0.1#MIG-004]]
---

# Common Element Metadata Standard 0.1

## Purpose

This standard defines a common metadata contract for canonical PosiBattery vault elements. It makes element identity, type, scope, lifecycle, evidence, relationships, uncertainty, and validation status visible and consistently queryable.

It is an adoption standard, not a bulk-conversion instruction. New canonical elements should use it when created. Existing notes are updated only in an approved, controlled migration or maintenance batch.

This document does not modify the current schemas, templates, or legacy notes. A later implementation step must reconcile this standard with `99_System/03_Schemas` and `99_System/05_Templates` before automated or broad adoption.

## Design principles

- One stable identity has one canonical note.
- Metadata identifies and scopes a note; the body contains explanation, claims, evidence synthesis, and decision-relevant detail.
- Folder location is a canonical storage decision, not a substitute for type, scope, or relationship semantics.
- Use typed relationships for material model claims; use ordinary links for navigation or incidental reference.
- Preserve uncertainty, conflict, and provenance rather than silently converting external material into asserted fact.
- Keep the common core small. Add type-specific fields only where they add query, validation, or traceability value.
- Use stable identifiers and controlled values where available. Do not introduce competing field names without a schema decision.

## Common core

Every new canonical element should use the following core fields unless the element type makes a field inapplicable.

```yaml
---
id: <stable-id>
element_type: <controlled-element-type>
title: <canonical-human-readable-name>
status: <lifecycle-status>
scope:
  kind: <scope-kind>
  applies_to: []
aliases: []
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### Core fields

| Field | Required | Meaning | Rules |
| --- | --- | --- | --- |
| `id` | Yes for new canonical elements | Stable vault identity | Never reuse an ID for a different identity; do not derive meaning solely from its sequence |
| `element_type` | Yes | Controlled model type | Use an existing controlled type whenever possible; proposed new types require schema review |
| `title` | Yes | Canonical human-readable name | Normally matches the note title; retain aliases separately |
| `status` | Yes | Lifecycle/evidence maturity | Use controlled status values below |
| `scope.kind` | Yes | Reuse and applicability classification | Use one controlled scope kind below |
| `scope.applies_to` | When applicable | Product, family, platform, market, or context references | Use canonical links; leave empty only when genuinely universal or not yet known |
| `aliases` | Recommended | Alternate names, product codes, abbreviations, former names | Do not create duplicate notes solely for aliases |
| `tags` | Optional | Discovery aids | Tags do not replace element type, scope, or typed relationships |
| `created` | Yes | Initial record date | ISO date |
| `updated` | Yes | Last material update date | ISO date; update on substantive changes |

## Controlled scope kinds

| Scope kind | Meaning | Canonical placement guidance |
| --- | --- | --- |
| `product-specific` | Applies to one identified product or configuration | Product, architecture, capability, or use domain associated with that product |
| `product-family` | Shared across a defined family or related variants | Product family or shared architecture/capability domain |
| `platform-shared` | Managed internal platform reused across product families | Product architecture or product capability domain |
| `cross-product` | Applies across multiple products or contexts | Domain folder expressing primary role; link all relevant applications |
| `external-reference` | Reusable external/public concept, taxonomy, or reference pattern | `90_Definitions and Reusable Reference`; evidence stays in `70_Research and Evidence` |

`scope.applies_to` identifies the product, product family, platform, use context, or external domain to which the element applies. A generic technology name does not establish product-specific scope.

## Lifecycle and evidence status

Use one `status` value for the current working maturity of the element.

| Status | Meaning |
| --- | --- |
| `draft` | Created but incomplete; not ready for model reliance |
| `provisional` | Plausible modeled content based on limited, indirect, or not-yet-reconciled evidence |
| `supported` | Has traceable external evidence appropriate to the claim, but has not been independently validated for internal use |
| `validated` | Has been checked against approved internal evidence, test, review, or decision criteria |
| `disputed` | Material evidence or interpretations conflict; conflict must be visible in the note |
| `superseded` | Retained for traceability but replaced by a newer element, revision, or decision |
| `archived` | Retained as historical context and not active in the current model |

Status describes knowledge maturity, not product availability, commercial status, or source-document publication state. Those belong in type-specific fields when needed.

## Evidence and uncertainty block

Add the following block when an element contains externally derived claims, design assertions, comparison results, or decision-relevant conclusions.

```yaml
evidence:
  basis: external-public | internal | mixed | inferred | none
  confidence: low | medium | high
  source_records: []
  last_reviewed: YYYY-MM-DD
uncertainty:
  assumptions: []
  open_questions: []
  conflicts: []
```

| Field | Meaning |
| --- | --- |
| `evidence.basis` | Principal evidence origin; `mixed` must distinguish internal and external sources in the body |
| `evidence.confidence` | Confidence in the specific note’s material claims, not a general statement of quality |
| `evidence.source_records` | Canonical links to source-record notes; avoid URLs here when a source record exists |
| `evidence.last_reviewed` | Date material evidence was last assessed |
| `uncertainty.assumptions` | Explicit working assumptions |
| `uncertainty.open_questions` | Unresolved questions needed to complete or verify the element |
| `uncertainty.conflicts` | Links to conflicting evidence, claims, or decisions; never silently collapse a conflict |

For short elements, the lists may be empty. Do not use empty fields as evidence that no uncertainty exists; state material uncertainties in the note body as well.

## Relationship metadata

Use typed relationships for claims that materially affect traceability, architecture, decisions, verification, or evidence. The existing relationship schema remains authoritative until the relationship-vocabulary review is completed.

Recommended interim structure:

```yaml
relationships:
  - type: <controlled-relationship-type>
    target: [[Canonical Target Note]]
    status: asserted | inferred | supported | validated | disputed
    evidence: []
    applicability: <optional context>
    notes: <optional concise qualifier>
```

Rules:

- Each relationship states one directional claim from the current element to a target element.
- Use the relationship type exactly as controlled by the active relationship schema or later vocabulary guide.
- Keep relationship status independent when it differs from the note’s overall status.
- Link source records in `evidence` when the relationship itself needs support.
- Use `inferred` only when the rationale is documented in the note body.
- Use `disputed` when sources or interpretations conflict; preserve alternatives and link the conflict.
- Do not use relationship metadata merely to duplicate all ordinary backlinks.

## Type-specific extensions

The following extensions are recommended. They are not a license to create new field names indiscriminately; they establish the fields that should be standardized during schema/template reconciliation.

### Product and offering

```yaml
product_class: product_category | product_type | product_family | product_variant | specific_offering
manufacturer: []
portfolio_owner: []
commercial_status: active | legacy | announced | discontinued | unknown
```

### Stakeholder, actor, and organization

```yaml
stakeholder_class: person | role | organization | organization_type
organization_role: customer | user | operator | buyer | maintainer | supplier | partner | competitor | regulator | standards_body | other
```

### Customer need

```yaml
need_class: outcome | pain_point | constraint | job_to_be_done | demand_signal
need_holder: []
priority: unknown | low | medium | high | critical
```

### Function and capability

```yaml
capability_class: function | requirement | property | state | failure_mode | verification
function_level: mission | primary | supporting | atomic | unknown
```

### Architecture and design

```yaml
design_class: system_architecture | subsystem | interface | component | implementation_pattern | design_trade
implementation_scope: product_specific | platform_shared | external_reference | unknown
```

### Metric, property, and comparison criterion

```yaml
measure_class: metric | property_definition | comparison_criterion
value_type: numeric | categorical | boolean | text | compound
unit: <controlled unit when applicable>
measurement_method: <method or source basis>
```

A `comparison_criterion` may aggregate several metrics or categorical attributes and must state its evaluation method and source/date context in the body. Commercial fields such as price and warranty are time-, geography-, and offering-specific; do not treat them as stable engineering properties.

### Source record and research synthesis

```yaml
source_class: web_page | datasheet | brochure | manual | standard | article | database | other
source_url: <canonical-url>
published_or_revision: <date-or-revision>
accessed: YYYY-MM-DD
source_stability: stable | unstable | access_controlled | unknown
```

Source records remain in `70_Research and Evidence`. A research-synthesis note should link to source records and to canonical model elements; it should not replace either.

### Decision and planning item

```yaml
decision_class: decision | assumption | issue | conflict | plan | backlog_item
priority: P0 | P1 | P2 | P3 | unknown
owner: []
due: YYYY-MM-DD
```

## Note-body minimums

Metadata alone is not a usable element. Each canonical note should have body sections appropriate to its type.

| Element type | Minimum body content |
| --- | --- |
| Product | Definition/scope, identity, market or use context, variants/relationships, evidence and open questions |
| Actor/stakeholder | Role, goals/responsibilities, operating context, needs/relationships, evidence |
| Customer need | Need statement, holder/context, outcome/constraint, rationale/evidence, linked requirements/functions |
| Function | Intent, inputs/outputs or triggering context, hierarchy, related requirements/designs, evidence |
| Design | Scope, intent, interfaces/parts, alternatives/tradeoffs, related functions/products, evidence |
| Metric/property | Definition, value type/unit, measurement/comparison method, applicability, source/date conditions |
| Source record | Original URL, source identity/revision, access date, relevance, extraction status, omitted information |
| Research synthesis | Question/scope, evidence summary, conclusions, conflicts/uncertainties, linked canonical elements |
| Decision/plan | Context, options, rationale, impact, unresolved risks, follow-up work |

## Relationship-first traceability

The intended model path remains:

```text
Stakeholder → Need → Use / Operation → Requirement → Function → Architecture / Design → Product → Metric / Verification
```

No element must use every relationship in this chain. The goal is sufficient traceability for a meaningful decision or engineering discussion, not artificial link density. Missing links should be visible as a model gap when they matter.

## Adoption sequence

1. Reconcile this standard with existing element types, local-model schema, relationship schema, and templates.
2. Publish the relationship-vocabulary guide, including directionality and permitted source/target types.
3. Update templates and validation scripts only after the reconciled schema is approved.
4. Use the reconciled metadata standard for all newly created canonical elements.
5. Apply metadata to legacy notes only as they are reviewed or moved in controlled batches.
6. Record exceptions, schema conflicts, and potentially valuable extensions in the canonical backlog.

## Change history

| Version | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-10-04 | Initial common core, scope/status/evidence/relationship blocks, type extensions, and adoption sequence |
