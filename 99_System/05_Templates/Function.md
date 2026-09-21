<%*
const kindChoices = ["system", "hardware", "software", "module"];
const kind = await tp.system.suggester(kindChoices, kindChoices);
const id = await tp.user.next_id(tp, "FUNC");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Function
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
hasBehavior: []
satisfies: []
addresses: []
---

# <% elementName %>

## Definition

## Behavior

## Inputs / outputs

## Performance / constraints

## Notes
