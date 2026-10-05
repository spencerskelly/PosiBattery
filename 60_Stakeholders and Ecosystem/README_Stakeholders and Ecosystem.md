# Stakeholders and Ecosystem

## Purpose

This is the canonical PosiBattery domain for people, roles, organizations, and external ecosystem context: customer actors, users, operators, buyers, maintainers, suppliers, partners, competitors, regulators, standards bodies, and other durable external parties.

See [[Canonical Vault Top-Level Taxonomy 0.1]] and [[PosiBattery Model Organization and Handoff]].

## Current areas

- [[README_Customer Actors|Customer Actors]] — generalized human or organizational roles that participate in needs and operational contexts.
- [[README_Organizations|Organizations]] — durable organization entities, market-role concepts, business relationships, and offering context.

Actors and Organizations are related but distinct. An Actor represents a role or participant type; an Organization represents a durable organizational entity or organization-class concept. Do not collapse one into the other merely because a company employs a person in a given role.

## Navigation

- `BASE_local_Stakeholders and Ecosystem.base` — direct Markdown contents of this domain.
- `BASE_all_Stakeholders and Ecosystem.base` — recursive Markdown contents across Actors and Organizations.
- [[CANVAS_Stakeholders and Ecosystem]] — curated map of the domain.

## Scope guidance

Use explicit relationships to connect Actors, Organizations, Customer Needs, Use Cases, Products, and evidence. Folder placement is navigation only and does not itself establish participation, ownership, employment, supply, partnership, competition, or any other relationship.

The Organizations area remains a migration candidate because it mixes organization entities, role/type concepts, ledgers, indexes, and synthesis. Later classification steps control any deeper restructuring.

## Actor–Organization–Product relationship semantics

Keep the three layers distinct:

- **Actor** — a person or role participating in a Need or operational Use Case. Use `participants` from the Use Case/Need. Do not infer employment, ownership, or customer-organization membership unless a dedicated relationship is deliberately modeled.
- **Organization** — a company, group, dealer, manufacturer, or other business entity. Use business relationships such as `makes / madeBy`, `offers / offeredBy`, `distributedBy / distributorOf`, `supplierOf / suppliedBy`, `partnerOf`, or `integratesWith` only when evidence supports them.
- **Product** — a commercial or reusable Object. Use `madeBy` only for supported maker identity; use `offeredBy` for channel/brand availability when maker identity is different or unknown; use `poweredBy` only for evidenced technology provenance.

Do not create direct Actor→Product or Actor→Organization structural links merely because an Actor uses, buys, services, installs, or works for that class of organization. Operational participation already captures the role without overloading the Actor note.

Examples:
- [[Triathlon Lithium-Ion Battery for UniCarriers]] is `madeBy` [[Triathlon USA]] and `offeredBy` [[Mitsubishi Logisnext Americas]].
- [[Hyster Battery Tracker]] is `offeredBy` [[Hyster-Yale]] and `poweredBy` [[PosiCharge]]; this does not establish who physically manufactures the hardware.
- [[Crown V-Force BMID]] is `offeredBy` [[Crown Equipment]]; do not infer a different maker without evidence.

## Related areas

- [[README_Customer Needs|Customer Needs]] — desired outcomes and problems associated with Actors.
- [[README_Use and Operations|Use and Operations]] — scenarios and workflows involving Actors and Organizations.
- [[README_Products|Products]] — offerings made, sold, integrated, operated, or supported by Organizations.
- [[README_Research and Evidence|Research and Evidence]] — evidence supporting ecosystem claims.
