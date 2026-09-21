<%*
const kindChoices = ["what", "where", "why", "when"];
const kind = await tp.system.suggester(kindChoices, kindChoices);
const id = await tp.user.next_id(tp, "UC");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Use Case
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
markets: []
subtypeOf: []
hasPart: []
dependsOn: []
derivedFrom: []
supersedes: []
describes: []
tracesTo: []
subject: []
hasParticipant: []
realizedBy: []
optionOf: []
causes: []
---

# <% elementName %>

## Intent

## Actor / participant goal

## Preconditions

## Scenario

## Options / exceptions

## Notes
