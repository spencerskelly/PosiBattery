---
icon: file-spreadsheet
filesPaths:
- 60_Verification/06_Results
fileClassNotesFolder: 60_Verification/06_Results
fileClassNoteTemplate: 99_System/05_Templates/Result.md
fieldsOrder:
- id
- type
- kind
- status
- control
- formerIds
- eaGUID
- aliases
- tags
- outcome
- subtypeOf
- hasPart
- dependsOn
- derivedFrom
- supersedes
- describes
- tracesTo
- resultOf
- hasEvidence
- dut
- equipmentUsed
fields:
- id: id
  name: id
  type: Input
  options: []
- id: type
  name: type
  type: Input
  options: []
- id: kind
  name: kind
  type: Input
  options: []
- id: status
  name: status
  type: Select
  options:
  - Draft
  - Review
  - Approved
  - Deprecated
  - Retired
- id: control
  name: control
  type: Select
  options:
  - controlled
  - modifiable
  - contextual
  - reference
- id: formerIds
  name: formerIds
  type: Input
  options: []
- id: eaGUID
  name: eaGUID
  type: Input
  options: []
- id: aliases
  name: aliases
  type: Input
  options: []
- id: tags
  name: tags
  type: Input
  options: []
- id: outcome
  name: outcome
  type: Select
  options:
  - Pass
  - Fail
  - Pass with Deviation
  - Not Run
  - Blocked
- id: subtypeOf
  name: subtypeOf
  type: Input
  options: []
- id: hasPart
  name: hasPart
  type: Input
  options: []
- id: dependsOn
  name: dependsOn
  type: Input
  options: []
- id: derivedFrom
  name: derivedFrom
  type: Input
  options: []
- id: supersedes
  name: supersedes
  type: Input
  options: []
- id: describes
  name: describes
  type: Input
  options: []
- id: tracesTo
  name: tracesTo
  type: Input
  options: []
- id: resultOf
  name: resultOf
  type: Input
  options: []
- id: hasEvidence
  name: hasEvidence
  type: Input
  options: []
- id: dut
  name: dut
  type: Input
  options: []
- id: equipmentUsed
  name: equipmentUsed
  type: Input
  options: []
---

# Result schema

Generated from the MDSE base methodology.
