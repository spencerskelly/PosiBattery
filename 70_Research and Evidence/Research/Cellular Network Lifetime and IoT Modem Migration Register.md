---
type: Info
subtype:
id: INFO-00972
uid: 20261017183000000skellyspencer
status: Draft
tags:
  - research
  - cellular
  - network-sunset
  - connectivity
  - lifecycle
  - north-america
describes:
  - "[[PosiCharge PosiLink]]"
  - "[[PosiCharge SkyLink]]"
  - "[[PosiCharge Battery Rx]]"
  - "[[PosiCharge E-Meter]]"
  - "[[PosiCharge PosiNet]]"
  - "[[Cellular Communication Interface]]"
describedBy:
  - "[[Document - MCA Cellular Network Sunset Notices Page (2023-02-10, modified 2024-02-13)]]"
  - "[[Document - Digi 2G 3G 4G LTE Network Shutdown Updates (2025-12-12)]]"
  - "[[Document - The Mobile Report T-Mobile to Begin LTE Phase-Out (2025-10-06)]]"
  - "[[Document - RCR Wireless AT&T Quits NB-IoT (2024-11-20)]]"
  - "[[Document - AT&T Business 3G Shutdown FAQ (undated, 2022)]]"
  - "[[Document - 5Gstore 4G Shutdown Timeline (2025-06-25)]]"
---

# Cellular Network Lifetime and IoT Modem Migration Register

## Definition

Register of what is documented about cellular network shutdowns that affect connected battery and charger products, which PosiCharge and OEM-branded devices use cellular, and what is not known. It checks the 2026-10-04 backlog row on cellular network lifetime and modem migration ([[Knowledge Base Backlog]]). Disagreements are numbered C328 to C331 in [[Battery Product Landscape Conflicts and Open Questions]]; new directions are IB-292 to IB-297 in [[Investigation Backlog]].

## Notes

- **Reading rule:** every source was read through a summarizing fetch tool (second-hand). Most are vendor blogs (T4). No carrier network-evolution page was readable. "Analyst reasoning" marks a conclusion no source states. Status is as of 2026-10-17.
- **Scope:** US carriers first; Canada and Europe only as listed in one vendor blog. No PosiCharge internal data exists in the vault (KB-010).

### Bottom line (analyst summary)

1. **The backlog's AT&T line is not supported.** "AT&T has committed to LTE only through the end of 2027" comes from one vendor page with no cited source (2023, modified 2024). AT&T's own 3G FAQ says it has "not currently announced a turn down date for our 4G LTE network"; a December 2025 vendor blog gives no AT&T LTE date; a June 2025 retailer blog says no US carrier has announced a 4G shutdown (C328). I found no later AT&T text confirming 2027. Treat 2027 as unconfirmed, not as a deadline.
2. **The backlog targets the wrong products.** [[PosiCharge PosiLink]] and [[PosiCharge SkyLink]] are cloud platforms in the vault. The cellular hardware named in vault sources is the battery-side devices: [[PosiCharge Battery Rx]] (optional cellular), [[PosiCharge E-Meter]] (cellular data capture, up to 4 weeks recorded), [[PosiCharge PosiNet]] (works with the cellular Battery Rx), and OEM-branded monitors (Hyster Battery Tracker, Yale Battery Vision) that use "existing wireless networks" (Hyster flyer, 2024) or cellular (2016 article). The vault's [[Cellular Communication Interface]] design also lists the PosiCharge High Voltage Power Station (AC) charger, the Philadelphia Scientific eGO!gateway and the OEM monitors as having cellular. Whether SkyLink-connected chargers use a cellular modem is not stated.
3. **No source names the cellular technology in any of these devices** (generation, module, carrier or plan), so the vault cannot say whether any unit is exposed (C329). The 3G shutdowns are already past (AT&T 2022, Verizon end of 2022, T-Mobile July 2022), so any 3G-only unit would already be dead; analyst reasoning: the live questions are LTE-only service life, NB-IoT, and Canada.
4. **Documented real dates that matter:** AT&T is retiring NB-IoT, as early as Q1 2025, moving customers to LTE-M (T-Mobile and Verizon say no plans to shut their NB-IoT networks); Rogers began retiring 3G on 2025-08-07 and Telus's Manitoba 3G ends 2025-12-31 and 2026-03-31 (one vendor blog); Vodafone Germany ends 2G for most users in September 2028 with some critical IoT until end of 2030.
5. **T-Mobile LTE is the one flagged risk, and it is a leak.** A blog describing a leaked document says most T-Mobile LTE goes around 2028, business LTE-only activations need exceptions from January 2026, and a 5 MHz LTE channel is kept until at least 2035 for IoT. Unconfirmed by T-Mobile (C331).
6. **Sources disagree on AT&T's 3G date:** MCA says 2021-03-01; Digi says February 2022; AT&T's FAQ says "not until 2022" (C330). Immaterial now, but shows the MCA table is unreliable.

### What is known by product (vault sources)

| Product | Cellular stated? | Technology stated? | Source |
|---|---|---|---|
| PosiCharge Battery Rx | Optional cellular connectivity and data services | No | [[PosiCharge Battery Rx]]; PosiCharge Battery Rx page (cellular text only) |
| PosiCharge E-Meter | Yes, cellular data capture | No | [[PosiCharge E-Meter]] |
| PosiCharge PosiNet | Works with cellular Battery Rx | No | [[PosiCharge PosiNet]] |
| Hyster Battery Tracker / Yale Battery Vision | Yes ("uses cellular communications", 2016); "existing wireless networks" (flyer, 2024) | No | [[Hyster Battery Tracker]] |
| PosiCharge High Voltage Power Station (AC); Philadelphia Scientific eGO!gateway | Listed as designs of the cellular interface in the vault | No | [[Cellular Communication Interface]] |
| PosiCharge PosiLink, SkyLink | Cloud platforms; no modem stated | No | [[PosiCharge PosiLink]], [[PosiCharge SkyLink]] |

### Hypotheses (analyst reasoning, untested)

- **CH1:** devices designed in 2016 to 2019 may carry LTE Cat 1 or older modules whose carrier certification could lapse before the hardware wears out. Test: IB-292 (needs PosiCharge hardware data).
- **CH2:** the practical risk is not network shutdown but carrier plan and certification rules (new NB-IoT certification ended; LTE-only activation limits). Test: IB-294, IB-295.
- **CH3:** over-the-air firmware is the cheapest migration path where it exists (SkyLink advertises OTA for chargers). Test: IB-292.

### Question for the owner

Which PosiCharge devices contain a cellular modem, and which module and carrier? This is internal data (KB-010) and decides whether this topic is a roadmap item or a non-issue.

## Open questions

- Is the AT&T "through 2027" statement real, and where was it published (IB-294)?
- Official T-Mobile and Verizon statements on LTE and LTE-M lifetimes (IB-293, IB-294).
- Canada and Europe sales: do those markets matter (IB-296, IB-297)?

## Sources

Listed in `describedBy`. Lead pages not readable here: PosiCharge Battery Rx PDF (robots-blocked for the fetch tool).

## Aliases

- Cellular Sunset Register

## Former ids
