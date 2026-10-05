---
# ACTIVE MDSE FileClass 2.1. Base generated fields retained; Step 82 merged approved schema additions after the historical generator became unavailable.
version: "2.1"
limit: 20
mapWithTag: false
icon: file-spreadsheet
fields:
  - name: id
    id: U54PRn
    type: Input
    path: ""
    options: {}
  - name: uid
    id: 9vjQkk
    type: Input
    path: ""
    options: {}
  - name: status
    id: wRVjlX
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList:
        "1": "Draft"
        "2": "Active"
        "3": "Retired"
  - name: subtypeOf
    id: pE08Aj
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Function"
  - name: hasPort
    id: SkUYBI
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Port"
  - name: hasChild
    id: 5diR9s
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: includes
    id: C0kul2
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: copyOf
    id: iJkMbz
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Function"
  - name: dependsOn
    id: lk9RF0
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: drives
    id: kSU4W2
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: precedes
    id: r0wP61
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Function"
  - name: triggeredBy
    id: mKH4Pm
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Design | Function | Item Flow | State"
  - name: supersedes
    id: Sdytqe
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Function"
  - name: tracesTo
    id: r4H9TU
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: satisfies
    id: KUQofm
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Requirement | Use Case"
  - name: conflictsWith
    id: 5VGlpQ
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: realizedBy
    id: fun02
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Design | Function"
---
# Function

Fileclass schema for notes with `type: Function`. Generated; see `99_System/01_Admin/Enabled Plugin Stack.md`.
