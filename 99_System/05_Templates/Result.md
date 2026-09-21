<%*
const kind = "";
const id = await tp.user.next_id(tp, "RES");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Result
<%* if (kind) { -%>
kind: <% kind %>
<%* } -%>
status: Draft
control:
formerIds: []
eaGUID: []
aliases: []
tags:
  - model
outcome:
subtypeOf: []
hasPart: []
dependsOn: []
derivedFrom: []
supersedes: []
describes: []
tracesTo: []
resultOf: []
hasEvidence: []
dut: []
equipmentUsed: []
---

# <% elementName %>

## Execution summary

## Actual result

## Evidence

## Deviations / observations

## Notes
