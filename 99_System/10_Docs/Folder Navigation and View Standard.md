# Folder Navigation and View Standard

## Purpose

Every model-facing folder should be understandable without first reading the entire methodology.

## Required local navigation package

Each model-facing folder contains:
1. `00 - Views and Bases.md` — purpose, scope, neighboring model areas, and maintenance guidance.
2. `00 - Folder Contents.base` — exhaustive immediate-folder inventory.
3. `00 - Folder Map.canvas` — readable local visual navigation.

## Element-count ceiling

A model-facing folder should contain **fewer than 25 modeled elements** in its immediate scope.

The ceiling does not count the required navigation files or a small number of focused supporting Canvases.

When a folder reaches 25 elements:
- create subfolders only when a durable semantic distinction exists;
- prefer intrinsic type, behavior, evidence form, role, flow content, or requirement/design concern before impacted feature/domain;
- do not create numeric overflow buckets or arbitrary A–M/N–Z splits;
- keep the hierarchy shallow;
- if no meaningful split exists yet, document the pressure and use focused Bases/Canvases temporarily rather than inventing false semantics.

## Diagram-size guideline

Automatically generated Canvases should normally contain about 12 semantic elements or fewer.

Use generous spacing so edge labels remain readable. A useful default starting point is roughly 500–600 px horizontal and 220–260 px vertical separation.

## Folder hierarchy vs semantic hierarchy

Folders answer: **where do I navigate?**

Relationships answer: **what is this element and how does it relate?**

Folder placement never substitutes for `subtypeOf`, `instanceOf`, `hasPart`, `performs`, `satisfies`, `appliesTo`, or any other semantic relationship.

## Base vs Canvas

- Base = completeness.
- Canvas = understanding.

The Base should be exhaustive for the immediate folder. The Canvas should remain readable and may show only the most useful subset plus links to focused views.

## Relationship labels on semantic Canvases

When a semantic relationship is known, label the Canvas edge with the exact model vocabulary (for example `subtypeOf`, `instanceOf`, `connects`, `carries`, `performs`, `satisfies`, `appliesTo`).

Do not invent a Canvas relationship label when the model relationship has not been established.

## Breadcrumbs

Breadcrumbs is the default note-level relationship navigator. The in-note Trail should expose immediate relationships while Tree/Matrix views support deeper navigation.
