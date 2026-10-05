---
# ACTIVE MDSE FileClass 2.1. Base generated fields retained; Step 82 merged approved schema additions after the historical generator became unavailable.
version: "2.1"
limit: 20
mapWithTag: false
icon: file-spreadsheet
fields:
  - name: id
    id: 8favLr
    type: Input
    path: ""
    options: {}
  - name: uid
    id: G1pN8R
    type: Input
    path: ""
    options: {}
  - name: status
    id: fUG6DP
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList:
        "1": "Draft"
        "2": "Active"
        "3": "Retired"
  - name: subtypeOf
    id: meHyys
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Actor"
  - name: hasPort
    id: jrmh2K
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Port"
  - name: hasChild
    id: zAtYyC
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: includes
    id: qyWLlu
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: copyOf
    id: fA6S7o
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Actor"
  - name: dependsOn
    id: XoWptS
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: drives
    id: xbqD17
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: precedes
    id: BornqH
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Actor"
  - name: supersedes
    id: 4dBRP1
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Actor"
  - name: tracesTo
    id: 9Lfhz4
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: conflictsWith
    id: IwV10w
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: hasNeed
    id: act01
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Use Case"
---
# Actor

Fileclass schema for notes with `type: Actor`. Generated; see `99_System/01_Admin/Enabled Plugin Stack.md`.
