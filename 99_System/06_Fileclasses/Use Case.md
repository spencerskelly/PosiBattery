---
# ACTIVE MDSE FileClass 2.1. Base generated fields retained; Step 82 merged approved schema additions after the historical generator became unavailable.
version: "2.1"
limit: 20
mapWithTag: false
icon: file-spreadsheet
fields:
  - name: id
    id: CE60zx
    type: Input
    path: ""
    options: {}
  - name: uid
    id: wIJHwX
    type: Input
    path: ""
    options: {}
  - name: subtype
    id: oqdFs8
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList:
        "1": "what"
        "2": "where"
        "3": "why"
        "4": "when"
        "5": "who"
  - name: status
    id: pwJZeF
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList:
        "1": "Draft"
        "2": "Active"
        "3": "Retired"
  - name: subtypeOf
    id: z2X4qm
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Use Case"
  - name: hasPort
    id: FnMPgp
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Port"
  - name: hasChild
    id: KeUnoR
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: includes
    id: 5bae3K
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: copyOf
    id: jKfBCu
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Use Case"
  - name: dependsOn
    id: tTgojT
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: drives
    id: 6xEf6N
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: precedes
    id: w9e9pW
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Use Case"
  - name: supersedes
    id: R7aQsd
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Use Case"
  - name: tracesTo
    id: HyHZwd
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: realizedBy
    id: n4mQ3U
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Design | Function"
  - name: optionOf
    id: oJJLgG
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Use Case"
  - name: affects
    id: zASfuZ
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: conflictsWith
    id: kRiFgy
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: participants
    id: FMieAb
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Actor | Document | Function | Object | Port"
  - name: arisesIn
    id: uc02
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Procedure | Setup | Use Case"
---
# Use Case

Fileclass schema for notes with `type: Use Case`. Generated; see `99_System/01_Admin/Enabled Plugin Stack.md`.
