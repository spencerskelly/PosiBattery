---
# GENERATED FOR STEP 79 PILOT from element-types.1.18.yaml, metadata.1.0.yaml, relationships.1.36.yaml
version: "2.1-pilot"
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
  - name: productClass
    id: objpc
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList: {"1":"product-category","2":"product-type","3":"product-family","4":"product-variant","5":"specific-offering"}
  - name: hasPart
    id: obj01
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Object"
  - name: hasDesign
    id: obj02
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Design"
  - name: satisfies
    id: obj03
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Requirement | Use Case"
  - name: poweredBy
    id: obj04
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Organization"
  - name: rebrandOf
    id: obj05
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Object"
  - name: integratesWith
    id: obj06
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Organization | Object"
  - name: offeredWith
    id: obj07
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Object"
---
# Object

Pilot FileClass for `type: Object`. It is not active production configuration until the pilot is adopted.
