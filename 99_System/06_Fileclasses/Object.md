---
# ACTIVE MDSE FileClass 2.1. Base generated fields retained; Step 82 merged approved schema additions after the historical generator became unavailable.
version: "2.1"
limit: 20
mapWithTag: false
icon: file-spreadsheet
fields:
  - name: id
    id: hlkSsI
    type: Input
    path: ""
    options: {}
  - name: uid
    id: zbiAZh
    type: Input
    path: ""
    options: {}
  - name: subtype
    id: 1N3vh0
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList:
        "1": "electrical"
        "2": "circuit"
        "3": "mechanical"
        "4": "software"
        "5": "firmware"
        "6": "part"
  - name: status
    id: fNIHRc
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList:
        "1": "Draft"
        "2": "Active"
        "3": "Retired"
  - name: subtypeOf
    id: 5fDswV
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: hasPart
    id: lupRqr
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: hasPort
    id: 6SvNP3
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Port"
  - name: hasChild
    id: Bf2vOK
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Actor | Artifact | Design | Diagram | Document | Failure Mode | Function | Functional Flow | Info | Issue | Item Flow | Plan | Port | Procedure | Requirement | Result | Setup | Step | Use Case | Verification | modelCheck"
  - name: hasState
    id: 9TtGIC
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "State | State Machine"
  - name: includes
    id: 6MGdbk
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: copyOf
    id: pK157v
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: dependsOn
    id: QB4OsE
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: drives
    id: asVSEa
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: precedes
    id: 4IgqKk
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: supersedes
    id: z8SdFQ
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: tracesTo
    id: omlp2g
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: performs
    id: CbNPub
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Function"
  - name: hasDesign
    id: mbvJ3V
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Design"
  - name: conflictsWith
    id: hTrIET
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: productClass
    id: objpc
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList: {"1":"product-category","2":"product-type","3":"product-family","4":"product-variant","5":"specific-offering"}
  - name: satisfies
    id: obj03
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Requirement | Use Case"
  - name: poweredBy
    id: obj04
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization"
  - name: rebrandOf
    id: obj05
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: integratesWith
    id: obj06
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization | Object"
  - name: offeredWith
    id: obj07
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
---
# Object

Fileclass schema for notes with `type: Object`. Generated; see `99_System/01_Admin/Enabled Plugin Stack.md`.
