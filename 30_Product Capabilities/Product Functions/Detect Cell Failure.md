---
type: Function
subtype:
id: FUNC-00023
uid: 20261002164202369skellyspencer
status: Draft
tags:
  - battery-monitoring
  - extra
  - product-function
subtypeOf:
  - "[[Sense Battery State]]"
performedBy:
  - "[[Cell Failure Diagnostic Firmware]]"
  - "[[Cell Failure Threshold Circuit]]"
  - "[[AMETEK Prestolite Power TruBid]]"
dependsOn:
  - "[[Cell Failure Diagnostic Design]]"
realizedBy:
  - "[[Cell Failure Diagnostic Design]]"
realizes:
  - "[[Prevent Battery Abuse and Premature Replacement]]"
---

# Detect Cell Failure

## Definition

Detect a failed cell in the battery.

## Notes

- Stated only for Prestolite TruBid in a trade-press source.
- Prestolite separately states that TruBID measures electrolyte specific gravity and identifies undercharged batteries, but the available sources do **not** state how its cell-failure diagnosis is derived. The model therefore does not infer cell-voltage sensing, specific-gravity-based diagnosis, impedance measurement, or another specific method.
- Product links are made only where a source states the behavior; no link means unknown, not absent. Overview: [[Function Map]].
- No Requirement is linked: nothing here is a committed requirement, so model-health will show these Functions without satisfied Requirements. That gap is intentional.
- **Sources** (product, evidence level, web page):
  - [[AMETEK Prestolite Power TruBid]] (V): <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>
- **Extra (round 30):** documented for 0 of 21 battery maker groups (0 percent), delivered by an accessory/device; the reusable dependency is now the method-neutral [[Cell Failure Diagnostic Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization family is [[Cell Failure Diagnostic Design]]. The commercial TruBID implementation mechanism remains unresolved, so the product is linked only to the generic Design family.

Two concrete engineering alternatives are retained:

- **Programmable diagnostic path:** [[Algorithmic Cell Failure Diagnosis]] -> [[Cell Failure Diagnostic Firmware]]. Firmware can evaluate one or more battery measurements or histories and classify a cell failure using thresholds, persistence, trends, plausibility checks, or expected-response comparisons.
- **Dedicated hardware path:** [[Dedicated Threshold Cell Failure Detection]] -> [[Cell Failure Threshold Circuit]]. Analog or mixed-signal circuitry can compare a sensed parameter against diagnostic thresholds without a programmable diagnostic algorithm.

Neither concrete alternative is allocated as a part or specific Design of [[AMETEK Prestolite Power TruBid]] because the available evidence does not disclose whether TruBID performs the diagnosis in firmware, dedicated hardware, charger-side logic, or another mechanism.

### Known TruBID evidence boundary

TruBID is verified to:
- place a probe in a battery cell,
- monitor electrolyte temperature and specific gravity,
- work with the charger to control charge,
- and detect cell failures.

Those facts establish the Function but **not the causal diagnostic chain**. The in-cell specific-gravity measurement is therefore treated as a plausible diagnostic input, not as a modeled dependency of this Function, until a source explicitly connects the two.

## Aliases


## Former ids
