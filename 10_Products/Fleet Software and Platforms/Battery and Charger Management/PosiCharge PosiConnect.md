---
type: Object
subtype: software
id: OBJ-00302
uid: 20261003143453036skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - posicharge-baseline
  - scope-oem-option
  - software
subtypeOf:
  - "[[Battery and Charger Management Software]]"
describedBy:
  - "[[Document - PosiCharge PosiConnect Product Page]]"
performs:
  - "[[Configure Device from Mobile App or PC]]"
madeBy:
  - "[[PosiCharge]]"
offeredWith:
hasDesign:
  - "[[Device Configuration and Service Design]]"
  - "[[Mobile App Interface]]"
  - "[[PosiCharge PosiGuard]]"
---

# PosiCharge PosiConnect

## Definition

PosiCharge mobile app that connects to PosiGuard for on-site configuration and status.

## Notes

- Mobile companion that connects with PosiGuard via Bluetooth, QR scan, or search. Public page lists live battery status, fault alerts, configurable thresholds, time-range data extraction, firmware updates, and Admin/Technician/Operator roles. App-store content says it is for on-site PosiGuard BMID management and directs centralized fleet management to PosiLink. Source: official PosiCharge page for PosiConnect, as summarized in the vault's Public Evidence Register (PUB-011 and PUB-012, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/posiconnect/>
- **Baseline confidence (PosiConnect):** Verified public—product level. **Still needed:** Supported OS/device versions; authentication/identity lifecycle; role permissions; update security; offline behavior; data export and synchronization; service and support ownership.
- **Functions performed, with citations:**
  - [[Configure Device from Mobile App or PC]] (V): <https://posicharge.com/products/posiconnect/>

- **Architecture realization — configuration and service:** published material supports [[Device Configuration and Service Design]] with the specific front-end path [[Mobile App Interface]]. Transport details remain represented by the product's verified communication interfaces.

## Aliases

- PosiConnect

## Former ids
