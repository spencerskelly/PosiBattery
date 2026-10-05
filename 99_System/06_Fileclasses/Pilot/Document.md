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
  - name: sourceClass
    id: docsc
    type: Select
    path: ""
    options:
      sourceType: "ValuesList"
      valuesList: {"1":"web-page","2":"datasheet","3":"brochure","4":"manual","5":"standard","6":"article","7":"database","8":"other"}
  - {name: sourceUrl, id: docsu, type: Input, path: "", options: {}}
  - {name: sourceRevision, id: docsr, type: Input, path: "", options: {}}
  - {name: accessed, id: docac, type: Input, path: "", options: {}}
  - name: supports
    id: doc01
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: contradicts
    id: doc02
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
  - name: describes
    id: doc03
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Any model note"
---
# Document

Pilot FileClass for `type: Document`. It is not active production configuration until the pilot is adopted.
