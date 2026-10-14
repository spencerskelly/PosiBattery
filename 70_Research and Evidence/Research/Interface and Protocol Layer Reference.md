---
type: Info
subtype:
id: INFO-90039
uid: 20261013233000019skellyspencer
status: Draft
tags:
  - research
  - interfaces
  - protocols
  - layers
describes:
  - "[[Battery Management System]]"
  - "[[CAN Interface]]"
  - "[[Cloud Portal Integration]]"
describedBy:
  - "[[Document - Wikipedia Modbus (retrieved 2026-10-13)]]"
  - "[[Document - CiA 418 CANopen Device Profile for Battery Modules (retrieved 2026-10-13)]]"
  - "[[Document - Wikipedia Open Charge Point Protocol (retrieved 2026-10-13)]]"
  - "[[Document - Wikipedia ISO 15118 (retrieved 2026-10-13)]]"
  - "[[Document - CiA 419 CANopen Device Profile for Battery Chargers (retrieved 2026-10-13)]]"
  - "[[Document - Wikipedia CHAdeMO (retrieved 2026-10-13)]]"
  - "[[Document - Wikipedia OpenADR (retrieved 2026-10-13)]]"
  - "[[Document - CiA CAN Newsletter Industrial Battery Chargers Support CANopen (Fischer, 2020-12)]]"
  - "[[Document - Wikipedia SAE J1939 (retrieved 2026-10-13)]]"
  - "[[Document - Delta-Q J1939 and CANopen Charger Release (2018-04-12)]]"
  - "[[Document - Wikipedia MQTT (retrieved 2026-10-13)]]"
  - "[[Document - Wikipedia CAN Bus (retrieved 2026-10-13)]]"
  - "[[Document - Wikipedia CANopen (retrieved 2026-10-13)]]"
---

# Interface and Protocol Layer Reference

## Definition

A layered list of the interfaces between a battery, its charger and truck, the site, the cloud, the grid and the users, with the protocols and standards used at each layer and where the vault already models them. It is the index for the interface mapping plan in [[PosiBattery Interface and Impact Mapping Plan]].

## Notes

### Layers

| Layer | Name | Between | Protocols and standards (source) | In the vault |
|---|---|---|---|---|
| L1 | Cell and module sensing | BMS slave or sensor to BMS master inside the pack | Cell-level and controller-to-controller links, including isolated or wireless serial (W1) | Pack internal; not seen as a product interface in the vault |
| L2 | Pack power path | BMS to contactors, fuses and the charge port | Contactor and precharge control (W1) | [[Disconnect Battery on Limit Violation]] |
| L3 | Battery to truck or vehicle | BMS or battery monitor to the truck controller and display | CAN with J1939 or CANopen (W2, W3, W4); proprietary messages also exist | [[CAN Interface]], [[Communicate Battery State over CAN]], [[Command Vehicle Operating Limits over CAN]] |
| L4 | Battery to charger | BMS or identification device to the charger | CANopen CiA 418 and 419 (W11, W12, W13); J1939 or CANopen charger options (W14); custom CAN (Hyster); voltage-only or ID-based starts | [[Charge Under BMS Control]], [[CAN BMS-Directed Charging]], [[BMID Charger Battery Information]] |
| L5 | Device to local tools and gateways | Monitor, BMS or charger to phone, PC, handheld or site gateway | Bluetooth, Wi-Fi, 900 MHz, serial, USB, NFC, infrared | Existing Designs: [[Bluetooth Low Energy Interface]], [[Wi-Fi Interface]], [[900 MHz Industrial Wireless Interface]], [[RS-232 and RS-485 Serial Interface]], [[USB Battery Data Export]] |
| L6 | Device or site to cloud | Charger, monitor or gateway to a vendor cloud portal | Cellular and Wi-Fi transport; MQTT (W8) or vendor HTTPS interfaces (not read); Modbus TCP (W9) at site level | [[Cloud Portal Integration]], [[Cellular Communication Interface]], [[Cloud Battery Data Upload Service]] |
| L7 | Charger to charging back office; vehicle to charger (high level) | Charger to a network operator; vehicle to charger for plug-and-charge and V2G | OCPP (W5); ISO 15118 (W6); CHAdeMO CAN data link for DC fast charging (W10) | None in the vault; these are road-EV protocols and their use on industrial trucks is not evidenced |
| L8 | Site to grid or utility | Site energy management to utility or aggregator | OpenADR demand-response signalling (W7); IEEE 2030.5 not read (page could not be fetched) | [[Energy Management Systems for Warehouses and Production Facilities]], [[Cost Driver 08 Utilities and Energy]] |
| L9 | Cloud to users | Portals, mobile apps, reports and exports to fleet managers and administrators | Web and mobile applications; role-based access | [[Fleet Manager and Admin Digital Access Evidence]], [[Mobile App Interface]] |

