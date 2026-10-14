---
type: Design
subtype:
id: DES-00141
uid: 20261014163455420skellyspencer
status: Draft
tags:
  - truck-design
  - design-characteristic
subtypeOf:
  - "[[Vehicle Control Device Design]]"
designOf:
  - "[[Linde Safety Pilot]]"
  - "[[Hyster Dynamic Stability System]]"
dependencyOf:
  - "[[Stabilize Truck Dynamically]]"
---

# Stability-Limit Function Intervention

## Definition

Controller that reads truck state (lift height, load, speed) and limits or blocks travel, lift or tilt as a stability limit is approached, with no mechanical actuator.

## Notes

- Design characteristic found in truck-side products, not a decision by us. No Requirement is linked.
- Alternative to [[Active Stability Actuator]] (Toyota's rear-axle swing lock) for [[Stabilize Truck Dynamically]]: one acts on the axle, this one acts on the truck's functions. Each is enough for the products that carry it; no source compares them.
- Linde Safety Pilot monitors load centre of gravity, lift height and driving speed and intervenes in driving, lifting and tilting; Hyster limits functions in real time while leaving the operator in control.
- **Sources** (product, evidence level, web page):
  - [[Linde Safety Pilot]] (V): <https://www.kiongroup.com/en/Newsroom/Story-Categories/Innovation/Article/7-solutions-that-make-the-warehouse-safer.html>
  - [[Hyster Dynamic Stability System]] (V): <https://www.inboundlogistics.com/articles/product-spotlight-safety-and-ergonomics/>

## Aliases


## Former ids
