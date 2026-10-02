---
type: Object
subtype: electrical
id: OBJ-00025
uid: 20261002161409688skellyspencer
status: Draft
tags:
  - battery-landscape
  - category
abstract: true
subtypeOf:
  - "[[Battery-Connected Product]]"
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
  - "[[Battery Product Landscape]]"
---

# Industrial Battery Charger

## Definition

Stationary charging equipment for industrial batteries. Adjacent to the battery rather than installed on it, but defines the interface most battery-installed devices exist to serve.

## Notes

- **Locus:** adjacent (charger-side). Included because the user's later focus is competitors to PosiCharge BMIDs, which only exist in relation to a charger.
- Fronius SelectION is a lithium-ion forklift charger range using BatteryLink CAN with automatic baud-rate detection; its Charge & Connect software shows charger availability, connected battery status and consumption. Source: Warehouse News report on Fronius (T2), retrieved 2026-10-02. <https://warehousenews.co.uk/2022/11/fronius-launches-range-of-lithium-ion-battery-chargers/>
- PosiCharge states fast charging can take a 48 V, 1000 Ah battery from 20 to 80 percent in about an hour with no cool-down period (vendor claim). Source: PosiCharge FAQ (T1), retrieved 2026-10-02. <https://www.posicharge.com/faq/>
- Crown offers FS3 and HFM3 charger series with an optional BMID module. Source: Crown (T1), retrieved 2026-10-02. <https://crown.com/en-vn/batteries-and-chargers/vhfm3-charger.html>
- **Charge-start modes observed:** (a) battery identified by an analog or wireless ID device such as a BMID; (b) CAN from a lithium BMS; (c) voltage-only with default settings. Observed on PosiCharge ProCore Edge and ProCore; not established for other vendors.
- **Unverified superlative:** Green Cubes calls itself the only maker of both Li-ion batteries and chargers for material handling. Not tested against other vendors.
- **Gaps:** charger classes (opportunity, fast, conventional), power ranges and ratings, standards, and competitor list are not yet researched.

## Aliases

- Motive power charger
- Forklift charger

## Former ids
