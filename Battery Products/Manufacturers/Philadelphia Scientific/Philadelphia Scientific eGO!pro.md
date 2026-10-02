---
type: Object
subtype: electrical
id: OBJ-00008
uid: 20261002150858944skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - lead-acid
subtypeOf:
  - "[[Battery Monitoring Device]]"
performs:
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Upload Battery Data to Cloud Portal]]"
  - "[[Indicate Battery Status Locally]]"
hasDesign:
  - "[[Split-Core Current Sensor]]"
  - "[[Local LED Indicator]]"
---

# Philadelphia Scientific eGO!pro

## Definition

Philadelphia Scientific commercial battery performance monitor for industrial lead-acid battery applications.

## Notes

- Manufacturer: Philadelphia Scientific
- Market evidence checked: 2026-10-02
- Installation locus: battery-mounted; vendor literature describes battery connection options and a split-core current sensor measuring battery energy flow.
- Published capabilities include bidirectional current/energy measurement, minute-by-minute battery metrics, high-temperature and electrolyte alerts, and data upload for online analysis.
- Vendor literature identifies flooded and VRLA models.
- Evidence:
  - https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/
  - https://www.phlsci.com/media/akpfbf1u/egopro-ssh-ps-us-en-doc0642.pdf
- **Verification 2026-10-02 (family verified; this model not re-opened):** the eGO! range (eGO!Mini, eGO!c, eGO!Tools app) is described as mounted on top of the battery with LED indicators; eGO!Mini stores data on a removable USB drive; eGO!c uploads each battery cycle to batterymanagement.net. Source: Warehouse News trade feature (undated) (T4) <https://warehousenews.co.uk/?p=68147>
- **Not re-verified:** the split-core current sensor, flooded and VRLA model split and alert details above. **Not stated in retrieved sources:** any charger interaction. This looks like a monitor and data gateway, not a charger-interface device.
- **Functions performed (evidence):** [[Measure Battery Current]] (C); [[Measure Battery Temperature]] (C); [[Alert on Abnormal Condition]] (C); [[Upload Battery Data to Cloud Portal]] (C); [[Indicate Battery Status Locally]] (C). V = verified this pass, C = carried from seed text, U = user-stated.
- **Design characteristics (evidence):** [[Split-Core Current Sensor]] (C); [[Local LED Indicator]] (C).

## Aliases

- eGO!pro
- eGO pro

## Former ids
