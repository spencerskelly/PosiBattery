# PosiBattery Relationship Recovery — Batch 04 (2026-10-08)

## Scope and control boundary

This is the fourth bounded repair under [issue #2](https://github.com/spencerskelly/PosiBattery/issues/2), continuing [draft PR #4](https://github.com/spencerskelly/PosiBattery/pull/4). It follows [[PosiBattery Relationship Recovery Batch 03 2026-10-08]].

**Incoming verified branch model SHA:** `464e2c2f34bee195be07342d1a4ab1337200c0c6`; two independent primary workflow logs reported **35** `endpoint_incompatible` and **176** `missing_inverse`, **211** errors total. The intervening Batch 03 commits up to `58f169d6` modified documentation only.

**Final Batch 04 model SHA:** `2e25f5b2daffd4fca2a930b54f9c8619aba2d077`.

## Governing semantics and evidence check

Per `99_System/03_Schemas/relationships.yaml` 1.36:
- `hasPart / partOf` is strictly **Object ↔ Object** composition, never physical containment of an Organization.
- `makes / madeBy` relates an Organization (currently some legacy `Info` notes tagged `organization`) to a product Object.
- `offers / offeredBy` represents a distributor or reseller's commercial offering of a product, separately from who makes it.

Before any changes, **all 17 source product notes and all 12 distinct target Organization notes** were inspected. In each of 16 maker cases, the Organization already listed the product through `makes`, while the product had an empty `madeBy`. The seventeenth case was clearly **not** a maker relationship: `Powerfleet Forklift Gateway` already had `madeBy: [[Powerfleet]]`; `Mitsubishi Logisnext Americas` already listed the same product under `offers`, with explicit reseller-agreement evidence in the product note. Correctly set `offeredBy` on the product without altering the maker.

Each affected product had a misplaced Organization link under `hasPart` alongside legitimate component Objects. Moved only that Organization entry into the corresponding `madeBy` or `offeredBy` list. All other component and architecture assertions, model identities, original evidence, and note bodies are retained.

## Exact changes

| Product Object | Existing Organization assertion | Correct product field |
| --- | --- | --- |
| [[Toyota Twistlock Snapshot Camera System]] | [[Toyota Material Handling]] `makes` | `madeBy` |
| [[Panacea Smart Start]] | [[Panacea Aftermarket Co.]] `makes` | `madeBy` |
| [[Toyota PIN Code Access Pad]] | [[Toyota Material Handling]] `makes` | `madeBy` |
| [[Philadelphia Scientific eGO!gateway]] | [[Philadelphia Scientific]] `makes` | `madeBy` |
| [[PosiCharge Single-Point Automatic Battery Watering]] | [[PosiCharge]] `makes` | `madeBy` |
| [[Flow-Rite Maverick Battery Watering System]] | [[Flow-Rite]] `makes` | `madeBy` |
| [[Delta-Q IC650]] | [[Delta-Q Technologies]] `makes` | `madeBy` |
| [[Lester Summit Series II]] | [[Lester Electrical]] `makes` | `madeBy` |
| [[Stryten EHI Charger]] | [[Stryten Energy]] `makes` | `madeBy` |
| [[PosiCharge DVS150]] | [[PosiCharge]] `makes` | `madeBy` |
| [[Fronius SelectION]] | [[Fronius International]] `makes` | `madeBy` |
| [[EnerSys IMPAQ Charger]] | [[EnerSys]] `makes` | `madeBy` |
| [[PosiCharge SVS200]] | [[PosiCharge]] `makes` | `madeBy` |
| [[EnerSys NexSys iON Battery]] | [[EnerSys]] `makes` | `madeBy` |
| [[TUG Endurance Baggage Tractor]] | [[Textron GSE]] `makes` | `madeBy` |
| [[Powerfleet Forklift Gateway]] | [[Mitsubishi Logisnext Americas]] `offers`; actual `madeBy` remains [[Powerfleet]] | `offeredBy` |
| [[PosiCharge SkyLink]] | [[PosiCharge]] `makes` | `madeBy` |

**Change scope confirmed by GitHub compare:** Exactly 17 product Markdown notes modified, each with **one YAML line added and one removed**, no Organization note edited and no non-relationship field changed.

## Diagnostic categorization and acceptance

The incoming validation logs show **exactly three** defects tied to each of the 17 misplaced Organization links:

1. Invalid `hasPart: Object -> Info` endpoint.
2. Missing `partOf` expected from the false Object-to-Organization composition.
3. Missing `madeBy` or `offeredBy` expected from the existing Organization `makes` / `offers` assertion.

The controlled correction is therefore predicted to remove **17 endpoint** errors and **34 missing inverse** errors, for a **51-error reduction** with no new semantics.

| Category | Incoming Batch 04 | Predicted after Batch 04 |
| --- | ---: | ---: |
| `endpoint_incompatible` | 35 | 18 |
| `missing_inverse` | 176 | 142 |
| **Total** | **211** | **160** |

**Acceptance source:** Independently capture the actual counts from **both** MDSE Vault Audit and Semantic Linking Completion Gate on the same SHA `2e25f5b2daffd4fca2a930b54f9c8619aba2d077`. The predicted result is **not** a passing check; unresolved relationship errors remain. Supporting Workbench, Local Model, True Orphan and Port Flow reviews should also be checked.

CI references for the model SHA:
- [MDSE Vault Audit run 37889549809](https://github.com/spencerskelly/PosiBattery/actions/runs/37889549809)
- [Semantic Linking Completion Gate run 37889549813](https://github.com/spencerskelly/PosiBattery/actions/runs/37889549813)

**Verified CI result for model SHA `2e25f5b2daffd4fca2a930b54f9c8619aba2d077`:**

- [MDSE Vault Audit run 37889549809](https://github.com/spencerskelly/PosiBattery/actions/runs/37889549809): **FAIL** (Check relationship invariants), with **18 endpoint_incompatible + 142 missing_inverse = 160**.
- [Semantic Linking Completion Gate run 37889549813](https://github.com/spencerskelly/PosiBattery/actions/runs/37889549813): **FAIL** (Relationship validation), with the same **18 endpoint_incompatible + 142 missing_inverse = 160**.
- This is an **exact 51-error reduction** from the incoming Batch 03 result of 211. All 17 invalid `hasPart: Object -> Info` endpoints disappeared, as did their corresponding 34 inverse findings.
- **Cumulative four-batch improvement against `main`: 331 -> 160 = 171 errors corrected.**
- Workbench, Local Model, and True Orphan checks passed on the model SHA. Port Flow was still in progress when the counts were recorded.
- **Acceptance:** PASS for the narrowly scoped 17-note relationship correction, **FAIL** for release/golden baseline. PR #4 remains draft and `main` is not modified.

## Next recovery work

After verifying this batch's measured delta, triage the **remaining 18 endpoint errors**:

1. Five product `hasDesign` links to another Object product: inspect product pairing, compatibility, integration and commercial evidence; do not use `hasDesign` as an arbitrary relationship.
2. Four Function `realizedBy` links to product/implementation Objects plus one to a Source Document: prefer product `performs` or Document `supports` when an already evidenced inverse makes that valid; do not assume every Object directly performs the Function.
3. Wrong-class Design `subtypeOf/supertypeOf/designOf/realizes` links: distinguish Design hierarchy, concrete product application, and sourced evidence. Preserve meaning and do not create unsupported generalizations.
4. One product `hasPart` to a Function on a remote-control kit: inspect the existing Function's `performedBy` link before changing to `performs`.

Then synchronize missing inverses for valid assertions. Track three separately failing PR-only semantic reviews in [issue #5](https://github.com/spencerskelly/PosiBattery/issues/5), distinct from the core relationship validation in issue #2.

PR #4 stays **draft**, the owner-reviewed `main` remains unchanged, and this batch alone does not prove a stable/golden vault.
