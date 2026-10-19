---
type: Info
subtype:
id: INFO-00973
uid: 20261017190000000skellyspencer
status: Draft
tags:
  - research
  - regulation
  - eu
  - battery-passport
  - europe
describes:
  - "[[PosiCharge BMID]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[Integrated Battery Management System]]"
  - "[[Battery Management System Design]]"
describedBy:
  - "[[Document - European Commission Guidance Support for Digital Batteries Passport News Item (2026-08-21)]]"
  - "[[Document - European Commission Batteries Page (retrieved 2026-10-17)]]"
  - "[[Document - European Commission Batteries Passport FAQ (retrieved 2026-10-17)]]"
  - "[[Document - EUR-Lex Regulation 2023-1542 Batteries and Waste Batteries Recitals and Definitions (retrieved 2026-10-17)]]"
  - "[[Document - EUR-Lex Regulation 2023-1542 Full Text as Published 2023-07-28 (Articles 3, 10, 13, 14, 77, 78 and Annexes IV, VII, XIII read)]]"
  - "[[Document - BatteryMBA EU Battery Regulation Passport Dates Page (2026-07-26)]]"
  - "[[Document - Cattwyk Omnibus Package IV Amendments to the Battery Ordinance (2025)]]"
  - "[[Document - Arianee Battery Passport for Material Handling Page (retrieved 2026-10-17)]]"
  - "[[Document - Battery-Tech Network EU Battery Passport Is Smaller Than You Were Told (2026-08-27)]]"
---

# EU Battery Passport and Battery Regulation Register

## Definition

Register of what is documented about the digital battery passport under Regulation (EU) 2023/1542, who carries the obligation, whether it reaches forklift traction batteries and battery-mounted monitoring devices, and what is not known. It checks the backlog claim that the passport "affects battery-mounted ID/monitoring data and partner battery makers" ([[Knowledge Base Backlog]]). Disagreements are numbered C332 to C337 in [[Battery Product Landscape Conflicts and Open Questions]]; new directions are IB-298 to IB-304 in [[Investigation Backlog]].

## Notes

- **Reading rule:** every source was read through a summarizing fetch tool (second-hand). Regulator pages ([[European Commission]]) are not covered by the T1 to T5 tiers; vendor and trade pages are T4. The operative articles of the regulation (Art. 77 passport, Art. 14 state of health and BMS, Art. 13 labelling, Annex XIII) were **not** read: only recitals and Articles 1 to 3 loaded (IB-298). Status is as of 2026-10-17.
- **Scope:** EU market only. No vault note says PosiCharge sells into the EU (IB-281 is still open).

### Update 2026-10-18: operative text read (IB-298)

The full 2023-07-28 text is now in the repo ([[Document - EUR-Lex Regulation 2023-1542 Full Text as Published 2023-07-28 (Articles 3, 10, 13, 14, 77, 78 and Annexes IV, VII, XIII read)]]). The reading rule above is unchanged for the other sources; the paragraphs below are first-hand from the file. The text above is not edited; where it disagrees with the primary text the difference is logged in C333, C337 and C351.

- **Scope of the passport (Art. 77):** each industrial battery above 2 kWh from 2027-02-18, defined by category and size, not chemistry; text search found no lead-acid exclusion (supports the vendor claim in C333). Forklifts are not named; the off-road machinery wording sits in a recital (analyst reasoning links it to forklifts).
- **State of health duty (Art. 14) is narrower than the Commission FAQ summary above.** Art. 14(1) names only stationary storage systems, LMT batteries and electric vehicle batteries. A forklift traction battery is none of the three on the reading above, so the Annex VII state-of-health data in the BMS is not required of it by this article. Annex XIII point 4(b) still lists "information on the state of health ... pursuant to Article 14" for every passport (C351).
- **What a forklift battery passport does require from use data (Annex XIII point 4(d)):** cycle counts, negative events, and periodically recorded temperature and state of charge. These are the kind of data a battery-mounted logger could supply (hypothesis, not stated by the text). The responsible party is the operator placing the battery on the market (Art. 77(4)).
- **Performance document (Art. 10, from 2024-08-18):** applies to industrial batteries above 2 kWh. Capacity fade, power fade and internal resistance increase must be declared with their test conditions (Annex IV). Minimum values from 2027-08-18 or 18 months after a delegated act due 2026-02-18; adoption not checked (IB-330).
- **BMS definition (Art. 3(25)) is functional:** controls or manages electric and thermal functions, stores Annex VII data, and communicates with the vehicle or charging infrastructure. Whether a monitor that only measures and reports meets it is not answered by the text (C337).
- **Not read or not in the file:** amendments after 2023-07-28 (IB-331), the Art. 77(9) access-rights act (deadline in the text 2026-08-18; the register above records a draft expected October or November 2026), the data carrier standards.

### Bottom line (analyst summary)

