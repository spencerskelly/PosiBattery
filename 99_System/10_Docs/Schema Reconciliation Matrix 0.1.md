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
related_documents:
  - [[99_System/10_Docs/Schema Reconciliation Plan 0.1]]
  - [[99_System/10_Docs/Common Element Metadata Standard 0.1]]
  - [[99_System/10_Docs/Relationship Vocabulary Usage Guide 0.1]]
---

# Schema Reconciliation Matrix 0.1

## Purpose

This matrix records the first reconciliation analysis between existing PosiBattery system controls and the approved taxonomy, metadata, and relationship usage standards. It is an analysis and decision-capture artifact only. It does not modify schemas, templates, scripts, property notes, Bases, Canvases, or model elements.

Existing system controls remain authoritative until a later, separately approved implementation change.

## Sources reviewed

| Control area | Artifacts reviewed |
| --- | --- |
| Element types | `99_System/03_Schemas/element-types.yaml` |
| Local model | `99_System/03_Schemas/local-model.yaml` |
| Relationships | `99_System/03_Schemas/relationships.yaml` |
| P0 templates | Actor, Function, Design, Requirement, Property Definition, Document, Plan, Verification |
| Legacy property vocabulary | `drives`, `satisfies`, `realizedBy`, `verifies`, `hasPart`, `hasChild`, `dependsOn`, `references`, `derivedFrom` |
| Approved standards | Top-level taxonomy, common metadata standard, relationship usage guide, schema reconciliation plan |

## Reconciliation posture

The existing vault has a strong MDSE-oriented foundation. The recommended approach is to retain formal element types and relationship names, then add controlled extensions for scope, evidence, lifecycle, product/business classification, and relationship quality.

Do not replace current MDSE types with folder names or business labels. For example, `function`, `design`, `requirement`, `document`, and `verification` remain formal element types; product class, source class, stakeholder role, metric class, and decision class are controlled extensions.

## Common metadata field matrix

| Target group | Proposed field | Existing coverage | Disposition | Compatibility rule | Later implementation target |
| --- | --- | --- | --- | --- |
| Identity | `id` | Legacy ID/UID conventions exist in property vocabulary and local model | Align | Preserve existing IDs; new canonical notes use one stable ID field after schema decision | Local model schema, P0 templates, validator |
| Identity | `element_type` | Existing element-type schema and template convention | Retain | Existing controlled types remain valid; no bulk rename | Element-type schema, templates |
| Identity | `title` | Filename/note-title convention exists | Add as optional explicit metadata | Note title remains authoritative where field absent; do not require legacy edits | Local model schema, templates |
| Identity | `aliases` | No confirmed common field | Add | Optional list; use to avoid duplicate canonical notes | Local model schema, templates |
| Lifecycle | `status` | Existing status property/convention exists | Normalize | Map legacy values explicitly; do not reinterpret existing status silently | Local model schema, status property, templates |
| Lifecycle | `created`, `updated` | Current conventions may be present in local model | Reconcile | Preserve existing date fields; define canonical ISO names/aliases | Local model schema, templates, validator |
| Scope | `scope.kind` | No confirmed common scope dimension | Add | Optional for legacy notes; required for newly adopted canonical notes | Local model schema, templates |
| Scope | `scope.applies_to` | `appliesTo` relationship/property exists | Keep relationship and add contextual field only if needed | Use typed `appliesTo` for semantic claims; use scope field for note-level applicability | Relationship schema, local model, templates |
| Discovery | `tags` | Existing tags property exists | Retain | Tags remain discovery aids and do not replace types/relationships | Local model schema, templates |
| Evidence | `evidence.basis` | No confirmed normalized field | Add | New/adopted notes only at first; values distinguish external, internal, mixed, inferred, none | Local model schema, templates |
| Evidence | `evidence.confidence` | No confirmed normalized field | Add | Claim/note confidence is distinct from lifecycle status | Local model schema, templates |
| Evidence | `evidence.source_records` | `references`, `derivedFrom`, and document links exist | Reconcile | Use source-record links as canonical provenance; retain legacy links | Relationship schema, templates |
| Evidence | `evidence.last_reviewed` | No confirmed normalized field | Add | Optional initially; use ISO date | Local model schema, templates |
| Uncertainty | `assumptions`, `open_questions`, `conflicts` | Issue/plan/note-body practices exist | Add | Lists may be empty; material uncertainty also remains visible in body | Local model schema, templates |
| Relationships | relationship records | Existing property-per-link model exists | Extend, do not replace | Preserve legacy property links; introduce structured relationship records only after schema/pilot approval | Relationship schema, local model, templates, validator |

