<%*
const kind = "";
const id = await tp.user.next_id(tp, "PLAN");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Plan
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
usesSetup: []
sequence: []
plannedDUTs: []
scopeRequirements: []
---

# <% elementName %>

## Objective

## Scope

## Sequence / campaign

## Resources

## Exit criteria

## Notes
