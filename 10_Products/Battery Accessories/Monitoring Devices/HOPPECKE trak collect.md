---
type: Object
subtype: electrical
id: OBJ-00036
uid: 20261002164202404skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - europe
  - forklift
  - lead-acid
  - scope-oem-option
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Accumulate Amp-Hours]]"
  - "[[Estimate Remaining Run Time]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Communicate with Charger]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Estimate State of Charge]]"
  - "[[Configure Device from Mobile App or PC]]"
  - "[[Communicate Battery State over CAN]]"
  - "[[Transmit Battery Data Wirelessly]]"
hasDesign:
  - "[[Current Integration Amp-Hour Accumulation]]"
  - "[[Battery-Monitor State of Charge Estimation]]"
  - "[[Remaining Runtime Estimation Design]]"
  - "[[Low-Current Electrolyte Level Input]]"
  - "[[Bluetooth Interface]]"
  - "[[Local LED Indicator]]"
  - "[[Cloud Portal Integration]]"
  - "[[Mid-Battery Voltage Tap]]"
  - "[[NFC Interface]]"
  - "[[CAN-LIN and Battery Bus Interface]]"
  - "[[Bluetooth Low Energy Interface]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Battery Event and Usage Logging Design]]"
  - "[[CAN Battery State Communication Design]]"
  - "[[Wireless Battery Data Communication Design]]"
hasPart:
  - "[[Battery Current Measurement Circuit]]"
  - "[[Battery Current Acquisition Firmware]]"
  - "[[Amp-Hour Accumulator Firmware]]"
  - "[[State of Charge Estimation Firmware]]"
  - "[[Control Circuit]]"
  - "[[Remaining Runtime Estimation Software]]"
  - "[[Mid-Battery Voltage Tap Harness]]"
  - "[[LED Status Indicator Element]]"
  - "[[Low-Current Electrolyte Level Input Circuit]]"
  - "[[Battery Event Logger Firmware]]"
  - "[[Event Log Memory]]"
  - "[[Event Time Base]]"
  - "[[Wireless Battery Data Communication Firmware]]"
madeBy:
  - "[[HOPPECKE]]"
offeredWith:
  - "[[HOPPECKE trak charger HF premium]]"
  - "[[HOPPECKE trak uplift iQ Battery]]"
---

# HOPPECKE trak collect

## Definition

HOPPECKE battery controller permanently affixed to lead-acid traction batteries that measures battery state and communicates with chargers, trucks, PCs and the trak | monitor system.

## Notes

**Summary:**
HOPPECKE battery controller permanently fitted to lead-acid traction batteries that measures battery state and communicates with chargers, trucks, PCs and trak monitor.

**Marketed features:**
- Shows state of usage (SOU) and state of readiness (SOR), plus SOC
- Measures full and mid voltage, charge/discharge current (shunt), temperature and electrolyte level
- Ah and Wh charged/discharged; remaining driving time
- Interfaces: NFC, Bluetooth, CAN, LIN and battery-bus; smartphone app and PC software
- Controls charge curve via trak charger; cloud collector for remote monitoring
- Fits all PzS and PzB batteries; retrofittable on site

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- HOPPECKE (T1), retrieved 2026-10-04. <https://www.hoppecke.com/uk/product/trak-collect-premium/>
- Warehouse News (T2), retrieved 2026-10-04. <https://warehousenews.co.uk/?p=103814>
- HOPPECKE (T1), retrieved 2026-10-04. <https://www.HOPPECKE.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_brochure_en.pdf>

