---
type: Object
subtype: electrical
id: OBJ-00056
uid: 20261002165629066skellyspencer
status: Draft
tags:
  - adjacent
  - battery-market-reference
  - commercial-product
  - gateway
  - scope-aftermarket
  - site-infrastructure
subtypeOf:
  - "[[Battery Telematics and Connectivity Device]]"
performs:
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Bluetooth Interface]]"
  - "[[Cellular Communication Interface]]"
  - "[[Cloud Battery Data Upload Design]]"
  - "[[Gateway-Mediated Cloud Upload]]"
madeBy:
  - "[[Philadelphia Scientific]]"
hasPart:
  - "[[Battery Data Gateway Upload Service]]"
  - "[[Philadelphia Scientific]]"
---

# Philadelphia Scientific eGO!gateway

## Definition

Philadelphia Scientific mains-powered gateway that collects data from eGO! devices over Bluetooth and uploads it over cellular.

## Notes

**Summary:**
Philadelphia Scientific mains-powered gateway that collects data from eGO! monitors over Bluetooth and uploads it over cellular.

**Marketed features:**
- Works with all eGO! monitors; collects data at the end of each charge cycle
- Uploads to batterymanagement.net; no engineer site visits
- 4G/3G/2G global cellular; Bluetooth range about 70 m
- Wall mount with power and internet cables; DHCP auto-configuration
- 90-264 VAC; 0-50 C; status LEDs
- Two-year warranty

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Philadelphia Scientific (T1), retrieved 2026-10-04. <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>

- The page says the eGO!gateway captures performance data from an eGO! installed on a battery and uploads it to the online portal, runs on 90 to 264 V AC, works on 4G/3G/2G cellular, has Bluetooth range of about 70 m, operates 0 to 50 C, and has a 2-year warranty. Source: PhilSci eGO!gateway page (T1), retrieved 2026-10-02. <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>
- **Locus:** site infrastructure, not battery-installed.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>
- **Design characteristics, with citations:**
  - [[Bluetooth Interface]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>
  - [[Cellular Communication Interface]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>
- **Sources used for the mapping above:** PhilSci eGO!gateway page <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-gateway/>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — cloud battery upload:** this gateway explicitly receives eGO! monitor data over Bluetooth and forwards it to batterymanagement.net over cellular. It therefore implements both [[Cloud Battery Data Upload Design]] and [[Gateway-Mediated Cloud Upload]], with [[Battery Data Gateway Upload Service]] representing the reusable gateway software role.

## Aliases

- eGO!gateway


## Former ids
