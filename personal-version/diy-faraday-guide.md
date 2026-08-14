# DIY Faraday Cage Guide for Open Capsule Personal Nodes

## 1. Objective
To construct a low-cost, high-efficiency Faraday enclosure to protect the Open Capsule Personal Node (Raspberry Pi, Storage, Power Bank) from EMP (Electromagnetic Pulse), CME (Coronal Mass Ejection), and lightning-induced surges.

**Target Attenuation:** >60 dB (Blocking 99.9999% of RF energy from 100 MHz to 2 GHz).

## 2. Core Principle: The "Box-in-Box" Method
A single metal container often has gaps in its lid that allow RF energy to leak. The gold standard for DIY protection is **two isolated conductive layers**.
*   **Inner Layer:** Protects against direct contact and minor fields.
*   **Air Gap:** Insulates the two layers (cardboard, foam, or wood).
*   **Outer Layer:** Absorbs and redirects the main electromagnetic wave.

## 3. Materials List (Off-the-Shelf)
| Item | Specification | Estimated Cost |
| :--- | :--- | :--- |
| **Outer Container** | Steel Ammo Can (30 cal or 50 cal) OR Galvanized Steel Trash Can with lid. | $20 - $40 |
| **Inner Container** | Smaller steel tin, aluminum baking pan (sealed edges), or second smaller ammo can. | $5 - $15 |
| **Insulation** | Cardboard, rigid foam board, or wood scraps. | $5 |
| **Conductive Tape** | Copper Foil Tape (with conductive adhesive) - 2 inch width. | $10 |
| **Gasket Material** | Copper mesh (from scrubbing pads) or conductive fabric. | $5 |
| **Desiccant** | Silica Gel packs (essential to prevent rust inside). | $5 |
| **Tools** | Screwdriver, wire brush, multimeter (optional for testing). | - |

**Total Estimated Cost:** ~$50 USD.

## 4. Step-by-Step Construction

### Step 1: Prepare the Outer Container
1.  **Clean:** Remove any paint, rust, or debris from the rim where the lid contacts the box. Use a wire brush or sandpaper until bare metal shines.
2.  **Seal Vents:** If using an ammo can with a rubber gasket, ensure it is intact. If using a trash can, line the rim with **Copper Foil Tape** to ensure metal-to-metal contact with the lid.
3.  **Grounding (Optional):** For permanent installations, attach a copper wire to the outer box and connect it to a ground rod. For portable capsules, leave floating.

### Step 2: Prepare the Inner Container
1.  **Wrap:** Completely wrap the inner container in cardboard or foam. **Do not let the inner box touch the outer box.** Direct contact creates a "antenna" effect that transfers energy inside.
2.  **Seal Gaps:** If using a baking pan, seal the edges with copper tape to create a continuous conductive surface.

### Step 3: Create the RF Gasket (Critical)
The gap between the lid and the box is the weak point.
1.  **Copper Mesh:** Place a strip of copper mesh (unfolded scrubbing pad) along the rim of the outer box.
2.  **Compression:** When closed, the lid must compress this mesh tightly, creating hundreds of contact points.
3.  **Tape Reinforcement:** For extra security, apply copper tape over the seam *after* closing (sacrificial seal).

### Step 4: Assembly
1.  **Line:** Place a layer of cardboard/foam at the bottom of the outer box.
2.  **Insert:** Place the Inner Container (with your electronics inside) into the center of the Outer Container.
3.  **Fill:** Pack more insulation around the sides and top to prevent shifting.
4.  **Dry:** Add 2-3 large Silica Gel packs to control humidity.
5.  **Close:** Shut the lid tightly, compressing the copper mesh gasket.

## 5. What Goes Inside?
*   **The Node:** Raspberry Pi, M-Discs, Power Bank.
*   **Cables:** Keep a short USB-C cable and HDMI adapter inside (shielded cables are better, but standard ones work if the cage is effective).
*   **Manual:** A printed copy of this guide.
*   **DO NOT:** Store batteries connected to the device. Disconnect everything to prevent surge paths.

## 6. Testing Your Cage (The "Radio Test")
You don't need expensive equipment to verify effectiveness.
1.  **Setup:** Tune an FM/AM radio to a strong station (or use a cell phone inside a call).
2.  **Baseline:** Note the signal strength outside the box.
3.  **Test:** Place the radio/phone inside the closed cage.
4.  **Result:**
    *   **FM Radio:** Should drop to complete silence/static.
    *   **Cell Phone:** Should go straight to "Out of Coverage" or "Voicemail" (Note: Cell signals are harder to block than EMP; if the phone loses signal, your cage is excellent. If it rings faintly, it may still protect against EMP, but add another layer of mesh).
    *   **Wi-Fi/Bluetooth:** If you have a second device, try pinging the Pi inside. It should be unreachable.

## 7. Maintenance & Longevity
*   **Corrosion Check:** Inspect the metal rims every 2-3 years. Clean rust and re-apply copper tape if needed.
*   **Desiccant:** Replace Silica Gel packs every 5 years or if color indicator changes.
*   **Battery Rotation:** If storing a Power Bank, check charge levels every 3-5 years. Li-Ion batteries degrade over time; consider storing **primary lithium batteries (Li-SOCl2)** and a simple charger circuit instead for 20+ year storage.

## 8. Common Mistakes to Avoid
*   **Painted Contact Points:** Painting the rim prevents electrical contact. Metal must touch metal.
*   **Single Layer:** A single thin aluminum foil wrap is often insufficient for strong EMP. Use the Box-in-Box method.
*   **Cables Penetrating:** Never leave a cable hanging out of the box. It acts as an antenna, channeling energy directly inside. If you need an external solar panel, use a **feed-through capacitor** or disconnect the panel during an event.

## 9. References & Further Reading
*   *ARRL Handbook for Radio Communications* - Section on Shielding.
*   *Security Engineering* by Ross Anderson - Chapter on Physical Security.
*   *Open Source Ecology* - DIY Electronics Shielding Guides.

---
*This guide is for educational purposes. Test your specific construction before relying on it for critical data preservation.*   
