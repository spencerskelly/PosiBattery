---
type: Info
subtype:
id: INFO-90001
uid: 20261005130510005skellyspencer
status: Draft
tags:
  - bmid
  - product-architecture
  - local-model
  - integration-context
describes:
  - "[[PosiCharge BMID]]"
---

# PosiCharge BMID Product Assembly Local Model

## Purpose

Provide the first governed Local Model representation for the [[PosiCharge BMID]] product-development pilot without inventing unsupported internal PCB, harness, connector, or protocol details.

This note is an **integration assembly context**, not a product BOM. The traction battery and charger occurrences below are external context used to express interaction topology. They do not become `hasPart` children of the BMID.

The BMID, battery, and charger definitions are abstract reusable families, so their contextual occurrences use `usage: variant`. A configured model resolves each occurrence to one concrete descendant without duplicating the reusable Object definitions.

## Modeling Boundary

The first assembly model intentionally captures only two evidence-backed interaction paths:

1. battery-side information entering a BMID-family device;
2. supported battery information leaving the BMID toward a compatible charger.

Physical mounting, exact sensor wiring, connector pinout, protocol selection, BMS ownership, cloud integration, and service-tool topology remain outside this first assembly until stronger product-specific evidence supports them.

## Local Model
<!-- MDSE:LOCAL-MODEL START schema=0.2 -->

### Part Occurrences

#### BMID Device
- definition: [[PosiCharge BMID]]
- usage: variant
- identifier: BMID
^part-20261005130510006skellyspencer

#### Traction Battery
- definition: [[Industrial Traction Battery]]
- usage: variant
- identifier: Battery
^part-20261005130510007skellyspencer

#### Compatible Charger
- definition: [[Industrial Battery Charger]]
- usage: variant
- identifier: Charger
^part-20261005130510008skellyspencer

### Local Interfaces

#### Battery Interaction — Battery Side
- definition: [[iBMID - Battery Interaction|BMID Battery Interaction]]
- part: [[#^part-20261005130510007skellyspencer|Traction Battery]]
- identifier: Battery interaction
^ep-20261005130510009skellyspencer

#### Battery Interaction — BMID Side
- definition: [[iBMID - Battery Interaction|BMID Battery Interaction]]
- part: [[#^part-20261005130510006skellyspencer|BMID Device]]
- identifier: BMID battery interaction
^ep-20261005130510010skellyspencer

#### Charger Communication — BMID Side
- definition: [[iBMID - Charger Communication|BMID Charger Communication]]
- part: [[#^part-20261005130510006skellyspencer|BMID Device]]
- identifier: BMID charger communication
^ep-20261005130510011skellyspencer

#### Charger Communication — Charger Side
- definition: [[iBMID - Charger Communication|BMID Charger Communication]]
- part: [[#^part-20261005130510008skellyspencer|Compatible Charger]]
- identifier: Charger BMID communication
^ep-20261005130510012skellyspencer

### Connections

#### Battery-to-BMID Information Path
- endpointA: [[#^ep-20261005130510009skellyspencer|Battery interaction]]
- endpointB: [[#^ep-20261005130510010skellyspencer|BMID battery interaction]]
- identifier: Battery sensing path
^conn-20261005130510013skellyspencer

##### Battery Sensing Information
- definition: [[BMID Battery Sensing Data]]
- identifier: Battery sensing data
- endpointA: transmit
- endpointB: receive
^flow-20261005130510014skellyspencer

#### BMID-to-Charger Information Path
- endpointA: [[#^ep-20261005130510011skellyspencer|BMID charger communication]]
- endpointB: [[#^ep-20261005130510012skellyspencer|Charger BMID communication]]
- identifier: Charger information path
^conn-20261005130510015skellyspencer

##### Charger Battery Information
- definition: [[BMID Charger Battery Information]]
- identifier: Battery information to charger
- endpointA: transmit
- endpointB: receive
^flow-20261005130510016skellyspencer

<!-- MDSE:LOCAL-MODEL END -->

## Architecture Interpretation

The Local Model records are contextual occurrences. The reusable definitions remain authoritative in their own notes.

- The BMID occurrence resolves to a concrete member of the [[PosiCharge BMID]] specialization family.
- The battery occurrence resolves to a concrete [[Industrial Traction Battery]] specialization.
- The charger occurrence resolves to a concrete [[Industrial Battery Charger]] specialization.
- The two Port definitions deliberately remain logical so this model does not invent physical connectors or protocol assignments.
- Item Flow definitions are reusable and abstract; direction is supplied by their Local Model occurrences on each connection.

## Deferred Architecture

The following remain explicit gaps rather than inferred structure:

- internal BMID electronics, PCBAs, power supply, memory, MCU, or enclosure composition;
- temperature-sensor physical connection and connector details;
- current-sensor and electrolyte-level hardware;
- CAN, Bluetooth, serial, or LoRa protocol/port selection for any family-wide occurrence;
- Battery Rx cellular/cloud topology;
- PosiGuard service/configuration topology;
- BMS ownership and lithium-specific charge-control paths.

These can be added as reusable Objects, Ports, Item Flows, and Local Model occurrences when a specific product variant and authoritative architecture evidence support them.
