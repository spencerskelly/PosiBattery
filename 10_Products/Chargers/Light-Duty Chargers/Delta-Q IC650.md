---
type: Object
subtype: electrical
id: OBJ-00083
uid: 20261002192008508skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - light-duty
  - oem-supplier
  - lithium
subtypeOf:
  - "[[Light-Duty Charger]]"
performs:
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Charge Under BMS Control]]"
hasDesign:
  - "[[Onboard Charger Mounting]]"
  - "[[USB Data Download]]"
  - "[[BMS-Directed Charge Control Design]]"
  - "[[CAN BMS-Directed Charging]]"
madeBy:
  - "[[Delta-Q Technologies]]"
hasPart:
  - "[[BMS-Directed Charge Control Firmware]]"
---

# Delta-Q IC650

## Definition

Delta-Q industrial charger with CAN bus (CANopen, CiA 419) for on-board or off-board integration with lead-acid and lithium packs.

## Notes

- Delta-Q says the IC650 Comm versions support CAN bus using an isolated physical layer and CANopen, with the CiA 419 charger device profile, for on-board or off-board use; with lithium, the charger acts as a slave to the BMS, which monitors cell voltages and temperatures and controls charging. Source: Delta-Q news release and EE Power report (T1), retrieved 2026-10-02. <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
- **Scope note (Q11):** light-duty OEM charger; included as the clearest example of the charger-as-slave-to-BMS pattern.
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Lithium-Ion Battery]] (V): <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
  - [[Charge Under BMS Control]] (V): <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
- **Design characteristics, with citations:**
  - [[Onboard Charger Mounting]] (V): <https://eepower.com/new-industry-products/delta-q-introduces-can-bus-functionality-to-the-ic650-charger/>
- Delta-Q's IC650 data sheet (hosted by a reseller, 2016 copyright) lists models 24 V / 27 A, 36 V / 18 A and 48 V / 13.5 A, lead-acid (wet, AGM, gel) and lithium chemistries, on- and off-board configurations, optional CAN bus, USB host port for data download and software upgrade, built-in charge cycle tracking, and a California Energy Commission compliance mark. Source: Delta-Q IC650 data sheet (T3 (reseller-hosted)), retrieved 2026-10-02. <https://www.simpower.co.nz/wp-content/uploads/2025/02/DQIC650-48_13.5.pdf>
- Reseller listings give 650 W maximum output, 252 x 186 x 80 mm, 2.4 kg, universal AC input 85-265 VAC, 45-65 Hz, IEC 320 C14 inlet, M6 threaded DC terminals; a catalog summary adds a sealed die-cast aluminum housing, CAN bus and Modbus communication, QuiQ charging profiles for popular battery brands and a USB host port. Source: Reseller listings and catalog summary (T3/T4), retrieved 2026-10-02. <https://frankiesautoelectrics.com.au/products/delta-q-940-0006-ic650-48v-13-5a-industrial-battery-charger-canbus>
- A catalog excerpt gives IP66 and an 85-270 V AC range for the IC650 series. Source: SimPower product page (T3), retrieved 2026-10-02. <https://www.simpower.co.nz/product/chargers-power-supplies/lithium-ion-polymer-chargers/delta-q-dqic650-48-13-5-charger/>
- **Conflict-visible (C57, C58):** the AC range is 85-265 VAC in the data sheet and listings but 85-270 V on one product page. Lester's Summit Series II 650 W sheet matches the IC650 on power (650 W), voltages (24, 36, 48 V), 18 A and 13.5 A currents, AC range and IP66, but differs on 24 V current (25 A versus 27.1 A) and size (287 x 183 x 93 mm versus 252 x 186 x 80 mm). Whether the two are related is not established; see [[Lester Summit Series II]].
- **Design characteristics, with citations (data sheet):**
  - [[USB Data Download]] (V): <https://www.simpower.co.nz/wp-content/uploads/2025/02/DQIC650-48_13.5.pdf>
- The Delta-Q IC650 sheet (Downloads/DQIC650-48_13.5.pdf) lists 24 V at 27 A, 36 V at 18 A and 48 V at 13.5 A, 650 W, lead acid (wet, AGM, gel) and lithium, on- and off-board versions, optional CAN, USB host port, for scissor lifts, lift trucks, floor care machines and golf cars. Source: Delta-Q IC650 sheet (read round 20) (T1), retrieved 2026-10-03. <https://www.simpower.co.nz/>
- Delta-Q says every lead-acid charge algorithm has three stages: Bulk (most energy returned at maximum power or current, exit at a conservative target voltage), Absorption (constant voltage while the current tapers) and Finish (a constant-current finish, sized to the battery as its maker specifies, used in cyclic applications); algorithms are developed with battery manufacturers, the IC650 datasheet lists up to 25 field-programmable charge profiles, a reseller lists 16 lead-acid and 2 lithium profiles preloaded and more than 200 developed, some algorithms are temperature compensated and need the charger's temperature sensor, and Delta-Q advises monitoring a new battery and algorithm pair for at least three cycles. Source: Delta-Q support articles, IC650 datasheet and reseller listing (T1/T3), retrieved 2026-10-03. <https://support.delta-q.com/hc/en-us/articles/360015387312-What-is-an-Algorithm-Charge-Profile>
- Delta-Q says lithium packs need a BMS and are generally charged at constant current until a target voltage; its lithium chargers use an algorithm-only method (charger and BMS do not communicate; the charger follows the battery or BMS maker's algorithm to the target voltage and the BMS may close or open a contact to enable or disable charging) or a remote-control method over CAN where the charger follows the BMS and can be commanded to deliver maximum voltage and current; it advises charging lithium by direct BMS communication, offers generic lithium algorithms that charge to a listed voltage, and warns against lead-acid algorithms on lithium because of overcharge risk. Source: Delta-Q support article FAQ164 and Delta-Q newsletter (T1), retrieved 2026-10-03. <https://support.delta-q.com/hc/en-us/articles/14188856858893-Choosing-an-Algorithm-for-a-Lithium-Battery>

- **Architecture realization — BMS-directed charging:** published behavior supports [[BMS-Directed Charge Control Design]] and the CAN-specific [[CAN BMS-Directed Charging]] path. [[BMS-Directed Charge Control Firmware]] is allocated at **>=95% engineering confidence** because charger-side executable control is required while the internal software partition is unpublished. The exact BMS message set, timeout/fallback behavior, and safety handoff remain product-specific.

## Aliases

- IC650


## Former ids
