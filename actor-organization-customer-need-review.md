# Actor, Organization, and Customer Need Review

Step 22 review of stakeholder need ownership and the governed business-relationship network.

## Summary

| Metric | Count |
|---|---:|
| actor_need_pairs | 57 |
| actors | 12 |
| actors_with_needs | 11 |
| assertions_distributedBy | 11 |
| assertions_integratesWith | 50 |
| assertions_makes | 451 |
| assertions_offers | 70 |
| assertions_partnerOf | 4 |
| assertions_playsRole | 157 |
| assertions_poweredBy | 3 |
| assertions_subsidiaryOf | 12 |
| assertions_successorOf | 2 |
| assertions_supplierOf | 3 |
| business_ledger_governance_aligned | 1 |
| business_relationship_assertions_reviewed | 763 |
| business_role_notes | 13 |
| business_vocabulary_governance_aligned | 1 |
| customer_needs | 30 |
| customer_needs_with_holder | 30 |
| customer_needs_with_realizedBy | 30 |
| generic_actors_without_direct_needs | 1 |
| legacy_info_organization_identities | 121 |
| organization_folder_nonidentity_notes | 5 |
| organization_identities_total | 121 |
| typed_organizations | 0 |
| findings | 0 |

## Findings

| Path | Kind | Detail |
|---|---|---|
| _None_ | | |

## Interpretation

- Customer Need is represented as Use Case subtype why; hasNeed/needOf identifies who holds the need, while participants remains scenario participation.
- The generic Vehicle Operator Actor may remain without direct hasNeed when its specialized Forklift Operator and GSE Operator roles carry the specific need ownership.
- No customer organization is invented merely because customer Actors exist. Actor roles and institutional Organizations are distinct concepts.
- Existing organization identities remain legacy Info notes where already established. relationships.yaml 1.36 explicitly supports those legacy organization endpoints; mass type migration is not required for semantic completeness.
- Business relationships such as makes, offers, supplierOf, distributedBy, subsidiaryOf, partnerOf, integratesWith, and playsRole are governed relationship semantics and must retain synchronized inverses or mirrors.
- playsRole is for durable organization identity in the market. Supplier, channel, partner, integration, and competition context must not be flattened into permanent global roles.
- madeBy and offeredBy remain distinct: maker identity is not inferred from brand or channel availability.
- poweredBy is technology provenance and does not assert physical manufacture.
- Customer and business context does not substitute for product architecture: organization-to-product commercial links do not imply hasPart, hasDesign, performs, or other engineering structure.