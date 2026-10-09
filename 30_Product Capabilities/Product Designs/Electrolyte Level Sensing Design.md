---
type: Design
subtype:
id: DES-90011
uid: 20261006081500001skellyspencer
status: Draft
tags:
  - general-design
  - design-characteristic
  - battery-monitoring
  - electrolyte
supertypeOf:
  - "[[Capacitive Electrolyte Level Probe]]"
  - "[[Electronic In-Cell Electrolyte Probe]]"
  - "[[Variable-Length Electrolyte Level Probe]]"
  - "[[Cell-Connector Electrolyte Level Sensing]]"
  - "[[Low-Current Electrolyte Level Input]]"
realizes:
  - "[[Sense Electrolyte Level]]"
dependencyOf:
  - "[[Sense Electrolyte Level]]"
  - "[[Alert on Low Electrolyte Level]]"
designOf:
  - "[[Electrolyte Level Measurement Circuit]]"
describedBy:
  - "[[Battery Sensor Element Design]]"
  - "[[Metric - Electrolyte Level Sensing]]"
---

# Electrolyte Level Sensing Design

## Definition

General design family for detecting whether electrolyte in a flooded lead-acid battery is above or below a useful level threshold.

## Notes

- This is the reusable implementation family for [[Sense Electrolyte Level]].
- Products link to the applicable specific child Design; the general class itself is not product-owned.
- The current evidence supports several distinct implementations: capacitive probes, electronic in-cell probes whose internal sensing principle is undisclosed, adjustable-length probes, and the Exide cell-connector multi-function sensor.
- A product that merely states "electrolyte sensor" or "level sensor" remains at the Function level until its physical implementation is established.
- The Design family separates sensing behavior from indication; LEDs, buzzers, displays, and watering actions are modeled separately.

## Former ids