## Element-type and extension matrix

| Modeling need | Existing formal type(s) | Recommended extension approach | Proposed placement | Decision status |
| --- | --- | --- | --- | --- |
| Product category/type/family/variant/offering | Object, artifact, info, or current local convention | Keep formal type after pilot decision; add `product_class` extension | `10_Products` | Open: determine preferred formal base type |
| Stakeholder/actor/organization | Actor, person, object | Keep `actor`/`person`; introduce or confirm organization treatment; add stakeholder/organization role extensions | `60_Stakeholders and Ecosystem` | Open: actor vs organization type boundary |
| Customer need | Requirement, issue, info, or local convention | Do not force into requirement; add first-class `need` only if schema review confirms value, otherwise controlled extension | `50_Customer Needs` | Open: formal type decision |
| Function/capability | Function, requirement, property definition, state, failure mode, verification | Retain formal types; add `capability_class` only where view/query value is demonstrated | `30_Product Capabilities` | Aligns conceptually |
| Architecture/design | Design, artifact, port, flow, diagram | Retain types; add `design_class` and `implementation_scope` extensions | `20_Product Architecture` | Aligns conceptually |
| Metric/property/comparison criterion | Property definition, result, info | Retain formal property/result semantics; add `measure_class`, `value_type`, unit/method fields | `30_Product Capabilities` | Open: metric formal type decision |
| Source record/research synthesis | Document, info | Retain document/info; add `source_class` and provenance extensions | `70_Research and Evidence` | Aligns conceptually |
| Decision/assumption/conflict/backlog | Plan, issue, info | Retain plan/issue; add `decision_class`, priority, owner, due extensions | `80_Decisions and Planning` | Aligns conceptually |
| Reusable technical reference | Object, info, property definition, design | Select formal type based on semantic role; add `scope.kind: external-reference` | `90_Definitions and Reusable Reference` | Requires note-level classification |

## Relationship reconciliation matrix

The following is a first-pass mapping. Endpoint restrictions remain provisional until the element-type decisions above are resolved.

