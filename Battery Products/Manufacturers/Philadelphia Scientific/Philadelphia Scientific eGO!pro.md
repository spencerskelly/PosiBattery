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
describedBy:
  - "[[Battery Product Landscape Conflicts and Open Questions]]"
performs:
  - "[[Measure Battery Voltage]]"
  - "[[Measure Battery Current]]"
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Alert on Abnormal Condition]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Transmit Battery Data Wirelessly]]"
  - "[[Upload Battery Data to Cloud Portal]]"
hasDesign:
  - "[[Hall-Effect Current Sensing]]"
  - "[[Split-Core Current Sensor]]"
  - "[[Local LED Indicator]]"
  - "[[Audible Alarm]]"
  - "[[Acid-Resistant Sealed Housing]]"
  - "[[Light-Triggered Data Upload]]"
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
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Voltage]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Measure Battery Current]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf> <https://www.phlsci.co.uk/ego/ego-pro/>
  - [[Measure Battery Temperature]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Sense Electrolyte Level]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Log Battery Events and Usage]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Alert on Abnormal Condition]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/> <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
  - [[Indicate Battery Status Locally]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Transmit Battery Data Wirelessly]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
  - [[Upload Battery Data to Cloud Portal]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
- **Design characteristics, with citations:**
  - [[Hall-Effect Current Sensing]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf> <https://www.phlsci.co.uk/ego/ego-pro/>
  - [[Split-Core Current Sensor]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf> <https://www.phlsci.co.uk/ego/ego-pro/>
  - [[Local LED Indicator]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Audible Alarm]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
  - [[Acid-Resistant Sealed Housing]] (V): <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
  - [[Light-Triggered Data Upload]] (V): <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
- **Sources used for the mapping above:** PhilSci eGO!pro product page (US) <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>; PhilSci eGO!pro sales sheet <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>; PhilSci eGO!pro page (UK) <https://www.phlsci.co.uk/ego/ego-pro/>
- The eGO!pro page lists 25 performance metrics per minute, flooded and VRLA versions, FlexiTap, M4 screw or M10 bolt connection, 24 to 80 V nominal (12, 72 and 120 V optional), integrated voltage sensor, internal temperature sensor, LED indications, cycle data and minute-by-minute logs, reversible power connection, flame-retardant case, IP65, 235 g flooded and 212 g VRLA, over-discharge threshold below 20 percent state of charge, and a 2-year warranty. Source: PhilSci eGO!pro page (US) (T1), retrieved 2026-10-02. <https://www.phlsci.com/products/ego-battery-performance-monitors/ego-pro/>
- The sales sheet says eGO!pro has a precision bi-directional Hall-effect split-core current sensor, measures energy in and out, uploads data through the eGO!cloudlink battery-room gateway, integrates with eGO!alerts, gives audible alerts, and supports light-triggered data upload using a phone torch. Source: PhilSci eGO!pro sales sheet (T1), retrieved 2026-10-02. <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf>
- **Verification 2026-10-02:** the seed claims above (split-core current sensor, flooded and VRLA models, alerts, data upload) are re-verified. **Conflict (C22):** the US page gives power as 2 W initial Bluetooth connection and 1.2 W nominal, while the UK page gives 200-24 mA at 24-80 V (radio transmitting) and 100-13 mA (not transmitting). Units and magnitudes differ <https://www.phlsci.co.uk/ego/ego-pro/>.

## Aliases

- eGO!pro
- eGO pro

## Former ids
