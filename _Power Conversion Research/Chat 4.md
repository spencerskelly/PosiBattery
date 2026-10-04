A 50 kW to 500 W range (a 100:1 turndown) is the defining challenge for your charger. The 50 kW peak demands a topology with low conduction losses, but the 500 W equalization (EQ) phase will be dominated by switching and core losses, potentially killing efficiency where the charger spends most of its time.

The most effective strategy is a **modular, interleaved architecture with phase shedding** on both the AC-DC and DC-DC stages. This allows the system to reconfigure itself—using all modules for high power and shedding most of them at light load—to stay in its high-efficiency operating region across the entire range.

### 🏗️ Stage-by-Stage Topology Selection

**AC-DC Stage: Three-Phase Active Front End (AFE)**

For the 480 VAC grid interface, a three-phase AFE is the clear choice. A two-level six-switch AFE is mature, but a **three-level T-type or Active Neutral-Point-Clamped (ANPC)** topology is superior for a 50 kW system, offering lower voltage stress and better harmonic performance. A 50 kW SiC-based three-phase PFC has been demonstrated with a **peak efficiency of 98.65%** and 97.10% at full load, while maintaining a current THD within 5%.

**DC-DC Stage: The Core Decision (DAB vs. CLLC)**

This is the critical choice for your wide power range. Both are bidirectional and isolated, but they have different strengths.

*   **Dual Active Bridge (DAB)** is often preferred for power ratings exceeding 5 kW due to **lower conduction losses** than resonant converters. Its main weakness is **higher switching losses at light load**, which is precisely your EQ phase. However, advanced modulation strategies like **Triple-Phase-Shift (TPS)** or **Dual-Phase-Shift (DPS)** can extend Zero-Voltage Switching (ZVS) to light loads and reduce RMS currents, directly targeting your efficiency challenge.

*   **CLLC Resonant Converter** is inherently designed for **soft-switching across a wide load range** and is a strong contender for bidirectional chargers. A three-phase CLLC can achieve efficiencies up to **98%** and, crucially, uses **phase-shedding** to improve light-load efficiency by **14% at 10% load**. Its main drawback is a more complex resonant tank design and a switching frequency that must vary widely to regulate output, which can be challenging to optimize across a 100:1 power range.

**Recommendation:** For your 100:1 range, **a three-phase CLLC converter with phase-shedding is likely the more robust choice** because it is architected for soft-switching across a wide load range. A DAB could work, but it would require sophisticated modulation (like TPS) to manage light-load losses, adding control complexity.

### 💡 Taming the 100:1 Range: Light-Load Efficiency Techniques

The 500 W EQ phase is where standard designs fail. These techniques are essential:

*   **Phase Shedding (The Key Technique):** This is the most powerful tool. For an interleaved or multiphase design, you simply turn off entire phases as load decreases. This keeps the active phases in their high-efficiency region and drastically cuts switching and core losses. For a three-phase CLLC, shutting down one or two bridges can improve light-load efficiency by **more than 9% at 20% load**. For a DAB, an efficiency-optimized modulation strategy has improved loss at **500 W by approximately 30%** compared to conventional control.

*   **Adaptive Switching Frequency:** Fixed-frequency designs are optimized for a narrow load band. A controller that adapts the switching frequency at light load can maintain ZVS and minimize circulating currents, directly improving efficiency where it matters most.

*   **Synchronous Rectification (SR):** On the 96 VDC side, replacing diodes with actively controlled MOSFETs is mandatory. At 96 V, even a 0.5 V diode drop is a significant loss at light load. Extending the SR ON-time can also help with regulation and efficiency at light load.

### 📊 Efficiency Expectations & Practical Design

*   **AC-DC Stage:** Expect **97–98.6%** peak efficiency with SiC devices.
*   **DC-DC Stage:** A well-designed CLLC with phase-shedding can maintain **>95%** efficiency down to 10% load. A DAB with advanced modulation can also achieve high efficiency but requires more careful tuning.
*   **System Target:** A combined **93–96%** efficiency across the entire range is a realistic and competitive goal.

**Key Design Tips:**
*   **Use SiC MOSFETs** for the AC-DC stage and the high-voltage side of the DC-DC stage to minimize switching losses and enable higher frequencies.
*   **Design for thermal balance.** At 95% efficiency and 50 kW, you are dissipating **2.5 kW of heat**. A liquid-cooled cold plate is likely necessary.
*   **Consider a modular approach.** Building the 50 kW system from several 10–15 kW modules simplifies thermal management, improves serviceability, and makes phase-shedding a natural control strategy.

If you can share the battery's specific charge profile (e.g., the voltage range during EQ) or any constraints on size or cost, I can help you narrow down the topology choice (e.g., a specific DAB variant vs. a three-phase CLLC) further.