| Relationship | Legacy support | Direction proposed | Allowed source categories | Allowed target categories | Evidence expectation | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `hasNeed` | Present in relationship schema; no reviewed legacy property note in this pass | Stakeholder → need | Actor, person, organization | Need | Recommended | Retain; define endpoint rules |
| `arisesIn` | Present in relationship schema; no reviewed legacy property note in this pass | Need → use/operation/context | Need | Use case, procedure, setup, operation/environment | Recommended | Retain; define endpoint rules |
| `drives` | Schema and reviewed property note | Need/constraint/decision → requirement/function/design/plan | Need, requirement, constraint, decision, issue | Requirement, function, design, plan, verification | Recommended | Retain; formalize semantics and endpoints |
| `satisfies` | Schema and reviewed property note | Product/capability/function/design/result → requirement/need | Product, function, design, artifact, verification/result | Requirement, need | Required for material claim | Retain; distinguish from possible contribution |
| `realizedBy` | Schema and reviewed property note | Intent/function/requirement → implementing design/artifact | Function, requirement, design intent | Design, artifact, component, interface | Recommended | Retain; distinguish from `hasDesign` and `hasPart` |
| `verifies` | Schema and reviewed property note | Verification/result → target being evaluated | Verification, result, document | Requirement, function, design, metric/property | Required | Retain; add method/result conventions |
| `measures` | Present in relationship schema; no reviewed legacy property note in this pass | Metric/method → measured target | Metric, property definition, verification | Property, function, requirement, need outcome, product | Required when used for a material metric claim | Retain; define metric formal type and endpoints |
| `supports` | Present in relationship schema; no reviewed legacy property note in this pass | Evidence/source/research → claim/element | Document, research synthesis, result | Element, relationship claim, decision | Required by definition | Retain; define claim-level target representation |
| `contradicts` | Present in relationship schema; no reviewed legacy property note in this pass | Evidence/source/claim → contested claim/element | Document, research synthesis, requirement, decision, result | Element, relationship claim, decision | Required by definition | Retain; define conflict-record pattern |
| `hasPart` | Schema and reviewed property note | Whole → direct constituent | Product, design, artifact, system/object | Product, design, artifact, component, port | Optional | Retain; prohibit use as generic association |
| `hasChild` | Schema and reviewed property note | Parent → immediate controlled child | Any hierarchical element | Same/hierarchical category | Optional | Retain; distinguish from composition and subtype |
| `subtypeOf` | Schema and property vocabulary | Specialized type → general type | Type/category/reference element | Type/category/reference element | Optional | Retain; constrain to taxonomy semantics |
| `optionOf` | Schema and property vocabulary | Option/variant → parent | Product variant, design option | Product family, design | Recommended | Retain; distinguish from mandatory part |
| `hasDesign` | Schema and property vocabulary | Product/system/capability → associated design | Product, system, function/capability | Design | Recommended | Retain; define relationship to `realizedBy` |
| `hasPort` | Schema and property vocabulary | Owner → port | Design, artifact, system | Port | Optional | Retain; define detailed interface model trigger |
| `hasFlow` | Schema and property vocabulary | Context → flow | Design, use case, procedure, system | Item flow, functional flow | Optional | Retain |
| `hasState` | Schema and property vocabulary | Owner → state | Function, design, system, state machine | State | Optional | Retain |
| `appliesTo` | Schema and reviewed property note | Rule/property/reference → applicable context | Requirement, property, metric, reference, design | Product, use case, environment, organization, domain | Recommended | Retain; distinguish note scope from semantic applicability |
| `dependsOn` | Schema and reviewed property note | Dependent → prerequisite | Any modeled element | Any modeled element | Recommended when material | Retain; require condition/rationale for material dependency |
| `interfaces` | Schema and property vocabulary | Interacting element → counterpart | Design, artifact, port, system | Design, artifact, port, system | Recommended | Retain; define when ports/flows are required |
| `exchanges` | Schema and property vocabulary | Participant → counterpart | Design, artifact, system, actor | Design, artifact, system, actor | Recommended | Retain; use flow element for named payloads |
| `transmits` | Schema and property vocabulary | Sender → payload/flow | Design, artifact, port, system | Item flow, data, energy, material | Recommended | Retain; pair destination where material |
| `receives` | Schema and property vocabulary | Receiver → payload/flow | Design, artifact, port, system | Item flow, data, energy, material | Recommended | Retain; pair source where material |
| `triggeredBy` | Schema and property vocabulary | Response/state/event → trigger | Step, state, function, procedure | Event, condition, state, input | Recommended | Retain; prohibit loose temporal use |
| `precedes` | Schema and property vocabulary | Earlier step/state → later step/state | Step, state, procedure, flow | Step, state, procedure, flow | Optional | Retain; require meaningful ordering |
| `derivedFrom` | Schema and reviewed property note | Derived item → source basis | Research, result, requirement, design, metric | Source record, requirement, model element | Required for material derivation | Retain; document method/limitations |
| `references` | Schema and reviewed property note | Referencing note → referenced item | Any | Any | Optional | Retain; non-assertive only |
| `describes` | Schema and property vocabulary | Document/note → described element | Document, research, info | Any modeled element | Recommended | Retain; does not prove every claim |
| `conflictsWith` | Schema and property vocabulary | Conflicting item → conflicting item | Requirement, design, decision, claim, result | Requirement, design, decision, claim, result | Required by definition | Retain; link conflict basis and resolution state |
| `supersedes` | Schema and property vocabulary | New/current item → replaced item | Revision, decision, document, design, requirement | Prior revision/item | Required by definition | Retain; preserve target history |
| `copyOf` | Schema and property vocabulary | Copy/derivative → source identity | Document, note, source record | Canonical source/note | Required by definition | Retain; do not use to justify duplicate canonical elements |
| `equals` | Schema and property vocabulary | Equivalent identity/meaning → equivalent item | Any | Any | Required by definition | Open: define duplicate/identity policy before broad use |
| `refines` | Schema and property vocabulary | More specific item → abstract item | Requirement, function, design, property | Requirement, function, design, property | Recommended | Retain; distinguish from realization and subtype |
| `tracesTo` | Schema and property vocabulary | Trace source → trace target | Requirement, function, design, verification, need | Requirement, function, design, verification, need | Recommended | Open: define when to use instead of specific relation |

