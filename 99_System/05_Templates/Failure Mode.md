<%*
const kind = "";
const id = await tp.user.next_id(tp, "FM");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Failure Mode
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
occurrence:
severity:
detection:
subtypeOf: []
hasPart: []
dependsOn: []
derivedFrom: []
supersedes: []
describes: []
tracesTo: []
appliesTo: []
causes: []
---

# <% elementName %>

## Definition

## Cause

## Local effect

## System effect

## Detection / controls

## Notes
