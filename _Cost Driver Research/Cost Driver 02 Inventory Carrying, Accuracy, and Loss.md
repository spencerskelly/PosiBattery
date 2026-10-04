# Cost Driver 02: Inventory Carrying, Accuracy, and Loss

**Scope:** Warehouses, distribution centers, and production facilities using material-handling equipment (MHE)  
**Research date:** October 2026

## Executive findings

Inventory cost includes capital tied up in stock, storage and handling, insurance and taxes, deterioration or obsolescence, shrinkage, count and reconciliation labor, shortages, emergency replenishment, and production disruption. Products reduce these costs through four layers:

1. Maintain a trustworthy transaction record.
2. Capture physical reality automatically.
3. Optimize how much inventory should exist and where.
4. Convert discrepancies into corrective workflows.

The main commercial categories used today are warehouse-management systems, barcode/mobile capture, RAIN RFID, autonomous inventory drones and tower robots, real-time location and ambient IoT, demand/inventory optimization, and condition/expiration monitoring. These categories are complementary rather than interchangeable.

Published productivity and savings figures are site-specific and often vendor-sponsored. They demonstrate achievable outcomes but should not be used as guaranteed forecasts without a controlled pilot.

## Cost mechanisms

| Inventory problem | Operational need | Product response | Costs reduced |
|---|---|---|---|
| Physical and system inventory disagree | Validate identity, quantity, status, and location | WMS transactions, barcode, RFID, computer vision | Counts, searches, rework, stockouts |
| Excess safety stock | Set stock according to uncertainty and service goals | Demand planning and multi-echelon optimization | Working capital, storage, insurance, handling |
| Phantom inventory | Detect discrepancies before allocation | Continuous sensing, cycle counting, exception workflows | Missed shipments, line-down, expedites |
| Shrinkage and lost assets | Detect movement and last-known location | RFID portals, RTLS, ambient IoT, digital chain of custody | Replacement, write-offs, claims, search labor |
| Obsolescence and expiration | Control age, lot, revision, and condition | WMS lot/date controls, FEFO, sensor alerts | Write-offs, markdowns, waste, recall scope |
| Slow manual counting | Automate physical observation | RFID, drones, autonomous tower robots | Count labor, lift time, operational shutdowns |
| Misshipments | Verify contents and transition events | Scan/RFID pack and dock audit | Returns, reshipment, claims, customer penalties |
| Returnable-asset loss | Track dwell, location, status, and turns | RTLS, RFID, BLE/cellular sensing | Container purchases, rentals, detention |
| Material shortages | Validate availability and trigger replenishment | WMS, IoT, planning, exception alerts | Production downtime, overtime, premium freight |

## Product landscape

| Product class | Commercial examples | Main need solved | Productivity gained | Primary costs reduced |
|---|---|---|---|---|
| WMS and perpetual inventory | Blue Yonder WMS; Manhattan Active WM; Oracle WMS Cloud | Inventory system of record and process control | Directed transactions, cycle counts, exception reconciliation | Count labor, errors, stockouts, obsolescence |
| Barcode/mobile capture | Zebra and Honeywell mobile computers, scanners, and printers | Low-cost item/location confirmation | Faster receiving, movement, picking, and counts | Rework, search, mispicks, count labor |
| RAIN RFID | Impinj platform; Zebra RFID readers/printers; partner software | High-volume, no-line-of-sight identification | Bulk reads and automated transition events | Count, receiving, shipping audit, shrinkage |
| Inventory drones | Gather AI | High-rack and large-area inventory observation | Autonomous counts and visual exception detection | Cycle-count labor, lift use, missed inventory |
| Autonomous tower robots | DexoryView | Daily wall-to-wall pallet/location validation | High-rate scanning and digital-twin exceptions | Audit labor, investigations, SLA failures |
| RTLS and ambient IoT | Roambee/Decklar; Wiliot | Continuous location, status, and condition | Less searching/scanning and better dwell visibility | Lost assets, delay, waste, excess buffers |
| Inventory optimization | ToolsGroup; Blue Yonder Planning; Kinaxis | Excess and mispositioned safety stock | Automated replenishment and exception planning | Working capital, stockouts, expedites, obsolescence |
| Condition/expiration monitoring | Wiliot; Roambee; RFID smart cabinets | Temperature, age, dwell, and quality exposure | Automated alerts and FEFO execution | Spoilage, write-offs, recalls, quality holds |

