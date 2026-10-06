---
type: Object
subtype: electrical
id: OBJ-00326
uid: 20261003152905109skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - scope-oem-option
  - truck-device
  - truck-oem-option
  - vehicle-accessory
subtypeOf:
  - "[[Operator Display]]"
performs:
  - "[[Display Battery Status to Operator]]"
  - "[[Display Truck Status to Operator]]"
  - "[[Indicate Maintenance Due]]"
hasDesign:
  - "[[Battery Discharge Indicator]]"
  - "[[Vehicle-Mounted Display]]"
hasPart:
  - "[[Vehicle-Mounted Display Module]]"
  - "[[Battery Discharge Indicator Module]]"
  - "[[Operator Display Controller Circuit]]"
  - "[[Operator Display HMI Firmware]]"
madeBy:
  - "[[Linde Material Handling]]"
---

# Linde MT18 Multifunction Display

## Definition

Display on the Linde MT18 pallet truck with hour meter, maintenance indication, battery discharge indicator and internal fault codes.

## Notes

**Summary:**
Standard multifunction display on the Linde MT18 lithium-ion walkie pallet truck.

**Marketed features:**
- Hour meter
- Maintenance indication
- Battery discharge indicator
- Internal fault-code indication

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Linde Material Handling (T1), retrieved 2026-10-04. <https://www.linde-mh.us/content/dam/linde/en/images/products/pallet-trucks/1133-03/Linde_MT18_Spec_Sheet_V2.pdf>
- Wolter (T3), retrieved 2026-10-04. <https://www.wolterinc.com/woltergroup/media/pdf-s/manufacturer%20catalogs/kion_full_product_catalog_2024_v2-3-(1).pdf>

- The KION North America catalog says the MT18 (Series 1133-03) features a multifunction display with hour meter, maintenance indication, battery discharge indicator and internal fault code indication. Source: KION North America catalog 2023 (T1), retrieved 2026-10-03. <https://expoproduction.thelogisticsworld.com/wp-content/themes/theme-summitexpo/directorio/assets/fichas/d0631ac8-a3f8-4b21-8640-bf6f41154ae8.pdf>
- **Functions performed, with citations:**
  - [[Display Battery Status to Operator]] (V): <https://expoproduction.thelogisticsworld.com/wp-content/themes/theme-summitexpo/directorio/assets/fichas/d0631ac8-a3f8-4b21-8640-bf6f41154ae8.pdf>
- **Design characteristics, with citations:**
  - [[Vehicle-Mounted Display]] (V): <https://expoproduction.thelogisticsworld.com/wp-content/themes/theme-summitexpo/directorio/assets/fichas/d0631ac8-a3f8-4b21-8640-bf6f41154ae8.pdf>
- **Architecture realization — truck status display:** the hour meter, maintenance indication and internal fault-code display are verified truck-status outputs. The existing [[Vehicle-Mounted Display Module]], [[Operator Display Controller Circuit]], and [[Operator Display HMI Firmware]] realization is reused; controller/HMI internals remain **>=95% engineering-confidence assumptions**.
- **Architecture realization — operator battery display:** the multifunction display and battery-discharge indication are verified. [[Vehicle-Mounted Display Module]] and [[Battery Discharge Indicator Module]] capture those physical roles. [[Operator Display Controller Circuit]] and [[Operator Display HMI Firmware]] are **>=95% engineering-confidence assumptions**; the source does not publish the internal electronics, software partition, or battery-data transport.
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Controls and Display]]; connects to [[Truck Controller and CAN Bus]]; acts on [[Truck Controls and Display]]. See [[Truck Part Connection Register]].
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Display Truck Status to Operator]] (V): <https://www.linde-mh.us/content/dam/linde/en/images/products/pallet-trucks/1133-03/Linde_MT18_Spec_Sheet_V2.pdf>
  - [[Indicate Maintenance Due]] (V): <https://www.linde-mh.us/content/dam/linde/en/images/products/pallet-trucks/1133-03/Linde_MT18_Spec_Sheet_V2.pdf>

## Aliases

- MT18 display

## Former ids
