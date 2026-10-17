# Product-to-Market Ecosystem Review

Step 23 reviews commercial/ecosystem semantics without treating them as product architecture.

## Summary

| Metric | Count |
|---|---:|
| abstract_product_objects | 61 |
| concrete_product_objects | 509 |
| concrete_products_with_direct_customer_need_behavior_route | 410 |
| concrete_products_with_offeredWith_customer_need_route | 213 |
| integratesWith_assertions | 48 |
| madeBy_assertions | 451 |
| offeredBy_assertions | 70 |
| offeredWith_assertions | 488 |
| organization_distributedBy_assertions | 11 |
| organization_partnerOf_assertions | 4 |
| organization_supplierOf_assertions | 3 |
| poweredBy_assertions | 3 |
| poweredBy_without_manufacturer_claim | 2 |
| product_objects | 570 |
| products_distinguishing_maker_and_offerer | 8 |
| products_with_integratesWith | 35 |
| products_with_madeBy | 449 |
| products_with_offeredBy | 70 |
| products_with_offeredWith | 263 |
| products_with_poweredBy | 3 |
| products_with_rebrandOf | 2 |
| rebrandOf_assertions | 2 |
| findings | 0 |
| review_prompts | 0 |

## Findings

| Path | Kind | Detail |
|---|---|---|
| _None_ | | |

## Step 24 attribution queue

| Path | Kind | Detail |
|---|---|---|
| _None_ | | |

## Semantic boundaries

- madeBy/makes identifies maker/manufacturer identity; offeredBy/offers identifies commercial/channel availability and must not be promoted to maker identity without evidence.
- poweredBy/powers records a named technology/platform source and does not prove physical manufacturing.
- rebrandOf/rebrandedAs is a commercial identity relationship between real products and is not copyOf or subtypeOf.
- offeredWith is market/configuration/bundle context. It does not mean hasPart and does not imply the option is present on every unit.
- integratesWith is compatibility/integration context and does not by itself imply interfaces, composition, or implementation ownership.
- supplierOf/distributedBy/privateLabelFor/partnerOf describe organization ecosystem context and remain distinct from product architecture.
- Customer-need routes through performs are stronger than routes through offeredWith; option context must remain visibly weaker.
- Missing maker/offerer attribution on a concrete catalog note is not auto-fixed. Step 24 will classify legitimate sparse reference leaves versus accidental gaps.