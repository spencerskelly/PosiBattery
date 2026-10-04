# Top Cost Drivers in an MHE-Enabled Warehouse

## Executive answer

For a warehouse or distribution center using material-handling equipment (MHE), **labor and lost productivity are normally the largest controllable costs**. The next major economic buckets are inventory carrying and loss, facility space, transportation/packaging, MHE lifecycle cost, safety and damage, energy, and software/administration. Exact ranking depends on whether the accounting boundary includes inventory capital and outbound freight.

The most important management insight is that **the purchase price and electricity consumption of forklifts are rarely the dominant costs**. Travel, waiting, congestion, charging labor, equipment downtime, poor slotting, unused space, damage, and insufficient fleet utilization often cost more.

## Cost hierarchy

| Rank | Cost category | Included costs | Why it becomes large | Best normalized measures |
|---:|---|---|---|---|
| 1 | Labor and productivity | Operators, pickers, loaders, supervisors, benefits, overtime, temporary labor, training and turnover | Labor is commonly reported as the largest warehouse operating expense; picking and travel dominate many manual operations.[^1][^2][^3] | Labor cost/order, cost/pallet move, lines/labor-hour, paid-to-productive time |
| 2 | Inventory carrying and loss | Cost of capital, storage, insurance, obsolescence, expiration, shrink and write-offs | Carrying cost grows with inventory value and dwell time; published general benchmarks commonly place annual carrying cost at 15–30% of inventory value.[^4] | Carrying cost/SKU, inventory turns, days on hand, shrink %, obsolete inventory % |
| 3 | Facility and space | Lease or depreciation, property tax, insurance, racking, docks, yard, battery room and maintenance | Every aisle, staging lane and charging area consumes paid space; low cube utilization can create apparent demand for expansion. Charging infrastructure also has an explicit space cost.[^5][^6] | Occupancy cost/order, storage density, cube utilization, dock utilization |
| 4 | Transportation and packaging | Inbound/outbound freight, parcel or LTL charges, pallets, cartons, dunnage and detention | If freight is inside the facility’s cost boundary, it can exceed all internal MHE costs; poor loading, staging and order accuracy also increase freight and rework. | Freight/order, freight/unit, trailer cube utilization, detention hours, packaging/order |
| 5 | MHE lifecycle cost | Purchase or lease, batteries/power systems, chargers, maintenance, tires, attachments, telematics and replacement | A proper forklift TCO includes the truck, energy system, infrastructure, charging/fueling labor, occupied space, truck maintenance and battery or fuel-system maintenance.[^5][^6] | TCO/truck-hour, maintenance cost/hour, availability, utilization, cost/move |
| 6 | Downtime, congestion and capacity loss | Queuing, blocked aisles, unavailable trucks, battery changes, fault recovery, missed throughput and overtime | Battery changing alone historically consumed about 15–20 minutes per shift in many facilities, showing why labor and availability can outweigh electricity cost.[^7][^8] | Availability %, idle %, wait minutes/order, lost moves, peak throughput |
| 7 | Safety, product and infrastructure damage | Injuries, workers’ compensation, insurance, rack/door/product damage, investigations, training and compliance | Warehousing and storage recorded 4.8 injury and illness cases per 100 full-time workers in 2024, versus 2.3 across private industry, making safety economically material as well as mandatory.[^9][^10] | Incidents/200,000 hours, impacts/1,000 hours, damage/move, near-miss closure time |
| 8 | Utilities and energy | HVAC, lighting, refrigeration, charging demand, demand peaks, compressed air and water | For U.S. warehouse/storage buildings, space heating represented 39% of site energy use and lighting 15% in the latest cited EIA building survey.[^11] | kWh/order, kWh/truck-hour, peak kW, charger efficiency, energy cost/move |
| 9 | Systems and administration | WMS/WES/LMS, telematics, network, licenses, integration, IT support, planning and reporting | These costs are usually smaller than labor but can enable or constrain labor, inventory accuracy, uptime and throughput. | System cost/order, uptime, scan compliance, exception rate, manual touches |

