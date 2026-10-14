---
type: Object
subtype: software
id: OBJ-00266
uid: 20261003101711501skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - scope-aftermarket
  - software
  - telematics
  - vehicle-accessory
subtypeOf:
  - "[[Truck Telematics Software]]"
describedBy:
  - "[[Document - Fleet Complete Forklift Gateway Page (retrieved 2026-10-13)]]"
performs:
  - "[[Control Operator Access]]"
  - "[[Detect and Record Impacts]]"
  - "[[Report Truck Telemetry]]"
  - "[[Enforce Pre-Shift Checklist]]"
  - "[[Detect Pedestrians and Objects Near Truck]]"
hasDesign:
  - "[[Impact Sensor]]"
  - "[[Truck Telemetry Reporting Design]]"
madeBy:
  - "[[Powerfleet]]"
offeredBy:
  - "[[Mitsubishi Logisnext Americas]]"
hasPart:
  - "[[Truck Telemetry Acquisition Logic]]"
  - "[[Truck Telemetry Reporting Service]]"
---

# Powerfleet Forklift Gateway

## Definition

Powerfleet forklift gateway (VAC) that handles driver access control, an impact sensor and optional cameras and sensors.

## Notes

- Powerfleet says its material handling telematics manages vehicle access by unique driver identification, connects to a machine-learning impact sensor mounted on the forklift frame, and its Forklift Gateway (VAC) connects optional external sensors and cameras including DVR, speed, load, GPS and pedestrian proximity detection. Source: Powerfleet material handling telematics page (T1), retrieved 2026-10-03. <https://www.powerfleet.com/?p=30065>
- **Functions performed, with citations:**
  - [[Control Operator Access]] (V): <https://www.powerfleet.com/?p=30065>
  - [[Detect and Record Impacts]] (V): <https://www.powerfleet.com/?p=30065>
  - [[Report Truck Telemetry]] (V): <https://www.powerfleet.com/?p=30065>
- **Design characteristics, with citations:**
  - [[Impact Sensor]] (V): <https://www.powerfleet.com/?p=30065>
- Mitsubishi Logisnext Americas entered a reseller agreement with PowerFleet in 2021; PowerFleet's Enterprise Telematics (VAC4 hardware and impact sensors) was offered as a factory option on Mitsubishi, Cat and Jungheinrich trucks with operator access control, electronic pre-shift checklists, impact sensing and speed monitoring. Source: GlobeNewswire release (2021) (T2), retrieved 2026-10-03. <https://www.globenewswire.com/news-release/2021/06/01/2239918/8494/en/Mitsubishi-Logisnext-Americas-Launches-Advanced-PowerFleet-Telematics-Solution-For-North-American-Market.html>
- **Name (C87):** the vault note says Forklift Gateway (VAC); the 2021 release names the VAC4.
- **Functions performed, with citations:**
  - [[Enforce Pre-Shift Checklist]] (V): <https://www.globenewswire.com/news-release/2021/06/01/2239918/8494/en/Mitsubishi-Logisnext-Americas-Launches-Advanced-PowerFleet-Telematics-Solution-For-North-American-Market.html>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controller and CAN Bus]]; connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controller and CAN Bus]], [[Truck Controls and Display]]. See [[Truck Part Connection Register]].

- **Architecture realization — truck telemetry:** published behavior establishes vehicle operating data and event reporting to a fleet-management system, supporting [[Truck Telemetry Reporting Design]]. [[Truck Telemetry Acquisition Logic]] and [[Truck Telemetry Reporting Service]] are allocated at **>=95% engineering confidence** where the vendor does not publish the internal software partition. Exact signal sources, CAN/J1939 mapping, buffering, wireless transport, and cloud protocol remain product-specific.

- **Update 2026-10-13:** the product page is now hosted by Fleet Complete ([[Fleet Complete]], which Powerfleet announced it would acquire on 2024-09-20) and says the unit fits virtually any industrial material handling equipment, supports nearly all wireless ID types with a keypad, enforces multilingual electronic pre-use checklists after login and runs access control and checks offline; optional AI impact sensor, GPS, speed/distance, loaded/unloaded sensing, pedestrian proximity detection and DVR; reports to Unity. Sources: <https://www.fleetcomplete.com/products/forklift-telematics/features/forklift-gateway/>; <https://www.sdcexec.com/home/news/22920934/powerfleet-powerfleet-to-acquire-fleet-complete> (T1/T2, second-hand). This is a third-party retrofit unit as well as a Mitsubishi/Cat/Jungheinrich factory option.
- **Functions performed, with citations:**
  - [[Enforce Pre-Shift Checklist]] (V): <https://www.fleetcomplete.com/products/forklift-telematics/features/forklift-gateway/>
  - [[Detect Pedestrians and Objects Near Truck]] (V, optional): <https://www.fleetcomplete.com/products/forklift-telematics/features/forklift-gateway/>

## Aliases

- Forklift Gateway (VAC)

## Former ids
