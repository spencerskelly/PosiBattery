---
type: Object
subtype: electrical
id: OBJ-00029
uid: 20261002162520379skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - charge-interface
  - lead-acid
subtypeOf:
  - "[[Battery Identification and Charge Interface Device]]"
---

# Fronius TagID

## Definition

Fronius battery-mounted sensor that identifies a lead-acid traction battery to a Fronius charger and measures temperature, with a TagID+ model that adds electrolyte-level sensing.

## Notes

- Manufacturer: Fronius International (Perfect Charging division)
- **Verification 2026-10-02 (verified (2022 launch)):** TagID has a temperature sensor as standard and the charger adjusts charging to battery temperature; TagID+ adds a level sensor for wet batteries, while TagID with temperature sensor is preferred for gel batteries; used with Selectiva 4.0 chargers; the sensor system lets the charger detect a deeply discharged battery and start desulphation, signal when water is needed, and run intelligent equalising charges. Source: Fronius TagID product page and launch press release (T1) <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
- **Related feature:** Fronius lists 'automatic ionic circulation' to prevent acid stratification as a function of the TagID and charger combination. Relationship to [[Electrolyte Circulation System]] is unresolved.
- **Not stated in retrieved sources:** how TagID communicates with the charger, wireless options, voltage range, whether TagID and TagID+ are separate hardware or one device with options, lithium support.

## Aliases

- TagID
- TagID+
- Fronius battery sensor

## Former ids
