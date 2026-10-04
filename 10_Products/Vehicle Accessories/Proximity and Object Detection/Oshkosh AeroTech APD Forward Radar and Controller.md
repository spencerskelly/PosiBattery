---
type: Object
subtype: electrical
id: OBJ-00416
uid: 20261003200030138skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - truck-device
  - vehicle-accessory
  - gse
  - gse-device
  - gse-option
subtypeOf:
  - "[[Proximity and Object Detection System]]"
partOf:
  - "[[Oshkosh AeroTech Aircraft Proximity Detection]]"
performs:
  - "[[Detect Pedestrians and Objects Near Truck]]"
  - "[[Slow and Stop Near Aircraft]]"
  - "[[Alert Operator of Hazards]]"
hasDesign:
  - "[[Radar Object Sensor]]"
madeBy:
  - "[[Oshkosh AeroTech]]"
offeredWith:
  - "[[Oshkosh AeroTech Commander 30i Cargo Loader]]"
  - "[[Oshkosh AeroTech Ranger 15E Cargo Loader]]"
---

# Oshkosh AeroTech APD Forward Radar and Controller

## Definition

Base Aircraft Proximity Detection system for Commander loaders: a forward-looking 5.8 GHz radar (6 m maximum range), a controller in the main electrical panel, a cab warning light, buzzer and 5 cm color LCD, and a hand throttle for creep speed, with password-protected interlocks.

## Notes

- Oshkosh AeroTech's APD brochure says the controller sits in the main electrical panel and interprets sensor input, alerting the operator through a warning light and buzzer on the cab control panel, which also carries a 5 cm (2.8 in) color LCD rated for outdoor use; the base system includes a forward-looking radar at 5.8 GHz with a maximum range of 6.0 m (20 ft), approved for airports, and a hand throttle lever for creep speed on final approach. Source: Oshkosh AeroTech APD brochure (06/18/24) (T1), retrieved 2026-10-03. <https://oshkoshaerotech.com/aircraft-proximity-detection-apd-06-18-24>
- The brochure says selectable, password-protected interlocks let maintenance staff choose what the radar does when it detects an obstacle at 6.0, 5.3, 4.5, 3.8 or 3.0 m: full stop, switch to snail speed or switch to hand-control creep speed, and warning light, buzzer and drive interlock when the cab is not retracted, the bridge is not lowered, the wing-down is not actuated or the chassis is not lowered. Source: Oshkosh AeroTech APD brochure (T1), retrieved 2026-10-03. <https://oshkoshaerotech.com/aircraft-proximity-detection-apd-06-18-24>
- **Functions performed, with citations:**
  - [[Detect Pedestrians and Objects Near Truck]] (V): <https://oshkoshaerotech.com/aircraft-proximity-detection-apd-06-18-24>
  - [[Slow and Stop Near Aircraft]] (V): <https://oshkoshaerotech.com/aircraft-proximity-detection-apd-06-18-24>
  - [[Alert Operator of Hazards]] (V): <https://oshkoshaerotech.com/aircraft-proximity-detection-apd-06-18-24>
- **Design characteristics, with citations:**
  - [[Radar Object Sensor]] (V): <https://oshkoshaerotech.com/aircraft-proximity-detection-apd-06-18-24>
- **GSE parts (round 33):** stated: connects to [[GSE Controls and Display]] (warning light, buzzer and color LCD on the cab control panel); acts on [[GSE Drive and Brakes]] (interlocks stop the loader or switch to snail or creep speed) | typical: mounts on [[GSE Front Body and Bumper]] (forward-looking radar; mount not named) and the controller on [[GSE Controller and CAN Bus]] (main electrical panel). See [[GSE Part Connection Register]].

## Aliases

- APD radar

## Former ids