1. **The date is real and not postponed in any source read.** The Commission says each EV, light means of transport and industrial battery above 2 kWh needs a passport from 2027-02-18 ([[Document - European Commission Guidance Support for Digital Batteries Passport News Item (2026-08-21)]]). The Commission batteries page lists no omnibus or postponement for the passport. The postponement that exists (to 2027-08-18) concerns supply-chain due diligence, not the passport.
2. **The backlog premise is wrong about who is affected.** The obligation sits on the economic operator placing the finished battery on the EU market (battery maker, importer, or whoever completes the battery), not on a charger or accessory maker. PosiCharge as a charger supplier carries no passport duty on the evidence read. The effect on PosiCharge is indirect: customers' battery makers may ask for data from battery-mounted devices (C332).
3. **Where a BMID could matter is unresolved.** The Commission FAQ says a traction battery normally includes the BMS, that the operator who completes a battery (for example adds a BMS) becomes responsible, and that state-of-health requirements apply only where the battery has a BMS. No source says whether an aftermarket [[PosiCharge BMID]] or [[PosiCharge Battery Rx]] is a "BMS" or "completes" a battery (C337). This is the single point that decides whether the topic is a product requirement or a non-issue for the company.
4. **Lead-acid forklift batteries in scope is a vendor claim only.** The one source that addresses material handling is a passport-software vendor, which says a lead-acid traction battery above 2 kWh is an industrial battery in scope. The Commission FAQ is silent on chemistry; the regulation text read gives a 5 kg rule and a definition based on design for industrial use (C333). Analyst reasoning: a 24 V to 80 V traction battery is far above 2 kWh, so it is likely in scope, but treat as unconfirmed until Art. 77 is read.
5. **Replacement and remanufactured batteries.** The Commission FAQ says a battery placed on the market before 2027-02-18 needs a passport if remanufactured afterwards. The vendor says replacement batteries placed on the market after that date are in scope. These are different statements and are not in conflict, but only the first is regulator-sourced (C336).
6. **Counts and thresholds disagree between secondary sources.** Mandatory data points for industrial batteries: vendor says 32 of 71; the Commission news item gives no count; the trade article gives EV 56 and LMT 59 and none for industrial (C335). Due diligence small-company exemption: vendor says EUR 40 million, law firm says EUR 150 million (C334).
7. **Open items that block firm requirements:** access-rights implementing act (draft expected October or November 2026, per the FAQ), Omnibus IV formal adoption (provisional agreement 2026-06-09, per one training page), the data carrier and QR standards, and which fields a device could fill.

### What is known by product (vault sources)

| Product | Passport relevance stated? | Source |
|---|---|---|
| PosiCharge BMID (all variants) | No source mentions it; relevance depends on C337 | [[PosiCharge BMID]] |
| PosiCharge Battery Rx | No source mentions it; logs voltage, temperature and events per vault note; could source dynamic data fields only if treated as part of the battery | [[PosiCharge Battery Rx]] |
| Integrated BMS in lithium traction batteries | FAQ: BMS is normally part of the finished traction battery, so the battery maker is responsible and state-of-health data comes from the BMS | [[Integrated Battery Management System]] |
| Standalone or external BMS | Not addressed; same open point as C337 | [[Battery Management System Design]] |

### Hypotheses (analyst reasoning, untested)

- **EH1:** battery makers selling lithium traction batteries into the EU will source passport dynamic data (state of health, usage history) from their integrated BMS, not from an aftermarket monitor. Test: IB-298, IB-302.
- **EH2:** aftermarket monitors on lead-acid or older batteries matter only if a passport is required for those batteries and the battery maker lacks usage data; a monitor could then be a data source. Test: IB-298, IB-304.
- **EH3:** a charger maker has no passport duty but may be asked to expose charge and usage data through its communication interface. Test: IB-304 (needs owner and customer input).

### Question for the owner

Does PosiCharge sell chargers or BMID/Battery Rx devices to the EU, and are BMID devices fitted by battery makers at production or retrofitted by users? This decides whether any requirement is derived. Not answered when asked for the fire-code topic (IB-281).

## Open questions

- What do Art. 77, Art. 14 and Annex XIII say about industrial batteries, lead-acid and BMS data (IB-298)? Answered in the 2026-10-18 update above; remaining question is C351.
- Which data points are mandatory for industrial batteries (IB-299)?
- Access-rights act: who may read usage data, and does it reach monitor data (IB-300)?
- What did Omnibus IV adopt (IB-301)?
- How is a BMS defined, and is an aftermarket monitor one (IB-302)?
- Standards for the data carrier and passport format (IB-303)?

## Sources

Listed in `describedBy`. Not readable here: the Commission data-points PDF. The operative text is read as of 2026-10-18 for the articles listed in the update above.

## Aliases

- EU Battery Passport Register

## Former ids
