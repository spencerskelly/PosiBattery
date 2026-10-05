---
type: Use Case
subtype: what
id: UC-00038
uid: 20261005111800000skellyspencer
status: Draft
tags:
  - operational-use-case
  - bmid-product-use-case
participants:
  - "[[Forklift Operator]]"
  - "[[GSE Operator]]"
  - "[[Maintenance Technician]]"
  - "[[PosiCharge BMID]]"
realizedBy:
  - "[[Identify Battery to Charger]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Communicate with Charger]]"
---

# Charge a BMID-Equipped Battery Using Battery Information

## Definition

An operator or technician connects a BMID-equipped battery to a compatible charging system so the charger can receive supported battery identity and condition information needed for the charging session.

## Notes

- Primary product: [[PosiCharge BMID]].
- Primary contexts: [[Centralized Battery Room and Charging Area]], [[Distributed and Opportunity Charging Area]], and [[Airport Ground-Support Operating Area]].
- Trigger: a BMID-equipped battery requires charging.
- Completion: the compatible charger has received the supported BMID information needed to proceed with its own charge-control logic.
- The BMID does not own charger power-control authority in this use case.
- This use case does not assert that every BMID generation sends the same data or uses the same communication method.

## Traceability

- Source needs: [[Charge Each Battery Correctly for Its Chemistry and Condition]], [[Integrate the Battery with Truck and Charger Controls]].
- Related generic workflow: [[Connect a Vehicle or Battery to a Charger]].

## Former ids
