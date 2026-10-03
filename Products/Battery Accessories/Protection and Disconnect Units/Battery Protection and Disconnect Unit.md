---
type: Object
subtype: electrical
id: OBJ-00024
uid: 20261002161409687skellyspencer
status: Draft
tags:
  - battery-landscape
  - category
abstract: true
subtypeOf:
  - "[[Battery-Connected Product]]"
describedBy:
  - "[[Battery Product Landscape]]"
---

# Battery Protection and Disconnect Unit

## Definition

Hardware that connects, isolates and protects a battery's power path: contactors, fuses, pre-charge circuits and related drivers.

## Notes

- **Applicability warning:** every retrieved source for this category is automotive or high-voltage EV material. Whether the same architecture is used in 24 V to 96 V forklift and GSE batteries is not established by these sources.
- An EV training source describes a pack with a main fuse, a main contactor at each end, and a pre-charge relay and resistor sequenced by the BMS. Source: HP Academy EV Fundamentals (T4), retrieved 2026-10-02. <https://www.hpacademy.com/courses/ev-fundamentals/batteries-battery-pack/>
- A Texas Instruments application brief describes an intelligent battery junction box with contactor drivers, pyro-fuse drivers and pack monitoring, and notes disconnect can use melting or pyro fuses. Source: Texas Instruments SLYY226 (T1), retrieved 2026-10-02. <https://ti.com/document-viewer/lit/html/SLYY226/GUID-81B7EF29-8949-470F-BA68-2D91DEB6A1C7>
- Littelfuse lists pack temperature-monitoring strips and fuse or protector parts for lithium battery packs. Source: Arrow Electronics article on Littelfuse (T2), retrieved 2026-10-02. <https://www.arrow.com/en/resources/articles/2024/06/littelfuse-enhances-protection-and-control-for-lithium-batteries.html>
- **Charger-side counterpart (adjacent):** Fronius describes an external stop/start function that safely disconnects the charger to avoid sparking, and PosiCharge describes an anti-arcing disconnect. These are charger features, not battery-installed.

## Aliases

- BDU
- Battery junction box
- Contactor and fuse assembly


## Former ids
