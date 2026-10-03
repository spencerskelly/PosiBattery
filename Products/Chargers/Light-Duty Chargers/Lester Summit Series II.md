---
type: Object
subtype: electrical
id: OBJ-00082
uid: 20261002192008507skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - charger
  - light-duty
  - lithium
subtypeOf:
  - "[[Light-Duty Charger]]"
describedBy:
  - "[[Document - Lester Summit Series II 1425 W Data Sheet (06-2023)]]"
performs:
  - "[[Charge Lithium-Ion Battery]]"
  - "[[Charge Under BMS Control]]"
  - "[[Compensate Charge for Battery Temperature]]"
  - "[[Manage Chargers Remotely]]"
  - "[[Identify Battery by Voltage]]"
hasDesign:
  - "[[Multi-Voltage Output]]"
  - "[[Onboard Charger Mounting]]"
madeBy:
  - "[[Lester Electrical]]"
---

# Lester Summit Series II

## Definition

Lester multi-voltage 24, 36 and 48 V charger family (650, 1050 and 1425 W) for lead-acid and lithium, with CAN, Bluetooth and cloud profile updates.

## Notes

- The data sheets list 650 W, 1050 W and 1425 W models, 24/36/48 V multi-voltage, lead-acid (wet, AGM, gel), lithium and custom battery types, a battery temperature input (sensor optional), CAN bus (CANopen) communication with a two-wire vehicle or battery interface, and DOE, CEC and NRCan compliance. Source: Lester Summit Series II data sheets (T3 (distributor-hosted)), retrieved 2026-10-02. <https://www.rjbatt.com.au/media/nufe2twh/summit-series-ii_650w_data-sheet_060223.pdf>
- A reseller says all Summit Series II chargers have Bluetooth and cloud connectivity, with app control and new charging profiles pulled from the cloud and pushed to the charger. Source: Voltloop product page (T3), retrieved 2026-10-02. <https://voltloop.ca/products/summit-series-ii-charger-1050w-24v-36v-48v>
- A distributor lists the 650 W model as IP66 with a multicolor charge LED and on-board mounting holes, for 130 to 325 Ah batteries. Source: Akkusys shop (T3), retrieved 2026-10-02. <https://akkusys.shop/en/accessories/chargers-of-all-types/4199/lester-electrical-summit-series-ii-industrial-charger-650w-for-36/48v-18a/13.5a-without-connector>
- **Scope note (Q11):** light-duty power (up to 1.4 kW); included as a comparison point for battery-ID and CAN features, not as a forklift fast charger.
- **Functions performed, with citations** (V = verified this pass):
  - [[Charge Lithium-Ion Battery]] (V): <https://www.rjbatt.com.au/media/nufe2twh/summit-series-ii_650w_data-sheet_060223.pdf>
  - [[Charge Under BMS Control]] (V): <https://www.rjbatt.com.au/media/nufe2twh/summit-series-ii_650w_data-sheet_060223.pdf>
  - [[Compensate Charge for Battery Temperature]] (V): <https://www.rjbatt.com.au/media/nufe2twh/summit-series-ii_650w_data-sheet_060223.pdf>
  - [[Manage Chargers Remotely]] (V): <https://voltloop.ca/products/summit-series-ii-charger-1050w-24v-36v-48v>
  - [[Identify Battery by Voltage]] (V): <https://jspowersolutions.b2bwave.com/products/view/492>
- **Design characteristics, with citations:**
  - [[Multi-Voltage Output]] (V): <https://www.rjbatt.com.au/media/nufe2twh/summit-series-ii_650w_data-sheet_060223.pdf>
  - [[Onboard Charger Mounting]] (V): <https://akkusys.shop/en/accessories/chargers-of-all-types/4199/lester-electrical-summit-series-ii-industrial-charger-650w-for-36/48v-18a/13.5a-without-connector>
- **Round 11 document (1425 W):** Source: [[Document - Lester Summit Series II 1425 W Data Sheet (06-2023)]] (T1, local copy; original <https://www.rjbatt.com.au/media/somkvf25/summit-series-ii_1425w_v2_data-sheet_060223.pdf>), absorbed 2026-10-02.
| Parameter | Value as stated |
|---|---|
| Models | 48 V/30 A (32310), 36 V/40 A (29610), 24 V/40 A (29510), 24-48 V multi-voltage 40-30 A (30510) |
| AC input | 100-240 Vac rated; 85-265 Vac operating (below 108 Vac reduced power); 50-60 Hz; single-phase; under 15 A |
| Efficiency | above 91% peak, DOE test procedure at 115 Vac, AC and DC losses included |
| DC output | power 1200 W and 1425 W; nominal 24/36/48 Vdc; maximum 36/54/72 Vdc; max current 40/40/30 A; minimum start-up 10 Vdc |
| Batteries | lead-acid (wet, AGM, gel), lithium, custom |
| Interfaces | Bluetooth apps for Apple and Android; CANopen and SAE J1939 standard; wake-up signal; lockout single wire; remote LED; battery temperature connector |
| LEDs | charge complete (green), charge status (yellow), AC present (blue), fault (red) |
| Environment | IP66, NEMA 4; operating -25 to 60 C; storage -40 to 85 C; natural convection |
| Mechanical | 13.438 x 8.188 x 4.531 in (341 x 208 x 115 mm); 13.428 lb (6.09 kg) |
| Safety | UL recognized/listed; cUL/CSA; FCC Part 15; ICES-003; EN; CE; RCM; DOE and CEC efficiency (CEC-approved lab in Lincoln, NE) |
- **Conflicts (C46):** the sheet lists Bluetooth apps and says nothing of cloud connectivity, which earlier notes took from a reseller; earlier notes said CAN bus (CANopen), the sheet adds SAE J1939. The sheet also invites readers to ask about 'Sigma', a product not yet identified (see [[Unidentified Products Review]]).
- **Round 12 (650 W sheet in the repo, Downloads/summit-series-ii_650w_data-sheet_060223.pdf):** 650 W models 48 V / 13.5 A, 36 V / 18 A, 24 V / 25 A, and 36-48 V multi-voltage; above 90% peak efficiency (DOE test, 115 Vac); 287 x 183 x 93 mm; IP66 and NEMA 4; Bluetooth apps, CANopen and SAE J1939; battery temperature input. Comparison with the Delta-Q IC650 is logged as C58. A distributor listing earlier cited for the 650 W (Akkusys) gives 252 x 186 x 80 mm, which matches the Delta-Q figure, not Lester's sheet, so that listing may mix products (not relied on for size).

## Aliases

- Summit Series II
- Summit Series 2


## Former ids
