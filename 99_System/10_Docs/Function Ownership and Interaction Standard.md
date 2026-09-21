# Function Ownership and Interaction Standard

## Purpose

Prevent Functions from becoming unowned feature labels.

## Product-controlled Function rule

A Function promoted into product scope must have at least one controlled Thing in its `performedBy` / `performs` relationship and must have a justified Requirement when committed.

A journey step performed by a user, operator, partner, external product, or environment does not become an internal Function merely because the modeled product participates in the same end-to-end scenario.

## Internal behavior

Internal Functions perform computation, storage, transformation, governance, or presentation within the controlled product boundary.

## Interaction behavior

A controlled Function that crosses the product boundary must be grounded in the thing it interacts with:
- Actor/Use Case for human interaction;
- concrete Interface and Item Flow for system interaction;
- explicit Document/Artifact source for import/extraction behavior.

Do not model a generic “integration” Function and then assume an external contract.

## Contextual observed behavior

Observed market/external Functions may be modeled for comparison or context. They do not become product Requirements or owned Functions until scope explicitly promotes them.

## Journey use

Stakeholder journeys are used to identify:
- controlled Functions;
- contextual/external behavior;
- manual handoffs;
- interface dependencies;
- missing Requirements;
- failure/verification candidates.

The journey itself is not proof that every step belongs inside the product.
