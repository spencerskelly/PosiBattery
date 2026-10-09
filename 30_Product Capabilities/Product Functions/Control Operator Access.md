---
type: Function
subtype:
id: FUNC-00051
uid: 20261003090225546skellyspencer
status: Draft
tags:
  - truck-function
  - product-function
subtypeOf:
  - "[[Manage Fleet Use]]"
dependsOn:
  - "[[Operator Identification Design]]"
  - "[[Operator Access Authorization Design]]"
performedBy:
  - "[[Crown InfoLink]]"
  - "[[Hyster Tracker Telemetry]]"
  - "[[Linde connect]]"
  - "[[Logisnext Lift Link]]"
  - "[[Powerfleet Forklift Gateway]]"
  - "[[STILL FleetManager]]"
  - "[[STILL Smart Portal]]"
  - "[[Crown RC 5700 Series]]"
  - "[[Hangcha XC Series Electric Forklifts]]"
  - "[[STILL RX 60 Electric Forklift]]"
  - "[[Raymond 8000 Series Pallet Trucks]]"
  - "[[STILL EXH-SF Low Lift Pallet Truck]]"
  - "[[Panacea Smart Start]]"
  - "[[Toyota PIN Code Access Pad]]"
  - "[[STILL Safety Assist]]"
  - "[[Crown InfoLink 7-inch Touch Display]]"
  - "[[Operator Access Authorization Logic]]"
  - "[[Vehicle Enable Interlock]]"
realizes:
  - "[[Control Who Operates Each Truck]]"
  - "[[Retrofit Safety and Telematics Onto Existing Trucks]]"
  - "[[Authenticate and Complete Pre-Shift Authorization]]"
realizedBy:
  - "[[Operator Access Authorization Design]]"
  - "[[Authenticate and Complete Pre-Shift Authorization]]"
---

# Control Operator Access

## Definition

Allow only authorized operators to start a truck, by PIN or RFID card.

## Notes

- Truck-side behavior found in product descriptions. Product links only where a source states the behavior; no link means unknown.
- No Requirement is linked (intentional gap).
- **Sources** (product, evidence level, web page):
  - [[Linde connect]] (V): <https://www.kiongroup.com/en/Newsroom/Story-Categories/Innovation/Article/7-solutions-that-make-the-warehouse-safer.html>
  - [[Powerfleet Forklift Gateway]] (V): <https://www.powerfleet.com/?p=30065>
  - [[Panacea Smart Start]] (V): <https://www.dcvelocity.com/articles/28818-spotlight-on-forklift-safety-products>
  - [[Toyota PIN Code Access Pad]] (V): <https://www.summithandling.com/wp-content/uploads/2023/03/2023_Side-Entry-End-Rider_Comprehensive_Digital.pdf>
  - [[Logisnext Lift Link]] (V): <https://www.mhlnews.com/new-products/article/21271747/forklift-telematics-solution>
  - [[Crown InfoLink]] (V): <https://crown.com/content/dam/crown/pdfs/apac/brochures/SP-1500-Broch-APAC.pdf>
  - [[Hyster Tracker Telemetry]] (V): <https://www.hyster.com/globalassets/coms/hyster/north-america/documents/trucks/0000hbxxbc001_e_en-us_hyster-solutions-brochure-view.pdf>
  - [[STILL FleetManager]] (V): <https://www.still.co.uk/company/news-press/news/detail/safe-safer-still.html>
  - [[STILL Smart Portal]] (V): <https://www.still.co.uk/forklift-trucks/new-forklifts/low-lift-pallet-trucks/exh-sf-16c-20c.html>
  - [[STILL Safety Assist]] (V): <https://www.still.co.uk/forklift-trucks/driver-assistance/safety-assist.html>
  - [[Hangcha XC Series Electric Forklifts]] (V): <https://www.summithandling.com/summit-product/hangcha-xc-series-mid-electric-outdoor-lithium-ion-forklift/>
  - [[STILL EXH-SF Low Lift Pallet Truck]] (V): <https://www.still.co.uk/forklift-trucks/new-forklifts/low-lift-pallet-trucks/exh-sf-16c-20c.html>
  - [[STILL RX 60 Electric Forklift]] (V): <https://aviationspares.com/rx-60-25-35-t-electric-forklift-truck/>
  - [[Crown RC 5700 Series]] (V): <https://www.crown.com/content/dam/crown/pdfs/en-uk/specs/forklift-rc5700-spec-GB.pdf>
  - [[Raymond 8000 Series Pallet Trucks]] (V): <https://raymondcorp.com/forklifts/pallet-trucks/8250-lithium-ion-pallet-jack>
  - [[Crown InfoLink 7-inch Touch Display]] (V): <https://www.crown.com/en-us/fleet-management/infolink.html>

## Implementation Allocation

The reusable realization is [[Operator Access Authorization Design]].

[[Operator Identification Design]] provides the credential mechanism. [[Operator Access Authorization Logic]] validates the credential against access rules, and [[Vehicle Enable Interlock]] enforces the resulting authorized/unauthorized state at the vehicle.

This separation is important because a PIN pad, RFID reader, fingerprint reader, or touch display only identifies an operator; it does not by itself decide access or inhibit the truck.

### Product examples

- [[Toyota PIN Code Access Pad]]: verified PIN-based credential entry; authorization and interlock logic are required at **>=95% engineering confidence**, while the exact controller/relay implementation is unpublished.
- [[Panacea Smart Start]]: verified fingerprint-based starter authorization; the starter-interlock enforcement role is directly supported.
- Fleet systems such as [[Crown InfoLink]] can apply centrally managed operator permissions while the truck-side system still performs the final enable/inhibit action.

No specific credential database, relay topology, CAN command, or access-policy synchronization method is asserted unless product evidence supports it.

## Aliases


## Former ids
