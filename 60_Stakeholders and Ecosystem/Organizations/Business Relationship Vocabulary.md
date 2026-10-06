---
type: Info
subtype:
id: INFO-00114
uid: 20261002191446825skellyspencer
status: Draft
tags:
  - organization
  - vocabulary
  - governed-business-vocabulary
describedBy:
  - "[[Business Relationship Ledger]]"
---

# Business Relationship Vocabulary

## Definition

Governed relationship vocabulary for connecting organizations, reusable business roles, and products while preserving distinct maker, offer, channel, supply, ownership, partnership, integration, and product-association meanings.

## Notes

- **Status:** governed. `99_System/03_Schemas/relationships.yaml` 1.36 is authoritative for these predicates, including legacy Info endpoints for existing organization records. Normal inverse synchronization and relationship audit tooling apply. `business-relationships.provisional.yaml` is historical design evidence only and is not semantic authority.
- **Class choices:** organizations and roles are Info notes tagged `organization`; products are Objects. ArchiMate's Business Actor, Business Role and Product map onto these; TOGAF's Organization/Actor and Product catalogs are the closest reference. Neither is adopted as a standard here.
- **Evidence rule:** no business link without a row in [[Business Relationship Ledger]] that gives the source URL and whether the link is stated or inferred. `makes` is used only where the vendor presents the product as its own; otherwise `offers`.
- **Governed alternatives (decision pending, Q9):** `includes` (membership without ownership) could model bundles and dealer networks; `dependsOn` could model supply; `copyOf` could model rebrands; `supersedes` could model successors. Using them would need no schema change but loses the business meaning.
- **Not defined yet:** `competesWith` (analyst judgement, needs a market definition), `licensedFrom`, `acquiredBy` with dates, `resellerOf`. Listed in [[Investigation Backlog]].

| Governed relationship | Endpoints | Nearest ArchiMate or TOGAF concept | Related generic relationship |
|---|---|---|---|
| playsRole / rolePlayedBy | org -> role note | Business Actor assigned to Business Role (ArchiMate); Actor and Role catalog (TOGAF) | none; governed alternative: tags |
| makes / madeBy | org -> Object | Business Actor realizes Product | hasPart is Object-only; none fits |
| offers / offeredBy | org -> Object | Product offered by Business Actor (TOGAF product and service catalog) | describes (about, not offered) |
| supplierOf / suppliedBy | org -> org | Serving relationship between actors | dependsOn (any to any) |
| distributedBy / distributorOf | org -> org | Serving, channel (TOGAF business footprint) | dependsOn |
| partnerOf (symmetric) | org <-> org | Association between actors, or Business Collaboration | tracesTo (provisional) |
| subsidiaryOf / parentOf | org -> org | Aggregation or composition of organization units | includes / hasChild |
| successorOf / predecessorOf | org -> org | Plateau and transition (TOGAF roadmap); no ArchiMate equivalent between actors | supersedes (same class, governed) |
| integratesWith (symmetric) | any <-> any | Association or Flow between actors or products | dependsOn |
| offeredWith (symmetric) | Object <-> Object | Aggregation inside a Product bundle | includes (a bundle note includes its members) |
| privateLabelFor / privateLabelledBy | org -> org | none; contract-like relation between actors | none |
| poweredBy / powers | Object -> org | none; technology or platform provider | dependsOn |
| rebrandOf / rebrandedAs | Object -> Object | Specialization of a Product under another brand | copyOf (same class, any to any) |
- **Multiple links (owner decision 2026-10-02):** a note may hold several links of the same kind. The body then says how the linked products differ; if none is known it says so. Where related products are not yet found, the field stays blank.
- **Round 13:** the first `supplierOf` instance now exists (Triathlon USA to Mitsubishi Logisnext, named in a Logisnext release). `distributedBy` is also used for a truck maker (Jungheinrich to Mitsubishi Logisnext).

## Aliases

- Business relationship vocabulary


## Former ids
