---
type: Object
subtype: electrical
id: OBJ-00058
uid: 20261002191446801skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
subtypeOf:
  - "[[Industrial Modular Charger]]"
describedBy:
  - "[[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]]"
performs:
  - "[[Continue Charging Through Module Fault]]"
  - "[[Desulfate Battery During Charge]]"
  - "[[Charge in Cold Storage]]"
  - "[[Charge Battery by Opportunity]]"
  - "[[Equalize Battery on Schedule]]"
  - "[[Adapt Charge to Battery Condition]]"
hasDesign:
  - "[[Lead-Acid Desulfation Charge Control Design]]"
  - "[[Modular Power Modules]]"
  - "[[Adaptive Charge Profile Control Design]]"
  - "[[Diagnostic-Loop Adaptive Charging]]"
madeBy:
  - "[[EnerSys]]"
hasPart:
  - "[[Desulfation Charge Control Firmware]]"
  - "[[Adaptive Charge Profile Control Firmware]]"
  - "[[EnerSys]]"
---

# EnerSys IMPAQ Charger

## Definition

EnerSys modular high-frequency charger line for material handling and floor-care equipment.

## Notes

- The guide describes IMPAQ chargers as having a flexible modular design that automatically maintains peak performance, for material handling equipment and floor cleaning. Source: EnerSys IMPAQ and NexSys+ guide (T1), retrieved 2026-10-02. <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
- **Design characteristics, with citations:**
  - [[Modular Power Modules]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>
- **Functions performed, with citations (round 11 document):**
  - [[Continue Charging Through Module Fault]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Desulfate Battery During Charge]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge in Cold Storage]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Charge Battery by Opportunity]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
  - [[Equalize Battery on Schedule]] (V): <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf> (also [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]])
- **Round 11 document:** Source: [[Document - EnerSys IMPAQ and NexSys+ Charger Product Guide (AMER 0125)]] (T1, local copy; original <https://www.enersys.com/490f6e/globalassets/documents/product-documentation/nexsys/modular-charger/amer/impaq-nexsys-plus-modular-charger-product-guide-1020.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Efficiency | up to 94% |
| Profiles | standard flooded profile and proprietary NexSys TPPL profiles; chart also shows opportunity, cold storage, desulfation, auto equalization |
| Display | intuitive LCD screen with programmable menu |
| Fault handling | self-diagnostics; modules switched on and off automatically; automatic minor-fault bypass |
| Battery compatibility (chart) | flooded (standard, opportunity), valve-regulated, AGM and gel, NexSys TPPL; no NexSys iON |
| Ideal applications (chart) | light to heavy material handling, cold storage, floor care and ground support equipment (manual), other equipment such as scissor lifts |
| Ratings | not given (n/s) |
- **Correction (C43):** an earlier link between this charger and the Wi-iQ monitor was withdrawn; the chart shows no Wi-iQ temperature adjustment for IMPAQ.
- Listed in the Logisnext Promatch parts program for Mitsubishi, Cat, Jungheinrich and UniCarriers trucks (2025). Source: Logisnext Americas release (T1), retrieved 2026-10-03. <https://www.logisnextamericas.com/en/logisnext/news/mla-enersys-expand-power-solutions-for-material-handling-operations>
- EnerSys' IMPAQ owner's manuals list charge profile codes: P21 STDWL standard waterless wet-cell profile (IUI), P22 HDUTY heavy-duty wet-cell pulse profile that diagnoses the battery status or capacity through continuous current loops, P19 FAST for flooded batteries with air mix (battery capacity, temperature and equalize values must be set and a programmed Wi-iQ fitted), P07 OPP opportunity charge for PzQ cells (finish current 5 percent), P25 LOWCHG low-rate charge, and NexSys TPPL profiles P31 NXBLOC (bloc), P29 NXSTND (2 V normal) and P30 NXFAST (2 V fast, charge rate 0.18 to 0.40 C5 with a FAST-programmed Wi-iQ); letter codes include IEI (constant current, constant voltage, constant current) with user-configurable settings, a gel IEI profile, O for opportunity and an IEIE (constant current, constant voltage, constant current, constant voltage) type; a weekly equalize charge can be programmed, an opportunity profile needs time scheduled after the weekly equalize for cooling, and refresh or maintenance charging is a function. Source: EnerSys IMPAQ and NexSys+ charger owner's manuals (T1), retrieved 2026-10-03. <https://integration.enersys.com/49bcd9/globalassets/documents/product-documentation/impaq/emea/emea-en-om-impaq-1022.pdf>
- **Functions performed, with citations:**
  - [[Adapt Charge to Battery Condition]] (V): <https://integration.enersys.com/49bcd9/globalassets/documents/product-documentation/impaq/emea/emea-en-om-impaq-1022.pdf>
  - [[Charge Battery by Opportunity]] (V): <https://integration.enersys.com/49bcd9/globalassets/documents/product-documentation/impaq/emea/emea-en-om-impaq-1022.pdf>
  - [[Equalize Battery on Schedule]] (V): <https://integration.enersys.com/49bcd9/globalassets/documents/product-documentation/impaq/emea/emea-en-om-impaq-1022.pdf>

- **Architecture realization — adaptive charge profile:** published behavior supports [[Adaptive Charge Profile Control Design]] with [[Diagnostic-Loop Adaptive Charging]]. [[Adaptive Charge Profile Control Firmware]] is allocated at **>=95% engineering confidence** because the adaptive control behavior is explicit while the internal firmware partition is unpublished.

- **Architecture realization — desulfation:** published product behavior explicitly includes a desulfation cycle/profile. [[Lead-Acid Desulfation Charge Control Design]] is therefore allocated directly; [[Desulfation Charge Control Firmware]] is allocated at **>=95% engineering confidence** because profile execution requires controller logic while the internal software partition is unpublished. No proprietary waveform or dedicated desulfation hardware is assumed.

## Aliases

- IMPAQ


## Former ids
