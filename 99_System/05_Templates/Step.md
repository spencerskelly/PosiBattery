<%*
const kind = "";
const id = await tp.user.next_id(tp, "STEP");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Step
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
subtypeOf: []
hasPart: []
dependsOn: []
derivedFrom: []
supersedes: []
describes: []
tracesTo: []
appliesTo: []
startState: []
endState: []
requiresSource: []
requiresLoad: []
requiresMeter: []
requiresInterfaceEquipment: []
requiresEnvironment: []
requiresFixture: []
---

# <% elementName %>

## Purpose

## Procedure

## Expected result

## Notes
