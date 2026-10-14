---
type: Design
subtype:
id: DES-00140
uid: 20261014163455406skellyspencer
status: Draft
tags:
  - truck-design
  - design-characteristic
subtypeOf:
  - "[[Vehicle Control Device Design]]"
designOf:
  - "[[STILL Curve Speed Control]]"
  - "[[Linde System Control]]"
  - "[[Hyster Dynamic Stability System]]"
dependencyOf:
  - "[[Slow Truck in Curves]]"
  - "[[Stabilize Truck Dynamically]]"
---

# Steering-Angle Curve Speed Control

## Definition

Controller that lowers travel speed according to how far the truck is steered, so cornering speed stays inside a stable limit.

## Notes

- Design characteristic found in truck-side products, not a decision by us. No Requirement is linked.
- Mechanism is stated for three of the 16 performers of [[Slow Truck in Curves]]: STILL (speed by steering angle), Linde System Control (stepless speed adjustment by steering angle, lift height and load weight) and Hyster Dynamic Stability System (slows in corners based on turn tightness). Jungheinrich curveCONTROL and UniCarriers Curve Control say the truck slows when cornering but their sources do not say what is measured, so they are not linked here (C271).
- **Sources** (product, evidence level, web page):
  - [[STILL Curve Speed Control]] (V): <https://www.still.co.uk/company/news-press/news/detail/safe-safer-still.html>
  - [[Linde System Control]] (V): <https://www.linde-mh.pl/media/Datasheets/EN_ds_v_br5213_en_c_0319.pdf>
  - [[Hyster Dynamic Stability System]] (V): <https://www.inboundlogistics.com/articles/product-spotlight-safety-and-ergonomics/>

## Aliases


## Former ids
