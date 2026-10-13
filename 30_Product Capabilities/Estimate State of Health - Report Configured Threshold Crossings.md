---
type: Requirement
subtype: engineering
id: REQ-00043
uid: 20261013113854528skellyspencer
status: Draft
tags:
  - battery-monitoring
  - state-of-health
  - candidate-from-research
appliesTo:
  - "[[Estimate State of Health]]"
---

# Estimate State of Health - Report Configured Threshold Crossings

## Definition

A state-of-health estimator shall detect and report each crossing of a configured state-of-health threshold (for example a replacement threshold), and not only provide an average-accuracy estimate.

## Notes

- **Proposed from the literature review; there is no stakeholder or customer source for it.** It stays Draft until a person decides whether it is a requirement. Evidence: [[SOC and Health Estimation Literature Review]].
- Rationale: in source 15 a gradient-boosted estimator with respectable average error caught the critical band (SOH below 70%) only 7.1% of the time (5.2% across protocols), so average error alone hides misses at the threshold (C167 in [[Battery Product Landscape Conflicts and Open Questions]]).
- The threshold values are not set here. The sources use 80% as the end-of-life convention (sources 11, 12, 14, 15) and source 15 uses 90%, 80% and 70% only as configurable bands; the NASA data set in source 13 ends tests at 70%. The values, and the detection target, are product decisions.
- Verification is not defined yet.

## Former ids