## Relationship decisions and conflicts

| ID | Topic | Decision/gap | Required action before enforcement |
| --- | --- | --- | --- |
| REL-001 | Endpoint types | Formal element-type mapping is incomplete for product, need, metric, organization, and source record | Resolve element-type extension decisions first |
| REL-002 | `hasDesign` versus `realizedBy` | Both may connect product/function/design but assert different semantics | Publish endpoint matrix and examples; prohibit ambiguous use in new templates |
| REL-003 | `satisfies` evidence threshold | Existing usage may vary between intended contribution and demonstrated fulfillment | Define minimum evidence/result rule and legacy migration handling |
| REL-004 | `references` versus `supports` | Both may point to source material, but only one asserts evidentiary support | Require source-record/evidence pattern in document and research templates |
| REL-005 | `tracesTo` versus specific relationships | Generic traceability can obscure meaning | Define reserved use cases or deprecate for new notes with compatibility alias |
| REL-006 | Relationship targets as claims | `supports` and `contradicts` may need claim-level targets, not only notes | Define claim identifier or conflict-record strategy |
| REL-007 | Hierarchy | `hasPart`, `hasChild`, `subtypeOf`, `optionOf` overlap in informal authoring | Add examples and endpoint/cardinality constraints |
| REL-008 | Relationship status/evidence | Current property-link style may not represent maturity or source support | Pilot structured relationship records before schema enforcement |

## P0 template reconciliation matrix

| Template | Retain | Add after schema decision | Minimum body additions | Relationship guidance |
| --- | --- | --- | --- | --- |
| Actor | Existing actor identity and MDSE role | Scope, stakeholder class/role, evidence, uncertainty | Role, responsibilities, operating context, needs | `hasNeed`, `interfaces`, `appliesTo`, `references` |
| Function | Existing function model | Scope, function level, evidence, uncertainty | Intent, triggers/inputs/outputs, hierarchy, realization | `hasChild`, `drives`, `realizedBy`, `dependsOn`, `measures` |
| Design | Existing design model | Design class, implementation scope, evidence, tradeoff/conflict fields | Scope, intent, parts/interfaces, alternatives, constraints | `hasPart`, `hasPort`, `interfaces`, `realizedBy`, `satisfies`, `dependsOn` |
| Requirement | Existing formal obligation model | Scope, rationale/source, priority, evidence, uncertainty | Statement, applicability, rationale, acceptance/verification | `drives`, `refines`, `satisfies`, `verifies`, `conflictsWith` |
| Property Definition | Existing property-definition model | Measure class, value type, unit, method, applicability | Definition, value semantics, use conditions, source/date caveats | `appliesTo`, `measures`, `references`, `derivedFrom` |
| Document | Existing document/source note model | Source class, URL, revision, access date, stability, extraction status | Source identity, relevance, extracted claims, omitted useful information | `describes`, `supports`, `contradicts`, `references` |
| Plan | Existing planning/control model | Decision class, priority, owner, due, evidence/uncertainty | Context, options, rationale, impacts, follow-up | `drives`, `dependsOn`, `conflictsWith`, `supersedes` |
| Verification | Existing verification model | Method, result status, configuration/scope, evidence | Objective, method, conditions, result, conclusion | `verifies`, `measures`, `supports`, `contradicts` |

## Validation impact matrix

