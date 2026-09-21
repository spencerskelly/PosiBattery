<%*
const kindChoices = ["information", "energy", "material"];
const kind = await tp.system.suggester(kindChoices, kindChoices);
const id = await tp.user.next_id(tp, "IFLOW");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Item Flow
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
---

# <% elementName %>

## Definition

## Payload / quantity

## Direction

## Notes
