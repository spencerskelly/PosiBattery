---
type: Info
subtype:
id: INFO-00114
uid: 20261002191446825skellyspencer
status: Draft
tags:
  - organization
  - vocabulary
  - provisional
describedBy:
  - "[[Business Relationship Ledger]]"
---

# Business Relationship Vocabulary

## Definition

Provisional relationship fields for connecting organizations, roles and products, mapped to ArchiMate and TOGAF concepts, to be refined into a standard later.

## Notes

- **Status:** provisional. The governed schema (`relationships.yaml` 1.35) has no organization relationships. These fields are listed in `99_System/03_Schemas/business-relationships.provisional.yaml`, mirroring the schema's format with `provisional: true`. No tool reads that file yet, so Nodian will not generate inverses; this vault writes forward and inverse fields by hand (the schema says the forward field wins).
- **Class choices:** organizations and roles are Info notes tagged `organization`; products are Objects. ArchiMate's Business Actor, Business Role and Product map onto these; TOGAF's Organization/Actor and Product catalogs are the closest reference. Neither is adopted as a standard here.
- **Evidence rule:** no business link without a row in [[Business Relationship Ledger]] that gives the source URL and whether the link is stated or inferred. `makes` is used only where the vendor presents the product as its own; otherwise `offers`.
- **Governed alternatives (decision pending, Q9):** `includes` (membership without ownership) could model bundles and dealer networks; `dependsOn` could model supply; `copyOf` could model rebrands; `supersedes` could model successors. Using them would need no schema change but loses the business meaning.
- **Not defined yet:** `competesWith` (analyst judgement, needs a market definition), `licensedFrom`, `acquiredBy` with dates, `resellerOf`. Listed in [[Investigation Backlog]].

| Provisional relationship | Endpoints | Nearest ArchiMate or TOGAF concept | Governed alternative today |
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

## Aliases

- Business relationship vocabulary

## Former ids
