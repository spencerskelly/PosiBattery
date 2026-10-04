---
type: Info
subtype:
id: INFO-00072
uid: 20261002150858936skellyspencer
status: Draft
tags:
  - battery-market-reference
  - market-research
describes:
  - "[[Battery-Installed Device]]"
---

# Battery Installed Device Market Reference

## Definition

Research framework and evidence register for products physically installed on or integrated into batteries and battery packs, beginning with industrial forklift/MHE and GSE applications.

## Notes

### Scope boundary

**Core in-scope**
- Battery-mounted: attached to the battery/cables/cells and remains with that battery.
- Battery-integrated: built into the pack or battery assembly and remains with it.

**Track separately as adjacent**
- Vehicle-mounted: stays with the truck/GSE vehicle when batteries change.
- Charger-mounted or charger-integrated.
- Site gateway/network infrastructure.
- Cloud/software-only products.
- Temporary diagnostic equipment that is connected for a study but does not remain with the battery.

A device that connects electrically between a truck and battery but remains with the truck is adjacent unless a specific installation says otherwise.

### Initial functional families

Current modeled families:
- [[Battery Monitoring Device]]
- [[Battery Water Level Monitor]]
- [[Battery Identification and Charge Interface Device]]
- [[Battery Watering System]]

Research backlog before creating additional family Objects:
- battery management/control/protection systems;
- battery telematics/connectivity modules;
- thermal management devices;
- safety/event detection devices;
- balancing and cell-management hardware;
- heaters/cooling devices;
- asset identity/tracking devices that do not fit charger-interface products.

### Comparison dimensions

Capture these in evidence notes before promoting any of them to governed model properties:

- manufacturer and product/family;
- market status and evidence date;
- installation locus;
- intended applications;
- supported battery chemistries;
- nominal/operating voltage range where published;
- measured quantities and sensors;
- control/protection actions;
- wired and wireless communications;
- human indicators/displays;
- charger interaction;
- cloud/gateway dependency;
- installation/service method;
- environmental and enclosure claims;
- standards/certifications;
- data retention/logging;
- fleet-management integration;
- whether hardware is aftermarket, OEM-integrated, or both.

### Initial market sample

- [[EnerSys Wi-iQ]]
- [[EnerSys iQ Mini]]
- [[Philadelphia Scientific eGO!pro]]
- [[Philadelphia Scientific SmartBlinky Pro]]
- [[AMETEK Prestolite Power BID]]
- [[AMETEK Prestolite Power WBID Pro]]
- [[PosiCharge PosiGuard]]
- [[PosiCharge BMID]]
- [[Energywith withBMS BMU]]
- [[Flow-Rite Maverick Battery Watering System]]
- [[Flow-Rite Eagle Eye Elite IV]]

### Research policy

“Current” means current vendor evidence was observed on **2026-10-02**. A future review should re-check market status rather than assume a product remains current.

Do not infer missing specifications from similar products. If an installation location, chemistry, interface, or capability is unclear, record it as unknown until supported by evidence.
- **Added in the merge (2026-10-02):** [[Crown V-Force BMID]], [[Fronius TagID]] and [[AMETEK Prestolite Power BID with Ah Accumulator]] extend the sample above. Competitor comparison: [[BMID Competitor Landscape]]. Verification status of each seed product is recorded on its own note.

## Aliases

- Battery-mounted device market reference
- Battery accessory market reference


## Former ids
- INFO-00001
