---
type: Info
subtype:
id: INFO-00949
uid: 20261014191236307skellyspencer
status: Draft
tags:
  - owner-supplied-manual
  - tier-T1
  - vendor-manual
describes:
  - "[[PosiCharge DVS300 Series]]"
  - "[[PosiCharge MVS400 and MVS800]]"
---

# Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)

## Definition

Operation and maintenance manual for the PosiCharge DVS300, DVS330, DVS330 IP55, DVS400 and MVS330, MVS400 and MVS800 GSE intelligent fast-charging systems (document 5914769, revision C03).

## Notes

**How it was read:** the owner attached the PDF on 2026-10-14; the 26-page file was converted to text and the sections on safety, system overview, battery information, startup, charging, equalization, full and reduced charging, display and external lights were read in full. On the second pass the same day the MVS setup, BMID parameter list, data logs, maintenance schedule and the structure of the fault and warning table (section 6.2) were also read. Figures and the individual fault descriptions were not reviewed line by line. **Handling:** the manual carries a copyright notice that bars copying without written permission, and this repository is public. The file is not stored here; this note paraphrases facts and keeps quotations to a few words. The revision table lists A01 (02/07/2025), B02 (07/09/2026) and C03 (10/09/2026) with no date format stated, so C03 may be a very recent or pre-release revision.

- **Models and batteries:** DVS300, 330, 330 IP55 and 400 (dual vehicle) and MVS330, 400 and 800 (multi-vehicle); lithium-ion, flooded and sealed lead-acid; one or two circuits; 12 to 48 cells (section 3.3).
- **Charging starts on connection (sections 3.1 and 4.4):** the manual says to connect the battery to either charge port to start charging; the charger then communicates with the battery monitor and identifier (BMID), works out the state of charge, picks the profile and starts. The marketing summary says to 'just connect' an IPC-compatible battery. The text describes no start button on the power station.
- **Charging ends on its own (section 4.4, step 2):** the charge stops when the battery reaches the state of charge preset in the BMID and the Charge Completed light comes on. The operator may stop at any time with the STOP button or by disconnecting the cable; if the cable is disconnected without STOP, the charger stops immediately 'and prevent any arcing or damage' (manual wording).
- **Safety section (1.2):** says to stop charging with the Stop button on the front panel of all power stations before disconnecting the battery, and says the stations are designed to stop the charge automatically on a hot disconnection 'to minimize arcing or burning' of the connections. See C276.
- **Front panel (section 3.2):** keypad, alphanumeric display and four status lights (charging, 80 percent, fully charged, equalization) plus a fault and warning light; optional external status lights, three per port (section 4.10).
- **BMID settings (section 4.1):** each BMID is preset with the start current limit, the state-of-charge limit that decides when charging stops, the maximum amp-hours and maximum days between equalizations, the equalization day of the week and the voltage limit for fast charging and equalization.
- **Equalization (sections 4.5, 3.1):** the schedule is stored in the BMID and runs automatically; during a charge the operator can press Equalize to schedule one after the fast charge, or hold it for three seconds to start one at once. The manual recommends equalizing at least weekly (twice weekly optimal under continuous use) and only if the battery maker recommends it.
- **Other modes (sections 4.6, 4.7):** full charging and overcharging in a user-set time window, and reduced charging at a set current in a time window. Charge profile is constant current, constant voltage, constant current. The manual does not say what customers use the two modes for; the owner's account is in the next bullet (IB-241, C278).
- **MVS main and support stations (section 4.2):** an MVS system has one main station, the one wired nearest the power server, and the others are support stations by default; the main/support role is set in the Network Config menu. The power server mode is either a communicated variable power mode (earlier power servers) or a fixed power mode of 30, 33, 40, 60 or 80 kW (the newer server). The number of ports is entered as twice the number of stations, main included; the manual's example is 5 stations (1 main and 4 support) as 10 ports. A control-board switch enables parallel mode, in which one connected vehicle gets both power sections of a station. The full wiring description is in a separate installation guide (PN 5914638) not in the vault. See C277.
- **BMID values beyond section 4.1's first list (section 4.1):** the BMID also holds an identification number for tracking one battery's charge history, a type code for maker and battery type, the number of cells, the amp-hour capacity, the internal resistance and a battery temperature foldback value. BMID versions named: BMID I, BMID III (Battery Rx) and PosiGuard, each with its own installation manual.
- **Data logs and menus (section 4.9):** the charger keeps a charge event log of the last 250 charges (Gen II control board) or 1,000 (Gen III), and a fault and warning log of the last 100 messages. A code-protected Charger Configuration menu sets date and time, charge algorithms, the equalization schedule and charge times; a Network Diagnostics screen reports on all chargers in the setup; a BMID Data Review screen lists the BMID parameters, charging history and equalization data; an Energy Saving Mode can be toggled. The manual states no purpose for Energy Saving Mode.
- **Fault and warning table (section 6.2):** codes with a message, a description and an action code. Messages seen include current sensor, logic supply, power-section (PS1 and PS2) transistor, general and over-temperature failures, BMID battery over-temperature, BMID configuration and mismatch warnings per port, BMID temperature sensor failures, network configuration failure and cable over-temperature per port. The individual descriptions and action codes were not read. No ground-fault or insulation fault message was found in the structure scan, so [[Detect Isolation Fault]] gains no manual evidence; the scan was a text search of message titles, not a full read.
- **Maintenance (section 5):** check the unit every six months for cabinet or connection damage and for debris in the air inlet (underside) and outlet (rear top); do not use water. DC output cables and battery output connectors are inspected and replaced as needed. SBX connector auxiliary contact pins can seat badly and cause a BMID communication fault or no vehicle recognition; the manual gives a rework procedure. The DVS330 IP55 has reusable air filters to be cleaned every three to six months depending on dust.
- **Owner account of the time-window modes (2026-10-14, U):** 'full charging is bring to full voltage, overcharging is equalization, reduced charging is windows of reduced energy usage'. Checked against the manual: full charging goes to 100 percent and then overcharges for a set time; the manual says overcharging 'resembles' equalization and reuses its finish-current setting, but lists it as its own feature with its own time window, so 'is equalization' is close and not identical. Reduced charging is stated as a set, lower charge current inside a time window; the manual gives no reason, so the purpose is the owner's account and has no document behind it. Owner (U, 2026-10-14): the windows are set by the site owners; what the owners are reacting to is not stated. Modeled as [[Reduce Charge Current in Site-Set Time Windows]]. C278.

## Provenance

- **Source type:** manufacturer manual (PosiCharge, a product line of Ampure).
- **Local artifact:** `a772eb97-31504-03_GSE_OM_5914769_1_2.pdf`, supplied by the owner 2026-10-14; not stored in the repository.
- **Original web address:** none; internal or customer manual.
- **Access date:** 2026-10-14. **Revision:** C03.
- **Evidence tier:** T1 maker document, read directly (not through a summarizing tool).

## Traceability

- `describes` links the document to the products it covers; disagreements are logged in the conflict register.

## Aliases

## Former ids
