---
type: Object
subtype: electrical
id: OBJ-00010
uid: 20261002150858946skellyspencer
status: Draft
tags:
  - battery-market-reference
  - commercial-product
  - forklift
  - charge-interface
subtypeOf:
  - "[[Battery Identification and Charge Interface Device]]"
supertypeOf:
  - "[[AMETEK Prestolite Power BID with Ah Accumulator]]"
---

# AMETEK Prestolite Power BID

## Definition

AMETEK Prestolite Power Battery Identification Device that provides a compatible forklift charger with battery identity, configuration, and temperature information.

## Notes

- Manufacturer: AMETEK Prestolite Power
- Market evidence checked: 2026-10-02
- Installation locus: battery device used with motive-power batteries.
- Published charger data includes battery ID, battery type, amp-hour capacity, number of cells, charge start rate, and continuous temperature updates.
- The charger uses this information for a battery-specific temperature-compensated charge profile.
- Evidence: https://www.prestolitepower.com/products/datadevices/bid
- **Verification 2026-10-02 (re-verified):** the BID provides the charger with battery ID, battery type, Ah capacity, cell count and start rate, and updates battery temperature throughout the charge so any BID-capable controlled charger can run a temperature-compensated profile. Source: AMETEK Prestolite Power BID page (T1) <https://www.prestolitepower.com/products/datadevices/bid>
- **Variant:** a BID with Amp Hour Accumulator exists; see [[AMETEK Prestolite Power BID with Ah Accumulator]].
- **Not stated in retrieved sources:** how temperature is sensed, chemistry coverage, and the physical interface to the charger.

## Aliases

- Prestolite BID
- Battery Identification Device (BID)

## Former ids
