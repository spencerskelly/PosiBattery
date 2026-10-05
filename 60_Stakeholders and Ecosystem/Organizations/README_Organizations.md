# Organizations

## Purpose

This folder contains organization records and market-role concepts for companies that make, sell, distribute, integrate, operate, or otherwise influence industrial batteries, chargers, monitoring products, forklifts, fuel-cell systems, ground-support equipment, and fleet technology.

## Contents

- Individual organization notes, including battery makers, charger makers, truck OEMs, distributors, software vendors, and accessory makers.
- Role/type notes such as [[Battery Maker]], [[Charger Maker]], [[Truck OEM]], [[Dealer or Distributor]], [[Monitor Maker]], and [[Software Vendor]].
- Evidence-backed relationship records and offering indexes.

## Key information

- [[Ampure]] — group context: PosiCharge, Power Designers Sibex and Automotive and Aftermarket EVSE are internal businesses, not competitors. See [[Ampure Group Portfolio Context|Ampure Group Portfolio Context]].
- [[Business Relationship Ledger]] — detailed relationship evidence and claims.
- [[Business Relationship Vocabulary]] — terms used for organization-to-organization relationships.
- [[Offerings by Organization]] — organization-centric offering index.
- [[Products Offered or Promoted with Industrial Batteries]] — product/organization relationship index.
- [[Industrial Battery Supply and Private-Label Relationships]] — supply-chain and private-label analysis.
- [[CANVAS_Organizations]] — visual organization map.
- `BASE_all_Organizations.base` and `BASE_local_Organizations.base` — organization views.

## Controlled role classification

Use two different mechanisms depending on whether the role is intrinsic to the organization or contextual to a specific relationship / offer space.

### Intrinsic organization roles

Use `playsRole / rolePlayedBy` only for durable roles that describe what the organization is in this market:

- [[Battery Maker]]
- [[Charger Maker]]
- [[Monitor Maker]]
- [[Truck OEM]]
- [[Dealer or Distributor]]
- [[Software Vendor]]
- [[Accessory Maker]]
- [[Brand Owner]]

These may coexist on one organization.

### Contextual ecosystem roles

Do **not** turn these into global `playsRole` labels unless the scope is explicit. Use the relationship field or scoped research record instead:

- **Supplier** — use `supplierOf / suppliedBy` between the specific organizations.
- **Channel partner** — use `distributedBy / distributorOf`.
- **Partner** — use `partnerOf` only where the partnership itself is evidenced.
- **Technology/integration partner** — use `integratesWith` or a scoped research record.
- **Competitor** — classify only in a defined offer space; see [[PosiCharge Competitive and Partner Landscape]]. Do not label an entire company a competitor merely because one product overlaps.
- **Customer / operator** — classify only when an actual buying/operating organization is identified. Customer Actors such as [[Fleet Operations Manager]] are not organization records.
- **Regulator** and **Standards body** — create organization records only when the organization itself is needed for traceability to a rule, standard, or Requirement. Do not infer the body from a product certification string alone.

### Evidence rule

Every contextual business role must be supported by either:

1. a corresponding relationship in the organization notes plus [[Business Relationship Ledger]], or
2. a scoped research record with the offer/market context and source evidence.

Avoid global role tags for contextual relationships because supplier, partner, customer, and competitor status can change by product, market, geography, and time.

## Related areas

- [[README_Products|Products]] — offerings and product categories.
- [[README_Source Documents|Source Documents]] — primary documents supporting organization claims.
- [[README_Research|Research]] — competitor landscapes, catalog review, and unresolved relationship questions.
- [[README_Definitions|Definitions]] — common relationship vocabulary and property semantics.

## Maintenance

Add a new organization note when evidence supports a durable entity record. Record uncertain, conflicting, or provisional relationships explicitly in the relevant ledger or research note; do not silently resolve or remove conflicts.
