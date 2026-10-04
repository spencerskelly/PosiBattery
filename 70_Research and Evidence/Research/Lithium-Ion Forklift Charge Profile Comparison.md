---
type: Info
subtype:
id: INFO-00274
uid: 20261003220714389skellyspencer
status: Draft
tags:
  - charge-profile
  - lithium-ion
  - comparison
  - review
describes:
  - "[[Industrial Traction Battery]]"
---

# Lithium-Ion Forklift Charge Profile Comparison

## Definition

How forklift lithium-ion batteries and their chargers are charged, as the makers describe it: who controls the charge, charge windows, rates and times, with sources, tiers and what is not published.

## Notes

- **Owner request (2026-10-03):** lithium-ion battery charge profiles, after flooded and VRLA ([[Flooded Lead-Acid Charge Profile Comparison]], [[VRLA Charge Profile Comparison (AGM and Gel)]]). Charger-side algorithm names are in [[Charger Charge Algorithm Comparison]].
- **Main finding:** lithium charging is described as BMS-controlled, not as a fixed voltage and current profile. Makers publish who controls the charge (the BMS over CAN, or a charger algorithm to a target voltage), the charge temperature window and fast-charge claims; none of the makers retrieved publishes per-cell voltage thresholds, C-rate stages or termination currents in the material found. Flux Power's 350 A maximum continuous charge current is the only charge current stated.
- **Reading rule:** each cell says what the source states; n/s means not stated in the retrieved text. Maker claims (charge times, efficiency, cycle life) are claims, not measurements. Metric notes carry values for products on file: [[Metric - BMS and Communication]], [[Metric - Charge Time]], [[Metric - Charge Temperature Limits]], [[Metric - Maximum Continuous Charge Current]].

**Parameters by source**

| Parameter | Hyster lithium-ion (T1 FAQ) | Flux Power LiFT Pack (T1 brochures and FAQ) | EnerSys NexSys iON (T2 trade items) | Green Cubes SAFEFlex (T1 and T2) | Delta-Q lithium chargers (T1) |
|---|---|---|---|---|---|
| Who controls the charge | the BMS, which adjusts the charger's current over CAN messaging | the patented BMS monitors charging so the pack cannot be overcharged; onboard charger | the BMS limits charge and discharge voltage; high-output NexSys+ chargers | internal BMS balances; the charger detects voltage over CAN | either the charger runs the battery maker's algorithm (algorithm-only) or follows the BMS over CAN (remote control) |
| Communication | custom Hyster CAN protocol between battery and charger; charger must provide a power signal | CAN integration with the truck | optional CAN to the truck | CAN voltage auto-detect, up to three ports per charger | optional CAN; BMS may close or open a contact to enable or disable charging in the algorithm-only method |
| Charge shape | n/s (current adjusted by the BMS) | constant current until the pack voltage reaches a set value (the rest cut off) | n/s | MultiVoltage charges at twice the output voltage | generally constant current until a target voltage; generic algorithms charge to a listed voltage |
| Termination and safety | BMS opens the charge contactor if any cell nears an unsafe limit | BMS prevents overcharge | voltage limitation | BMS protection | do not use lead-acid algorithms on lithium (overcharge risk) |
| Charge temperature window | n/s | 0 to 45 C charge; -20 to 55 C discharge; integrated heaters for cold | n/s | charger operates -4 to 122 F | n/s |
| Charge rate and time | n/s | maximum 350 A continuous (M36, X80); fast charge in as little as one hour (M36) | fast and opportunity charging; no equalize | full charge under one hour with MultiVoltage (claim); 98 percent or higher charging efficiency (claim) | n/s |
| Opportunity charging | n/s | plug in at any state of charge with no negative effect | yes | yes, around the clock with the charger | n/s |
| Equalize | n/s | n/s | none: 'no long equalize charges' | n/s | n/s |
| Lead-acid charger compatible | no | needs higher voltage than lead-acid; a lead-acid charger can partly charge it in some cases | n/s | MultiVoltage works with standard chargers | no, not advised |

**Other sources on file (names and claims only)**

- Crown V-Force lithium: 'true opportunity charging', no gassing, one battery for one or several shifts (FC 5700 brochure, T1); Crown V-HFM3 offers a V-Force Lithium-Ion profile ([[Charger Charge Algorithm Comparison]]).
- Jungheinrich lithium: 50 percent in 40 minutes and full in 80 minutes (trade report); Godrej: 20 to 80 percent in 2.5 hours (maker claim); EnerSys NexSys TPPL (not lithium): under 4 hours from 60 percent depth of discharge. See [[Metric - Charge Time]].
- The ProCore Edge manual shows a lithium-ion BMS pause state ('the lithium-ion BMS has paused the charging') and cascading charging for lithium-ion; details in the manual (in repo).

**Conflicts and gaps**

- **Charge-time claims use different bases (C100):** 'as little as one hour' (Flux M36), 'full charge in under one hour' (Green Cubes MultiVoltage, at double voltage), 50 percent in 40 minutes and full in 80 minutes (Jungheinrich), 20 to 80 percent in 2.5 hours (Godrej). Start and end state of charge, charger power and temperature are not stated alike, so they are not ranked.
- Not published in the retrieved material: per-cell charge voltage limits (for example LFP or NMC cutoffs), C-rate by stage, termination currents, balancing thresholds, low-temperature charge derating and the BMS-to-charger message set. They would come from BMS integration manuals or CAN specifications that the makers share under agreement.
- Not read: EnerSys NexSys iON manual and NexSys+ lithium profile table, Crown V-Force charging manual, Toyota, Linde and Raymond lithium charging pages, Triathlon, HOPPECKE and Exide Motion+ lithium documents beyond what is already on their notes.
- **Curves:** none recorded; lithium charge curves would show constant current then a voltage taper, but no maker retrieved prints tabulated points.

## Aliases

- Lithium-ion charge profiles
- Li-ion charge profiles

## Former ids
