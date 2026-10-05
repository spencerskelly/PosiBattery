Your intuition is correct: **a DC bus between the AC-DC and DC-DC stages is exactly what enables bidirectional power flow** in a modular, controllable way. The key insight is that each stage can be made individually bidirectional, and the DC bus acts as the energy exchange node. When the 96 VDC load (e.g., a battery) discharges, the DC-DC stage runs in reverse, pushing energy onto the DC bus. The AC-DC stage then converts that DC bus energy back to 480 VAC grid power. This is the standard architecture used in commercial bidirectional power supplies, energy storage systems, and vehicle-to-grid (V2G) applications.

## Why the DC Bus Architecture Works

The DC bus (often 700–800 VDC for a 480 VAC system) serves as a **common high-voltage DC link** that both converters share. In forward mode (AC to DC load), the AC-DC stage rectifies 480 VAC to the bus, and the DC-DC stage steps the bus down to 96 VDC. In reverse mode (DC load to AC), the DC-DC stage operates as a boost converter, stepping 96 VDC up to the DC bus voltage. The AC-DC stage then operates as an inverter, converting the DC bus back to 480 VAC with controlled power factor and low harmonic distortion. This is exactly how commercial bidirectional supplies like the MEAN WELL BIC-5K-96 work, achieving 93% conversion efficiency in both directions with a 1 ms transition time between modes.

## Stage-by-Stage Bidirectional Topologies

### AC-DC Stage (480 VAC ↔ DC Bus)

The **Vienna rectifier** is the gold standard for unidirectional three-phase PFC, but it is inherently **unidirectional**—it only allows power flow from AC to DC. For bidirectional operation, you must replace it with a **bidirectional active front end (AFE)**. The most common topologies are:

| Topology | Key Characteristics | Typical Efficiency |
|---|---|---|
| **Two-level AFE** (six-switch) | Simple, mature, but higher switching losses | 96–97% |
| **Three-level T-type** | Lower voltage stress, better harmonic performance | 98.6% peak (TI reference design) |
| **Three-level ANPC** (Active Neutral-Point-Clamped) | Best efficiency and power density for 480 VAC | 98%+ (Wolfspeed 25 kW design) |

Wolfspeed's 25 kW bidirectional AFE reference design handles **480 VAC input, 800 VDC output**, and uses SiC MOSFETs to achieve high switching frequencies with smaller magnetics. TI's 11 kW bidirectional three-level T-type design achieves **98.6% peak efficiency** and handles 600–900 V on the DC bus with 400 VAC grid input.

### DC-DC Stage (DC Bus ↔ 96 VDC)

For the isolated DC-DC stage, two topologies dominate bidirectional designs:

**Dual Active Bridge (DAB)** is the most natural choice for bidirectional operation. It consists of two full bridges (one on the DC bus side, one on the 96 V side) coupled through a high-frequency transformer and an energy transfer inductor. Power flow direction and magnitude are controlled by the phase shift between the two bridges. DAB converters routinely achieve **95–98% efficiency** and are widely used in V2G and battery energy storage systems. TI's 10 kW DAB reference design for DC microgrids supports 700–800 V bus voltage and achieves 2.25 kW/L power density using SiC MOSFETs.

**CLLC resonant converter** is an alternative that achieves soft switching (ZVS and ZCS) in both directions. It uses a symmetrical resonant tank that allows identical operation in forward and reverse modes. CLLC is particularly attractive when the voltage ratio is not extreme—RECOM notes that CLLC is ideal when "battery and PFC bus voltages are similar". For a 750 V bus to 96 V output, the ratio is roughly 7.8:1, which is well within CLLC's capability, though the resonant tank design must be optimized for both directions.

**Phase-Shifted Full-Bridge (PSFB) with active secondary** is a third option. Replacing the secondary diode bridge with an active full bridge creates a bidirectional DAB-like structure. PSFB is preferred for substantial voltage gaps, such as 48 V or 800 V systems.

## Practical Implementation Considerations

**Galvanic isolation** is provided by the high-frequency transformer in the DC-DC stage. This is essential for safety and for breaking ground loops between the 480 VAC grid and the 96 VDC load.

**Efficiency in both directions** is not automatically symmetrical. Conduction losses are similar, but switching losses and gate drive losses may differ. Commercial bidirectional supplies typically specify efficiency separately for each direction—for example, 92% AC-to-DC and 91.5% DC-to-AC at 480 VAC.

**Control complexity** increases significantly with bidirectionality. The controller must manage mode transitions (often within milliseconds), maintain power factor in both directions, and handle seamless handover between charging and discharging.

**Protection** must be designed for both directions: overvoltage on the DC bus during reverse operation, overcurrent on the AC side during inversion, and anti-islanding protection if the system is grid-tied.

## Recommended Architecture for 480 VAC ↔ 96 VDC Bidirectional

For a system in the 5–25 kW range, the optimal architecture is:

1. **AC-DC stage:** Three-level T-type or ANPC active front end with SiC MOSFETs, producing a regulated 750–800 VDC bus.
2. **DC bus:** 750–800 VDC with adequate capacitance to buffer bidirectional power transients.
3. **DC-DC stage:** DAB or CLLC with synchronous rectification on the 96 V side and SiC devices on the bus side.
4. **Control:** Digital controller (DSP or FPGA) managing bidirectional power flow, mode transitions, and protection.

This architecture is commercially validated. The MEAN WELL BIC-5K-96 is a 5 kW bidirectional unit with 96 VDC output and 93% efficiency in both directions. RECOM offers bidirectional AC/DC supplies from 2 kW to 11 kW with three-phase 340–480 VAC input and DC outputs up to 300 V.

If you can share the **target power level** and whether the 96 VDC side is a **battery with a specific charge/discharge profile**, I can narrow the topology choice (DAB vs. CLLC) and recommend specific SiC/GaN devices for each stage.