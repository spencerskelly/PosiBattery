---
type: Object
subtype: electrical
id: OBJ-00122
uid: 20261002193402978skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - battery
chemistry: lfp
voltageClassV:
  - 24
  - 36
  - 48
  - 80
voltageMinV: 24
voltageMaxV: 80
productCategory: battery
subtypeOf:
  - "[[Lithium-Ion Traction Battery]]"
describedBy:
  - "[[Document - Green Cubes Lithium SAFEFlex PLUS Product Page (retrieved 2026-10-13)]]"
  - "[[Document - Green Cubes SAFEFlex PLUS Datasheet (2026.03.18)]]"
  - "[[Document - Green Cubes SAFEFlex PLUS Datasheet (refresh, copyright 2025)]]"
  - "[[Document - Green Cubes SAFEFlex PLUS UL Listing Press Release (2025-08-15)]]"
performs:
  - "[[Balance Cells]]"
  - "[[Estimate State of Charge]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Protect Battery from Harm]]"
  - "[[Sense Battery State]]"
hasDesign:
  - "[[CAN Interface]]"
  - "[[Integrated Battery Heater]]"
  - "[[Integrated Battery Management System]]"
  - "[[Wi-Fi Interface]]"
madeBy:
  - "[[Green Cubes Technology]]"
---

# Green Cubes SAFEFlex PLUS Battery

## Definition

Green Cubes lithium iron phosphate battery family for material handling and GSE in four voltage classes (24, 36, 48 and 80 V), with UL 2580 listing and EE rating.

## Notes

- A trade item says Green Cubes announced UL certification and EE rating for its whole line, including 24, 36, 48 and 80 V lithium models. Source: M H&W magazine category page (T3), retrieved 2026-10-02. <https://www.mhwmag.com/category/products/page/13/>

- **Official sources found 2026-10-13 (read through a summarizing tool, IB-168):** [[Document - Green Cubes Lithium SAFEFlex PLUS Product Page (retrieved 2026-10-13)]] <https://greencubes.com/product/safeflexplus/>; [[Document - Green Cubes SAFEFlex PLUS Datasheet (2026.03.18)]] <https://greencubes.com/wp-content/uploads/2026/04/GCT_DS_SAFEFlex-Plus_2026.03.18_8.5x11.pdf>; [[Document - Green Cubes SAFEFlex PLUS Datasheet (refresh, copyright 2025)]] <https://greencubes.com/wp-content/uploads/2025/11/GCT_DS_SAFEFlex-Plus_refresh.pdf>; [[Document - Green Cubes SAFEFlex PLUS UL Listing Press Release (2025-08-15)]] <https://greencubes.com/press-releases/green-cubes-technology-secures-ul-listing-with-ee-rating-for-lithium-safeflex-plus-battery-family/>.
- **Specifications by voltage class** (one family note, owner decision 2026-10-13; the four classes are not split into variant notes for now). Values are the 2026 product page and 2026.03.18 datasheet unless marked; "2025" is the copyright-2025 datasheet; all read through a summarizing tool (IB-168). Source: Green Cubes product page (T1), retrieved 2026-10-13. <https://greencubes.com/product/safeflexplus/>

  | Item | 24 V class | 36 V class | 48 V class | 80 V class |
  |---|---|---|---|---|
  | Nominal voltage | 25.6 V | 38.4 V | 51.2 V | 83.2 V |
  | Operating voltage | 24 to 28.8 V | 36 to 43.2 V (2025: 37.2 to 42.6 V) | 48 to 57.6 V (2025: 49.6 to 56.8 V) | 78 to 93.6 V |
  | Nominal capacity | 420 to 630 Ah | 525 to 945 Ah (2025: 630 to 840 Ah) | 525 to 840 Ah | 315 to 735 Ah |
  | Nominal energy | 11 to 16 kWh | 20 to 36 kWh (2025: 24 to 32 kWh) | 26 to 43 kWh | 26 to 61 kWh |
  | Peak discharge | 600 A | 1,200 A | 1,200 A (2025: 636 A for 30 s and 1,200 A for 7 s) | 800 A (page: "1,200 A / 800 A" in its last column) |
  | Continuous discharge | 250 A with SB 175 connector, 320 A with others | 320 A | not assigned in any source read | 300 A for 315 Ah, 320 A for 420 Ah and up (assignment inferred, C216) |
  | Continuous charge | not assigned | not assigned | not assigned (2025: 320 A, column unclear) | 240 A for 315 Ah, 320 A for 420 Ah and up (assignment inferred, C216) |
  | Operating temperature, with heater | -20 to +54 C | -20 to +55 C | -20 to +50 C | -20 to +53 C |
  | Operating temperature, without heater | 0 to +54 C | 0 to +55 C | 0 to +50 C | 0 to +53 C |
  | Dimensions, weight | not stated | not stated (2025 model matrix: about 736 to 1,158 lb, unpaired) | not stated (2025 model matrix: about 1,061 to 1,811 lb, unpaired) | not stated |

  Common to all classes: lithium iron phosphate; 4,000 cycles (maker claim); IP 2X; storage 0 to +35 C and 70 percent RH or less; powder-coated steel tray; CAN bus, USB and Wi-Fi (2025 adds Ethernet); UL 2580:2020 (2025: pending), ISO 13849, UN 38.3 Rev 7, Type EE. Nominal voltage x capacity matches the stated energy in every class (checked). Mapping of the 2026 current and temperature rows to classes follows the order the summaries returned and is unconfirmed (C215, C216).
