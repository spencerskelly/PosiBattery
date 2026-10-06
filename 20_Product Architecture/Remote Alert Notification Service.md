---
type: Object
subtype: software
id: OBJ-90076
uid: 20261006175500008skellyspencer
status: Draft
tags:
  - reusable-architecture
  - battery-monitoring
  - alert
  - cloud
  - software
reuseScope: cross-product
hasDesign:
  - "[[Remote Exception Notification]]"
dependsOn:
  - "[[Cloud Portal Integration]]"
performs:
  - "[[Alert on Abnormal Condition]]"
partOf:
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!plus]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Yale Battery Vision]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[Crown Battery Health Monitor]]"
---

# Remote Alert Notification Service

## Definition

Software/service role that turns an abnormal battery event into a remote notification such as email, text, portal alert, or fleet exception message.

## Notes

- Product links represent the end-to-end commercial alert capability, not necessarily software physically embedded in the battery-mounted device.
- [[Hyster Battery Tracker]], [[Yale Battery Vision]], [[PosiCharge Battery Rx]] and [[Crown Battery Health Monitor]] explicitly publish remote alert behavior.
- The transport path and hosted platform remain product-specific and are represented separately by communication and cloud-integration Designs.

## Former ids
