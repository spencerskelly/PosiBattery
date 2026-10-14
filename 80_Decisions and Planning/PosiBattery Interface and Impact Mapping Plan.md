# PosiBattery Interface and Impact Mapping Plan

## Purpose

Let a reader pick any element (a product, an interface, a protocol, a function, a requirement, a customer need) and see everything that **impacts it** and everything **it impacts**, across the layers from cell to grid, cloud and user. The same model has to serve two readers:

- **Product manager (less technical):** a one-page answer to "what does this change touch, who is affected, what is at risk", in product, customer and requirement terms.
- **Engineer (deeply technical):** the path behind that answer: which interface, which protocol and version, which message group, which relationship, which source.

Companion notes: [[Interface and Protocol Layer Reference]], [[BMS Function Definitions]], [[BMS Product Function and Requirement Driver Map]].

## What the review found (2026-10-13)

| Finding | Evidence | Consequence |
|---|---|---|
| The relationship vocabulary already supports interface modeling | `relationships.1.36.yaml` defines `hasPort/portOf`, `interfaces` (Port to Port, symmetric), `hasFlow/flowOf`, `transmits`, `receives`, `exchanges`; the Local Model schema 0.2 defines parts, endpoints, connections and flows | No schema change is needed to start |
| It is almost unused | 2 Port notes and 2 Item Flow notes exist (BMID only), and both Ports have `interfaces: []`; one Local Model exists (BMID product assembly) | Interfaces cannot be traversed as interfaces today |
| Interfaces are modeled as Designs | About 37 interface Designs (CAN Interface, Bluetooth, Wi-Fi, Cloud Portal Integration and others) link products to functions | Good for "which products have a CAN interface"; cannot say which protocol, which counterpart, which messages |
| Protocols appear only as prose | J1939 and CANopen are named inside notes; no note exists for any protocol, version or profile | A protocol change cannot be searched or traced |
| Grid, utility and cloud-provider elements are absent | No utility, aggregator or cloud-provider organization notes; EMS research exists as research notes only | The top layers (L7 to L9) cannot be reached from a product |
| Requirements are thin | 8 Requirements, covering BMID, PosiGuard and the SOC and SOH estimator | "What drives this element" mostly ends at a Use Case or Customer Need hypothesis |
| Untyped traversal is too noisy to use | A breadth-first walk from the CAN Interface Design over every relationship reaches 19 notes at one hop, 148 at two and 465 at three, because generic hubs (Wired Interface Design, Truck Telematics Software and similar) connect everything | The impact query must follow typed, directional relationships and stop at abstract hubs |
| Evidence is strong where it was built | The BMS, SOC and SOH, and fleet-digital-access notes carry source Documents, tiers and recorded conflicts | The pattern to repeat is already in place |

## Target model

### Layers

Make the layer list in [[Interface and Protocol Layer Reference]] (L1 cell sensing to L9 users) a governed taxonomy, applied as a tag on interface notes and used to group impact results.

### Note patterns

| Element | Pattern | Relationships |
|---|---|---|
| Product interface | One **Port** per physical or logical interface of a product (for example "ProCore Edge CAN port to battery") | `hasPort` from the product; `interfaces` to the counterpart Port; `layer` tag |
| Data carried | One **Item Flow** per message group or data set (for example "battery limits to charger") | `hasFlow` from the Port; `transmits`, `receives` or `exchanges` on the Ports |
| Protocol and version | One **Info** note per protocol or profile and version (CANopen CiA 418 v1.2.0, J1939/14, OCPP 2.0.1) tagged `protocol`, with transport, layer and source Documents | Port `references` the protocol note; protocol note `describedBy` its Documents; ask the schema owner whether a precise `conformsTo` or `implements` field is wanted instead of `references` |
| Contextual connection | **Local Model** record inside an assembly or system note (battery, charger and truck in one site) | Native block links; quantity from multiplicity, per Ruleset 15.7 |
| External party | **Organization** notes for utilities, aggregators, cloud providers and network operators | `playsRole`, `integratesWith` |
| Driver | **Requirement** or standard Info note per driver, with `appliesTo` on the interface or function | `drives`, `satisfies`, `verifies` as today |

### Three levels of interface detail

| Level | Content | Where it lives |
|---|---|---|
| A. Public standard | Protocol, profile and version as published (CiA 419, J1939/14) | Vault Info note and source Documents |
| B. Product-declared | Which protocol, bit rate or profile a product states in a public source | Port note with the source and tier |
| C. Internal specification | Message identifiers, scaling, state machines, DBC files, node roles | **Not in this repository.** A Port note holds an opaque reference identifier and the owner of the private document |

Reason for level C: this repository is public (checked 2026-10-13). Internal CAN definitions must stay out unless the owner decides otherwise.

## Impact query

### Definition

For a start element, return two sets:

