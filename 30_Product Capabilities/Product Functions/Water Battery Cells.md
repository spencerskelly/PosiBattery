---
type: Function
subtype:
id: FUNC-00064
uid: 20261003101711509skellyspencer
status: Draft
tags:
  - accessory-function
  - extra
  - product-function
subtypeOf:
  - "[[Maintain Battery Electrolyte]]"
performedBy:
  - "[[HAWKER Perfect Plus Battery]]"
  - "[[Crown V-Force Single Point Watering System]]"
  - "[[Exide Automatic Watering System and Level Sensor]]"
  - "[[Midac Aquamatic Watering System]]"
  - "[[Philadelphia Scientific Stealth Watering System]]"
  - "[[Philadelphia Scientific Water Injector System]]"
  - "[[PosiCharge Single-Point Automatic Battery Watering]]"
  - "[[PosiCharge SVS200]]"
  - "[[Flow-Rite Maverick Battery Watering System]]"
  - "[[Single-Point Watering Manifold Assembly]]"
  - "[[Cell Watering Shutoff Valve]]"
  - "[[Battery Watering Distribution Tubing]]"
  - "[[Water Injector Shutoff Assembly]]"
  - "[[Automatic Watering Control Logic]]"
realizes:
  - "[[Keep Trucks Working Without Battery Maintenance Labor]]"
dependsOn:
  - "[[Battery Cell Watering Design]]"
realizedBy:
  - "[[Battery Cell Watering Design]]"
  - "[[Keep Trucks Working Without Battery Maintenance Labor]]"
---

# Water Battery Cells

## Definition

Refill the cells of a flooded battery with water, by tool or automatically.

## Notes

- Accessory behavior found in product descriptions. Product links only where a source states the behavior.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Crown V-Force Single Point Watering System]] (V): <https://www.crown.com/en-ca/batteries-and-chargers/>
  - [[Midac Aquamatic Watering System]] (V): <https://www.batterie-siems.de/en-gb/2-pzs-280-2mdl140>
  - [[Exide Automatic Watering System and Level Sensor]] (V): <https://www.exidegroup.com/eu/sites/default/files/2021-08/GNB_MP_Overview_EN_web.pdf>
  - [[Philadelphia Scientific Stealth Watering System]] (V): <https://og.mhi.org/members/13790>
  - [[Philadelphia Scientific Water Injector System]] (V): <https://og.mhi.org/members/13790>
  - [[PosiCharge Single-Point Automatic Battery Watering]] (V): <https://posicharge.com/accessories/>
  - [[PosiCharge SVS200]] (V): <https://www.posicharge.com/svs200/>
  - [[HAWKER Perfect Plus Battery]] (V): <https://enersys.com/4a6cd5/globalassets/documents/product-documentation/hawker/perfect-plus/emea/hawker-perfect-plus-instruction-for-use-english.pdf>
  - [[Flow-Rite Maverick Battery Watering System]] (V): <https://www.flow-rite.com/battery-care/>
- **Extra (round 30):** documented for 3 of 21 battery maker groups (14 percent); the reusable realization family is now [[Battery Cell Watering Design]]. Rule and caveats remain in [[Extra Functions Register]].

## Implementation Allocation

The reusable realization is [[Battery Cell Watering Design]], with three product-backed architectures.

### Float-valve single-point watering

[[Float-Valve Single-Point Watering]] -> [[Single-Point Watering Manifold Assembly]], composed of [[Cell Watering Shutoff Valve]] and [[Battery Watering Distribution Tubing]].

This path is directly supported by [[Philadelphia Scientific Stealth Watering System]] and [[Flow-Rite Maverick Battery Watering System]]. Crown also publishes float-system kits within its V-Force watering range. [[HAWKER Perfect Plus Battery]] is allocated at the method level for Aquamatic refilling, while the exact valve construction remains unpublished.

### Injector level-sensing watering

[[Injector Level-Sensing Watering]] -> [[Water Injector Shutoff Assembly]].

[[Philadelphia Scientific Water Injector System]] explicitly uses a precision level-sensing shutoff valve at the injector tip and does not use floats.

### Charger-controlled automatic watering

[[Charger-Controlled Automatic Watering]] -> [[Automatic Watering Control Logic]].

[[PosiCharge Single-Point Automatic Battery Watering]] explicitly uses charger-controlled watering. [[PosiCharge SVS200]] explicitly offers automatic watering as an option. The current evidence does not identify the valve, pump, reservoir, water-level sensor, or hydraulic topology, so those details are not inferred.

### Generic automatic watering

[[Exide Automatic Watering System and Level Sensor]] and [[Midac Aquamatic Watering System]] remain at the generic [[Battery Cell Watering Design]] level because their current sources confirm automatic watering but not enough implementation detail to select one of the specific paths confidently.

## Aliases


## Former ids