- The product page says trak | collect (premium) records voltage, current, temperature and electrolyte level, communicates with the charger, trak | monitor, PC and industrial truck, and transmits diagnostic data; area of application is industrial trucks, special-purpose vehicles and cleaning machines; technology lead-acid; listed standards include EN 12895, EN 1175-1, DIN EN IEC 62485-3, EN 55011 and EN 61000-6-2 and -3. Source: HOPPECKE trak | collect premium page (T1), retrieved 2026-10-02. <https://www.hoppecke.com/uk/product/trak-collect-premium/>
- The Advanced version is described as showing state of usage and state of readiness, giving access to charged and discharged Ah and Wh, and sending data to a remote monitoring system through a cloud collector. Source: Warehouse News feature on trak | collect Advanced (undated) (T2/T4), retrieved 2026-10-02. <https://warehousenews.co.uk/?p=103814>
- The brochure says trak | collect remains on the battery for its whole life, installs on PzS and PzB batteries, and links to trak | monitor, trak | charger and the vehicle over LIN and battery bus. Source: HOPPECKE brochure (T1), retrieved 2026-10-02. <https://www.HOPPECKE.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_brochure_en.pdf>
- In a case study, trak | collect allowed temperature-controlled charging in combination with trak | charger HF premium; trak | uplift iQ shows battery status on an LED display near the battery socket. Source: HOPPECKE case study and trak | uplift iQ page (T1), retrieved 2026-10-02. <https://www.hoppecke.com/uk/product/trak-uplift-iq/>
- **Not stated in retrieved sources:** voltage range, current range, enclosure rating, wireless interfaces. HOPPECKE also names a Batcom Plus controller, not researched.
- **Electrolyte-level implementation:** the technical data sheet specifies an electrolyte-level electrical input of 11.3 V, 55 µA trigger current and 100 µA maximum current. This supports [[Low-Current Electrolyte Level Input]] and [[Low-Current Electrolyte Level Input Circuit]] without assuming the connected probe technology.
- **Note on name:** the product is written trak | collect; the pipe is replaced in the file name per the naming rule.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Measure Battery Current]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Measure Battery Temperature]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Sense Electrolyte Level]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Accumulate Amp-Hours]] (V): <https://warehousenews.co.uk/?p=103814>
  - [[Estimate Remaining Run Time]] (V): <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
  - [[Log Battery Events and Usage]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/> <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
  - [[Alert on Abnormal Condition]] (V): <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
  - [[Indicate Battery Status Locally]] (V): <https://www.hoppecke.com/uk/product/trak-uplift-iq/>
  - [[Report Battery Temperature to Charger]] (V): <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
  - [[Communicate with Charger]] (V): <https://www.hoppecke.com/uk/product/trak-collect-premium/> <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://warehousenews.co.uk/?p=103814>
  - [[Estimate State of Charge]] (V): <https://warehousenews.co.uk/?p=103814>
  - [[Configure Device from Mobile App or PC]] (V): <https://www.HOPPECKE.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_brochure_en.pdf>
  - [[Communicate Battery State over CAN]] (V): <https://www.HOPPECKE.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_brochure_en.pdf>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.HOPPECKE.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_brochure_en.pdf>
- **Design characteristics, with citations:**
  - [[Bluetooth Interface]] (V): <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[Local LED Indicator]] (V): <https://www.hoppecke.com/uk/product/trak-uplift-iq/>
  - [[Cloud Portal Integration]] (V): <https://warehousenews.co.uk/?p=103814>
  - [[Mid-Battery Voltage Tap]] (V): <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[NFC Interface]] (V): <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
  - [[CAN-LIN and Battery Bus Interface]] (V): <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
- **Sources used for the mapping above:** HOPPECKE trak | collect premium page <https://www.hoppecke.com/uk/product/trak-collect-premium/>; HOPPECKE news: trak | collect and digital age <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>; HOPPECKE news: improved battery management <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>; Warehouse News on trak | collect Advanced (undated) <https://warehousenews.co.uk/?p=103814>; HOPPECKE trak | uplift iQ page <https://www.hoppecke.com/uk/product/trak-uplift-iq/>; HOPPECKE case study on temperature-controlled charging <https://hoppecke.com/en/stories/show/switch-from-gas-to-electrically-powered-forklift-trucks>
- HOPPECKE says up to five communication interfaces are available (NFC, Bluetooth, CAN-LIN and battery bus), that it measures battery voltage, medium voltage, charging and discharging current, temperature and electrolyte level, can be attached or retrofitted to all lead-acid batteries, and saves processed data on the battery. Source: HOPPECKE news on trak | collect (T1), retrieved 2026-10-02. <https://www.hoppecke.com/uk/news/hoppecke-trak-collect-taking-lead-acid-batteries-into-the-digital-age/>
- HOPPECKE says trak | collect highlights incorrect treatment such as deep discharge or temperature warning, and that remaining driving time data helps OEMs optimize drive mode. Source: HOPPECKE news on improved battery management (T1), retrieved 2026-10-02. <https://www.hoppecke.com/uk/news/improved-battery-management-with-trak-collect/>
- The trak | collect technical data sheet (status 2024-07-31) gives the electrical, mechanical, measurement, data, interface, environmental and standards data summarized below. Source: HOPPECKE trak | collect data sheet (T1), retrieved 2026-10-02. <https://www.hoppecke.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_data_sheet_en.pdf>
| Parameter | Value as stated |
|---|---|
| Supply voltage | 17 to 150 VDC (200 V pulse for 10 s) |
| Current consumption | 7.5 mA at 150 V to 70 mA at 17 V |
| Switch-off | over-voltage above 203 V; under-voltage below 16 V |
| Current measuring range | max 500 A permanent, shunt measuring (battery current 0 to +/-2100 A, see conflict) |
| Battery voltage | 17 to 200 VDC, 10 mV resolution, 0.1% at 25 C plus 0.004%/K |
| Battery medium voltage | 0 to 200 VDC, 10 mV resolution |
| Current accuracy | 1% (+/-10 to 2100 A), 5% (+/-2 to 10 A), 20% (+/-0.5 to 2 A), plus 0.02%/K |
| Temperature | -30 to 100 C, 0.1 K resolution |
| Electrolyte level | UB 11.3 V, trigger current 55 uA, max 100 uA |
| Processor and memory | DSP 40 MHz; 8 MB (4 MB ring buffer); stores I, U, temperature at 10 s default; ring buffer 30 days |
| Real-time clock | +/-2 s per day, 30-day buffer |
| Interfaces | NFC (1 kB, 16 mm), Bluetooth 4.0 Low Energy / 2.0, HOPPECKE Battery Bus (60 baud, 12 V level) |
| Environment | use and storage -30 to 80 C; sulfuric acid 60% at 50 C; IP 69K |
| Mechanical | base 120 x 52 x 26 mm; satellite 82 x 50 x 32 mm; 340 g; cable 25 to 95 mm2 |
| Standards | EN 12895, EN 60721-3-3, EN 55022, EN 55011, EN 61000-6-2 and -6-3, EN 60068-2-6, -2-27 and -2-31, EN 62485-3, UL 583 |
- **Conflict-visible (C39):** the data sheet gives 'max 500 A permanent' as the current measuring range and '0 to +/-2100 A' as the battery current measuring value; the two describe permanent versus peak or end value but the sheet does not say so. An earlier HOPPECKE news item lists up to five interfaces including CAN-LIN; the data sheet lists NFC, Bluetooth and the Battery Bus only.
- **Design links added from the data sheet:** [[Bluetooth Low Energy Interface]], [[NFC Interface]], [[Acid-Resistant Sealed Housing]] (IP 69K, acid resistance).
- **Design characteristics, with citations (data sheet):**
  - [[Low-Current Electrolyte Level Input]] (V): <https://www.hoppecke.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_data_sheet_en.pdf>
  - [[Bluetooth Low Energy Interface]] (V): <https://www.hoppecke.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_data_sheet_en.pdf>
  - [[Acid-Resistant Sealed Housing]] (V): <https://www.hoppecke.com/fileadmin/Redakteur/Hoppecke-Main/Products-Import/trak_collect_data_sheet_en.pdf>
