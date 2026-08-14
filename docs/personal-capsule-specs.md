# Open Capsule: Personal Node Specifications (Draft v0.1)

## 1. Vision: The Distributed Network
While the **Institutional Capsule** serves as a fortified library for civilization-scale recovery, the **Personal Capsule** acts as a distributed node in a global mesh of knowledge. 
*   **Goal:** Enable individuals, families, and small communities to curate and preserve their own cultural, technical, and historical data at a low cost.
*   **Philosophy:** "Diversity ensures survival." Thousands of unique personal capsules increase the probability that specific, localized, or niche knowledge survives a global collapse.
*   **Relationship:** Personal Capsules use the same **Data Schema** (Phase 1) and **AI Protocol** (Phase 2) as the Institutional version, ensuring interoperability. If found, they can "handshake" with other capsules to share data.

## 2. Hardware Specifications (Low-Cost & Accessible)
Designed to be built with off-the-shelf components available in 2026.

### A. Storage Medium (The "Book")
*   **Primary:** **M-Disc Blu-ray (BD-XL 100GB)** or **M-Disc DVD (4.7GB)**.
    *   *Why:* Etched in stone-like layer, rated for 1,000+ years. Immune to humidity, light, and magnetic fields.
    *   *Cost:* ~$5-10 per disc.
    *   *Capacity Strategy:* A full "University" curriculum can fit on ~20-30 discs (compressed text/images). Critical data fits on 1 disc.
*   **Alternative:** **Industrial Grade SD Cards** (SLC NAND) stored in anti-static, light-proof containers. (Less durable than M-Disc, but higher capacity).

### B. Compute Module (The "Reader")
*   **Core:** **Raspberry Pi 5 (8GB)** or **Orange Pi 5**.
    *   *Why:* Low power, ubiquitous, GPIO pins for expansion.
*   **AI Accelerator:** **Google Coral USB TPU** (for running quantized LLMs efficiently).
*   **Display:** 7-inch E-Ink display (low power, readable in sunlight) or simple HDMI output to any found screen.
*   **Power:** 
    *   Small 10W-20W Solar Panel (foldable).
    *   20,000mAh Li-Po Power Bank (standard, replaceable).
    *   *Estimated Runtime:* 10+ hours of active use on a single charge.

### C. Enclosure (The "Box")
*   **DIY Faraday Cage:** Constructed from stacked steel ammo cans or aluminum baking trays lined with copper tape. 
    *   *Guide:* See `docs/diy-faraday-guide.md` (link to external resources like *Security Engineering* manuals).
*   **Protection:** Silica gel packs for moisture control.
*   **Portability:** Designed to fit in a standard backpack or dry bag.

## 3. Software & Data Strategy
*   **OS:** **Alpine Linux** or **DietPi** (minimal footprint, runs from RAM to save SD card wear).
*   **AI Model:** 
    *   **TinyLlama-1.1B** or **Phi-3-mini (3.8B)** quantized to 4-bit (GGUF format).
    *   *Capability:* Sufficient for tutoring, translation, and Q&A on stored data. Runs locally on Pi + Coral TPU.
*   **Data Content (Curated by Owner):**
    *   **Core Pack:** Universal survival guides (water, first aid, agriculture).
    *   **Niche Pack:** Owner's expertise (e.g., "Pediatrics for Tropics," "Small-Scale Hydro Engineering," "Local Flora of Andes").
    *   **Cultural Pack:** Family history, local music, art, philosophy.
*   **Interoperability:** 
    *   Uses the same `JSON-LD` schema as Institutional Capsules.
    *   **Mesh Feature:** If two Personal Capsules meet, they can automatically exchange metadata indexes via Wi-Fi Direct or LoRa, creating a decentralized "library catalog."

## 4. Cost Breakdown (Estimate 2026)
| Component | Item | Estimated Cost (USD) |
| :--- | :--- | :--- |
| **Compute** | Raspberry Pi 5 + Case + Cooling | $80 |
| **AI Accel** | Google Coral USB TPU | $60 |
| **Storage** | M-Disc BD-XL (Pack of 10) + Drive | $150 |
| **Power** | Solar Panel (20W) + Power Bank | $50 |
| **Enclosure** | Steel Box + Copper Tape + Silica | $30 |
| **Display** | E-Ink HAT or Small HDMI Screen | $60 |
| **Total** | | **~$430 USD** |

*Note: Costs can be reduced to <$200 by omitting the E-Ink screen (using headless mode) and using used hardware.*

## 5. Implementation Guide for Individuals
1.  **Curate:** Select your data. Use the `open-capsule-ingestion-script` (Phase 2) to validate and format your files.
2.  **Burn:** Write data to M-Discs using a standard Blu-ray burner. Verify hashes.
3.  **Build:** Assemble the Raspberry Pi, install the OS and AI model (pre-configured image available on GitHub).
4.  **Shield:** Place the compute module and discs inside the DIY Faraday enclosure.
5.  **Deploy:** Bury, hide, or store in a safe location. Leave a physical marker or map for future finders.

## 6. Strategic Value
*   **Redundancy:** If the Institutional Capsule is destroyed, thousands of Personal Capsules may still survive.
*   **Pluralism:** Prevents a single narrative from dominating the post-collapse world. A doctor's capsule teaches medicine; a farmer's teaches agriculture; a poet's teaches culture.
*   **Immediate Action:** Individuals can build this *today*, without waiting for university partnerships.

## 7. Collaboration Needs
*   **Makers/Hobbyists:** Test and refine the DIY Faraday enclosure designs.
*   **Developers:** Create a "One-Click Installer" image for the Raspberry Pi that includes the AI tutor and ingestion scripts.
*   **Educators:** Curate "Starter Packs" of data (e.g., "The 100 Essential Papers for Survival") that individuals can easily download and burn.

---
*This is a living document. Propose changes via a Pull Request.*   