## Evidence highlights

- XPO Logistics reports 99.9% stock accuracy for some customers using Blue Yonder warehouse management.[cite:271]
- Terza reports RFID-driven inventory accuracy above 98% and annual count time reduced from three days to six hours.[cite:242]
- China Outfitters reports a 25-fold improvement in inventory, shipping, and returns efficiency with an Impinj-enabled RFID solution.[cite:241][cite:243]
- Langham Logistics reports inventory accuracy increasing from 97% to above 99% and daily pallet exceptions falling from 20–30 to one or two using Gather AI.[cite:270]
- Dexory reports customers reaching 99.9% location accuracy; GXO reports scanning 10,000 pallets per hour and freeing 16 staff-hours per day in cited deployments.[cite:265][cite:268]
- ToolsGroup reports Grupo Gallo reaching 99% service while reducing inventory by roughly ten days of coverage.[cite:285]
- Prinsel reports 2% less inventory, 30% higher warehouse efficiency, and 62% shorter fulfillment time after Blue Yonder WMS deployment.[cite:293]

## Needs solved

### Inventory accuracy

The core need is agreement between the physical item—its identity, quantity, condition, status, and location—and the digital record. WMS products enforce transactions; barcode systems validate identity and location; RFID and vision automate observations; reconciliation software converts mismatches into count or investigation tasks.

### Carrying cost

Planning and optimization products determine where inventory should be held and how much buffer is justified by demand, lead-time uncertainty, service targets, constraints, and network structure. ToolsGroup describes multi-echelon optimization that balances service, investment, and risk across suppliers, plants, warehouses, stores, and service locations.[cite:297]

### Shrinkage and loss

Automated transition reads, location sensing, shipment verification, and continuous observation narrow the time and place in which an item can disappear. Christie Lites uses fixed and handheld RFID readers to automate returns, approach 100% tag reads, locate equipment, and reduce the risk of assets appearing missing because someone failed to scan them.[cite:244]

### Obsolescence and waste

Lot, serial, revision, date, dwell, temperature, and condition data support first-expired-first-out allocation, quality holds, recalls, and aging alerts. Blue Yonder WMS supports lot/date controls, replenishment rules, and recall processes.[cite:274] Wiliot and Roambee products add continuous item or container location and condition observations.[cite:298][cite:302][cite:303]

### Stockouts and line-down

Reliable inventory prevents planning and allocation from relying on phantom stock. Gather AI compares visual observations with WMS or ERP records so discrepancies can be corrected before causing production interruption or missed shipments.[cite:262]

## WMS and perpetual inventory

### Products and functions

Blue Yonder, Manhattan, and Oracle provide receiving, directed putaway, location control, allocation, replenishment, picking, lot/serial control, and cycle counting. Blue Yonder states that system-directed cycle counting can produce accuracy above 99%; XPO reports 99.9% stock accuracy for some customers.[cite:271][cite:274]

Oracle describes real-time transaction updates and system-directed work as mechanisms that maintain current inventory data and direct workers to the correct material and locator.[cite:272] An Oracle WMS Cloud implementation for an EV-battery operation reported approximately 99% inventory accuracy using closed-loop acknowledgements from MHE, middleware, and PLC automation.[cite:277]

### Needs solved

- Inventory held in spreadsheets or disconnected systems.
- Uncontrolled receiving, movement, or picking.
- Weak lot, serial, revision, expiration, and status control.
- Annual physical inventory shutdowns.
- Allocation against unavailable or incorrect stock.

### Productivity gained

- System-directed receiving, putaway, replenishment, and counting.
- Immediate inventory updates at transaction completion.
- Exception-based cycle counting instead of broad recounting.
- Faster recall, status, and revision searches.
- Reduced investigation and supervisory coordination.

### Costs reduced

- Count and reconciliation labor.
- Mispicks, missed shipments, and returns.
- Emergency replenishment and premium freight.
- Excess safety stock maintained because inventory is untrusted.
- Obsolescence and recall effort.

### Limits

The WMS record is only as reliable as execution. Unrecorded moves, label errors, bad master data, integration latency, uncontrolled manual work, and mismatched ownership between WMS and automation can create silent discrepancies. Manhattan recommends explicit inventory authority and synchronization rules in hybrid automated facilities.[cite:281]

