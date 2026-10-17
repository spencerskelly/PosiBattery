# Requirement Applicability Review

Step 13 review of every Requirement's explicit scope and reciprocal product applicability.

## Summary

| Metric | Count |
|---|---:|
| appliesTo_assertions | 9 |
| family_level_requirements | 4 |
| requirements | 8 |
| requirements_with_explicit_scope | 8 |
| unique_family_scope_targets | 1 |
| unique_variant_scope_targets | 1 |
| variant_specific_requirements | 2 |
| findings | 0 |

## Applicability map

| Requirement | appliesTo | Requirement scope | Target productClass | Target abstract |
|---|---|---|---|---|
| 30_Product Capabilities/BMID - Preserve Battery Association.md | 10_Products/Battery Accessories/Identification and Charge Interface Devices/PosiCharge BMID.md | family-level | product-family | True |
| 30_Product Capabilities/BMID - Provide Battery Identity to Compatible Charger.md | 10_Products/Battery Accessories/Identification and Charge Interface Devices/PosiCharge BMID.md | family-level | product-family | True |
| 30_Product Capabilities/BMID - Provide Supported Battery Condition Information to Charger.md | 10_Products/Battery Accessories/Identification and Charge Interface Devices/PosiCharge BMID.md | family-level | product-family | True |
| 30_Product Capabilities/BMID - Retain Battery-Specific Usage History.md | 10_Products/Battery Accessories/Identification and Charge Interface Devices/PosiCharge BMID.md | family-level | product-family | True |
| 30_Product Capabilities/Estimate State of Charge and Health - Declare Accuracy Basis.md | 20_Product Architecture/Model-Based State of Charge Estimator Firmware.md | unclassified |  | False |
| 30_Product Capabilities/Estimate State of Charge and Health - Declare Accuracy Basis.md | 20_Product Architecture/Data-Driven State of Health Estimator Firmware.md | unclassified |  | False |
| 30_Product Capabilities/Estimate State of Health - Report Configured Threshold Crossings.md | 20_Product Architecture/Data-Driven State of Health Estimator Firmware.md | unclassified |  | False |
| 30_Product Capabilities/PosiGuard - Support Lead-Acid and Lithium Battery Fleets.md | 10_Products/Battery Accessories/Identification and Charge Interface Devices/PosiCharge PosiGuard.md | variant-specific | specific-offering | False |
| 30_Product Capabilities/PosiGuard - Support Local Service Configuration.md | 10_Products/Battery Accessories/Identification and Charge Interface Devices/PosiCharge PosiGuard.md | variant-specific | specific-offering | False |

## Findings

| Path | Kind | Detail |
|---|---|---|
| _None_ | | |

## Interpretation

- appliesTo/applies is the authoritative applicability relationship; folder placement and prose alone do not establish product scope.
- Family-level Requirements target the reusable product-family Object. They are not duplicated onto every child product because doing so would assert child applicability/compliance that may not yet be evidenced.
- Variant-specific Requirements target the specific offering/variant that owns the obligation.
- Product specialization and Requirement applicability are separate semantics. subtypeOf does not automatically copy Requirements to a child.
- If a family Requirement later gains exceptions or variant refinements, represent those with explicit Requirement/model semantics rather than relying on inherited folder structure.