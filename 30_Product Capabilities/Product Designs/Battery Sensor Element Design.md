---
type: Info
subtype:
id: INFO-00900
uid: 20261003101711539skellyspencer
status: Superseded
tags:
  - legacy-model
  - superseded
describes:
  - "[[Electrolyte Level Sensing Design]]"
  - "[[Battery Temperature Measurement Design]]"

---

# Battery Sensor Element Design

## Definition

Legacy general Design class that previously grouped electrolyte-level and temperature sensing elements together.

## Notes

- **Superseded 2026-10-05.** This note is retained as a compatibility target for historical review records and old links; it is no longer an active Design class.
- Replacement targets are [[Electrolyte Level Sensing Design]] and [[Battery Temperature Measurement Design]]. They are documented in the note body rather than with governed `supersededBy` relationships because this compatibility note is now type Info and the relationship schema requires same-class endpoints.
- Electrolyte-level implementations are now organized under [[Electrolyte Level Sensing Design]].
- Temperature implementations are now organized under [[Battery Temperature Measurement Design]].
- The split removes a cross-domain generalization and restores the rule that active general Design classes represent a coherent family with multiple specific children.
- New model relationships must not use this note as a Design dependency or parent.

## Aliases

## Former ids

- DES-00080
