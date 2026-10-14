---
type: Document
subtype:
id: DOC-00113
uid: 20261013191023168skellyspencer
status: Draft
tags:
  - source-document
  - brochure
  - tier-T1
sourceClass: brochure
sourceUrl: "https://www.fluxpower.com/hubfs/GSE%20Battery%20Pack%20V.2%20-%20Brochure.pdf"
accessed: 2026-10-13
describes:
  - "[[Flux Power GSE Pack]]"
---

# Document - Flux Power GSE Battery Pack V.2 Brochure (2021)

## Definition

Flux Power brochure for the GSE battery pack family (GSE2, GSE3, GSE4, GSE6): ratings, sizes, weights, charge current, temperature ranges, BMS and CAN.

## Notes

**How it was read.** Through a fetch tool that returns a model-written summary of the file, not the raw text, on 2026-10-13. The direct download from the workspace was refused by the network proxy, so no value was checked against the raw PDF (IB-166).

- Voltage: system and nominal 80 V (76.8 V); packs "from 80V up to 400V".
- Capacity and energy listed as 210, 315, 420 and 630 Ah and 16.8, 25.2, 33.6 and 50.4 kWh; the summary did not map them to models (IB-166). Arithmetic check: 80 V x 315 Ah = 25.2 kWh, so 315 Ah goes with 25.2 kWh; 76.8 V x 315 Ah = 24.2 kWh (C213).
- Sizes (L x W x H) and weights: GSE2 44.2 x 14.0 x 22.5 in, 535 lb (243 kg); GSE3 35.3 x 19.9 x 26.2 in, 875 lb (397 kg); GSE4 35.3 x 26.3 x 26.2 in, 925 lb (420 kg) or 1,178 lb (534 kg); GSE6 35.3 x 39.0 x 26.0 in, 1,753 lb (795 kg).
- Maximum continuous external charge current: GSE2 200 A, GSE3 300 A, GSE4 350 A, GSE6 350 A; custom charge profiles with higher current available. Charge temperature 0 to 55 C (32 to 131 F); discharge -20 to 55 C (-4 to 131 F).
- BMS 2.0, designed in-house with patented software; sleep mode with automatic shutoffs; individual cell monitoring. Isolated external CANbus for GSE integration.
- Chemistry stated only as "advanced lithium-ion". Not stated: certifications, warranty, cycle life.

## Provenance

- **Source identity:** Flux Power product brochure, official manufacturer site.
- **Original web address:** <https://www.fluxpower.com/hubfs/GSE%20Battery%20Pack%20V.2%20-%20Brochure.pdf>.
- **Access date:** 2026-10-13. **Revision:** footer shows 955005 and 2/21 with Copyright 2021 Flux Power; the summary says the date is likely a February 2021 revision, not labelled on the page.
- **Evidence tier:** T1 official vendor document (values second-hand through the fetch tool's summary).

## Traceability

- `describes` links the brochure to [[Flux Power GSE Pack]]. Disagreements with the other Flux brochure and with the 2016 report are logged in C212 and C213.

## Aliases

## Former ids