- **Chemistry and life:** lithium iron phosphate; 4,000 cycles (maker claim, no end-of-life basis stated). Same source.
- **Temperature and protection:** operating -20 to +50/55 C with heater and 0 C up with none (class-dependent upper limits 50 to 55 C); IP 2X; storage 0 to +35 C. Same source.
- **Certifications listed:** UL 2580:2020 (MH66684), ISO 13849-1:2023 and 13849-2:2012 (MH66684), UN 38.3 Rev 7, Type EE rating. The 2025 datasheet says UL 2580 **pending**. Same source and <https://greencubes.com/wp-content/uploads/2025/11/GCT_DS_SAFEFlex-Plus_refresh.pdf>.
- **Conflicts kept visible:** UL listing covered the 48 V family in the 2024 announcement and all four classes in the 2025 release (C214); the 2025 and 2026 datasheets differ on the 36 V and 48 V ranges, UL status and communications (C215); current-rating columns are ambiguous across sources (C216). The earlier trade item in this note (24, 36, 48, 80 V all certified, T3) matches the 2025 release and not the 2024 one.
- **Not stated anywhere read:** dimensions, weight, warranty, price, compatible chargers. A model matrix exists in the 2025 datasheet (FBP2-036 and FBP2-048 codes) but could not be paired with sizes (IB-170).
- **Functions performed, with citations:**
  - [[Sense Battery State]] (V): individual cell monitoring. <https://greencubes.com/product/safeflexplus/>
  - [[Protect Battery from Harm]] (V): cell over and undervoltage and temperature, module overcurrent and overvoltage, recoverable short-circuit protection. <https://greencubes.com/product/safeflexplus/>
  - [[Balance Cells]] (V, partial): "state-of-charge monitoring and balancing"; the balancing method is not stated. <https://greencubes.com/press-releases/green-cubes-technology-secures-ul-listing-with-ee-rating-for-lithium-safeflex-plus-battery-family/>
  - [[Estimate State of Charge]] (V, partial): "state-of-charge monitoring"; the method is not stated. <https://greencubes.com/press-releases/green-cubes-technology-secures-ul-listing-with-ee-rating-for-lithium-safeflex-plus-battery-family/>
  - [[Log Battery Events and Usage]] (V): data logging in the distributed BMS. <https://greencubes.com/product/safeflexplus/>
- **Design characteristics, with citations:**
  - [[Integrated Battery Management System]] (V): modular, distributed BMS (the 2025 datasheet calls it a custom BMS controlling internal contactors and a disconnect fuse). <https://greencubes.com/product/safeflexplus/>
  - [[CAN Interface]] (V): CAN bus with separate buses for truck and charger, galvanically isolated. <https://greencubes.com/product/safeflexplus/>
  - [[Wi-Fi Interface]] (V): Wi-Fi with over-the-air firmware upgrades; what data it carries is not stated. <https://greencubes.com/product/safeflexplus/>
  - [[Integrated Battery Heater]] (V, partial): the page gives "with heater" and "without heater" temperature ranges, so the heater is an option or variant; the heater itself is not specified. <https://greencubes.com/product/safeflexplus/>
- **Not linked, and why:** [[Communicate Battery State over CAN]] and [[CAN Battery State Communication Design]] (CAN is named, battery-state messages are not); [[Transmit Battery Data Wirelessly]] (Wi-Fi is named, the data sent is not); [[Disconnect Battery on Limit Violation]] (contactors and a service disconnect exist, but tripping on a limit is not stated); [[Active Cell Balancing]] and [[Passive Cell Balancing]] (method not stated); USB (purpose not stated); [[Green Cubes SAFEFlex Charger]] (compatibility with PLUS not stated).
- **Class split:** decided 2026-10-13 (owner): keep one note for now with the class table above; variant notes like [[Flux Power GSE Pack]] can come later (IB-171).

## Aliases

- SAFEFlex PLUS


## Former ids
