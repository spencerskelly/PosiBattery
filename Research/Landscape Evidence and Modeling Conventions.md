---
type: Info
subtype:
id: INFO-00075
uid: 20261002163028872skellyspencer
status: Draft
tags:
  - battery-landscape
  - conventions
describes:
  - "[[Battery-Connected Product]]"
---

# Landscape Evidence and Modeling Conventions

## Definition

Working conventions for researching and recording battery-connected products: how evidence is graded, dated and challenged, how conflicts are kept visible, and the modeling choices carried over from the earlier seed work. Proposed, not yet approved by the user.

## Notes

- **Provenance:** research rules and modeling choices below were carried from the seed branch's architecture-alignment note (2026-10-02, written by ChatGPT at the user's direction). Evidence tiers and conflict handling were added in this survey. Nothing here is a governed MDSE rule; the governed rules are in `MDSE Modeling Ruleset 1.23`.
- **Research rules (from seed):** prefer current manufacturer or product pages and current manuals or data sheets for market claims; record the evidence date; distinguish current, obsolete and unclear market status; preserve unknowns and do not infer a missing specification from a similar product; record battery-adjacent products separately from products installed on or integrated into the battery.
- **Evidence tiers (proposed):** T1 manufacturer product page, data sheet, manual or vendor-published app listing; T2 manufacturer press release, or trade press quoting the manufacturer; T3 reseller or parts-catalog listing; T4 third-party blog, training material or vendor marketing; T5 patent, which describes an invention and not product availability. Mark a source '(dated)' when the document shows signs of age.
- **Verification wording on product notes:** 're-verified' means a source retrieved on the date given supports the claim; 'carried' means the claim comes from earlier seed text and was not re-checked; 'refinement' or 'conflict' means a retrieved source differs from earlier text.
- **Conflict handling:** never overwrite earlier text. Add the new statement beside it with its source, and log the difference as a numbered item in [[Battery Product Landscape Conflicts and Open Questions]]. Resolve an item only with a primary source or a user decision. Use `supersedes` only after resolution. `conflictsWith` is defined in the schema as a mutual compatibility conflict, so it is not used for disagreeing sources.
- **User-stated facts:** record who stated it and the date, tag the note `stated-by-user`, and keep unknowns explicit. A user statement is source evidence; it is not mapped to public documents until a source ties them together.
- **Modeling choices carried from seed (not approved):** a commercial product is modeled once as a reusable Object; use on a particular battery, truck or GSE pack is a contextual occurrence in the Local Model, not a duplicate definition; abstract Objects organize a specialization family and `subtypeOf` is used only for true specialization; Ports, Item Flows, Functions and Requirements are added only when evidence or an engineering question justifies them.
- **Identity:** `uid` and `id` follow `AI_INSTRUCTIONS`. A renumbered draft keeps its `uid` and lists its earlier id under Former ids.

## Aliases

- Landscape research conventions


## Former ids
