---
type: Info
subtype:
id: INFO-00110
uid: 20261005210000000skellyspencer
status: Draft
tags:
  - product-definition
  - bmid
  - posicharge
describes:
  - "[[PosiCharge BMID]]"
---

# PosiCharge BMID Product Abstract and Definition

## Product Abstract

The PosiCharge BMID family is a battery-installed identification, sensing, logging, and charger-interface product family used with industrial battery systems. A BMID-family device stays with the battery, provides a persistent electronic identity and supported battery-condition/history information, and exchanges supported information with compatible PosiCharge charging or fleet-management systems.

The product-family boundary includes the battery-mounted electronic device, its directly integrated sensing functions, stored battery identity/profile/history, and its product-defined external communication interfaces. The traction battery, charger power electronics, vehicle, cloud/fleet platform, and service/configuration device are external context unless a specific BMID variant explicitly incorporates that function.

Primary operating contexts are industrial MHE/forklift and airport GSE battery fleets. The core value is to carry battery identity and battery-side condition/history with the battery so compatible chargers and fleet tools can identify, monitor, and manage the battery using supported data rather than relying only on charger-side inference.

This is a family-level definition. It does not imply that every modeled child product supports every family-adjacent sensing, communication, cloud, or configuration feature.

## Product Definition

**Canonical product family:** [[PosiCharge BMID]]

**Parent classification:** [[Battery Identification and Charge Interface Device]]

**Modeled family members:**
- [[PosiCharge BMID 1]] — stakeholder-named legacy variant; public mapping remains unresolved.
- [[PosiCharge BMID 3]] — stakeholder-named variant with stated BLE, CAN, international, and E-meter options; option structure remains unresolved.
- [[PosiCharge Battery Rx]] — publicly documented smart-BMID/battery-monitor product; mapping to BMID 1 or BMID 3 remains unresolved.
- [[PosiCharge PosiGuard]] — current product described by PosiCharge as a BMID device and by the stakeholder as the next generation of BMID; exact predecessor mapping remains unresolved.

**Family-level supported behavior already represented in the model:**
- [[Measure Battery Voltage]]
- [[Measure Battery Temperature]]
- [[Estimate State of Charge]]
- [[Log Battery Events and Usage]]
- [[Identify Battery to Charger]]
- [[Report Battery Temperature to Charger]]
- [[Communicate with Charger]]
- [[Transmit Battery Data Wirelessly]]

These functions are valid at the family level only to the extent supported across the current family evidence. Child-specific functions must remain on the applicable child product. Examples include Battery Rx cellular/cloud capabilities and PosiGuard CAN, LoRa, and mobile-app functions.

**Existing reusable designs associated with the family:**
- [[Electrolyte-Immersed Temperature Sensor]]
- [[Bluetooth Interface]]

These are family-associated reusable design concepts, not proof that every family member implements the same physical design.

## Product Boundary

### In scope

- Battery-mounted BMID electronics.
- Directly integrated battery sensing defined by a BMID product.
- Battery identity/profile/history stored by the BMID.
- BMID external interfaces to compatible chargers and supported configuration/fleet systems.
- Product-family and variant structure.

### External context

- Industrial traction battery.
- PosiCharge charger power electronics and charging controller.
- MHE/forklift vehicle.
- Airport GSE vehicle.
- PosiLink/PosiNet/cloud or fleet-management systems.
- Mobile/PC configuration tools.
- Dealer/service organizations and fleet operators.

These external elements may participate in use cases and context models but are not part of the BMID product boundary unless a specific variant explicitly incorporates the function.

## Product Value

The product family exists to make battery identity and battery-side condition/history available at the battery edge. This supports compatible charging and fleet workflows including battery recognition, charge adaptation using battery information, battery usage/history tracking, and service/fleet decisions based on battery-specific data.

The product-definition model must not claim charging control authority that belongs to the charger or battery BMS. BMID provides information and supported interfaces; later requirements and architecture must distinguish sensing/data functions from charger-controlled charging behavior.

## Variant and Lifecycle Uncertainty

The model must preserve the following unresolved items rather than force a lineage:

- Which public product names map to BMID 1 and BMID 3.
- Whether Battery Rx corresponds to one of those generations or is a separate branch.
- Whether PosiGuard is strictly a successor, a parallel family member, or both depending on commercial and technical context.
- Whether BMID 3 BLE, CAN, international, and E-meter labels are options, configurations, variants, or part numbers.
- Whether a BMID 2 existed.
- How lithium support changes the BMID role relative to a battery BMS and CAN-based charger communication.

See [[PosiCharge BMID Variants]] for the current evidence-separated naming record.

## Evidence Basis

The current family framing is supported by the existing PosiCharge BMID family note, current PosiCharge product pages and manuals summarized in the vault, the dedicated variant-reconciliation research, and the modeled Battery Rx and PosiGuard product records.

No unsupported internal PCB, wiring, sensing topology, protocol behavior, or implementation detail is added by this definition.

## Modeling Rule for Phase M

This document is the concise product-framing authority for the Phase M BMID model. Detailed product facts remain on the canonical product and evidence notes. Later steps should link use cases, requirements, functions, designs, Local Model occurrences, and verification back to [[PosiCharge BMID]] rather than copying detailed evidence into this note.