## Barcode and mobile capture

### Products and functions

Barcode systems use printed labels, fixed or mobile scanners, vehicle-mounted terminals, printers, and WMS/ERP applications to confirm item, location, quantity, lot, serial, and task. They remain the economical baseline for controlled inventory transactions.

### Needs solved

- Handwritten receiving and movement records.
- Wrong-location putaway.
- Incorrect item or quantity selection.
- Slow manual counts and later data entry.
- Lack of lot/serial traceability.

### Productivity gained

- Faster data capture than paper entry.
- Immediate system updates.
- Directed work and validation at each touch.
- Faster investigation using transaction history.

### Costs reduced

- Transaction and reconciliation labor.
- Wrong-location inventory and search.
- Mispicks, returns, and reshipment.
- Inventory buffers caused by low confidence.

### Limits

Barcode usually requires line of sight and one-at-a-time reads. Benefits disappear when scans are bypassed, labels are damaged or inaccessible, or workflows create unnecessary scan burden. Barcode is transaction-based rather than continuous; uncontrolled movement remains invisible.

## RAIN RFID

### Products and functions

Impinj, Zebra, and integration partners provide passive RFID endpoints, labels, handhelds, fixed readers, portals, printers, antennas, and software. RAIN RFID can identify multiple tagged items without optical line of sight, enabling bulk counts and automatic dock, conveyor, doorway, or process-transition events.[cite:241][cite:243][cite:254]

### Business use

Terza integrated RFID with SAP to track carpet rolls from production through warehouse operations. Zebra reports accuracy above 98%, count time falling from three days to six hours, and receiving/loading completed in seconds.[cite:242]

Plexus reported 97% less search time, 95% less manual scanning on a production line, 92% less repalletizing time, 30% less warehouse space, and 100% shipment accuracy after deploying an Impinj-enabled system.[cite:248] Impinj also reports a fivefold increase in intake capacity at Heilan Home and three-to-fivefold process efficiency at La Chapelle.[cite:248]

### Costs reduced

- Counting, receiving, and shipping-audit labor.
- Search and repalletizing.
- Misshipments, claims, and reshipment.
- Shrinkage and lost assets.
- Inventory buffer and occupied space.

### Limits

Read performance depends on metal, liquids, tag orientation, density, reader placement, interference, and process geometry. Read zones must identify the intended business event rather than merely detect a nearby tag. Tag economics and source-tagging effort determine which item classes justify item-level deployment.

## Inventory drones

### Products and functions

Gather AI uses autonomous drones and computer vision to capture labels, text, locations, case counts, damage, and other attributes in high-bay warehouses, then compares observations with WMS or ERP data.[cite:256][cite:262][cite:263]

### Business use

Gather AI reports scan rates up to 900 bins per hour using three drones and one operator, 15-fold faster counting, and one customer reducing full-facility count time from 90 days to 2.5 days.[cite:256][cite:258]

Langham Logistics reports moving from four inventory employees plus a supervisor to the supervisor plus one employee, raising accuracy from 97% to above 99%, and reducing pallet fire drills from 20–30 per day to one or two.[cite:270]

### Costs reduced

- Manual count and recount labor.
- Forklift or lift use to inspect high locations.
- Aisle disruption and count-related downtime.
- Lost inventory, emergency searches, and mis-shipments.
- Production interruption caused by missing material.

### Limits

Drones observe labels and visible conditions but do not prove the contents of opaque pallets or cartons. Label placement, rack geometry, lighting, netting, flight restrictions, battery operation, local safety rules, and exception-resolution labor determine value.

## Autonomous tower robots

### Products and functions

DexoryView combines an autonomous tall robot, sensors, AI, and a warehouse digital twin to scan pallet racking and identify inventory/location discrepancies.[cite:259][cite:265]

### Business use

Dexory reports up to 99.9% location accuracy, 16 staff-hours freed per day at a customer, and 47 hours per week saved on empty-location checks.[cite:259][cite:260] GXO reports automated counts and audits at multiple sites; one deployment scans 10,000 pallets per hour and completes a million-square-foot warehouse in under one shift.[cite:268]

### Costs reduced

- Physical counts and audits.
- Empty-location checks and discrepancy investigations.
- Lost inventory and missed customer SLAs.
- Operational shutdowns for full counts.

