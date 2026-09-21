<%*
const kind = "";
const id = await tp.user.next_id(tp, "TRANS");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Transition
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
source: []
target: []
trigger:
---

# <% elementName %>

## Definition

## Guard / trigger / effect

## Notes