Layer numbers are working labels for this note, not a governed taxonomy; the plan proposes making them one.

### Protocols and standards, from neutral sources

| Protocol or standard | Layers | What the neutral sources say | Source |
|---|---|---|---|
| ISO 11898-1/-2/-3 CAN | L3, L4 | Data link and physical layer of CAN; high speed to 1 Mbit/s with 120 ohm termination; fault-tolerant to 125 kbit/s; classic CAN has 11-bit or 29-bit identifiers and up to 8 data bytes, CAN FD up to 64 bytes | W4 |
| SAE J1939 | L3, L4 | Vehicle bus practice on CAN, 29-bit identifiers only, messages identified by parameter group number (PGN) with data items (SPN); 250 kbit/s (J1939/11, /15) or 500 kbit/s (J1939/14); proprietary PGNs in a reserved range | W2 |
| CANopen (CiA 301) | L3, L4 | Higher-layer protocol with an object dictionary, SDO (parameter access), PDO (up to 8 bytes of process data), NMT (state control) and heartbeat; profiles per device type | W3 |
| CiA 418 battery module | L4 | Battery side of a charger link: mandatory battery type, capacity, cell count, maximum charge current and temperature; optional identity, charge history, voltage, SOC, requested current, flooded-battery water level; default transmit PDO sends temperature and status on a timer; needs NMT server and heartbeat. v1.2.0 (2012) is a public specification; v1.2.1 is a working draft | W11, W13 |
| CiA 419 battery charger | L4 | Charger side of the same link: receives the battery PDOs and sends charger status; optional 'charge returned' (Ah delivered in the last charge); the charger finds the battery by reading object 1000h and configures PDO identifiers dynamically; default bit rate 125 kbit/s, charger node 10 and battery node 1; covers lead-acid and lithium | W12, W13 |
| Delta-Q CANopen and J1939 options | L3, L4 | A charger maker states it offers both CANopen and J1939 for OEM integration, including charge monitoring and software update over CAN | W14 |
| CHAdeMO | L7 | DC fast-charging system whose connector carries a CAN data link for interlock, target voltage, capacity and stop conditions; also V2G and V2H; IEC 61851-23 and -24 | W10 |
| ISO 15118 | L7 | Vehicle to grid communication: secure communication, smart charging, plug and charge with certificates; parts for network, physical, wireless and battery-information exchange (Part 12 under development) | W6 |
| OCPP | L7 | Application protocol between charging stations and a central management system; versions 1.6, 2.0.1 (IEC 63584 edition 3) and 2.1 (adds distributed energy resource control and vehicle-to-grid); stewarded by the Open Charge Alliance | W5 |
| OpenADR | L8 | Data model for automated demand-response signals from a utility or system operator to buildings and industrial sites; the page covers versions 1.0 and 2.0 only | W7 |
| MQTT | L6 | Publish-subscribe messaging through a broker over TCP, QoS 0, 1 and 2; plain-text credentials unless TLS is added; ISO/IEC 20922 | W8 |
| Modbus | L6 | Polled client-server fieldbus (RTU, ASCII, TCP on port 502) with coils and 16-bit registers; no security against unauthorized commands or interception | W9 |

Not yet sourced: GB/T 27930 and other regional charging protocols, IEEE 2030.5, SunSpec and other energy-device Modbus maps, UDS/ISO-TP diagnostics detail, CAN FD use in industrial trucks, and the J1939 parts that define battery messages. They are on the [[Document Wishlist]].

### CAN protocols stated by products in the vault

