---
icon: file-spreadsheet
filesPaths:
- 21_Item_Flows
fileClassNotesFolder: 21_Item_Flows
fileClassNoteTemplate: 99_System/05_Templates/Item Flow.md
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
- subtypeOf
- hasPart
- dependsOn
- derivedFrom
- supersedes
- describes
- tracesTo
- source
- target
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
  type: Select
  options:
  - information
  - energy
  - material
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
- id: source
  name: source
  type: Input
  options: []
- id: target
  name: target
  type: Input
  options: []
---

# Item Flow schema

Generated from the MDSE base methodology.
