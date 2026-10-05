---
type: Use Case
subtype: what
id: UC-00041
uid: 20261005111800003skellyspencer
status: Draft
tags:
  - operational-use-case
  - bmid-product-use-case
  - variant-dependent
participants:
  - "[[Dealer Service Technician]]"
  - "[[Maintenance Technician]]"
  - "[[Equipment Installer]]"
  - "[[PosiCharge BMID]]"
realizedBy:
  - "[[Configure Device from Mobile App or PC]]"
---

# Configure and Service a Supported BMID

## Definition

A qualified installer or technician configures, reads, updates, or services a BMID variant using the interfaces and tools supported by that product.

## Notes

- This is a family-level use case with **variant-dependent applicability**.
- Current direct evidence for mobile/app configuration is strongest for [[PosiCharge PosiGuard]] and associated PosiConnect tooling.
- The use case must not be interpreted as proof that BMID 1, BMID 3, or Battery Rx all support the same configuration mechanism.
- Completion: the supported configuration or service task is completed without changing unsupported product parameters.

## Traceability

- Related product functions: [[Configure Device from Mobile App or PC]], [[Log Battery Events and Usage]].
- Product applicability must be confirmed at the child-product level before requirements are created.

## Former ids