| Product | CAN detail stated | Where |
|---|---|---|
| EnerSys Wi-iQ | CANopen or J1939 | [[CAN Interface]] note |
| Inventus Smart Battery Monitor SBM-01 | auto-detects 125 kbps to 1 Mbps | [[CAN Interface]] note |
| EnerSys NexSys iON | CANopen and BMS CAN protocols on the display interface; charger CAN needed before charging starts | [[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]] |
| Orion BMS 2 | two CAN 2.0B interfaces at 125, 250, 500 or 1000 kbps; cited CANopen, J1939 and ISO 15765 compatibility | [[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]] |
| Hyster Power Cellect | custom Hyster CAN protocol between battery and charger | [[Metric - BMS and Communication]] |
| Fronius chargers | BatteryLink with automatic baud-rate detection on the charger side | [[Battery Management System]] note |
| PosiCharge BMID 3, PosiGuard, ProCore Edge | CAN stated; protocol, bit rate and message set not stated in any public source in the vault | [[CAN Interface]], [[BMS-Directed Charge Control Design]] |

### Our products' interface definitions

- **What is public:** only that BMID 3, PosiGuard and ProCore Edge use CAN or BMS-directed charging. The protocol, bit rate, message set and node roles are not in any source in the vault.
- **What is held internally:** the owner says several CAN protocols are held internally. They are not in this vault and are not described here.
- **Caution:** this repository is public. Internal message definitions (identifiers, scaling, state machines) must not be committed without a decision; the plan proposes three levels of detail (public standard, product-declared, internal reference by identifier only).

### Gaps

- Only two Ports and two Item Flows exist (BMID). Interfaces are otherwise Designs, and protocols appear only in prose.
- No note exists for any protocol; the table above is the only place they are listed.
- No grid, utility or aggregator organization note exists, and no cloud-provider note.
- Conflicts: C204 and C205 in [[Battery Product Landscape Conflicts and Open Questions]].

## Sources

- **W2** [[Document - Wikipedia SAE J1939 (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/SAE_J1939>
- **W3** [[Document - Wikipedia CANopen (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/CANopen>
- **W4** [[Document - Wikipedia CAN Bus (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/CAN_bus>
- **W5** [[Document - Wikipedia Open Charge Point Protocol (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/Open_Charge_Point_Protocol>
- **W6** [[Document - Wikipedia ISO 15118 (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/ISO_15118>
- **W7** [[Document - Wikipedia OpenADR (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/OpenADR>
- **W8** [[Document - Wikipedia MQTT (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/MQTT>
- **W9** [[Document - Wikipedia Modbus (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/Modbus>
- **W10** [[Document - Wikipedia CHAdeMO (retrieved 2026-10-13)]] <https://en.wikipedia.org/wiki/CHAdeMO>
- **W11** [[Document - CiA 418 CANopen Device Profile for Battery Modules (retrieved 2026-10-13)]] <https://can-cia.org/can-knowledge/cia-418-canopen-device-profile-for-battery-modules>
- **W12** [[Document - CiA 419 CANopen Device Profile for Battery Chargers (retrieved 2026-10-13)]] <https://can-cia.org/can-knowledge/cia-419-canopen-device-profile-for-battery-chargers>
- **W13** [[Document - CiA CAN Newsletter Industrial Battery Chargers Support CANopen (Fischer, 2020-12)]] <https://old.can-cia.org/fileadmin/resources/documents/publications/cnlm_issues/december_2020/20-4_p18_industrial_battery_chargers_support_canopen_olga_fischer_cia.pdf>
- **W14** [[Document - Delta-Q J1939 and CANopen Charger Release (2018-04-12)]] <https://www.manufacturing.net/product-announcement/2018/04/delta-q-technologies-includes-j1939-capabilities-better-support-electric-vehicle-manufacturers>
- Product evidence: [[Document - EnerSys NexSys iON Operating Manual (Spanish, GLOB-ES-OM-NEX-ION 0323)]], [[Document - Orion BMS 2 Specifications (Ewert Energy Systems)]]

## Aliases

- interface layers
- protocol list
- CAN protocols
- J1939
- CANopen
- CiA 418
- CiA 419
- OCPP
- ISO 15118
- OpenADR
- MQTT
- Modbus
- grid interface
- cloud interface

## Former ids
