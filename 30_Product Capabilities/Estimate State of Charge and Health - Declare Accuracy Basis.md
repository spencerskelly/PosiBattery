---
type: Requirement
subtype: engineering
id: REQ-00044
uid: 20261013113854535skellyspencer
status: Draft
tags:
  - battery-monitoring
  - state-of-charge
  - state-of-health
  - candidate-from-research
appliesTo:
  - "[[Estimate State of Charge]]"
  - "[[Estimate State of Health]]"
---

# Estimate State of Charge and Health - Declare Accuracy Basis

## Definition

Each state-of-charge or state-of-health estimator shall state its accuracy on the battery chemistry and duty cycle it is applied to, together with the test conditions and error definition under which that accuracy was established.

## Notes

- **Proposed from the literature review; there is no stakeholder or customer source for it.** It stays Draft until a person decides whether it is a requirement. Evidence: [[SOC and Health Estimation Literature Review]].
- Rationale: the accuracy figures in the review come almost entirely from lithium cells on laboratory data, and the sources define and report error differently (units, abbreviations and numbers disagree within and between papers; see the conflict register [[Battery Product Landscape Conflicts and Open Questions]]). None tests partial discharge or opportunity charging.
- The accuracy values are not set here; they are product decisions.
- Verification is not defined yet.

## Former ids
