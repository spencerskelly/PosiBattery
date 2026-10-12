---
type: Object
subtype: electrical
id: OBJ-00235
uid: 20261003094918649skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - gse
  - gse-vehicle
  - lithium
subtypeOf:
  - "[[GSE Baggage and Tow Tractor]]"
performs:
  - "[[Recover Energy by Regeneration]]"
  - "[[Diagnose Vehicle Remotely]]"
hasDesign:
  - "[[Regenerative Braking]]"
  - "[[Electric Parking Brake]]"
  - "[[Bluetooth Interface]]"
  - "[[Remote Vehicle Diagnostics Design]]"
madeBy:
  - "[[Textron GSE]]"
hasPart:
  - "[[Vehicle Diagnostic Data Acquisition Logic]]"
  - "[[Remote Vehicle Diagnostic Service]]"
---

# TUG Endurance Baggage Tractor

## Definition

Textron new lithium baggage tractor, CE certified.

## Notes

- A trade listing names TUG Endurance as a new CE-certified lithium baggage tractor; Textron's other tractors include the TUG MA, MT, MH, M7 and MR (power types not stated). Source: The Flying Engineer listing and AirlineGeeks (T2), retrieved 2026-10-03. <https://theflyingengineer.com/?p=25152>
- **Verification 2026-10-03 (round 40, verified):** Textron GSE's TUG Endurance page lists regenerative braking and a General Motors and PCS lithium powertrain with opportunity charging; the introduction release (republished by AviationPros) names an electronic parking brake, Bluetooth remote diagnostics and a drivetrain that monitors for ground faults and disconnections, and says TUG Endurance models are also available with gas or diesel powertrains. Sources: Textron GSE product page (T1) <https://textrongse.txtsv.com/products/tractors/tug-endurancer>; Textron GSE introduction release (T2) <https://www.aviationpros.com/ground-support-worldwide/gse/baggage-cargo/press-release/21280484/textron-gse-textron-gse-introduces-the-tug-endurance-baggage-tractor>. See conflict C107.
- **Not linked (no matching function yet):** ground-fault and disconnection monitoring (IB-136); J1772 Level 2 AC and DC fast charging are charge-interface properties (metric).
- **Functions performed, with citations (round 40, gap review 2026-10-03):**
  - [[Recover Energy by Regeneration]] (V): <https://textrongse.txtsv.com/products/tractors/tug-endurancer>
  - [[Diagnose Vehicle Remotely]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/baggage-cargo/press-release/21280484/textron-gse-textron-gse-introduces-the-tug-endurance-baggage-tractor>
- **Design characteristics, with citations (round 40, gap review 2026-10-03):**
  - [[Regenerative Braking]] (V): <https://textrongse.txtsv.com/products/tractors/tug-endurancer>
  - [[Electric Parking Brake]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/baggage-cargo/press-release/21280484/textron-gse-textron-gse-introduces-the-tug-endurance-baggage-tractor>
  - [[Bluetooth Interface]] (V): <https://www.aviationpros.com/ground-support-worldwide/gse/baggage-cargo/press-release/21280484/textron-gse-textron-gse-introduces-the-tug-endurance-baggage-tractor>

- **Architecture realization — remote vehicle diagnostics:** published behavior supports [[Remote Vehicle Diagnostics Design]]. [[Vehicle Diagnostic Data Acquisition Logic]] and [[Remote Vehicle Diagnostic Service]] are allocated at **>=95% engineering confidence** because the internal diagnostic software partition is not published. The exact diagnostic protocol, controller coverage, snapshot content, wireless session, and technician tool remain product-specific.

## Aliases

- TUG Endurance

## Former ids
