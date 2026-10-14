---
type: Info
subtype: research
id: INFO-00923
uid: 20261014104222825skellyspencer
status: Draft
tags:
  - research-note
  - connector
describedBy:
  - "[[Document - DIN 43589-1 Listing (DIN Media)]]"
  - "[[Document - DIN 43589-2 Listing (DIN Media)]]"
  - "[[Document - DIN VDE 0623-589 Listing (VDE Verlag)]]"
  - "[[Document - Anderson EBC Data Sheet (DIN 43589-1)]]"
  - "[[Document - Anderson SBX350 Housing Page (retrieved 2026-10-14)]]"
  - "[[Document - Anderson SBE320 Housing Page (retrieved 2026-10-14)]]"
  - "[[Document - Anderson SBE SBX SBO Product Line Page (retrieved 2026-10-14)]]"
  - "[[Document - Anderson SB350 Housing Page (retrieved 2026-10-14)]]"
  - "[[Document - Anderson SB Series Page (retrieved 2026-10-14)]]"
  - "[[Document - REMA Lipprandt Connector Data Sheet]]"
  - "[[Document - McMaster European Battery Connectors Listing]]"
  - "[[Document - Intella Parts Battery Connectors Category]]"
  - "[[Document - Industrial Monitor Direct SB 175 to SB 350 Article]]"
  - "[[Document - Genorma EN 1175 2020 Record]]"
---

# Industrial Battery Connector Specification Register

## Definition

Specifications of the connector families used between industrial truck batteries, trucks and chargers, as stated by makers and standards bodies, with the differences between families and the conflicts between sources.

## Notes

- Values are as stated; blank means not stated. Anderson figures come from its pages and data sheet (T1, read second-hand); the shop and article rows are weaker evidence (T3/T4). Terms are explained in [[Industrial Battery Connector Glossary and Differences]].
- Charger-to-vehicle context: [[Charger-Vehicle Interface Register]].

### Standards behind the connectors

| Standard | Scope as stated | Status as found |
|---|---|---|
| DIN 43589-1:1994-08 | Connector for battery powered industrial trucks 80, 160, 320 A, 150 V; connecting dimensions, material, marking | Withdrawn; replaced by DIN VDE 0623-589:2011-06 |
| DIN 43589-2:1980-07 | Plug connection 160 and 320 A, 150 V; requirements and test schedules | Withdrawn; replacement not stated |
| DIN VDE 0623-589 | Plug device for battery powered industrial trucks, types 80, 160, 320 and 640 / 150 V; suitable for emergency switching off per EN 1175-1 except type 640 | Listed with 2011-06 in the URL and 2023-06 in the text (C249) |
| EN 1175:2020 | Electrical and electronic requirements for self-propelled industrial trucks; battery connectors not mentioned in the record read | Withdrawn 2025-11-19, revised by EN 1175:2025 per Genorma; Anderson pages still cite 2020 (C249) |
| UL / CSA | 600 V ratings used for SB, SBE, SBX and EBC | Cited by Anderson |

### Families

| Family | Maker | Current | Voltage | Contacts | Coding | Standards | Cycles | Evidence |
|---|---|---|---|---|---|---|---|---|
| DIN-type 80 / 160 / 320 A (generic) | several | 80, 160, 320 A | 150 V | 2 power, 4 aux (Anderson catalog) | wet/dry pin colours | DIN 43589, VDE 0623-589 | 5,000 minimum (DIN, catalog) | catalog, standards listings |
| [[Anderson EBC Euro Battery Connector]] 80 / 160 / 320 | Anderson | by wire size, 95-350 A (EN1175) | 150 V AC/DC EN1175; 600 V CSA/UL | upper aux and lower pilot, air tube option | grey wet, green dry, yellow universal (male only) | EN1175-1:1998 (data sheet) | >5,000 no load; 5 hot-plug at 96 V | data sheet T1 |
| [[Anderson IBC Industrial Battery Connector]] | Anderson | not stated | not stated | up to 10 aux, IP68 kit, latching handle | not stated | EN 1175 | not stated | pages T1/T2 |
| [[REMA Euro DIN Battery Connector]] 80 / 160 / 320 / 400 | REMA Lipprandt | 80, 160, 320 A; 400 A cont. / 450 A 15 min | 150 V | 2 power; options 2 pilot, 2 aux, 4 aux, air | pin set for 24, 36, 48, 72, 80, 96 V; grey, green, yellow | EN 1175-1, DIN 43589 | not stated | data sheet T1 |
| [[Anderson SB Connector Series]] SB50 / SB120 / SB175 / SB350 | Anderson | 50-500 A; SB120 240 A; SB350 450 A (4/0) or 500 A (350 mcm) | 600 V UL | up to 20 aux (catalog) | colour keys per voltage; Anderson: identifiers | UL | 10,000 (catalog) | pages T1 |
| SBS | Anderson | up to 110 A | 600 V UL | 5 to 20 aux | keyed | UL | 10,000 | catalog T1 |
| [[Anderson SBE SBX SBO Connector Series]] | Anderson | up to 350 A per pole (SBE320 / SBX350 pages) or 550 A per pole (line page, catalog) | 600 V UL | 2 power + up to 8 last-mate/first-break aux | colour keys | SBE EN 1175:2020; SBX UL/CSA, not EN 1175-1 | 10,000 | pages T1 (C250) |
| Crown-specific housings, SR175 | Crown, Anderson | | | | | | | names only (distributor T3) |

### Voltage identification by truck practice

| Source | Gray | Blue | Black | Tier |
|---|---|---|---|---|
| Yale ERC045-070VG sheet | SB350, 36 V | SB350, 48 V | SBE320, 80 V | T1 |
| Industrial Monitor Direct article | 36 V | 48 V | not listed (red 24 V, green 72 V, orange 18 V, yellow 12 V) | T4 |
| Toyota 7FBCU35-55 and 8FBCU25 sheets | SB350 gray on 36 V and 48 V models | | | T2/T3 (C252) |

### Differences that matter

- **Gendered versus genderless:** DIN-type connectors are plug and socket pairs; SB, SBE and SBX are genderless (mate when one half is rotated 180 degrees).
- **Voltage rating:** 150 V for DIN-type (EN 1175, DIN 43589) against 600 V for the UL-rated SB family; the DIN types cover up to 96 V truck systems via the pin set, SB-type up to 120 V via colour keys per the catalog.
- **Voltage keying method:** replaceable hexagonal coding pins in DIN-type (also marking wet versus dry batteries), moulded colour keys in SB-type.
- **Signals:** DIN-type has fixed aux and pilot positions (2 to 4); SBE and SBX carry up to 8 sequenced last-mate/first-break aux contacts; IBC adds up to 10.
- **Not interchangeable:** SBE320 and SBX350 with the same colour code cannot be mated; an SBX350 is not EN 1175-1 compliant per Anderson.
- **Standards status:** DIN 43589-1 and -2 are withdrawn in favour of DIN VDE 0623-589; EN 1175:2020 was withdrawn in November 2025 per Genorma, so datasheets citing it may be out of date.

## Aliases

## Former ids
