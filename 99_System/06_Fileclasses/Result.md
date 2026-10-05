---
# ACTIVE MDSE FileClass 2.1. Base generated fields retained; Step 82 merged approved schema additions after the historical generator became unavailable.
version: "2.1"
limit: 20
mapWithTag: false
icon: file-spreadsheet
fields:
  - name: id
    id: jEhKBp
    type: Input
    path: ""
    options: {}
  - name: uid
    id: 30g4dV
    type: Input
    path: ""
    options: {}
  - name: status
    id: pW7fgD
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList:
        "1": "Draft"
        "2": "Active"
        "3": "Retired"
  - name: subtypeOf
    id: ctt6Cn
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Result"
  - name: hasPort
    id: mcIu0L
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Port"
  - name: hasChild
    id: ApNpVJ
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: includes
    id: TrfEjP
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: copyOf
    id: AdLnqB
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Result"
  - name: dependsOn
    id: BGp4TC
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: drives
    id: yvGJlp
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: precedes
    id: IBsd1o
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Result"
  - name: supersedes
    id: PvaDc1
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Result"
  - name: tracesTo
    id: EDpn46
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: conflictsWith
    id: CCf1v0
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: satisfies
    id: res01
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Requirement | Use Case"
  - name: verifies
    id: res02
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Requirement | Function | Design | Info"
  - name: supports
    id: res03
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: contradicts
    id: res04
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
---
# Result

Fileclass schema for notes with `type: Result`. Generated; see `99_System/01_Admin/Enabled Plugin Stack.md`.
