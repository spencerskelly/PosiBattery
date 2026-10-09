---
type: Object
subtype: software
id: OBJ-00275
uid: 20261003141234124skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - scope-oem-option
  - software
  - truck-device
  - truck-oem-option
  - vehicle-accessory
subtypeOf:
  - "[[Operator Display]]"
performs:
  - "[[Display Battery Status to Operator]]"
  - "[[Display Truck Status to Operator]]"
  - "[[Program Travel, Lift and Tilt Speeds]]"
hasDesign:
  - "[[Operator Touch Display]]"
hasPart:
  - "[[Operator Display HMI Firmware]]"
dependsOn:
  - "[[Operator Touchscreen Display Module]]"
  - "[[Operator Display Controller Circuit]]"
madeBy:
  - "[[Crown Equipment]]"
offeredWith:
  - "[[Crown InfoLink]]"
  - "[[Crown ProximityAssist System]]"
partOf:
  - "[[Crown InfoLink]]"
---

# Crown Gena Operating System

## Definition

Crown lift truck operating system with a 7 inch touch screen, widgets, zone select and safety messages, integrated with InfoLink.

## Notes

**Summary:**
Crown's connected lift-truck operating system with a touchscreen, widgets and contextual guidance, integrated with InfoLink.

**Marketed features:**
- 7 in touchscreen with customizable widgets (battery capacity, hour meter, height and steer-angle indicators)
- Wireless updates
- Adjustable driving parameters (acceleration, braking, travel speed) per operator and application
- Onboarding prompts, safety reminders and real-time task guidance
- 25 to more than 40 languages, depending on source
- Integrates with InfoLink (required); optional USB charging port on ESR

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Crown (T1), retrieved 2026-10-04. <https://www.crown.com/en-la/forklifts/esr-reach-truck.html>
- Crown (T1), retrieved 2026-10-04. <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>

- Crown says the Gena operating system has a 7 inch touch screen programmable in 25 languages, customizable widgets, wireless updates and, on the ESR reach truck, integrates an optional Capacity Data Monitor. Source: Crown ESR reach truck page (T1), retrieved 2026-10-03. <https://www.crown.com/en-la/forklifts/esr-reach-truck.html>
- On the SP Series order picker, Zone Select lets three clear heights be programmed per application, safety messages show at log-in, and Gena integrates with the optional InfoLink Operator and Fleet Management System (access control, visual inspection checklist, impact detection and alerts, equipment lockout; InfoLink service plan required). Source: Crown SP 1500 page and APAC brochure (T1), retrieved 2026-10-03. <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
- Crown says ProximityAssist alerts appear on the Gena touch screen. Source: IVT International (T2), retrieved 2026-10-03. <https://www.ivtinternational.com/?p=22917>
- **Design characteristics, with citations:**
  - [[Operator Touch Display]] (V): <https://www.crown.com/en-la/forklifts/esr-reach-truck.html>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controls and Display]]; connects to [[Truck Controller and CAN Bus]]. See [[Truck Part Connection Register]].
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Display Battery Status to Operator]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Display Truck Status to Operator]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Program Travel, Lift and Tilt Speeds]] (V): <https://www.crown.com/en-la/forklifts/esr-reach-truck.html>

- **Architecture realization — truck status display:** Gena's verified touchscreen, customizable widgets, safety messages and operating guidance reuse [[Operator Touchscreen Display Module]], [[Operator Display Controller Circuit]], and [[Operator Display HMI Firmware]] for [[Display Truck Status to Operator]]. The underlying truck-state data transport is not inferred.
- **Architecture realization — operator battery display:** Gena's 7-inch touch screen and battery-capacity widget are verified. Because Gena is modeled as software, [[Operator Display HMI Firmware]] is a software role within it while [[Operator Touchscreen Display Module]] and [[Operator Display Controller Circuit]] are hardware dependencies. The source does not identify the battery-data transport used by the Gena display.

## Aliases

- Gena

## Former ids
