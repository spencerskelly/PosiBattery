---
type: Info
subtype:
id: INFO-00135
uid: 20261002195812527skellyspencer
status: Draft
tags:
  - performance-metric
  - monitor
  - comparison
describes:
  - "[[Battery Monitoring and Identification Device]]"
  - "[[Log Battery Events and Usage]]"
  - "[[Non-Volatile Event Memory]]"
---

# Metric - Data Storage

## Definition

Data Storage: Logged data capacity.

## Notes

- **Code and class:** MM07; monitor metric. Unit or format: events, bytes or days; interval.
- **Comparability rule:** Events, bytes and days are not interchangeable; record the logging interval where stated.
- **Direction:** larger is better.
- **Values on file (as stated in each product note; n/s means not stated):**
  - [[AMETEK Prestolite Power BID]]: non-volatile memory; size n/s
  - [[EnerSys Wi-iQ]]: 8,000 events (C42)
  - [[HOPPECKE trak collect]]: 8 MB (4 MB ring buffer); 10 s interval; 30-day ring buffer
  - [[Philadelphia Scientific eGO!pro]]: minute-by-minute logs and cycle data
  - [[PosiCharge PosiGuard]]: 16 MB
  - [[Power Designers PowerTrac 3]]: 10,000 events (sheet; equals DT3, C47); earlier note: 10,000 events
  - [[Power Designers PowerTrac DT3]]: 10,000 events
- **Source rule:** the product note holds the source URL for each value; this note copies the value for comparison. If they differ, the product note wins and this note is fixed.
- **Gaps and to-do:** 6 product(s) have a value; document-based values to be added as documents are supplied.

## Aliases

- MM07
- Data Storage


## Former ids