## MHE-specific cost stack

MHE should be evaluated as a **system**, not as isolated truck and charger purchases. The lifecycle model should include:

- Vehicle capital or lease and financing.
- Battery, fuel-cell or engine capital and planned replacements.
- Charger/fueling equipment, electrical distribution and installation.
- Charging/fueling labor and operator travel.
- Dedicated floor space and ventilation or safety infrastructure.
- Preventive and corrective maintenance, tires and attachments.
- Electricity, fuel and utility demand charges.
- Availability loss, spare fleet and rental equipment.
- Damage to products, racks, doors, docks and vehicles.
- Training, inspections, compliance, telematics and software.
- Residual value and end-of-life disposal.

A U.S. Department of Energy forklift TCO study illustrates the cost structure: in its battery-powered Class I/II example, charging labor, battery maintenance, lift-truck maintenance and charging-space cost all exceeded electricity cost. The dollar values are dated and should not be used as a current quote, but the **relative lesson remains useful: energy is only one part of power-system economics**.[^5][^6]

## Where labor hides

Picking has repeatedly been estimated at approximately 55% of warehouse operating cost in the academic literature, with travel consuming a major portion of picking effort. Consequently, labor improvement should focus less on hourly wage alone and more on removing non-value-added minutes:[^2][^12][^3]

- Empty or partially loaded travel.
- Searching for inventory, pallets or available trucks.
- Congestion and queueing at aisles, docks and chargers.
- Battery change, charging and watering labor.
- Replenishment delays and stockouts at pick faces.
- Double handling, rework and exception processing.
- Shift handoffs, inspection paperwork and system latency.

The core financial measure should therefore be **cost per completed unit of work**, not merely fleet size, utilization percentage or hourly wage. Suitable units include pallet moves, cases, lines, orders or production kits.

## Safety and compliance

OSHA requires operator training and evaluation, truck examinations at least daily—and after each shift for continuous operations—and removal from service when a truck is unsafe. These activities create visible labor and maintenance cost, but inadequate execution creates larger exposure through incidents, product damage, downtime and liability.[^13]

Safety telemetry should distinguish normal operating shocks from damaging impacts and connect each event to truck, operator, location, load and shift. Useful leading indicators include speeding, impacts, near misses, seat-belt compliance, repeated defects, blocked intersections and overdue corrective actions.

## Energy perspective

Building energy and MHE energy should be measured separately. EIA data show that warehouse/storage buildings are generally less energy-intensive than many other commercial building types, while heating and lighting are major building loads. In high-throughput electric fleets, however, charger demand can still influence transformer sizing, peak-demand charges, charging schedules and operational readiness.[^11][^14]

For battery-powered MHE, the most valuable energy metrics are not only kWh consumed, but also:

- kWh per productive truck-hour and per material move.
- Peak coincident charger demand.
- Charging labor minutes per truck-shift.
- Battery temperature, imbalance, charge efficiency and avoidable equalization.
- Truck availability at shift start.
- Battery replacements and premature capacity loss.

## Priority actions

| Priority | Action | Financial question answered |
|---:|---|---|
| 1 | Establish cost per order, line, pallet or move | Is total facility productivity improving? |
| 2 | Build a paid-time loss tree | How much labor is spent traveling, waiting, charging, searching and reworking? |
| 3 | Measure each truck’s productive hours and availability | Is the fleet oversized, undersized or poorly deployed? |
| 4 | Connect impacts and damage to truck, operator and location | Where are safety and damage costs originating? |
| 5 | Track charger demand and battery-readiness by shift | Are charging practices causing peaks, labor loss or unavailable equipment? |
| 6 | Quantify space by operational purpose | What does storage, staging, charging and congestion cost per square foot? |
| 7 | Link maintenance alerts to work orders and closure | Do detected faults actually reduce downtime and failures? |
| 8 | Review inventory dwell, shrink and obsolete stock | Is working capital larger than the direct warehouse operating budget? |

