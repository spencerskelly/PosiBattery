---
# ACTIVE MDSE FileClass 2.1 for Organization, adopted in Step 82.
version: "2.1"
limit: 24
mapWithTag: false
icon: file-spreadsheet
fields:
  - {name: id, id: id01, type: Input, path: "", options: {}}
  - {name: uid, id: uid01, type: Input, path: "", options: {}}
  - name: status
    id: sts01
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList: {"1": "Draft", "2": "Active", "3": "Retired"}
  - name: playsRole
    id: org01
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Info"
  - name: makes
    id: org02
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: offers
    id: org03
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Object"
  - name: supplierOf
    id: org04
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization"
  - name: distributedBy
    id: org05
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization"
  - name: subsidiaryOf
    id: org06
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization"
  - name: successorOf
    id: org07
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization"
  - name: privateLabelFor
    id: org08
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization"
  - name: partnerOf
    id: org09
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization"
  - name: integratesWith
    id: org10
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Organization | Object"
  - name: hasNeed
    id: org11
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/MDSE Link Targets.base"
      viewName: "Use Case"
---
# Organization

Fileclass schema for notes with `type: Organization`. Existing organization `Info` notes remain valid until individually migrated.