### Limits

The robot validates what its sensors can observe from aisles. Block stacks, deep lanes, occlusion, labels facing away, floor congestion, and inaccessible zones require other capture methods or process changes. Vendor metrics should be verified at the target rack height, aisle width, label format, and pallet density.

## RTLS and ambient IoT

### Products and functions

Roambee/Decklar uses BLE, cellular, gateways, cloud software, and analytics for location, dwell, condition, and shipment visibility. Wiliot uses battery-free Bluetooth IoT Pixels and a cloud platform for item, case, container, location, and condition observations.[cite:302][cite:303]

### Business use

A chemical company used Roambee to track 23,000 returnable tanks across 210 customer facilities, automate status and quality-check visibility, reduce dispatch delay, and improve truck utilization by locating empty assets near pickup opportunities.[cite:302]

An aftermarket battery distributor uses item-level sensing across more than 250,000 dealers to infer shelf status, sales velocity, expiration, and replenishment demand.[cite:308]

Wiliot reports an online retailer gaining visibility into more than 80% of missing packages, reducing missing packages by 60%, and saving more than $58 million in package value.[cite:310] Wiliot also describes warehouse deployments that detect misplaced, misloaded, or left-behind packages.[cite:298]

### Costs reduced

- Asset search, rental, and replacement.
- Returnable-container detention and idle dwell.
- Lost packages and inventory.
- Manual scan labor.
- Missed replenishment, spoilage, and excess buffers.

### Limits

Resolution, infrastructure density, tag life or harvested power, metal environments, roaming, data volume, subscription cost, and event interpretation vary by technology. Continuous sensing creates value only when alerts are accurate, actionable, and integrated with operating workflows.

## Inventory optimization

### Products and functions

ToolsGroup, Blue Yonder Planning, and Kinaxis use forecasts, service targets, demand and lead-time variability, constraints, and multi-echelon logic to set inventory targets and replenishment policies.[cite:292][cite:294][cite:297]

### Business use

- Grupo Gallo reached 99% service while reducing inventory by about ten days of coverage and reducing demand-planning/replenishment work to slightly more than one FTE.[cite:285]
- Amara reported a 12% MRO inventory reduction in six months as part of a 38% working-capital improvement.[cite:289]
- ToolsGroup customer materials cite examples including 18% less safety stock, 7% less inventory with 83% fewer expedites, and 12% less inventory with higher sales; results are customer-specific.[cite:287]
- Prinsel reports 2% inventory reduction alongside higher warehouse efficiency and shorter fulfillment time after implementing Blue Yonder WMS capabilities.[cite:293]

### Costs reduced

- Working capital.
- Warehouse space, insurance, taxes, and handling.
- Obsolescence, markdowns, and waste.
- Stockouts, transfers, and premium freight.
- Planner workload and manual spreadsheet management.

### Limits

Optimization cannot compensate for unreliable demand history, inventory records, lead times, BOMs, supplier constraints, or service policies. Forecast improvement is not itself a financial result; recommended changes must be executed and sustained without shifting shortages elsewhere.

## Condition and expiration monitoring

### Products and functions

Condition-monitoring products combine lot/serial records with temperature, humidity, shock, dwell, location, and expiration data. Wiliot describes case-level location and temperature monitoring for produce and alerts that allow a retailer to correct cold-chain and process problems before inventory is wasted.[cite:298]

Roambee’s chemical-tank case combines status, location, fill history, and quality-check dates to prevent unqualified assets from being dispatched.[cite:302]

### Costs reduced

- Spoilage, expiration, and scrapping.
- Quality holds and broad recall scope.
- Claims and replacement freight.
- Safety stock used to compensate for uncertain condition.

### Limits

Sensor accuracy, calibration, mounting, sampling interval, data continuity, excursion logic, and evidentiary requirements must match product risk. Monitoring does not replace validated packaging or quality processes.

## Impact matrix

