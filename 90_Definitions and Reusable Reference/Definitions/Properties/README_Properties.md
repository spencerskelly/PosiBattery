# Properties

## Purpose

This folder contains the controlled definitions for note metadata and note-level relationship fields used by the current MDSE runtime.

Use this README to choose the right property family and understand the semantic boundaries between similar fields. Use [[Property Dictionary]] for the exhaustive tabular inventory.

The active implementation authorities remain:

- `99_System/03_Schemas/element-types.yaml` for common, optional, and type/subtype rules;
- `99_System/03_Schemas/relationships.yaml` for relationship direction, inverse, endpoint, symmetric, temporary, and one-way rules.

Property notes explain the vocabulary; they do not override those schemas.

## Identity and classification

- [[type]] — primary MDSE semantic class.
- [[subtype]] — approved classification within a type; distinct from the relationship [[subtypeOf]].
- [[id]] — short human-readable identifier.
- [[uid]] — permanent globally unique identity token.
- [[status]] — review/lifecycle state.
- [[tags]] — free-list metadata; value governance remains intentionally limited.
- [[abstract]] — marks a reusable definition as non-selectable for an occurrence.
- [[eaType]] — temporary source classification retained on translated EA notes.

## Reusable hierarchy and containment

- [[subtypeOf]] — true reusable specialization/generalization.
- [[hasPart]] — Object-to-Object assembly composition.
- [[hasChild]] — generic ownership/hierarchy where a more specific relationship does not govern.
- [[includes]] — membership without ownership.
- [[hasPort]] — ownership of a Port.
- [[hasFlow]] — Port ownership of Item Flow definitions.
- [[hasState]] — State/State Machine ownership under the governed state rules.

These are not interchangeable. Folder nesting does not create any of them.

## Interaction, interfaces, and flow

- [[interfaces]] — governed symmetric interaction between Ports.
- [[exposes]] — outer Port exposes an inner Port at a higher boundary.
- [[equals]] — temporary imported BindingConnector evidence pending resolution.
- [[transmits]], [[receives]], [[exchanges]] — one-way flow-direction semantics from a Port to an Item Flow.
- [[triggeredBy]] — behavior trigger relationship.

## Behavior, intent, and realization

- [[performs]] — Object to Function.
- [[hasDesign]] — governed ownership/applicability of a Design under the current runtime schema.
- [[realizedBy]] — current runtime realization relationship.
- [[drives]] — source gives rise to or causes the target.
- [[affects]] — source impacts a target that exists independently.
- [[dependsOn]] — dependency relationship; detailed semantic reconciliation remains pending.
- [[precedes]] — ordered flow/sequence relationship.
- [[participants]] — one-way Use Case participation.

## Requirement and verification traceability

- [[appliesTo]] — Requirement scope.
- [[satisfies]] — current runtime satisfaction relationship.
- [[verifies]] — current runtime Verification-to-Requirement relationship.
- [[refines]] — Requirement adds precision to another Requirement.
- [[derivedFrom]] — Requirement derivation.
- [[references]] — governed Requirement reference/citation relationship.
- [[tracesTo]] — provisional relationship used when a stronger predicate is not yet selected.

Several of these property notes still have intentionally incomplete local wording. Consult the active schemas until Steps 73–78 complete formal reconciliation.

## Lifecycle, identity relationship, and conflict

- [[copyOf]] — copy/source-copy traceability.
- [[supersedes]] — replacement lifecycle.
- [[conflictsWith]] — symmetric compatibility conflict.
- [[optionOf]] — Use Case option relationship.
- [[hasClassifier]] — temporary import relationship resolved during post-import review.

## State-machine markers

- [[initialState]] — one-way State Machine start state.
- [[finalState]] — one-way State Machine terminal state(s).

## Choosing between similar properties

Prefer the narrowest governed meaning:

- hierarchy: [[subtypeOf]] vs [[hasPart]] vs [[hasChild]] vs [[includes]];
- realization/intent: [[hasDesign]] vs [[realizedBy]] vs [[satisfies]];
- interaction: [[interfaces]] vs [[exposes]] vs temporary [[equals]];
- flow: [[hasFlow]] owns an Item Flow; [[transmits]]/[[receives]]/[[exchanges]] describe its direction/use;
- causality: [[drives]] means the target exists/happens because of the source; [[affects]] means the target exists independently;
- evidence/trace: prefer a precise governed relationship over [[tracesTo]] whenever the meaning is known.

## Current reconciliation status

[[Property Definition Quality Inventory Step 71 0.1]] found no exact duplicate or confirmed alias properties. The remaining work is primarily incomplete definitions, a small number of documentation conflicts, and proposed-vs-runtime semantic drift that is intentionally deferred to the schema-reconciliation phase.

Do not rename, merge, broaden, or deprecate controlled properties from this navigation guide alone.

## Related navigation

- [[README_Definitions|Definitions]] — shared authoring and vocabulary guidance.
- [[README_Definitions and Reusable Reference|Definitions and Reusable Reference]] — domain entry point.
- [[README_Research and Evidence|Research and Evidence]] — source-specific evidence and analysis supporting reusable technical definitions.
