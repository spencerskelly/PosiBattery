# AI Model Kickoff Workflow

## Purpose

Use AI to accelerate initial model coverage before team workshops without allowing AI-generated breadth to masquerade as authoritative engineering truth.

## Inputs to provide

Prefer primary material first:
- product/system descriptions;
- stakeholder notes/interviews;
- requirements/specifications;
- architecture diagrams;
- interface documents;
- existing test/verification material;
- issue/risk history;
- external standards or regulations;
- legacy models/imports.

Tell the AI which sources are authoritative, historical, hypothetical, or examples.

## Pass 1 — Evidence inventory

AI should identify:
- source name/type/date;
- apparent authority;
- covered topics;
- conflicts/duplicates;
- missing evidence;
- statements that are explicit versus inferred.

Do not create a polished model first. Understand the evidence first.

## Pass 2 — Broad semantic coverage

Propose candidate coverage across:
- Things / architecture;
- Actors;
- stakeholder journeys;
- Use Cases;
- Functions;
- Interfaces / Item Flows;
- Requirements;
- Designs / decisions;
- Contexts;
- States / State Machines / Transitions;
- Failure Modes / Issues;
- Documents / Artifacts;
- Verification intent.

Missing categories are acceptable. Do not create filler elements merely to populate the taxonomy.

## Pass 3 — Identity and reuse review

For every candidate element:
1. search existing model;
2. decide reuse / instance / subtype / part / independent element;
3. state why;
4. identify control classification;
5. identify evidence/basis;
6. identify minimum meaningful relationships.

## Pass 4 — Boundary and ownership review

For each behavior/journey step, determine:
- controlled by modeled product;
- modifiable/shared;
- contextual/external;
- manual human behavior.

Only controlled product behavior becomes product Function scope without an explicit scope decision.

## Pass 5 — Trace-chain review

Where evidence supports committed behavior, aim toward:

`Actor → Use Case/Need → Requirement → Function/Design → Thing → Verification`

Do not force the chain where evidence is missing; leave explicit gaps/questions.

## Pass 6 — Interface review

Capture external interactions concrete-first:
- exact endpoints;
- exact direction;
- actual payload/information/material/energy;
- known mechanism/protocol;
- lifecycle/status/error behavior when supported;
- unknowns.

Do not standardize similar-looking interfaces until multiple true examples justify it.

## Pass 7 — Team-review packet

AI should present:
- proposed model structure;
- highest-confidence accepted candidates;
- hypotheses/questions;
- duplicate/identity decisions;
- scope/boundary ambiguities;
- missing interfaces;
- missing requirements;
- missing verification;
- top model-health risks;
- decisions needing team authority.

## Promotion rule

Keep AI-generated proposals in `90_Concept/AI_Workspace` until reviewed or explicitly authorized for promotion.
