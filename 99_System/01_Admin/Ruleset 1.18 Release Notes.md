# Ruleset 1.18 Release Notes

## Purpose

Bring the reusable base vault forward with modeling-method decisions learned since the 2026-09-19 package, without importing any project/domain model.

## Modeling decisions added

- meaning before structure / reuse before creation;
- strict subtype-vs-instance decision rule;
- `control` classification independent of type and boundary;
- evidence classes and explicit no-assumption rule;
- stakeholder journey broader than Use Case;
- product Function requires controlled ownership;
- concrete-first external Interface and Item Flow modeling;
- persisted generated inverse relationships for repository-wide visibility;
- Breadcrumbs trail and Canvas relationship visibility expectations;
- behavior-first Function navigation;
- semantic folder ceiling below 25 modeled elements;
- guide/Base/Canvas package for every model-facing folder;
- AI-assisted early coverage workflow with explicit promotion discipline;
- model-health checks for control vocabulary and missing relationship inverses.

## What is intentionally not included

- project-specific product structures;
- project-specific Actors, Requirements, Functions, Designs, interfaces, or taxonomies;
- domain-specific reference knowledge;
- assumptions inherited from the project in which these rules were refined.

The `98_Examples` folder remains generic demonstration content and can be removed when starting a real model.
