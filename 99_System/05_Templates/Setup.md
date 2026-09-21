<%*
const kind = "";
const id = await tp.user.next_id(tp, "SETUP");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Setup
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
providesSource: []
providesLoad: []
providesMeter: []
providesInterfaceEquipment: []
providesEnvironment: []
providesFixture: []
---

# <% elementName %>

## Purpose

## Physical configuration

## Equipment provided

## Configuration

## Notes
