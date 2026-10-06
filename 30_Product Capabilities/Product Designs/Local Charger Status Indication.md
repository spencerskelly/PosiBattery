---
type: Design
subtype:
id: DES-90020
uid: 20261006161000001skellyspencer
status: Draft
tags:
  - general-design
  - charger
  - design-characteristic
  - local-status
subtypeOf:
  - "[[Charger Operator Interface Design]]"
supertypeOf:
  - "[[Charger Status LED Bar]]"
  - "[[Remote Charger Status Stack Light]]"
realizes:
  - "[[Indicate Charger Status Locally]]"
dependencyOf:
  - "[[Indicate Charger Status Locally]]"
---

# Local Charger Status Indication

## Definition

General charger-interface design family for presenting charger or charge-process status locally through dedicated visual indicators.

## Notes

- This family separates charger-local indication from [[Indicate Battery Status Locally]], whose scope is the battery or battery-installed device.
- Specific implementations currently represented are integrated charger LED bars and remote/tower/stack lights.
- Products link to the specific child Designs rather than directly to this general class.

## Former ids
