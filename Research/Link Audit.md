---
type: Info
subtype:
id: INFO-00179
uid: 20261002214410043skellyspencer
status: Draft
tags:
  - research
  - links
  - quality
describes:
  - "[[Battery-Connected Product]]"
---

# Link Audit

## Definition

Audit of web addresses in the vault: which are direct file downloads, which are pages, which are home or landing pages, and which are known bad.

## Notes

- **What this audit can and cannot do:** it classifies every address by its form (file, page, home or landing). It cannot test whether an address is alive: the build environment can only fetch addresses it has just seen in a search result. The owner can run `99_System/09_Tools/check-links.py` locally to test every address and write a report.
- **Citation policy from now on:** a spec value or fact cites a direct file address or a specific product page, never a company home page. A home or landing address is allowed only in the Document Wishlist as a placeholder, marked as such.
- **Pattern findings:** (1) Exide 'document/' addresses fail: the US one returned 404 and the Italian one redirected to the Exide home page, while files under 'sites/default/files' work. (2) Reseller-hosted PDFs (Lester via RJ Batt, Delta-Q via SimPower) work but are copies, not the maker's address. (3) Industry-association member sites (og.mhi.org) host many sheets under numeric names. (4) The Raymond iBATTERY page is on a test host. (5) Product pages that use '?p=' numbers may change.

| Class | Distinct URLs in model notes |
|---|---|
| file | 44 |
| home-or-landing | 8 |
| page | 180 |

**Known or suspected bad addresses**

| Address | Problem | Used in |
|---|---|---|
| <https://fronius.com/~/downloads/Perfect%20Charging/Flyer/PC_FLY_Selectiva_4.0_96V-120V_EN_fin-MRM_.pdf> | owner flagged: bad link; replaced by a working brochure address (see Document Wishlist) | [[Document Wishlist]], [[Fronius Selectiva 4.0]], [[Investigation Backlog]], [[Manage Chargers Remotely]] |
| <https://exidegroup.com/us/en/document/solition-light-traction-battery-leaflet> | owner flagged bad; returns 404 when fetched; the same /document/ address pattern for other regions redirected to the Exide home page | [[Business Relationship Ledger]], [[Charge Lithium-Ion Battery]], [[Charge Under BMS Control]], [[Document Wishlist]], [[Exide Motion+ Lithium Charger]], [[Exide Solition Light Traction Battery]], [[Exide Technologies]], [[Integrated Battery Management System]] ... |
| <https://www.phlsci.com/media/vbohieng/egopro-ssh-ps-us-en-doc0642.pdf> | owner flagged: bad link | [[Alert on Abnormal Condition]], [[Audible Alarm]], [[Document Wishlist]], [[Hall-Effect Current Sensing]], [[Light-Triggered Data Upload]], [[Measure Battery Current]], [[Philadelphia Scientific eGO!pro]], [[Split-Core Current Sensor]] ... |
| <https://www.phlsci.com/media/151762/ego-mini-egou-ps-ssh-doc0184-eng.pdf> | owner flagged: bad link | [[Alert on Abnormal Condition]], [[Audible Alarm]], [[Document Wishlist]], [[Export Battery Data to PC]], [[Indicate Battery Status Locally]], [[Local LED Indicator]], [[Log Battery Events and Usage]], [[Measure Battery Temperature]] ... |
| <https://exidegroup.com/it/en/document/gnb-pro-20-battery-protection-brochure> | returned 404 when fetched (round 3) | [[Accumulate Amp-Hours]], [[Battery Product Landscape Conflicts and Open Questions]], [[Exide Motion+ EasyMonitor]], [[Measure Battery Temperature]], [[Sense Electrolyte Level]], [[Unidentified Products Review]] |
| <https://www.exidegroup.com/en/document/easy-monitor-leaflet> | same /document/ pattern as the Exide addresses that 404 or redirect to the home page; unverified | [[Accumulate Amp-Hours]], [[Alert on Abnormal Condition]], [[BMID Competitor Landscape]], [[Monitor Comparison Matrix]], [[Detect Voltage Imbalance]], [[Document Wishlist]], [[Estimate State of Charge]], [[Exide Motion+ EasyMonitor]] ... |
| <https://exidegroup.com/en/document/tensor-xgel-brochure> | same /document/ pattern as the Exide addresses that 404 or redirect to the home page; unverified | [[Battery Product Landscape Conflicts and Open Questions]], [[Business Relationship Ledger]], [[Document Wishlist]], [[Exide TENSOR xGEL Battery]], [[Exide Technologies]], [[GNB Industrial Power]], [[Gel Electrolyte]], [[Industrial Battery Supply and Private-Label Relationships]] ... |
| <https://test-iwarehouseknows.raymondcorp.com/products/battery-monitoring> | test subdomain; may not be production (C25) | [[Alert on Abnormal Condition]], [[BMID Competitor Landscape]], [[Battery Product Landscape Conflicts and Open Questions]], [[Cloud Portal Integration]], [[Estimate State of Health]], [[Raymond iBattery]], [[Upload Battery Data to Cloud Portal]] |
| <https://shop.crown.com/crown/en/Batteries-and-Chargers/Battery-and-Charger-Parts-and-Accessories/Battery-and-Charger-Accessories//p/396525-BTM> | could not be re-fetched in round 9 (not in the fetch tool's allowed set); unverified | [[Acid-Resistant Sealed Housing]], [[BMID Competitor Landscape]], [[Monitor Comparison Matrix]], [[Battery Monitoring and Identification Device]], [[Battery Product Landscape Conflicts and Open Questions]], [[Bluetooth Class 1 Interface]], [[Configure Device from Mobile App or PC]], [[Crown V-Force BMID]] ... |

**Home or landing addresses cited in notes (should be replaced by a page or file address)**

| Home or landing address | Used in |
|---|---|
| <https://delta-q.com/> | [[Document Wishlist]] |
| <https://eastpennmanufacturing.com/divisions/motive-power/> | [[Document Wishlist]], [[East Penn Manufacturing]] |
| <https://hoppecke.com/en-us/applications/trak> | [[HOPPECKE]], [[HOPPECKE trak power Lithium Battery]], [[Integrated Battery Management System]], [[Investigation Backlog]] |
| <https://www.crown.com/en-us/batteries-and-chargers> | [[Document Wishlist]] |
| <https://www.energy-xprt.com/companies/green-cubes-technology-131836/products> | [[Green Cubes SAFEFlex Battery]], [[Green Cubes Technology]], [[Products Offered or Promoted with Industrial Batteries]] |
| <https://www.fluxpower.com/> | [[Document Wishlist]] |
| <https://www.prestolitepower.com/products> | [[Document Wishlist]] |
| <https://www.stryten.com/> | [[Document Wishlist]], [[Unidentified Products Review]] |

## Aliases

- Link check


## Former ids