| Validation area | Proposed rule | Initial enforcement | Legacy compatibility | Later control target |
| --- | --- | --- | --- | --- |
| File naming | Follow canonical naming rules where adopted | Report-only | Legacy names exempt until moved/adopted | `check-names.py` |
| Broken links | Detect unresolved targets | Preserve current enforcement/behavior | No regression | `check-dependencies.py` |
| Common core | Require ID/type/status/scope for adopted/new canonical notes | Report-only pilot | Legacy notes exempt unless adoption marker exists | New or extended validator |
| Controlled values | Validate element type, scope, lifecycle, extension values | Warn-only pilot | Preserve legacy values and aliases | Schema + validator |
| Relationship type | Validate canonical relationship names | Warn-only pilot | Legacy property links remain valid | Relationship schema + validator |
| Relationship endpoints | Validate source/target type pairs | Disabled until REL-001 is resolved | No legacy enforcement initially | Relationship validator |
| Evidence completeness | Flag material claims/relationships without source basis | Advisory/report-only | No hard fail | Quality reporting |
| Base/Canvas paths | Detect references to moved/missing files | Report-only before first migration | Existing artifacts preserved | New migration/view checker |

## Pilot proposal

Use a small, representative pilot after schemas/templates are updated and before broad migration. The pilot should create or formally adopt one element of each type:

| Pilot role | Candidate legacy note | Purpose |
| --- | --- | --- |
| Actor | [[Fleet Operations Manager]] | Stakeholder role, need relationships, scope/evidence |
| Customer need | [[Know Battery State Before and During the Shift]] | Need classification, holder/context, drives relationship |
| Function | [[Estimate State of Charge]] | Function level, realization, measurement, evidence |
| Design | [[Integrated Battery Management System]] | Design class, implementation scope, parts/interfaces, realization |
| Metric | [[Metric - Availability]] | Metric versus comparison-criterion decision, measurement semantics |
| Source record | [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]] | Provenance, source class, describes/supports relationships |

### Pilot acceptance criteria

1. Every pilot note can be authored using the updated template without ad hoc fields.
2. Each note has a stable identity, formal type, scope, lifecycle status, evidence basis, and material uncertainty recorded.
3. Every material relationship uses an approved controlled term, correct direction, clear target, and suitable maturity/evidence.
4. Legacy notes not in the pilot remain valid and unaffected.
5. Existing Bases, Canvases, links, dependency checks, and name checks do not regress.
6. The pilot produces at least one useful cross-domain traceability view from actor/need through function/design/metric/source evidence.
7. Gaps, exceptions, and user-experience problems are captured before broad rollout.

## Required decisions before implementation

| ID | Decision | Options to resolve |
| --- | --- | --- |
| DEC-001 | Formal base type for product records | New `product` type; controlled object/artifact subtype; or extension-only approach |
| DEC-002 | Formal base type for customer needs | New `need` type; requirement extension; issue/info extension |
| DEC-003 | Formal representation for organizations | New organization type; actor/person/object extension; organization-specific subtype |
| DEC-004 | Formal representation for metrics and comparison criteria | New metric type; property-definition/result extensions; mixed controlled extension |
| DEC-005 | Scope data shape | Nested `scope` object; flat fields; relationship-only approach with limited note field |
| DEC-006 | Relationship-record representation | Structured frontmatter records; existing property fields plus companion metadata; hybrid pilot |
| DEC-007 | Claim-level evidence targets | Claim IDs; conflict/decision notes; note-level support only with body references |
| DEC-008 | `tracesTo` future use | Retain as generic fallback; restrict to traceability views; deprecate for new authoring |

## Recommended next implementation step

Do not modify schemas yet. First resolve DEC-001 through DEC-008 in a decision record, then prepare one reviewable implementation proposal that updates only:

1. The minimum required schema controls.
2. The P0 templates.
3. Report-only validation behavior.
4. A small pilot set of notes.

Any move of legacy folders or bulk adoption of metadata remains outside that implementation proposal.

## Change history

| Version | Date | Change |
| --- | --- |
| 0.1 | 2026-10-04 | Initial field, type, relationship, template, validation, pilot, and decision reconciliation matrix |
