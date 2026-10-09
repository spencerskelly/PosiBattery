---
type: Object
subtype: software
id: OBJ-00304
uid: 20261003143453038skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - posicharge-baseline
  - scope-oem-option
  - software
subtypeOf:
  - "[[Battery and Charger Management Software]]"
performs:
  - "[[Manage Chargers Remotely]]"
madeBy:
  - "[[PosiCharge]]"
hasDesign:
  - "[[Remote Charger Management Design]]"
hasPart:
  - "[[Remote Charger Management Service]]"
  - "[[PosiCharge]]"
---

# PosiCharge SkyLink

## Definition

PosiCharge cloud platform for charger performance, energy and charge-session reporting and remote support.

## Notes

- Cloud-based charger and energy reporting platform. Public page describes real-time charger performance/energy visibility, charge-session records, vehicle-level activity using BMID, charger summaries, remote troubleshooting, manual billing support, and OTA firmware updates. Source: official PosiCharge page for SkyLink, as summarized in the vault's Public Evidence Register (PUB-013, class P1/P2/P3 per that note) (T1), retrieved 2026-10-03. <https://posicharge.com/products/skylink/>
- **Baseline confidence (SkyLink):** Verified public—product level. **Still needed:** Define relationship to PosiLink; supported chargers/BMID generations; deployment/onboarding; data retention; API/export; security/cyber model; user-role and commercial model.
- **Functions performed, with citations:**
  - [[Manage Chargers Remotely]] (V): <https://posicharge.com/products/skylink/>

- **Architecture realization — remote charger management:** published material supports [[Remote Charger Management Design]]. [[Remote Charger Management Service]] represents the remote portal/application role. The exact commands, permissions, network protocol, and safety handoff remain product-specific.

## Aliases

- SkyLink

## Former ids
