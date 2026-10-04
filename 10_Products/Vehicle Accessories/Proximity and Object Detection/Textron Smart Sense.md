---
type: Object
subtype: electrical
id: OBJ-00243
uid: 20261003094918662skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - gse
  - proximity
  - scope-oem-option
  - truck-device
subtypeOf:
  - "[[Proximity and Object Detection System]]"
performs:
  - "[[Limit Truck Speed Automatically]]"
  - "[[Detect Pedestrians and Objects Near Truck]]"
  - "[[Slow and Stop Near Aircraft]]"
  - "[[Stop Vehicle When Operator Is Out of Position]]"
  - "[[Indicate Aircraft Proximity to Operator]]"
hasDesign:
  - "[[Ultrasonic Distance Sensor]]"
  - "[[Aircraft Proximity Indicator Light]]"
madeBy:
  - "[[Textron GSE]]"
offeredWith:
  - "[[TUG 660 Belt Loader]]"
---

# Textron Smart Sense

## Definition

Textron anti-collision system for TUG belt loaders using ultrasonic sensors that slow and stop the loader near an aircraft and light indicators.

## Notes

- Textron says Smart Sense uses ultrasonic sensors on the front of the conveyor to judge aircraft proximity and signals the transmission to control speed; speed is limited to 3.5 mph, slows to 0.5 mph within 6 ft (1.8 m) with a flashing yellow light, and the vehicle cannot move forward once the conveyor is within 2 to 4 inches (5 to 10 cm); indicator lights are on the conveyor front and the back of the TUG 660. Source: Airport Industry Review company insight (T2), retrieved 2026-10-03. <https://airport.h5mag.com/air_dec18/textron_company_insight>
- A trade report adds that Smart Sense stops the belt loader if the operator leaves the seat while it is moving or a system fault is detected, and quotes IATA research that belt loaders and other ground support vehicles account for 40 percent of ramp incidents. Source: Ground Handling International (April 2023) (T2), retrieved 2026-10-03. <https://ghi.mydigitalpublication.co.uk/april-2023/page-44>
- **Functions performed, with citations:**
  - [[Limit Truck Speed Automatically]] (V): <https://airport.h5mag.com/air_dec18/textron_company_insight>
  - [[Detect Pedestrians and Objects Near Truck]] (V): <https://airport.h5mag.com/air_dec18/textron_company_insight>
  - [[Slow and Stop Near Aircraft]] (V): <https://airport.h5mag.com/air_dec18/textron_company_insight>
  - [[Stop Vehicle When Operator Is Out of Position]] (V): <https://airport.h5mag.com/air_dec18/textron_company_insight>
  - [[Indicate Aircraft Proximity to Operator]] (V): <https://airport.h5mag.com/air_dec18/textron_company_insight>
- **Design characteristics, with citations:**
  - [[Ultrasonic Distance Sensor]] (V): <https://airport.h5mag.com/air_dec18/textron_company_insight>
  - [[Aircraft Proximity Indicator Light]] (V): <https://airport.h5mag.com/air_dec18/textron_company_insight>
- Textron's company insight adds that a red indicator light shows if the conveyor is within 2 inches (5 cm) of an object, the operator leaves the seat, or the system has a fault; a Textron GSE executive says anti-collision technology is only a recommendation within IATA AHM 913, not a regulatory requirement, so not every operator fits it. Source: Airport Industry Review and Ramp Equipment News (Feb-Mar 2023) (T2), retrieved 2026-10-03. <https://airport.h5mag.com/air_dec18/textron_company_insight> <https://ren.mydigitalpublication.co.uk/february-march-2023/page-16>
- **GSE parts (round 32):** stated by the source: mounts on [[GSE Load-Handling Structure]] (ultrasonic sensors on the front of the conveyor); acts on [[GSE Drive and Brakes]] (signals the transmission to control speed, and stops the belt loader if the operator leaves the seat) | typical (inferred from the device type, not from a source): connects to [[GSE Controller and CAN Bus]]. See [[GSE Part Connection Register]].

## Aliases

- Smart Sense

## Former ids
