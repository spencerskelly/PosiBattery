<%*
const kindChoices = ["electrical", "circuit", "mechanical", "software", "firmware"];
const kind = await tp.system.suggester(kindChoices, kindChoices);
const id = await tp.user.next_id(tp, "THG");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Thing
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
boundary: internal
productLine:
specs: []
propertyDefinitions: []
subtypeOf: []
hasPart: []
dependsOn: []
derivedFrom: []
supersedes: []
describes: []
tracesTo: []
instanceOf: []
performs: []
hasDesign: []
hasStateMachine: []
hasContext: []
addresses: []
---

# <% elementName %>

## Definition

## Purpose / responsibility

## Boundary

## Key properties

## Notes