For a site that already monitors lead-acid and BMS-controlled batteries and sends cloud alerts, the next value layer is closing the loop from detection to action: automatic work orders, truck-level utilization correlation, charger coordination and reporting by truck, shift and location. This turns battery information into labor, fleet, maintenance and energy savings rather than another dashboard.[^15]

## Recommended cost model

Use three boundaries so unlike costs are not mixed:

1. **Four-wall operating cost:** labor, occupancy, utilities, MHE, maintenance, systems, consumables, safety and damage.
2. **Inventory economics:** working-capital charge, shrink, obsolescence, expiry and insurance.
3. **Network logistics:** inbound/outbound freight, packaging, detention, external storage and service failures.

Within each boundary, calculate both annual dollars and a normalized unit cost. A practical facility metric is:

`Four-wall cost per order = (labor + occupancy + MHE + maintenance + utilities + systems + damage + overhead) / shipped orders`

Use a parallel operational metric such as cost per pallet move where order profiles vary substantially. Segment results by shift, zone, process, customer and equipment class so product mix does not mask poor performance.

---

## References

1. [White Paper](https://www.raymondwest.com/-/media/dealers/raymond-handling-solutions/raymond-west/covid/cost-of-labor-white-paper.pdf?rev=638ec5231a5f4cdd8513e02dd94fe2b2)

2. [Simulation and order picking in a very-narrow-aisle ...](https://www.tandfonline.com/doi/full/10.1080/1331677X.2018.1505532) - The revolution of information brought new possibilities for the business organisations: new manageme...

3. [Design and control of warehouse order picking: a literature review](https://research.rug.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/)

4. [What are inventory carrying costs - QuickBooks Global - Intuit](https://quickbooks.intuit.com/global/resources/inventory-management/carrying-costs/) - With inventory carrying costs generally accounting for 15-30% of a business's total inventory value,...

5. [An Evaluation of the Total Cost of Ownership of Fuel Cell](https://www.energy.gov/sites/prod/files/2014/03/f10/fuel_cell_mhe_cost.pdf)

6. [[PDF] An Evaluation of the Total Cost of Ownership of Fuel Cell](https://www.energy.gov/eere/fuelcells/articles/evaluation-total-cost-ownership-fuel-cell-powered-material-handling)

7. [Early Markets: Fuel Cells for Material Handling Equipment](https://www.energy.gov/sites/prod/files/2016/12/f34/fcto_early_markets_mhe_fact_sheet.pdf)

8. [Early Markets: Fuel Cells for Material Handling Equipment](https://www.energy.gov/eere/fuelcells/articles/early-markets-fuel-cells-material-handling-equipment)

9. [TABLE 1. Incidence rates of nonfatal occupational injuries ...](https://www.bls.gov/web/osh/table-1-industry-rates-national.htm) - Incidence rates(1)of nonfatal occupational injuries and illnesses by industry and case types, 2024 I...

10. [Employer-Reported Workplace Injuries and Illnesses, 2023 ...](https://www.bls.gov/news.release/osh.nr0.htm) - Injuries occurred at a rate of 2.2 cases per 100 FTE workers. The incidence rate of illnesses decrea...

11. [Principal Building Activities Warehouse and Storage](https://www.eia.gov/consumption/commercial/pba/warehouse-and-storage.php) - Space heating accounted for the largest share of end-use consumption in warehouse and storage buildi...

12. [Comparing manual and automated production and picking systems](https://www.econstor.eu/bitstream/10419/267191/1/hicl-2021-33-327.pdf)

13. [1910.178 - Powered industrial trucks.](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.178)

14. [[PPT] PPT - EIA](https://www.eia.gov/consumption/commercial/data/2018/ppt/CBECS%202018%20CE%20Release%202%20Flipbook.pptx)

15. [We already have solid monitoring of the battery, whether it’s lead acid or BMS controlled. We communicate the data to the cloud and send alerts for various issues.](https://www.perplexity.ai/search/6fd1c014-decf-4730-9ba4-6d6097bbda0c) - That means you’re already covering the highest-value core monitoring layer, so the next opportunitie...