| Need | Product function | Productivity result | Financial result | KPI |
|---|---|---|---|---|
| Trust system stock | Validate every controlled movement | Less search and reconciliation | Lower labor and buffer stock | Inventory accuracy by unit/location |
| Count faster | Bulk RFID or autonomous vision | More locations per hour | Lower count cost and disruption | Locations/hour; cost/count |
| Detect mismatch sooner | Compare physical observations with WMS | Exception-based investigation | Lower loss and recovery expense | Detection latency; open exceptions |
| Prevent misshipments | Pack/dock verification | Less audit and rework | Fewer returns, claims, and reshipments | Shipping accuracy |
| Reduce excess stock | Service-driven optimization | Planner management by exception | Working-capital and storage release | Days on hand; excess value |
| Avoid stockouts | Accurate availability and replenishment | Fewer fire drills | Higher service, lower premium freight | Fill rate; stockout rate |
| Reduce obsolescence | Aging, lot/date, revision, and FEFO control | Better allocation | Lower write-offs and markdowns | Obsolete/expired value |
| Control returnables | Track location, dwell, and status | Faster turns and retrieval | Fewer purchases, rentals, and losses | Asset cycle time; loss rate |
| Protect condition | Sensor alerts and quality workflow | Earlier intervention | Less spoilage and claim cost | Excursion rate; waste value |
| Prevent line-down | Validate material availability | Fewer shortage investigations | Less downtime and schedule recovery | Inventory-caused downtime |

## MHE product adjacency

A connected battery/charger platform can create inventory value even though it is not the inventory master. Forklifts, tuggers, batteries, and chargers are mobile observation points located where pallets and materials move.

### Near-term functions

1. **Movement-event gateway:** Associate truck motion, lift events, operator, battery, time, and zone with WMS tasks.
2. **RFID integration:** Host or power vehicle-mounted readers and forward filtered observations.
3. **BLE/UWB scanning:** Detect pallets, containers, tools, batteries, and returnable assets near the vehicle.
4. **Location context:** Combine truck and inventory observations to establish last-seen location.
5. **Task-versus-motion reconciliation:** Flag physical moves lacking a corresponding WMS transaction.
6. **Misplacement alert:** Warn when observed asset, destination, or task does not match.
7. **Cycle-count route mode:** Use instrumented trucks to collect counts during normal travel.
8. **Condition gateway:** Collect temperature, shock, door, and environmental data from nearby assets.
9. **Exception workflow:** Create tasks with asset, location, vehicle, operator, and timestamp evidence.
10. **Shared edge platform:** Support battery, charger, truck, RFID/BLE, and environmental data through one gateway.

### Extended features

- Fork-height and load-presence sensing to infer pickup and drop events.
- Camera/OCR for pallet IDs, labels, and location markers.
- Offline event storage with ordered synchronization.
- Geofenced filtering to reduce cross-aisle RFID ambiguity.
- Cryptographic device/asset identity and signed events.
- WMS connectors for receipt, move, putaway, pick, count, and ship confirmation.
- Rules distinguishing raw observations, inferred events, and confirmed transactions.
- Digital chain of custody for high-value or regulated materials.
- Battery-powered sensor support for returnables and yard assets.
- Analytics linking inventory errors to route, shift, zone, equipment, and process step.

### Strategic boundary

The MHE platform should not become another inventory master. WMS or ERP should retain authoritative quantity, ownership, lot, and financial records. The differentiated role is to provide high-quality physical observations and equipment context, detect mismatches quickly, and trigger corrective workflows.

## Architecture principles

1. **Separate observation from transaction.** A tag read or image is evidence; business rules determine whether it confirms a move.
2. **Preserve provenance.** Store the sensor, reader, location, confidence, timestamp, and associated task.
3. **Design for ambiguity.** RFID and proximity systems need confidence thresholds, duplicate suppression, and zone logic.
4. **Filter at the edge.** Enterprise systems should receive meaningful events rather than every raw read.
5. **Keep WMS authoritative.** Synchronize observations and exceptions without creating parallel inventory.
6. **Support degraded mode.** Buffer events during network loss and reconcile them in order.
7. **Protect security and privacy.** Encrypt data, limit worker tracking, and apply role-based access.
8. **Make exceptions actionable.** Include owner, urgency, evidence, next action, and closure state.

## ROI measurement

### Baseline data

Capture at least one complete inventory-control cycle and representative peak conditions:

- Inventory value by class, location, and status.
- Inventory accuracy by SKU, unit, and location.
- Count labor, equipment hours, shutdowns, and recounts.
- Search and investigation time.
- Misplacements, misshipments, shortages, returns, and claims.
- Stockouts, expedites, production shortages, and downtime.
- Excess, slow-moving, obsolete, expired, damaged, and quarantined value.
- Returnable-asset turns, losses, rentals, and dwell.
- Days on hand, turns, fill rate, and forecast error.

