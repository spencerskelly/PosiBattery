---
type: Info
subtype:
id: INFO-90062
uid: 20261018200000040skellyspencer
status: Draft
tags:
  - research
  - provenance
  - audit
describes:
  - "[[Battery-Connected Product]]"
---

# Non-Public Content Audit Register

## Definition

Lists content in the vault that rests on a statement by the vault owner or on a file with no public web address, found 2026-10-18 by text search for "owner statement", "owner's account" and similar wording, after the owner directed that all data in the repository come from public information ([[Landscape Evidence and Modeling Conventions]]). Nothing has been removed yet: the register is the list for a decision. A text search can miss lines that do not use those words.

## Notes

### Proposed handling

- **Keep as scope or modeling choice, labelled as such:** decisions about how the vault is organized (part lists, priorities, modeling splits). They are not facts about the world.
- **Find a public source or remove:** statements about how a product behaves, what an accessory does, how customers use a charger.
- **Not requested again:** internal prices, costs, sales or installed-base numbers. Earlier questions asking for them are withdrawn.

### A: claims resting on an owner statement

| # | Note | Claim | Public support found? | Proposed handling |
|---|---|---|---|---|
| 1 | [[HVPS Communications Kit]] | Name, role (kit shares power, DC variant configured to use it), AC variant does not need it | No web page (IB-162) | Find public source or remove |
| 2 | [[PosiCharge High Voltage Power Station (DC)]] and [[Share Power Between Charging Stations]] | Power sharing via the kit | No web page for the kit; the manual's MVS wording is public if the manual is | Keep the manual-backed text; remove the kit link until sourced |
| 3 | [[Battery Cabinet Cooling Fan]], [[Manage Temperature During Fast Charging]] | Cooling Fan Box cools the battery and fits in the truck battery cabinet | Marketing line only at posicharge.com/accessories/ (IB-144) | Reword to the marketing line; remove the rest |
| 4 | [[Voltage-Triggered Ready-State Top-Up]], [[Float Charge Battery]] | ProCore Solo restarts charging below a voltage threshold | Product PDF (marketing) cited; the exact behavior is the owner's | Check the PDF text; reword to what it says |
| 5 | [[Drive Up, Plug In and Walk Away]] and linked notes ([[Reduce Charge Current in Site-Set Time Windows]], [[Start and Stop Charge from an External Control]], [[Avoid Arcing at the Charge Connection]]) | Usual use case, start/stop button on some sites, history of arcing | Partly the public manual (see B) | Keep what the manual and public pages say; remove the rest |
| 6 | [[Ampure]], [[Power Designers]], [[Ampure Automotive and Aftermarket EVSE]] | Three business units; shared teams | Ampure acquired Power Designers Sibex (Transom Capital press release, 2025-09-02) and was formerly Webasto Charging Systems (GlobeNewswire, 2024-04-02), found by search 2026-10-18 and not yet fetched; no source found for the three-unit split or shared teams | Add the press releases; remove shared teams and any unsourced split |
| 7 | [[Industrial Truck Anatomy]] | Part list chosen by the owner | Not a fact about the world | Relabel as a modeling choice |
| 8 | [[Wireless and Hands-Free Charging Market Notes]] | ACT bought a wireless charging company | A Motive Companies quote about the acquisition of Resonant Link (public) | Keep the public quote only |
| 9 | [[Regional Market Differences Brief]] | Owner's market priority: North America, South America, Asia, Europe, rest of world | None; it is a strategy choice | Relabel as project scope or remove; decision needed |
| 10 | [[SOC and SOH Decision Criteria]] | Owner's voltage scope: up to 96 V nominal, 80 V a reasonable maximum for most | EPRI voltage classes (public) cover 12 to 80 V | Keep the EPRI-backed range; relabel the owner's range as scope |

### B: file with no public web address

| Note | State | Proposed handling |
|---|---|---|
| [[Document - PosiCharge DVS and MVS GSE Operation and Maintenance Manual (5914769 rev C03)]] | No `sourceUrl`; the owner attached the PDF on 2026-10-14. Whether a public copy exists is not recorded | Search for a public posting; if none, treat everything sourced only to it as non-public and remove or reword |

### C: process notes that mention the owner

[[External Context and Provenance]], [[Research Change and Decision Tracker]], [[Knowledge Base Backlog]] and conflicts C229 and C276 record who decided or said what. They are history, not data, and can stay.

## Traceability

- Created because of the public-information rule in [[Landscape Evidence and Modeling Conventions]].

## Aliases

- non-public audit
- owner statements audit

## Former ids
