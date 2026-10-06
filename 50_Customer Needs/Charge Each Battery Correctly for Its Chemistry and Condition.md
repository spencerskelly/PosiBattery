---
type: Use Case
subtype: why
id: UC-00004
uid: 20261003215631068skellyspencer
status: Draft
tags:
  - customer-need
  - need-hypothesis
  - vendor-stated
realizedBy:
  - "[[Adapt Charge to Battery Condition]]"
  - "[[Identify Battery to Charger]]"
  - "[[Compensate Charge for Battery Temperature]]"
  - "[[Charge Under BMS Control]]"
participants:
  - "[[Maintenance Technician]]"
  - "[[Fleet Operations Manager]]"
needOf:
  - "[[Maintenance Technician]]"
  - "[[Fleet Operations Manager]]"
arisesIn:
  - "[[Charge a BMID-Equipped Battery Using Battery Information]]"
---

# Charge Each Battery Correctly for Its Chemistry and Condition

## Definition

Customer need: Charge Each Battery Correctly for Its Chemistry and Condition. The problem behind it: Mixed fleets hold different chemistries and battery states; a wrong or uncompensated charge damages batteries or creates unsafe conditions.

## Notes

- **Evidence status: need hypothesis.** The statements below are what makers and dealers say their products do for customers. No customer, user or buyer source in the vault confirms that customers hold this need or rank it. Per the ruleset, source research becomes a validated need only after customer-side evidence.
- **Problem solved (analyst wording):** Mixed fleets hold different chemistries and battery states; a wrong or uncompensated charge damages batteries or creates unsafe conditions.
- **Who has the problem:** [[Maintenance Technician]], [[Fleet Operations Manager]].
- **Operating segments (analyst crosswalk to [[PosiCharge Market Segments and Jobs-to-Be-Done]], hypothesis):** Mixed-chemistry fleets, Battery-room and centralized charging.
- **Realized by (specific functions; products link to these):** [[Adapt Charge to Battery Condition]], [[Identify Battery to Charger]], [[Compensate Charge for Battery Temperature]], [[Charge Under BMS Control]].
- **Products reaching this need:** 47 by function, design or option (owner decision, round 40: design and option routes count as reached); 27 of those perform a realizing function. Largest families by function: Chargers/Industrial Modular Chargers (17), Battery Accessories/Identification and Charge Interface Devices (4), Battery Accessories/Monitoring Devices (2), Chargers/Light-Duty Chargers (2), Fleet Software and Platforms/Battery and Charger Management (1), Chargers/Wireless Chargers (1). The metric route (hypothesis) adds 0 more. Per-product routes in [[Product to Customer Need Map]].
- **Vendor-stated evidence (by product):**
  - [[EnerSys NexSys AIR Wireless Charger]]: The brochure says NexSys AIR wireless chargers can charge multiple battery technologies including flooded lead-acid, are compatible with all EnerSys battery technologies, and can reduce AGV waiting time for charging. Source: EnerSys NexSys AIR brochure (T1), retrieved 2026-10-02. <https://www.enersys.com/493367/globalassets/documents/product-documentation/_enersys/apac/apac_en-imp-nex-com-air-0623.pdf>
  - [[Stryten inCOMMAND]]: Stryten says M-Series chargers communicate with inCOMMAND, which monitors key battery data points in real time, and the charger adjusts its charge rate if battery temperature rises; the M-Series Li610 integrates with inCOMMAND. Source: Stryten article on X-7 chargers and Li610 release (T1/T2), retrieved 2026-10-03. <https://stryten.com/?p=173790>
  - [[AMETEK Prestolite Power BID with Ah Accumulator]]: [[Identify Battery to Charger]] (V): <https://www.prestolitepower.com/-/media/ametekprestolite/documentation/bid/bid-ah-accumulator-datasheet-aug-2018.pdf>
- **Gaps:** no customer-side source; each function in the list is realized by only the products that state it, so the product count is a lower bound; no Requirement is linked (the vault leaves requirements as an intentional gap).

## Aliases


## Former ids
