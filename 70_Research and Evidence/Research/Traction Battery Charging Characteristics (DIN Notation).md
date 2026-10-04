---
type: Info
subtype:
id: INFO-00264
uid: 20261003201704431skellyspencer
status: Draft
tags:
  - charge-profile
  - reference
  - review
describes:
  - "[[Industrial Traction Battery]]"
---

# Traction Battery Charging Characteristics (DIN Notation)

## Definition

What the DIN charging characteristic codes (W, Wa, W0Wa, Wsa, IUIa and others) mean for traction battery chargers, with the tolerances, charge factors and assignment table that the ZVEI leaflet gives.

## Notes

- **Source:** ZVEI information leaflet 'Charger assignments for traction batteries in vented (PzS) and valve regulated (PzV) design' (Working Group Industrial Batteries, edition April 2004), read in full. Tier: T2 with a note: an industry association leaflet, independent of one maker, not a manufacturer sheet. <https://www.zvei.org/fileadmin/user_upload/Verband/Fachverbaende/Batterien/Merkblaetter/Industriebatterien/11_e_Charger_Assignments_for_Traction_Batteries_2004-04.pdf>
- **Notation (DIN 41772 as the leaflet describes it):** W is a taper characteristic (current falls as voltage rises), U constant voltage, I constant current; 0 (zero) marks automatic switch-over between regimes and a marks automatic shut-off. Examples the leaflet lists: W-types W, Wa, W0Wa, WU, WUWa; U; I-types I, Ia, I0Ia, IU, IUW, IUIa.
- **Tolerances:** for I characteristics under DIN 41773, 2 percent on current and 1 percent on voltage; for W characteristics under DIN 41774, 0.05 V per cell.
- **Reference conditions:** all leaflet diagrams are for a battery at its nominal 30 C and 80 percent depth of discharge; the end-of-charge voltage of 2.65 V per cell is the DIN reference and real applications use higher or lower values with battery technology, temperature and service.
- **Gassing voltage and IUIa:** for vented PzS batteries the W0Wa and IUIa regimes allow a higher nominal current until the gassing voltage of 2.4 V per cell (at 30 C) is reached than the Wa regime; for valve-regulated gel PzV batteries only regulated IUIa chargers may be used, the last phase time is set from the main charging time and a charge-factor control is not permitted because of recombination; the leaflet's PzV diagram shows a main current of 12 to 14 A per 100 Ah and a final current of 1.0 to 1.4 A per 100 Ah.
- **Charging factor (CF):** ampere-hours charged divided by ampere-hours discharged; standard 1.2 for vented PzS (example: 80 percent of a 500 Ah battery is 400 Ah, times 1.2 gives 480 Ah), about 1.07 for batteries with air mix, 1.17 for the steeper Wsa regime and 1.1 for gel PzV when estimating energy use; matching tolerances are CF 0.02, charging time 0.5 h and depth of discharge 5 percent.
- **Wsa:** a special steeper taper for PzS batteries with higher acid density and lower antimony grids, charged in 8 to 14 hours at 30 C from 80 percent depth of discharge, with a timer safety cut-off if 2.4 V per cell is not reached within 8 h at more than 16 A per 100 Ah; it reduces the dependence of current on mains fluctuation by 20 percent at 2.4 V per cell and 30 percent at 2.65 V per cell.
- **Depth of discharge for PzV:** an optimized life is reached at 60 percent at most; 80 percent is possible according to the maker.
- **Opportunity charging:** partial charges to prolong operation; they cannot replace regular full charges.
- **Wrong charger assignment causes:** deviating charging times, excessive battery temperature, excessive gassing, shedding of positive active mass, high water consumption, increased corrosion, insufficient charges and overcharge.

**DIN 41774 curve shape (from a patent's description of the standard, T5, to be confirmed against the standard)**

A US patent describes DIN 41774 as requiring the charger to supply I5 at 2 V per cell, with the current falling to 50 percent of I5 at 2.4 V per cell (the gassing level) and to 25 percent of I5 at 2.65 V per cell; in an IUW process the characteristic changes to a W curve when the current has fallen to 20 percent of I5, crossing the voltage axis at 2.7 V per cell, and in an IUI charger it returns to constant current at 20 percent of I5. Source: <https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4833391> (a patent describes prior art, not product availability).

**Charger-battery assignment (ZVEI appendix, selected rows)**

Charging factor 1.2 (1.17 for Wsa), battery at 30 C, 80 percent depth of discharge, charger correctly adapted to mains voltage, tolerance 0.5 h. Battery capacity in Ah (C5) a charger of the nominal current can serve in the stated time.

| Charger nominal current (A) | Wa 11 h | Wa 14 h | Wsa 8 h | Wsa 9 h | W0Wa 8 h | W0Wa 9 h | IUIa 8 h | IUIa 9 h |
|---|---|---|---|---|---|---|---|---|
| 15 | 90 | 125 | 83 | 93 | 54 | 68 | 75 | 94 |
| 30 | 190 | 250 | 167 | 185 | 107 | 136 | 150 | 188 |
| 50 | 310 | 415 | 278 | 309 | 179 | 227 | 250 | 313 |
| 80 | 500 | 670 | 444 | 494 | 288 | 364 | 400 | 500 |
| 100 | 625 | 830 | 556 | 617 | 357 | 455 | 500 | 625 |
| 150 | 930 | 1,250 | 833 | 926 | 536 | 682 | 750 | 938 |
| 200 | - | - | 1,111 | 1,235 | 714 | 909 | 1,000 | 1,250 |
| 240 | - | - | 1,333 | 1,481 | 857 | 1,091 | 1,200 | 1,500 |

Worked example in the leaflet: a Wa charge of an 800 Ah PzS battery without air mix (CF 1.2) at 80 percent depth of discharge in at most 12 hours needs 14 A per 100 Ah, so a charger of 8 times 14 = 112 A.
- **Standards named by the leaflet:** DIN EN 50272-3 (replacing DIN VDE 0510-3) and DIN EN 60146-1 and -2 for chargers; EN 50272-3 was superseded by EN 62485-3:2014, whose Table 1 gives the maximum final charging current in A per 100 Ah during normal charging (title seen in the contents; values are in the paid standard): <https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec62485-3{ed2.0}b.pdf>.

## Aliases

- DIN charging characteristics
- IUIa
- W0Wa

## Former ids
