# Definitions

## Purpose

This folder defines the shared vocabulary, note conventions, and relationship properties used across the PosiBattery knowledge base. Consult it when creating or interpreting linked notes, metadata, and model relationships.

## Contents

- Note-authoring and layout guidance.
- Enterprise Architect source and traceability guidance.
- Author-code maintenance guidance.
- `Properties/`, the controlled dictionary for metadata and relationship fields.

## Key information

- [[Note Layout]] — required structure and layout conventions for notes.
- [[EA Source Section]] — how source information and Enterprise Architect references are represented.
- [[Changing Your Author Code]] — procedure for changing an author identifier.
- [[Properties/Property Dictionary]] — index of controlled relationship and metadata properties.
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

## Maintenance

Update this index when a new authoring convention or property family is added. Define reusable terminology and relationship semantics here rather than creating inconsistent local variants.
