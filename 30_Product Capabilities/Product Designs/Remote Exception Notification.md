---
type: Design
subtype:
id: DES-90027
uid: 20261006175500004skellyspencer
status: Draft
tags:
  - battery-monitoring
  - design-characteristic
  - alert
  - cloud
  - notification
subtypeOf:
  - "[[Abnormal Condition Alert Design]]"
designOf:
  - "[[Philadelphia Scientific eGO!pro]]"
  - "[[Remote Alert Notification Service]]"
  - "[[Hyster Battery Tracker]]"
  - "[[Yale Battery Vision]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[Crown Battery Health Monitor]]"
  - "[[Philadelphia Scientific eGO!core]]"
  - "[[Philadelphia Scientific eGO!plus]]"
---

# Remote Exception Notification

## Definition

Abnormal-condition alert delivered remotely through a hosted service, email, text message, portal notification, or equivalent fleet-management channel.

## Notes

- [[Hyster Battery Tracker]] explicitly sends email alerts for high temperature, overdue equalization, deep discharge, electrolyte high/low and imbalance.
- [[Yale Battery Vision]] and [[PosiCharge Battery Rx]] explicitly provide email alerts through their remote monitoring ecosystems.
- [[Crown Battery Health Monitor]] explicitly supports email or text alerts.
- Philadelphia Scientific eGO products publish configurable eGO!alerts / Critical Alert Service through batterymanagement.net.
- This Design describes notification delivery and does not imply a specific wireless transport; cellular, gateway, Wi-Fi and other paths remain separate communication implementations.

## Former ids
