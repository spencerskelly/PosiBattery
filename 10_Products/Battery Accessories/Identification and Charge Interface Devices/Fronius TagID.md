---
type: Object
subtype: electrical
id: OBJ-00029
uid: 20261002162520379skellyspencer
status: Draft
tags:
  - battery-market-reference
  - charge-interface
  - commercial-product
  - forklift
  - lead-acid
  - scope-aftermarket
subtypeOf:
  - "[[Battery Identification and Charge Interface Device]]"
performs:
  - "[[Measure Battery Temperature]]"
  - "[[Sense Electrolyte Level]]"
  - "[[Report Battery Temperature to Charger]]"
  - "[[Identify Battery to Charger]]"
  - "[[Indicate Battery Status Locally]]"
  - "[[Configure Device from Mobile App or PC]]"
hasDesign:
  - "[[Local LED Indicator]]"
hasPart:
  - "[[LED Status Indicator Element]]"
  - "[[Status Indicator Driver Circuit]]"
madeBy:
  - "[[Fronius International]]"
offeredWith:
  - "[[Fronius Selectiva 4.0]]"
---

# Fronius TagID

## Definition

Fronius battery-mounted sensor that identifies a lead-acid traction battery to a Fronius charger and measures temperature, with a TagID+ model that adds electrolyte-level sensing.

## Notes

**Summary:**
Fronius battery-mounted sensor that identifies a lead-acid traction battery to a Selectiva 4.0 charger and guides charging from measured values.

**Marketed features:**
- Digital identification and parameterization for TagID guided charging
- Standard temperature sensor; TagID+ adds electrolyte-level sensing
- Automatic ionic circulation, desulfation and intelligent equalizing (up to 4 percent energy efficiency)
- Self-configuring charge curve
- NFC configuration via TagID Config App with automatic voltage check
- LED status; IP65; 20-200 VDC; under 0.5 W

**Summary and features sources:**
Maker or publisher marketing claims as stated, not independently verified.
- Fronius (T1), retrieved 2026-10-04. <https://manuals.fronius.com/html/4204102645/en-US.html>
- Fronius (T1), retrieved 2026-10-04. <https://www.fronius.com/de-at/austria/batterieladetechnik/unsere-loesungen/individuelle-batterieladeloesungen/batteriesensor-tagid>
- Fronius (T1), retrieved 2026-10-04. <https://www.fronius.com/de-ch/switzerland/batterieladetechnik/our-solutions/individuelle-batterieladeloesungen/batteriesensor-tagid>

- Manufacturer: Fronius International (Perfect Charging division)
- **Verification 2026-10-02 (verified (2022 launch)):** TagID has a temperature sensor as standard and the charger adjusts charging to battery temperature; TagID+ adds a level sensor for wet batteries, while TagID with temperature sensor is preferred for gel batteries; used with Selectiva 4.0 chargers; the sensor system lets the charger detect a deeply discharged battery and start desulphation, signal when water is needed, and run intelligent equalising charges. Source: Fronius TagID product page and launch press release (T1) <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
- **Related feature:** Fronius lists 'automatic ionic circulation' to prevent acid stratification as a function of the TagID and charger combination. Relationship to [[Electrolyte Circulation System]] is unresolved.
- **Not stated in retrieved sources:** how TagID communicates with the charger, wireless options, voltage range, whether TagID and TagID+ are separate hardware or one device with options, lithium support.
- **Functions performed, with citations** (V = verified this pass, C = carried from seed text, U = user-stated):
  - [[Measure Battery Temperature]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
  - [[Sense Electrolyte Level]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
  - [[Report Battery Temperature to Charger]] (V): <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
  - [[Identify Battery to Charger]] (V): <https://manuals.fronius.com/html/4204102645/en-US.html>
  - [[Indicate Battery Status Locally]] (V): <https://manuals.fronius.com/html/4204102645/en-US.html>
  - [[Configure Device from Mobile App or PC]] (V): <https://manuals.fronius.com/html/4204102645/en-US.html>
- **Design characteristics, with citations:**
  - [[Local LED Indicator]] (V): <https://manuals.fronius.com/html/4204102645/en-US.html>
- **Implementation assumption — LED driver:** [[LED Status Indicator Element]] is verified by the published LED status. [[Status Indicator Driver Circuit]] is allocated at **>=95% engineering confidence** because the internal LED-driver topology is not published.
- **Sources used for the mapping above:** Fronius TagID product page <https://www.fronius.com/en/battery-charging-technology/our-solutions/individual-battery-charging-solutions/battery-sensor-tagid>
- **Truck parts (round 31):** typical (inferred from the device type, not from a source): mounts on [[Truck Battery Compartment]]. See [[Truck Part Connection Register]].

## Aliases

- TagID
- TagID+
- Fronius battery sensor


## Former ids
