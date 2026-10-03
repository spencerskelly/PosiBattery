# Research Change and Decision Tracker

## Purpose

Provide a concise, durable record of material changes to the business knowledge base and the method or decision behind each change. Use this tracker to avoid repeatedly re-litigating settled scope, modeling, research, and information-architecture decisions.

## Entry rules

Create an entry when a change affects repository structure, modeling conventions, comparison methodology, business scope, decision criteria, or an important research conclusion. Do not record routine spelling fixes or minor formatting changes.

Each entry should state: date, change, reason/method, affected notes, evidence or basis, and any follow-up. Keep entries concise.

## Entries

| Date | Change | Method / decision | Affected information | Follow-up |
| --- | --- | --- | --- | --- |
| 2026-10-03 | Modeled Ampure as a three-business group | PosiCharge is the focus; Power Designers Sibex is internal industrial portfolio; Automotive and Aftermarket EVSE is context. Basis: vault owner direction and Ampure acquisition release | [[Ampure]], [[Ampure Group Portfolio Context]] | Map shared teams |
| 2026-10-03 | Power Designers Sibex treated as internal, not competitor | Moved out of external cohorts with the move recorded in place; overlap kept visible in a dedicated map, all rows Unresolved | [[Power Designers]], [[PosiCharge Competitive and Partner Landscape]], [[Ampure Industrial Portfolio Overlap and Synergy Map]] | Classify overlap rows; re-scope older Charger and Monitor matrices |
| 2026-10-03 | EVSE boundary rule | EVSE offers are capability references, not comparators, unless the same customer job, industrial context and buying alternative are documented | [[Ampure Automotive and Aftermarket EVSE]], [[PosiCharge Business Scope and Portfolio]] | List transferable EVSE capabilities |
| 2026-10-03 | Group check and response paths for gaps | A PosiCharge-only absence is not an Ampure gap; choose build, reuse, transfer, partner or research, and record what was checked | [[PosiCharge Capability Gap Assessment]], [[PosiCharge Product Comparison Matrix]] | Apply to first gap entries |
| 2026-10-03 | Provisional ownership links to Ampure | Wrote subsidiaryOf for Power Designers (acquisition) and PosiCharge (brand; legal status open, C69), with ledger rows; no link for the EVSE unit because no relationship fits | [[Organizations/Business Relationship Ledger\|Business Relationship Ledger]] | Propose a business-unit relationship |
| 2026-10-03 | Conflicts found, not resolved | C32 Power Designers names now partly informed by the acquisition; framework notes from 0e0b952 lack template frontmatter. Both logged as backlog items, unchanged here | [[PosiCharge Opportunity Backlog]] | Resolve in later commits |
| 2026-10-03 | Added top-level folder navigation readmes | Reviewed content folders before editing; created missing indexes for Definitions and Downloads; enhanced existing indexes without changing system folders | Top-level content folders | Maintain links as key records evolve |
| 2026-10-03 | Established PosiCharge-centered business-analysis scope | Analyze PosiCharge as an Ampure business across offer spaces; compare product to product and customer job to customer job, not company to company | [[PosiCharge Business Scope and Portfolio]] | Normalize PosiCharge product records |
| 2026-10-03 | Established offer-scoped competitor/partner method | Organizations can be competitors, partners, or both depending on the defined offer and segment; vehicle OEMs are not competitors by default | [[PosiCharge Competitive and Partner Landscape]] | Populate classifications from evidence |
| 2026-10-03 | Established direct comparison protocol | Require shared customer job, operating context, named comparator offer, measurable criteria, and evidence before treating an offer as comparable | [[PosiCharge Product Comparison Matrix]] | Build first charger and BMID comparison cohorts |
| 2026-10-03 | Established gap-assessment method | Separate portfolio, capability, integration, commercial, positioning, and evidence gaps; preserve hypotheses until verified | [[PosiCharge Capability Gap Assessment]] | Convert validated findings into actions |
| 2026-10-03 | Created PosiCharge opportunity backlog | Track research, partnership, product, integration, positioning, and evidence work separately from committed roadmap work | [[PosiCharge Opportunity Backlog]] | Prioritize and assign items as evidence develops |

## Methodology summary

- Evidence before assertion: link claims to source records whenever possible.
- Offer-scoped relationships: do not use a permanent global label for an organization.
- Product-level comparison: compare substitutable offers in the same customer context.
- Segmented decisions: retain differences among MHE, eGSE, chemistry, duty cycle, environment, and deployment model.
- Conflicts are data: document contradictions, uncertainty, and unknowns rather than silently resolving them.
- Group before gap: check Ampure-internal capability before declaring an external gap; internal businesses are never external competitors.
- Reversible work first: prioritize evidence, taxonomy, and comparison clarity before irreversible product or market commitments.

## Maintenance

Append new entries in reverse chronological order. Link decisions to the relevant notes and backlog items. If a prior decision changes, add a new entry explaining why; do not erase the original decision history.
