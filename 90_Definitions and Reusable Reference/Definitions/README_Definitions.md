# Definitions

## Purpose

This folder defines the shared vocabulary, note conventions, and relationship properties used across the PosiBattery knowledge base. Consult it when creating or interpreting linked notes, metadata, and model relationships.

## Contents

- Note-authoring and layout guidance.
- Enterprise Architect source and traceability guidance.
- Author-code maintenance guidance.
- `Properties/`, the controlled dictionary for metadata and relationship fields, with [[README_Properties|Properties]] as its semantic navigation guide.

## Key information

- [[Note Layout]] — required structure and layout conventions for notes.
- [[EA Source Section]] — how source information and Enterprise Architect references are represented.
- [[Changing Your Author Code]] — procedure for changing an author identifier.
- [[README_Properties|Properties]] — grouped guide for choosing and interpreting controlled properties.
- [[Properties/Property Dictionary|Property Dictionary]] — exhaustive tabular inventory of controlled relationship and metadata properties.
- [[uid]] and [[id]] — identifier semantics.
- [[status]] — lifecycle/status semantics.
- [[hasDesign]], [[performs]], [[satisfies]], and [[tracesTo]] — common cross-domain relationships.

## Related areas

- [[README_Products|Products]] — catalog entities that use the shared vocabulary.
- [[README_Product Functions|Product Functions]] and [[README_Product Designs|Product Designs]] — linked functional and design concepts.
- [[README_Performance Metrics|Performance Metrics]] — controlled comparison dimensions.
- [[README_Research|Research]] — synthesized analysis using these concepts.

## Definition versus research boundary

Keep reusable definitions concise and context-independent.

A definition/reference note may contain:

- the canonical meaning of a term or property;
- allowed values, direction, inverse, or usage rules;
- stable authoring/modeling conventions;
- short examples that clarify semantics.

Move or keep content under [[README_Research|Research]] when it is primarily:

- product- or vendor-specific source extraction;
- literature review, comparison, or market evidence;
- long quoted/paraphrased source findings;
- conflicting source claims;
- dated observations whose meaning may change with new evidence.

Definitions may link to Research for provenance, but they should not accumulate large evidence dumps. Research should support the definition rather than become embedded inside it.

Enterprise Architect translation/layout guidance such as [[EA Source Section]] and [[Note Layout]] is methodology/reference content, not research extraction. Its long form does not by itself make it Research.

## Evidence linkage and separation

When a reusable definition needs evidentiary support, keep the reusable semantic statement here and place source-specific extraction or analysis in the evidence layer.

Use the following pattern:

- link to a curated [[README_Source Documents|Source Document]] record when a specific external document directly supports the definition;
- link to [[README_Research|Research]] when the support depends on synthesis, comparison, conflicting evidence, or interpretation across sources;
- keep vendor wording, dated observations, extracted tables, long source summaries, and unresolved source conflicts out of reusable definition notes;
- preserve uncertainty in the Research or Source Document record rather than converting it into unconditional definition text.

A definition does not require an evidence link when it is itself a controlled internal modeling convention or schema vocabulary. Evidence links are appropriate when the definition makes an externally sourced technical, market, standards, product, or technology claim.

## Maintenance

Update this index when a new authoring convention or property family is added. Define reusable terminology and relationship semantics here rather than creating inconsistent local variants.