### Value calculations

- **Carrying-cost reduction:** Average inventory removed multiplied by the organization’s approved annual carrying-cost rate.
- **Working-capital release:** Permanent reduction in average inventory value; report separately from annual P&L savings.
- **Count-labor saving:** Baseline count and recount hours minus post-deployment hours, multiplied by fully burdened labor cost.
- **Error-cost saving:** Avoided errors multiplied by validated investigation, handling, freight, material, and claim cost per event.
- **Obsolescence saving:** Reduction in write-offs adjusted for demand and product-lifecycle changes.
- **Downtime avoidance:** Prevented inventory-caused downtime multiplied by validated contribution or recovery cost.
- **Asset avoidance:** Returnable containers, forklifts, lifts, or storage capacity no longer required.

### Pilot controls

- Select representative SKUs, materials, rack types, tag environments, and volumes.
- Measure read/recognition accuracy separately from inventory accuracy.
- Track false positives, false negatives, ambiguous events, and closure effort.
- Reconcile automated observations against blind physical audits.
- Normalize for receipts, shipments, production, seasonality, and policy changes.
- Prove financial realization rather than reporting only more frequent counts.

## Selection framework

Score alternatives against:

1. Required granularity: item, case, pallet, container, zone, or site.
2. Required latency: transaction, hourly, daily, or periodic.
3. RF/material environment: metal, liquid, dense loads, freezer, or outdoor.
4. Label visibility and physical access.
5. Item value and tag economics.
6. Process stability and master-data quality.
7. WMS/ERP integration and event ownership.
8. Infrastructure and installation disruption.
9. Counting/search labor and MHE opportunity cost.
10. Accuracy, safety, traceability, and compliance requirements.
11. Five-year total cost of ownership.
12. Vendor interoperability and exit strategy.

## Risks and conflicts

- More observations do not automatically create accurate inventory; event interpretation and exception closure are essential.
- Vendor metrics use different baselines and are not directly comparable.
- RFID can generate false associations if read zones are poorly engineered.
- Computer vision cannot verify invisible contents without another control mechanism.
- Optimization can reduce stock while increasing service risk if demand, lead-time, or policy data are wrong.
- Continuous tracking creates cybersecurity, workforce-privacy, and customer-data concerns.
- Parallel inventory records can conflict unless system authority is explicit.
- Tagging and sensor cost may exceed the value of low-cost items.
- Automation can remove count labor while adding engineering and exception-management work.
- Working-capital release is not recurring cost savings.

## Recommended product strategy

The strongest adjacency is an **MHE-based physical-observation and exception platform**, not a standalone WMS or inventory-planning product.

### Build

- Vehicle, battery, and charger identity with location context.
- Open edge interfaces for RFID, BLE, UWB, cameras, load, and fork sensors.
- Observation-to-event inference with confidence scoring.
- Offline buffering, ordered synchronization, and evidence retention.
- Inventory-exception workflows and WMS/CMMS connectors.
- Analytics linking discrepancies to movement, equipment, location, process, and time.

### Partner

- WMS vendors for authoritative inventory and task context.
- RFID vendors for tags, readers, antennas, and RF engineering.
- RTLS providers for precise location.
- Drone and robot inventory providers for wall-to-wall observation.
- Planning vendors for inventory target optimization.
- System integrators for labeling, workflow, ERP, and automation integration.

## Future work

- Build a vendor matrix for WMS, RFID, drones, tower robots, RTLS/IoT, and inventory optimization.
- Gather pricing, recurring fees, implementation time, tag economics, and infrastructure requirements.
- Compare barcode, RFID, vision, BLE, and UWB by object type and environment.
- Define standard observation, inferred-event, confirmed-event, and exception schemas.
- Evaluate forklift-mounted RFID and camera products and OEM integration constraints.
- Create a read-zone and event-confidence test plan.
- Develop ROI calculators for cycle counting, shrinkage, returnables, and working-capital reduction.
- Seek independent evidence beyond vendor-sponsored cases.
- Model cybersecurity, privacy, and data-retention requirements.
- Continue with Cost Driver 03: Facility and Space using the same needs → products → evidence → cost-impact framework.
