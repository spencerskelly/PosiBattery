---
type: Object
subtype: electrical
id: OBJ-00292
uid: 20261003141234141skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - scope-oem-option
  - truck-device
  - truck-oem-option
  - vehicle-accessory
subtypeOf:
  - "[[Proximity and Object Detection System]]"
performs:
  - "[[Detect Pedestrians and Objects Near Truck]]"
  - "[[Limit Truck Speed Automatically]]"
  - "[[Stop Truck for Detected Obstacle]]"
hasDesign:
  - "[[LiDAR Object Sensor]]"
madeBy:
  - "[[Raymond]]"
offeredWith:
  - "[[Raymond Orderpickers]]"
---

# Raymond In-Aisle Detection System

## Definition

Raymond LiDAR option for Orderpicker and Swing-Reach trucks that keeps trucks apart in very narrow aisles; speed limited to 1 mph until an object is removed.

## Notes

**Summary:**
Raymond LiDAR option for Orderpicker and Swing-Reach trucks that stops the truck for objects in the aisle path and then limits speed.

**Marketed features:**
- LiDAR detects objects in the tractor-first travel path and decelerates to a stop
- Continued travel limited to 1 mph until the object is removed
- Programmable sensing distance of 30 ft or more
- Keeps wire-guided VNA trucks separated
- Orderpicker 5300/5400/5500/5600; Swing-Reach 9600/9700 (wire guidance required)

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Raymond (T1), retrieved 2026-10-04. <https://raymondcorp.com/campaign/in-aisle-detection-system>

- Raymond says the In-Aisle Detection System (IADS) uses a LiDAR sensor, is an option on Orderpicker and Swing-Reach models (9600 and 9700, which require wire guidance), and limits speed to 1 mph until the object is removed. Source: Raymond IADS page (T1), retrieved 2026-10-03. <https://raymondcorp.com/campaign/in-aisle-detection-system>
- **Functions performed, with citations:**
  - [[Detect Pedestrians and Objects Near Truck]] (V): <https://raymondcorp.com/campaign/in-aisle-detection-system>
  - [[Limit Truck Speed Automatically]] (V): <https://raymondcorp.com/campaign/in-aisle-detection-system>
- **Design characteristics, with citations:**
  - [[LiDAR Object Sensor]] (V): <https://raymondcorp.com/campaign/in-aisle-detection-system>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Overhead Guard]] (alternative) or [[Truck Rear Body]] (alternative); connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Drive and Brakes]]. See [[Truck Part Connection Register]].
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Stop Truck for Detected Obstacle]] (V): <https://raymondcorp.com/campaign/in-aisle-detection-system>

## Aliases

- IADS

## Former ids