- **Impacting (upstream):** what constrains or drives it: requirements, standards, needs and use cases it serves, the interfaces and protocols it depends on, the parts it contains.
- **Impacted (downstream):** what depends on it: products that have it, functions it enables, use cases, actors and customers, other interfaces on the far side of its Ports, verifications.

### Rules (tested in the prototype run)

1. Follow only directed, typed relationships: `dependsOn/dependencyOf`, `hasPort`, `interfaces`, `transmits/receives`, `hasFlow`, `hasPart/partOf`, `performs/performedBy`, `realizes/realizedBy`, `drives`, `satisfies`, `appliesTo`, `verifies`, `designOf/hasDesign`.
2. Do not traverse `subtypeOf`, `describes` or `references` as impact (they classify or cite); show them as context.
3. Stop at notes marked `abstract: true` and at general-level Functions, and list them as boundary elements.
4. Limit depth (default 3 hops) and group results by layer, then by type.
5. Carry the relationship path and the evidence tier with every result so an engineer can audit it.

### Outputs

| Reader | View | Content |
|---|---|---|
| Product manager | Impact summary (generated note or Obsidian Base) | Counts and names by product family, customer need, actor and requirement; the layers touched; open conflicts and evidence gaps on the affected elements; no protocol detail |
| Engineer | Impact table and path list | Each affected element with layer, relationship path, protocol and version, source and tier; Port-to-Port diagrams per layer (Canvas or Mermaid generated from Ports) |
| Both | Change record | A Decision or Info note for each real change, listing the query result at the time, so impact is reviewable later |

## Phases

| Phase | Work | Exit test |
|---|---|---|
| 0. Decisions (owner) | Confidentiality of internal protocols; adopt the layer taxonomy; scope of the first slice; whether utilities and cloud providers are in scope for the first release | Decisions written in the Research Change and Decision Tracker |
| 1. Pilot slice | One chain end to end: a lithium battery BMS, a PosiCharge charger (ProCore Edge), the truck, PosiLink or SkyLink, the fleet user. Create Ports, Item Flows and protocol notes for L3, L4, L6 and L9 only; level A and B detail; level C as references | A reader can follow battery to user through Ports without reading prose; every Port has a counterpart, a protocol note and a source |
| 2. Impact query | A read-only script in `99_System/09_Tools/` implementing the rules above, a PM summary template and an engineer table | Run on 5 known elements; results reviewed by one PM and one engineer; false-positive hubs removed |
| 3. Widen layers | L1, L2, L5, then L7 and L8: utility, aggregator and cloud-provider Organizations; OCPP, OpenADR and similar protocol notes with the standards read, not only the encyclopedia | Each added layer has at least one traced path to a product |
| 4. Requirements | Interface requirements on our products from levels A and B, with `appliesTo` on Ports; BMS requirements only after the owner answers whether PosiCharge offers a BMS | Requirements trace to a driver and a verification |
| 5. Validation | Replay two past changes (for example a charger CAN profile change and a cloud portal change) and compare the query result with what actually needed rework | Missed or spurious elements recorded and the rules adjusted |

Each phase ends with the existing gates passing and a short evidence note; do not combine phases.

## New checks to add (Phase 2)

- Every interface Design that names a protocol has a Port with a protocol note.
- Every Port has `interfaces` to a counterpart or an explicit exception.
- Every protocol note has a source Document and a version.
- No Port note contains level C content (no message identifiers or scaling) unless the owner has cleared it.

## Risks

| Risk | Handling |
|---|---|
| Internal protocol details leak into a public repository | Level C rule; check in Phase 2; owner decision in Phase 0 |
| Over-modeling before the query proves useful | Pilot slice only; Phase 2 before widening |
| Protocol notes written from encyclopedia pages only | Each protocol note states which sources were read; standards go on the wishlist and notes are upgraded when read |
| Hub notes flood the results | Rule 3; abstract-hub list reviewed in Phase 2 |
| Requirements written for a BMS PosiCharge does not make | Settled: the BMS is external; Phase 4 writes interface requirements only |

## Decisions (settled 2026-10-13)

Recorded in [[Research Change and Decision Tracker]].

1. **Internal protocols:** none exist in the repository yet (everything is public). Only levels A and B are written; level C stays out and enters only as opaque references.
2. **First slice:** PosiCharge lithium and BMID path, battery to charger to truck to PosiLink or SkyLink to fleet user.
3. **Top layers:** entries now ([[Electric Utility or Grid Operator]], [[Cloud Platform Provider]]); deeper work later.
4. **BMS aim:** the BMS is external. PosiCharge has none, so no BMS Requirements are written for PosiCharge. BMS functions and designs are defined in the model ([[Battery Management System Design]], [[BMS Function Definitions]]) and external BMS products are noted ([[External BMS Product Landscape]]). Phase 4 covers interface requirements on PosiCharge products only.
