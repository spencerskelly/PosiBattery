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
  - name: hasNeed
    id: act01
    type: MultiFile
    path: ""
    options:
      baseFile: "99_System/06_Fileclasses/Pilot/MDSE Link Targets.base"
      viewName: "Use Case"
---
# Actor

Pilot FileClass for `type: Actor`. It is not active production configuration until the pilot is adopted.
