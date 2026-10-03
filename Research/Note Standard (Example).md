---
type: Info
subtype:
id: INFO-00128
uid: 20261002194458538skellyspencer
status: Draft
tags:
  - standard
  - example
  - conventions
describes:
  - "[[Battery-Connected Product]]"
  - "[[Industrial Traction Battery]]"
---

# Note Standard (Example)

## Definition

The working layout for product and organization notes, with one exemplar for each kind, so later notes follow the same pattern.

## Notes

- **Layout inside Notes (no extra headings; bold-labeled bullets and one table):** Identity; Specifications as stated (table with parameter and value, source named below it); Features (functions and designs, each with its citation line); Related products and how they differ; Differences and conflicts; Gaps and to-do; then 'Source history' holding earlier bullets unchanged.
- **Exemplars:** monitor [[EnerSys Wi-iQ]]; charger [[Crown V-HFM3 Charger]]; battery [[Stryten M-Series T330 Battery]]; organization [[EnerSys]]; also a full data-sheet example, [[HOPPECKE trak collect]].
- **Rules decided with the owner:** (1) Battery Objects have subtype electrical: electrical means anything electricity passes through. (2) A product may link to several products; when it does, the body says how the linked products differ, and if no difference is known the note says so. (3) If related products are not found yet, the link stays blank (listed under gaps and to-do). (4) Light-duty chargers stay in scope and are on the to-do list. (5) A fact needs a URL; a user statement is marked as such. (6) Documents that cannot be fetched are listed in the backlog with links for the owner to download.
- **Spec rows:** value as the source states it, units unchanged, 'not stated' where the document is silent, conflicts written beside the row and logged in the conflicts register.
- **Spec parameter names (added with the metric dictionary):** spec table rows use the metric names in [[README_Performance Metrics]] where one exists, so products compare row for row; new parameters get a metric note first. Existing product tables are aligned as documents are read (to-do).
- **Documents:** the owner downloads files the fetch tool cannot open and adds them to the chat; if a file is mentioned but absent, the note says so and nothing is invented from it.
- **Citation rule (round 12):** cite a direct file address or a specific product page, never a company home or landing page; home or landing addresses live only in the Document Wishlist as placeholders. Checked by [[Link Audit]] and the check-links tool.
- **Owner decisions, round 14:** forklifts and other powered trucks use subtype electrical, including internal combustion trucks (they have electrical systems); the survey stays with electric trucks but records features of internal combustion and fuel-cell trucks that electric trucks may lack; truck-side devices matter more than lifting performance.
- **Re-use and folders (owner, round 15):** follow [[Note Reuse Audit]]: one note per thing, owners as relationships not folders, product folders by type then category under `Products`, merged notes keep retired ids in Former ids.

## Aliases

- Product note example
- Note layout example


## Former ids
