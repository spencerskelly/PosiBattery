# Power Conversion Research

## Purpose

This folder contains migrated power-conversion research covering AC–DC, DC–DC, DC–AC, bidirectional conversion, wide-turndown charger architectures, semiconductor choices, light-load efficiency, and thermal/control trade-offs.

These notes are **research reasoning**, not approved product architecture or verified design requirements.

## Current notes

- [[Chat 1]] — general power-conversion primer covering conversion paths, loss mechanisms, topologies, efficiency techniques, and trade-offs.
- [[Chat 2]] — research hypothesis for 480 VAC three-phase to 96 VDC using a two-stage PFC plus isolated DC–DC architecture.
- [[Chat 3]] — bidirectional 480 VAC ↔ 96 VDC research hypothesis using an active front end plus bidirectional isolated DC–DC stage.
- [[Chat 4]] — wide-turndown 50 kW to 500 W research hypothesis emphasizing modularity, phase shedding, DAB/CLLC trade-offs, and light-load efficiency.

## Evidence status

The notes contain no embedded authoritative source links. Specific efficiency values, commercial product examples, topology rankings, device recommendations, control claims, thermal recommendations, and architecture conclusions should therefore be treated as **unverified hypotheses** until checked against primary sources and product requirements.

## Navigation

The parent [[README_Research|Research]] recursive view already includes this folder, so no additional Base or Canvas is created here.

## Maintenance

Preserve the reasoning, but do not promote it directly into Product Architecture, Designs, Requirements, Interfaces, or product commitments. Later engineering work should reconcile these hypotheses against actual charger voltage range, power level, isolation, safety, bidirectionality, thermal, regulatory, and charge-profile constraints.
