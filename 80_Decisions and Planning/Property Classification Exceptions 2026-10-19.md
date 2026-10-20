# Property Classification Exceptions — 2026-10-19

## Authority and scope
Review disposition for the remaining nine `subtype: unknown` commercial records from the PosiBattery property validation CSV. Existing `unknown` values are **not** compliant with element-types schema 1.19; these are explicitly tracked exceptions, **not** a schema change or successful validation. Linked draft PR #8 contains the independent, well-supported corrections.

## Approved technical classification rule
Technical classification is independent of structural level. `electrical` applies to physical products involving transfer, storage, conversion, control or delivery of electrical energy, including integrated hardware/firmware/software products. `mechanical` is for entirely non-electrical structures and mechanisms. `circuit` applies to PCB circuitry. `firmware` runs on the product microcontroller; `software` runs elsewhere, including phone apps. A product's interaction with an electrical system does not alone make the product electrical. Do not invent physical implementation to make the validator pass.

## Nine dispositions
| Record | Existing subtype | Disposition | Missing evidence or model question |
|---|---|---|---|
| Flux Power GSE3 Truck Adapter | unknown | Hold | Adapter only said to meet OEM weight requirement; determine whether structural ballast/tray/frame or electrical adapter |
| Midac Air-Tech Air-Mixing System | unknown | Hold | Confirm whether product boundary includes electrically powered pump, or only pneumatic distribution |
| Amaron DIY Rx | unknown | Hold | Brochure identifies diagnosis feature but does not establish physical device vs procedure/chart/software |
| Deka Ready Power BDI | unknown | Hold | BDI is mentioned only as flyer/function; determine whether separate product/physical display exists |
| Midac MB2 Battery Brain | unknown | Hold | Named charging solution; determine physical hardware, software or integrated system |
| Leoch PzS Automatic Water Filling System | unknown | Hold | Automatic refill may be gravity/floats; determine actuation, electric pump, and product boundary |
| Banner Traction Bull Filling System | unknown | Hold | Water-refill option with undocumented actuation; distinguish mechanical valves/tubing from electrical pump |
| Amaron AFS System | unknown | Hold | Even the expansion of AFS is not established; validate identity before subtype |
| Raymond iWAREHOUSE GATEWAY | unknown | Hold | Distinguish hardware gateway, software service, login portal, or integrated product |

## Acceptance gates
1. Obtain manufacturer documentation or owner-approved engineering model boundary for each record.
2. Either assign `electrical`, `mechanical`, `circuit`, `firmware`, or `software` with supporting rationale; or retype/restructure the note through controlled modeling decision. Preserve id/uid and traceability when changing meaning.
3. If still unresolved, do not silently permit `unknown` in the schema. Report exceptions separately; property validation must not be declared fully green.
4. Before merging PR #8, run the current property scan and the repository's identity, relationship, and structural audits on the exact candidate head, and verify PR Actions conclusions. Note that current property scan on the unmodified unknown records is expected to report nine subtype findings.
5. Resolve the `hasPart` alternative-versus-required-composition modeling issue independently.

## Status
Nine hold decisions recorded; no speculative product classifications committed. This is not evidence of passing CI or local validation.
