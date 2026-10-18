# California Regulatory Requirements

## Purpose

Requirement notes for regulatory programs that affect forklift charging (energy reporting, fuel-credit programs and similar external obligations).

Parent: [[README_Product Capabilities|30_Product Capabilities]]. See [[Canonical Vault Top-Level Taxonomy 0.1]] for the domain structure.

## Folder review (2026-10-18)

Part of the vault-cleanup review: [[Vault Cleanup Findings 2026-10-18]] defines the finding IDs (F-xx) used below. Numbers come from a read-only audit of this folder on 2026-10-18.

### Snapshot

| Measure | Value |
| --- | --- |
| Markdown notes (this folder / incl. subfolders) | 19 / 19 |
| Typed model notes (incl. subfolders) | 19 (Requirement 19) |
| Status | Draft 19 of 19 |
| Notes with a `describedBy` link / notes linking a Document note anywhere | 0 / 16 of 19 |
| Tags | 26 distinct, 11 used once |
| Size | median 1,650 bytes; largest [[California LCFS - Forklift Volumes Are Reported by Lift Capacity Class]] (2 KB) |

### Analysis

- 19 Requirement notes, all with `appliesTo`; 14 have `references`. Prefix counts: California LCFS 5, California ZEF 3, Charging Energy Reporting 5, Washington CFS 3, Oregon CFP 2, New Mexico CTFP 1.
- Sampled program notes label themselves external obligations, not product requirements, and mark product use as analyst reasoning; the Charging Energy Reporting notes derive from them (`derivedBy`).
- The folder name says California, but 6 of the 19 notes are Washington, Oregon or New Mexico rules and 5 are derived Charging Energy Reporting requirements (F-11).

### Key links

- [[Charging Energy Reporting - Provide kWh by Charging Location with Declared Accuracy]] — 8 inbound links
- [[California LCFS - Forklift Charging Energy Shall Be Metered]] — 7 inbound links
- [[Charging Energy Reporting - Tag Charging Records with Forklift Identifier, Lift Capacity Class and Model Year]] — 7 inbound links
- [[California LCFS - Forklift Volumes Are Reported by Lift Capacity Class]] — 6 inbound links
- [[Charging Energy Reporting - Keep Meter and Energy Records for Verification]] — 6 inbound links
- [[Charging Energy Reporting - Provide Unadjusted Energy Data at the Output or Forklift Side]] — 6 inbound links

### Improvement steps

1. **F-11** Rename candidate: a jurisdiction-neutral folder name. Requires inventory, link check and your approval.
2. **F-07** No governed relationship expresses a disagreement between two Requirement notes: `contradicts` allows only Document, Info or Result as the source, and `conflictsWith` is reserved for compatibility conflicts. Decide how jurisdiction conflicts are recorded.
