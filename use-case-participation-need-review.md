# Use Case Participation and Need-Link Review

Step 11 whole-vault review of Use Case participants, customer-need holders, operational realization, and scenario links.

## Summary

| Metric | Count |
|---|---:|
| context_use_cases | 21 |
| customer_needs | 31 |
| needs_with_actor_or_org_participant | 31 |
| needs_with_governed_needOf | 31 |
| needs_with_realizedBy | 31 |
| operational_use_cases | 23 |
| operational_with_actor_or_org_participant | 23 |
| operational_with_drives | 5 |
| operational_with_realizedBy | 23 |
| use_cases | 75 |
| use_cases_with_participants | 75 |
| governed Actor/Organization need pairs missing or unsynchronized | 0 |
| other findings | 0 |

## Missing governed need pairs

| Actor/Organization | Customer Need |
|---|---|
| _None_ | |

## Other findings

| Path | Kind | Detail |
|---|---|---|
| _None_ | | |

## Interpretation

- participants states who/what participates in a Use Case; it does not replace the semantic statement that an Actor or Organization has a Customer Need.
- For Customer Needs, Actor/Organization participants should also be represented by the governed hasNeed/needOf pair when the note explicitly says that role has the problem.
- Operational Use Cases should normally have an Actor/Organization participant and a realizedBy Function/Design when the behavior boundary is mature.
- Customer Need realizedBy links express the capability/functions that address the need; they are distinct from need ownership.
- Includes/optionOf are required only when scenario membership/option semantics actually exist; their absence is not itself a defect.
- External actor behavior stays in Use Cases; product-controlled behavior stays in Functions.