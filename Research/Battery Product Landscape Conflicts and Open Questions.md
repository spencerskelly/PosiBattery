---
type: Info
subtype:
id: INFO-00071
uid: 20261002161409691skellyspencer
status: Draft
tags:
  - battery-landscape
  - conflicts
  - open-questions
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Battery Connector Assembly]]"
  - "[[Battery Thermal Management Device]]"
  - "[[Industrial Battery Charger]]"
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge PosiGuard]]"
  - "[[AMETEK Prestolite Power WBID Pro]]"
  - "[[EnerSys Wi-iQ]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Yale Battery Vision]]"
  - "[[AMETEK Prestolite Power TruBid]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Exide Motion+ EasyMonitor]]"
  - "[[Raymond iBattery]]"
  - "[[Flux Power]]"
  - "[[Crown Equipment]]"
  - "[[East Penn Manufacturing]]"
  - "[[Hyster-Yale]]"
---

# Battery Product Landscape Conflicts and Open Questions

## Definition

Register of conflicting, ambiguous or unverified evidence and open modeling questions found while building the landscape survey.

## Notes

- Each item states what differs, the sources, and what would resolve it. Nothing here is resolved. Items stay visible until a primary source or a user decision settles them.
- **C1 - BMID acronym used by two vendors.** PosiCharge expands it as Battery Monitor and Identifier (FAQ) or Smart Battery Monitor and Identification Device (spec sheets). Crown expands it as Battery Monitoring Identification Device. Crown describes it as a lead-acid battery-top module that detects low electrolyte and adjusts charge rate; PosiCharge describes it as holding identity, profile and event history with an immersed thermistor. No source shows they are interchangeable or compatible. Resolve with: both vendors' datasheets; keep as separate Objects. Sources: PosiCharge FAQ <https://www.posicharge.com/faq/>; Crown <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM>.
- **C2 - What a PosiCharge BMID physically includes.** The FAQ says the BMID has two parts, an immersed thermistor and an electronic device. Charger spec sheets list a Smart BMID and an Electrolyte Immersed Thermistor as separate features. The ProCore manual calls Battery Rx a smart BMID, and ProCore Edge refers to a wireless BMID over Bluetooth. This suggests several BMID hardware variants, but no source lists them. Resolve with: PosiCharge BMID and Battery Rx datasheets and part numbers. Sources: <https://www.posicharge.com/faq/>; <https://www.posicharge.com/source/PDF/2500series.pdf>; <https://www.posicharge.com/procoreedge>.
- **C3 - Age of PosiCharge documents.** The Battery Rx sheet names AeroVironment and the 2500 Series sheet mentions approvals 'in process'. Both likely predate current product lines. Treat their specifications as possibly obsolete until current documents confirm. Source: <https://www.posicharge.com/source/PDF/BatteryRx.pdf>.
- **C4 - Connector color and voltage coding.** One reseller says any color connector can be used on any forklift battery, then says not to mix colors and that a battery will not accept a charger set to a different voltage. Anderson and TVH describe color or coding pins as the mechanism that prevents a voltage mismatch. The reseller wording is ambiguous or inaccurate. Resolve with: Anderson's voltage and color chart and the REMA datasheet. Sources: <https://intellaparts.ca/c/battery-connectors/battery-connectors.html>; <https://www.mouser.lt/pdfDocs/AG-MHCS.pdf>; <https://www.tvh.com/en-us/parts/parts-for/forklifts/electrical-parts/forklift-battery-connectors>.
- **C5 - DIN coding-pin meaning.** TVH describes coding pins as preventing voltage mismatch. A REMA listing describes pin color as distinguishing dry, wet and universal batteries. These may both be true on different pin attributes (position vs color), but no source says so. Resolve with: DIN 43589-1 and REMA datasheet. Sources: TVH and Akkusys links in [[Battery Connector Assembly]].
- **C6 - Cold-weather figures are not comparable.** Toyota: cold-store version used down to -30 C. BSLBATT: heating 'up to -40 C'. ROYPOW: rated -40 C, charging in place typically to -30 C. Stromcore: tested idle at -40 F (equal to -40 C) for up to 14 hours. These describe operating, storage and charging limits inconsistently. Resolve with: per-vendor datasheets that separate operating, storage and charge limits. Sources: links in [[Battery Thermal Management Device]].
- **C7 - Heater power source varies.** BSLBATT describes a heater designed to run during overnight in-truck charging. Stromcore describes a heater drawing about 2 percent of battery capacity. ROYPOW says buyers should ask whether it runs off the charger or the cells. No retrieved source gives a per-product answer. Resolve with: datasheets and manuals. Sources: <https://www.thescxchange.com/articles/5994-case-study-industrial-lithium-battery-for-freezer-forklift-truck-environments>; <https://www.stromcore.com/cold-storage>; <https://www.roypow.com/blog/cold-storage-forklift-batteries/>.
- **C8 - Superlative claim.** Green Cubes states it is the only manufacturer of both Li-ion batteries and chargers for material handling equipment. HOPPECKE markets its own batteries and chargers, but the retrieved HOPPECKE evidence is lead-acid, so this is not a direct contradiction. Not tested. Source: <https://www.groundhandlinginternational.com/content/news/green-cubes-announces-patent-award-for-bms>.
- **C9 - Protection hardware applicability.** Sources for contactors, pre-charge and pyro fuses are automotive or high-voltage EV. Applicability to 24 to 96 V MHE and GSE batteries is unverified. Do not carry these into MHE or GSE models without an MHE or GSE source. Sources: <https://www.hpacademy.com/courses/ev-fundamentals/batteries-battery-pack/>; <https://ti.com/document-viewer/lit/html/SLYY226/GUID-81B7EF29-8949-470F-BA68-2D91DEB6A1C7>.
- **Q1 - Scope.** Installed-only (as in the seed branch) or all battery-connected products with locus recorded per product? This survey used the second.
- **Q2 - Category subtype.** Categories use Object subtype by dominant discipline (electrical or mechanical) and the root uses part. Subtype for abstract families is provisional.
- **Q3 - One product, several families.** Battery Rx is monitor, identifier and telematics. Multiple subtypeOf or one primary family?
- **Q4 - Schema gaps.** The schema has no first-class type for manufacturer, market, or evidence tier, and `derivedFrom` is Requirement-only. This survey records those as note text. An amendment is a release-owner decision, not made here.
- **Q5 - Evidence tiers and conventions.** Proposed tiers and conflict handling in [[Landscape Evidence and Modeling Conventions]] need approval or replacement.
- **C10 - PosiGuard vs BMID classification.** The seed text files PosiGuard under Battery Monitoring Device and the BMID under identification and charge interface. PosiCharge's own PosiConnect app listing calls PosiGuard a 'BMID device'. The user listed PosiGuard separately from BMID 1 and BMID 3. Unresolved. Sources: <https://apps.apple.com/mx/app/posiconnect/id6748969496>; [[PosiCharge PosiGuard]].
- **C11 - Prestolite WBID charger interaction.** Seed text treats WBID Pro as monitoring only. A 2014 release for the obsolete WBID says charger communication can run over the DC cable and works with Charger Interface Devices. Current WBID Pro page is silent on charger communication. Source: <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>; [[AMETEK Prestolite Power WBID Pro]].
- **C12 - PosiCharge BMID names do not map to the stated variants.** FAQ, spec sheets, ProCore pages and the app listing use BMID, Smart BMID, Battery Rx, wireless BMID and PosiGuard BMID. The user stated BMID 1 and BMID 3 (with BLE, CAN, international and E-meter). No source ties the public names to BMID 1 or 3. See [[PosiCharge BMID Variants]]. Sources: <https://www.posicharge.com/faq/>; <https://www.posicharge.com/source/PDF/BatteryRx.pdf>; <https://www.posicharge.com/procoreedge>; <https://apps.apple.com/mx/app/posiconnect/id6748969496>.
- **C13 - Wi-iQ CAN is optional.** Seed text says Wi-iQ specifications list CAN. The EnerSys Wi-iQ4 manual describes CAN as an optional module (CANopen or J1939). Both are kept on [[EnerSys Wi-iQ]]. Source: <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>.
- **C14 - Seed taxonomy vs category draft.** The seed taxonomy splits Monitoring Device from Identification and Charge Interface Device, both under a locus-based root. The category draft has one Monitoring and Identification category and treats locus as a per-product attribute. Resolved structurally by making both seed families subtypes of both parents; whether that is the right model is open (Q1).
- **C15 - Seed note dates.** Seed notes say market evidence was checked on 2026-10-02. Where re-checked, some sources are older (SmartBlinky Pro item, 2014 and 2017 Prestolite releases, 2019 and earlier PosiCharge sheets). Product status for those is unclear. Sources: see C15 detail below.
- **Q6 - BMID 2.** Is there a BMID 2 and, if so, what is it?
- **Q7 - PosiGuard vs BMID 3.** Resolved in part on 2026-10-02: the user states PosiGuard is the next generation of BMID. Still open: which variant it directly follows.
- **C10 resolution (2026-10-02):** the user states PosiGuard is the next generation of BMID. PosiGuard is now a subtype of PosiCharge BMID. The original conflict text above is kept.
- **C16 - Wi-iQ charger link.** The competitor table said no charger interaction was stated for EnerSys Wi-iQ. The Wi-iQ3 brochure lists wireless communication with the EnerSys modular charger. Generation matters: this is Wi-iQ3, not Wi-iQ4. Source: <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>; [[EnerSys Wi-iQ]].
- **C17 - BMID chemistry coverage.** PosiCharge FAQ and charger pages are lead-acid oriented. The Salt Lake City airport rule requires BMIDs on lithium-ion electric GSE (effective 2020-09-15). The rule uses the generic term and does not name a vendor. See [[SLC Airport EGSE BMID Requirement]]. Whether a PosiCharge BMID works on lithium batteries is not established. Sources: <https://www.Slcairport.Com/assets/pdfDocuments/EGSEInspectionProcedures.pdf>; <https://www.posicharge.com/faq/>.
- **C18 - Powered-by-PosiCharge devices.** Hyster Battery Tracker and Yale Battery Vision are described as 'Powered by PosiCharge technology' with capabilities similar to Battery Rx. Relationship to [[PosiCharge Battery Rx]] and PosiNET is not stated. Sources: [[Hyster Battery Tracker]], [[Yale Battery Vision]].
- **C19 - TruBid status.** [[AMETEK Prestolite Power TruBid]] appears in trade press but not on the current Prestolite Data Devices page. Market status unclear. Sources: <https://dcvelocity.com/articles/31462-ametek-s-trubid-system-accurately-measures-battery-charge>; <https://www.prestolitepower.com/products/datadevices>.
- **C20 - Seed classification of WBID Pro and Wi-iQ.** Both sit under Battery Monitoring Device only. Retrieved sources show charger communication for the earlier WBID (DC cable, 2014) and Wi-iQ3 (wireless to charger). Not changed; flagged for a decision on dual parentage.
- **C21 - Locus of PowerTrac DT3 and Site Probe.** Both are study or diagnostic tools, so they are filed under the category, not the installed-device family. The seed scope treats temporary diagnostic equipment as adjacent.
- **C16 update (2026-10-02):** the Wi-iQ4 manual itself (not only the Wi-iQ3 brochure) lists Zigbee communication to chargers (NexSys+ battery charger). The earlier 'no charger link stated' cell was wrong. Source: <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>; [[EnerSys Wi-iQ]].
- **C17 update (2026-10-02):** PosiGuard's current page says it is designed for both lead-acid and lithium batteries, so the newest BMID generation covers lithium. Whether earlier BMIDs did is still open. Source: <https://posicharge.com/products/posiguard/>.
- **C22 - eGO!pro power figures disagree.** US page: 2 W initial Bluetooth connection, 1.2 W nominal. UK page: 200-24 mA (radio transmitting) and 100-13 mA (not transmitting) at 24-80 V. Units differ and the magnitudes cannot be reconciled. Sources: <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>; <https://www.phlsci.co.uk/ego/ego-pro/>; [[Philadelphia Scientific eGO!pro]].
- **C23 - eGO! product names.** Trade sources use eGO!Mini and eGO!c; current PhilSci pages list eGO!core, eGO!plus and eGO!pro. No source says which replaced which. Sources: <https://www.phlsci.com/products/ego-battery-performance-monitors/>; <https://warehousenews.co.uk/?p=68147>; [[Philadelphia Scientific eGO!Mini]], [[Philadelphia Scientific eGO!c]].
- **C24 - Exide EasyMonitor and GNB PRO 2.0.** Two Exide documents use near-identical wording and specs for a 3-in-1 sensor monitor. Whether GNB PRO 2.0 is the earlier name is not stated. The GNB PRO 2.0 URL returned 404 on direct fetch though a search excerpt was available. Sources: <https://www.exidegroup.com/en/product/easymonitor>; <https://exidegroup.com/it/en/document/gnb-pro-20-battery-protection-brochure>; [[Exide Motion+ EasyMonitor]].
- **C25 - Raymond page host.** The iBATTERY page found is on a 'test-' subdomain, so it may not be production content. The 2010 launch release is on raymondcorp.com. Sources: <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring>; <https://raymondcorp.com/news/2010/ibattery-launch>; [[Raymond iBattery]].
- **C13 detail:** CAN is optional on Wi-iQ4 according to its feature list, yet two of six part numbers are sold only as 'Premium CAN' versions. Both statements are in the same manual. Source: <https://enersys.com/4a788d/globalassets/documents/product-documentation/_misc/wi-iq/emea/emea-en-om-ens-wiq-0524.pdf>.
- **C15 detail:** dated sources used in this register include the 2014 and 2017 Prestolite releases <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html>, the 2010 Raymond release <https://raymondcorp.com/news/2010/ibattery-launch>, the 2016 Yale item <https://www.mhlnews.com/new-products/forklift-battery-monitor-new-products> and the 2014 and 2018 PowerTrac sheets <https://powerdesignerssibex.com/wp-content/uploads/2024/04/PD-TRA-SP_PowerTrac_SP_BatteryDataLogger.pdf>.
- **C20 and C21 detail:** charger communication evidence for the earlier WBID is at <https://finance.yahoo.com/news/ametek-prestolite-power-launches-wireless-142836825.html> and for Wi-iQ3 at <https://integration.enersys.com/493bb4/globalassets/documents/product-documentation/_misc/wi-iq/emea/wi-iq3-battery-monitoring-device-brochure.pdf>; the seed scope on temporary diagnostic tools is in [[Battery Installed Device Market Reference]].
- **C26 - Flux Power private-label partners are unnamed.** Two filings or releases say private-label OEM relationships exist; neither names the OEM. A separate presentation names six OEM relationships without saying private label. Do not equate the two lists. Sources: <https://www.sec.gov/Archives/edgar/data/1083743/000165495419003678/flux_8k.htm>; <https://www.businesswire.com/news/home/20240912587367/en>; <https://www.fluxpower.com/hubfs/investors/Flux-Power-Company-Presentation-October-2019.pdf>; [[Flux Power]].
- **C27 - Crown Equipment and a similarly named battery company.** Supplier lists include 'Crown Battery' alongside makers of forklift batteries; Crown Equipment sells V-Force-branded batteries. Any link between the two is not established. Sources: <https://www.foxtronpowersolutions.com/forklift-battery-manufacturers/>; <https://www.crown.com/en-us/newsroom/articles/product-news/crown-equipment-unveils-integrated-lithium-ion-energy-storage-system-for-forklifts.html>; [[Crown Equipment]].
- **C28 - East Penn private-label statement scope.** East Penn says most Transportation-division products are sold private label; that does not describe motive power. Source: <https://www.eastpennmanufacturing.com/divisions/transportation/>; [[East Penn Manufacturing]].
- **C29 - Hyster-Yale product names.** EnerSys writes Hyster Tracker and Yale Vision; trade press writes Hyster Battery Tracker and Yale Battery Vision. Sources: <https://www.enersys.com/de/about-us/news/fleet-managers-get-powerful-flexibility-combining-enersys-technology-breadth-with-yale-power-key-and-hyster-power-cellect/>; <https://refrigeratedfrozenfood.com/articles/91289-forklift-battery-management-solution-monitors-health-usage>; [[Hyster-Yale]].
- **Q8 - Organization modeling.** Keep organizations as Info notes and relationships as register rows, or amend the schema to add an Organization type and a supplier or rebrand relationship? Context: [[Industrial Battery Supply and Private-Label Relationships]]; schema files <https://github.com/spencerskelly/PosiBattery/blob/main/99_System/03_Schemas/relationships.yaml>.

## Aliases

- Landscape conflicts register

## Former ids
