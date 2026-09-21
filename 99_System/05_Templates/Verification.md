<%*
const kindChoices = ["test", "analysis", "inspection", "demonstration"];
const kind = await tp.system.suggester(kindChoices, kindChoices);
const id = await tp.user.next_id(tp, "VER");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Verification
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
verifies: []
startState: []
endState: []
operatingState: []
exercises: []
requiresSource: []
requiresLoad: []
requiresMeter: []
requiresInterfaceEquipment: []
requiresEnvironment: []
requiresFixture: []
---

# <% elementName %>

## Purpose

## Method

## Procedure / criteria

## Expected result

## Notes