- **Related products and how they differ (offeredWith):**
  - [[HOPPECKE trak charger HF premium]]: no difference stated in the sources.
  - [[HOPPECKE trak uplift iQ Battery]]: no difference stated in the sources.
- The trak collect data sheet (in repo as Downloads/trak_collect_data_sheet_en.pdf) lists supply 17 to 150 VDC, a current measuring range of maximum 500 A permanent by shunt with battery current readings to +/-2,100 A, temperature -30 to 100 C, 8 MB memory with a 30-day ring buffer at a 10 s interval, NFC, Bluetooth 4.0 Low Energy and 2.0 and a HOPPECKE battery bus at 60 baud, 340 g, use range -30 to 80 C and chemical resistance to 60 percent sulfuric acid at 50 C. Source: HOPPECKE trak collect data sheet (read round 20) (T1), retrieved 2026-10-03. <https://www.hoppecke.com/uk/product/trak-collect-premium/>
- **C39 update (round 20):** the data sheet gives both current figures with their meaning (500 A permanent measuring range, readings to +/-2,100 A); interfaces are NFC, Bluetooth and the battery bus.
- **Truck parts (round 31):** stated by the source: connects to [[Truck Controller and CAN Bus]] (links to the vehicle over LIN and battery bus) | typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

- **Architecture realization — remaining runtime:** HOPPECKE explicitly publishes remaining-driving-time information generated from processed battery data. [[Remaining Runtime Estimation Design]] and [[Remaining Runtime Estimation Software]] therefore capture the estimation role. The exact algorithm and input weighting are not published.

- **Architecture realization — amp-hour accumulation:** this product combines battery-current sensing/monitoring with accumulated amp-hour information, supporting [[Current Integration Amp-Hour Accumulation]]. [[Amp-Hour Accumulator Firmware]] and the prerequisite current-acquisition/controller roles are allocated at **>=95% engineering confidence** because the internal firmware partition is not published.

- **Architecture realization — event and usage logging:** the product explicitly retains event/history data, supporting [[Battery Event and Usage Logging Design]], [[Battery Event Logger Firmware]], and [[Event Log Memory]]. Published clock/timekeeping capability also supports [[Event Time Base]]. The internal record schema, memory technology, and firmware partition remain unpublished.

- **Architecture realization — CAN battery state communication:** the product is allocated [[CAN Battery State Communication Design]] because published evidence establishes battery-state exchange over CAN or a CAN-based vehicle/battery interface. Message identifiers, signal maps, update rates, and protocol details remain product-specific.

- **Architecture realization — wireless battery data:** the product explicitly transmits battery information over a published wireless interface, supporting [[Wireless Battery Data Communication Design]]. [[Wireless Battery Data Communication Firmware]] is allocated at **>=95% engineering confidence** because the internal software partition is not published. The specific radio/interface remains represented separately by the product's verified wireless Design(s).

## Aliases

- trak | collect
- trak collect premium
- trak collect advanced


## Former ids
