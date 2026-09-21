<%*
const kindChoices = ["functional", "design", "standard", "stakeholder"];
const kind = await tp.system.suggester(kindChoices, kindChoices);
const id = await tp.user.next_id(tp, "REQ");
let elementName = tp.file.title;
if (/^Untitled/i.test(elementName)) elementName = await tp.system.prompt("Element name");
await tp.file.rename(`${id} - ${elementName}`);
-%>
---
id: <% id %>
type: Requirement
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
designation:
contentType:
applicabilityStatus:
applicabilityComment:
stakeholderId:
priority:
engineeringComment:
origin:
productManagementComment:
salesComment:
userStory:
subtypeOf: []
hasPart: []
dependsOn: []
derivedFrom: []
supersedes: []
describes: []
tracesTo: []
appliesTo: []
---

# <% elementName %>

## Requirement statement

## Rationale

## Verification intent

## Applicability exceptions

## Notes
