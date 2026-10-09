---
type: Function
subtype:
id: FUNC-00126
uid: 20261004183002126skellyspencer
status: Draft
tags:
  - accessory-function
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
performedBy:
  - "[[Toyota Twistlock Snapshot Camera System]]"
  - "[[Load-Handling Camera Assembly]]"
  - "[[Load-Handling Image Capture Logic]]"
  - "[[Load-Handling Image Storage]]"
  - "[[Load-Handling Image Sensor Module]]"
realizes:
  - "[[Detect and Learn from Truck Impacts]]"
  - "[[Review an Impact Event and Decide Whether to Return the Vehicle to Service]]"
dependsOn:
  - "[[Load-Handling Image Capture Design]]"
realizedBy:
  - "[[Load-Handling Image Capture Design]]"
  - "[[Review an Impact Event and Decide Whether to Return the Vehicle to Service]]"
---

# Record Images of Load Handling

## Definition

Capture images of a load or attachment before and after it is handled, as a record of how it was handled.

## Notes

- Added 2026-10-04 from the accessory marketed-features review. Product links only where a source states the behavior; no link means unknown.
- **Customer need (2026-10-04, analyst link, hypothesis):** realizes [[Detect and Learn from Truck Impacts]]; weak fit: the source says images are taken before and after each container is handled but does not say they are used for damage or incidents (open question C117) (see [[Research Change and Decision Tracker]]).
- **Depends on:** none written: no general camera or image-capture design note exists (Pedestrian Detection Camera is detection-specific); rule and basis in [[Function Design Dependencies]].
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Toyota Twistlock Snapshot Camera System]] (V): <https://www.toyotaforklift.com/content/dam/tmh/marketing/es/pdf/about-toyota/2025_Toyota%20Assist%20Brochure_Digital.pdf>

## Implementation Allocation

The reusable realization is [[Load-Handling Image Capture Design]].

[[Load-Handling Camera Assembly]] provides the camera hardware, while [[Load-Handling Image Capture Logic]] determines when images are taken and associates them with the handling event. [[Load-Handling Image Storage]] retains the resulting records.

This separation matters because a camera by itself does not satisfy the Function. The system must also trigger capture at the correct point in the handling cycle and retain the image as an event record.

[[Toyota Twistlock Snapshot Camera System]] is the verified product implementation: Toyota states that images are captured before and after each container is handled. The exact trigger source, camera count, image format, storage medium, and review/export workflow are not published.

## Aliases


## Former ids
