For converting **480 VAC (three-phase) to 96 VDC**, the most efficient and standard approach is a **two-stage architecture**: a three-phase Power Factor Correction (PFC) rectifier followed by an isolated DC-DC converter. This is the topology used in commercial products like the MEAN WELL BIC-5K-96, which achieves up to **93.5% efficiency** for this exact conversion.

## Recommended Two-Stage Architecture

| Stage | Function | Typical Efficiency | Best Topology |
|---|---|---|---|
| **Stage 1: AC-DC** | Rectify 480 VAC to a regulated high-voltage DC bus (e.g., 700–800 VDC) with power factor correction | 97–98% | Vienna Rectifier |
| **Stage 2: DC-DC** | Isolate and step down the DC bus to 96 VDC | 95–97% | LLC Resonant or Phase-Shifted Full-Bridge |
| **Combined** | 480 VAC → 96 VDC | **92–95%** | — |

The key reason for splitting the conversion is that **galvanic isolation** is almost always required for safety and for breaking ground loops between the AC mains and the 96 VDC load. The two-stage approach lets each stage operate at its optimal switching frequency and voltage level.

---

## Stage 1: Three-Phase PFC Rectifier

The Vienna Rectifier is the **gold-standard topology** for three-phase PFC at this power level. It is a unidirectional, three-level boost-type converter that uses only three active switches and a diode bridge, significantly reducing conduction losses compared to a six-switch boost converter.

- **Efficiency**: A 10 kW Vienna Rectifier with 480 VAC input has demonstrated **98% system efficiency** experimentally. For lower power levels (3–5 kW), efficiencies above **95% at 50% load** are typical.
- **Key advantages**: True three-wire input (no neutral needed), low input current distortion (THD < 5%), and a regulated DC bus that can be set to ~700–800 VDC.
- **Device choice**: For 480 VAC input, the DC bus voltage must exceed the peak line-to-line voltage (√2 × 480 ≈ 679 V). Using **SiC MOSFETs** or **GaN HEMTs** in the Vienna rectifier reduces switching losses and allows higher switching frequencies, shrinking the boost inductors.

---

## Stage 2: Isolated DC-DC Converter

With a ~750 VDC bus, you need to step down to 96 VDC with isolation. Two topologies dominate:

### Option A: LLC Resonant Converter (Highest Efficiency)

The LLC converter achieves **zero-voltage switching (ZVS)** on the primary side and **zero-current switching (ZCS)** on the secondary rectifiers, virtually eliminating switching losses. A 960 W LLC design for a 96 VDC output has demonstrated **96.1% average efficiency**.

- **Best for**: Fixed-ratio or narrow-output-voltage applications, and where the DC bus voltage is well-regulated.
- **Design note**: The LLC gain is sensitive to the resonant tank design. With a 750 VDC input and 96 VDC output, the transformer turns ratio is roughly 7:1.
- **Secondary rectification**: Use **synchronous rectification** with low-Rds(on) MOSFETs instead of Schottky diodes to eliminate forward-drop losses. This is critical at 96 VDC output where currents are high (e.g., ~10 A for 1 kW, ~50 A for 5 kW).

### Option B: Phase-Shifted Full-Bridge (Wider Input Range)

The phase-shifted full-bridge (PSFB) is more robust to input voltage variations and is widely used in medium-to-high power applications. It also achieves ZVS on the primary switches, though the ZVS range is narrower than LLC.

- **Best for**: Applications where the DC bus may sag or where you need a wide output voltage range (e.g., battery charging from 80–100 VDC).
- **Design note**: The PSFB has a freewheeling interval that causes circulating current losses. Modified PSFB topologies that reduce this interval can improve efficiency. A 2.2 kW vehicle charger using PSFB with soft-switching control targets 96 VDC output.

---

## Alternative Approaches

### Single-Stage (Non-Isolated)
A three-phase rectifier followed directly by a **buck converter** can step 480 VAC down to 96 VDC without isolation. This is simpler and cheaper, but it lacks galvanic isolation and the DC bus is unregulated, so the buck converter must handle a wide input range (peak bus voltage ~680 V down to near zero during AC zero-crossings). Efficiency is typically **lower** (85–90%) because the buck switch must block the full bus voltage.

### Multi-Phase Interleaved Buck
For very high currents at 96 VDC (e.g., >100 A), an **interleaved multiphase buck** on the secondary side reduces ripple and spreads thermal load. This is common in 48 V data-center power supplies and can be adapted for 96 VDC.

### Matrix Converter / Dual Active Bridge
A **four-leg matrix dual active bridge** can convert AC directly to DC with isolation in a single stage, but the control complexity is very high and efficiency is not yet competitive with the two-stage approach for this voltage ratio.

---

## Comparison Summary

| Approach | Efficiency | Isolation | Complexity | Best Use Case |
|---|---|---|---|---|
| Vienna + LLC | **92–95%** | Yes | Medium | Most efficient, fixed output |
| Vienna + PSFB | **90–93%** | Yes | Medium | Wide input/output range |
| 3-phase rectifier + buck | 85–90% | No | Low | Cost-sensitive, non-isolated |
| Matrix DAB | ~88–92% | Yes | Very High | Research / bidirectional |

---

## Practical Design Tips

1. **Use SiC or GaN devices** in the Vienna rectifier and primary side of the DC-DC stage. The 750 VDC bus exceeds the practical limit of standard silicon MOSFETs for high-frequency switching.
2. **Synchronous rectification is mandatory** on the 96 VDC secondary. At 96 V, a Schottky diode drop of 0.5 V represents ~0.5% loss at full load, which is significant.
3. **Optimize the transformer** for the LLC or PSFB. Use litz wire and a low-loss ferrite core (e.g., PC95 or 3C95). The turns ratio is critical for achieving ZVS across the load range.
4. **Consider phase-shedding** at light load. Efficiency at 10% load is often much lower than at 50% load. Disabling one of multiple interleaved phases at light load keeps the remaining phases in their high-efficiency region.
5. **Thermal management**: At 95% efficiency and 5 kW output, you still dissipate ~260 W. Plan for forced-air cooling or a heatsink with adequate thermal resistance.

If you can share the **power level**, **whether bidirectional operation is needed**, and **whether the 96 VDC load is a battery or a resistive/electronic load**, I can narrow down the topology and device recommendations further.