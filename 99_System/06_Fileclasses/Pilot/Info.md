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
  - name: measureClass
    id: infmc
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList: {"1":"metric","2":"property-definition","3":"comparison-criterion"}
  - name: valueType
    id: infvt
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList: {"1":"numeric","2":"categorical","3":"boolean","4":"text","5":"compound"}
  - {name: unit, id: infun, type: Input, path: "", options: {}}
  - {name: measurementMethod, id: infmm, type: Input, path: "", options: {}}
  - name: appliesTo
    id: inf01
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: measures
    id: inf02
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: supports
    id: inf03
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: contradicts
    id: inf04
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: describes
    id: inf05
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
---
# Info

Pilot FileClass for `type: Info`. It is not active production configuration until the pilot is adopted.
