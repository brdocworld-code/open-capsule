# Open Capsule Architecture Draft (Phase 2) - Two-Stage AI System

## Overview
This document outlines the software and hardware architecture for the Open Capsule prototype. The system utilizes a **Two-Stage AI Architecture** to balance extreme energy efficiency during standby with high-performance intelligence during active recovery.

The core philosophy: **A low-power "Pilot" wakes a high-power "Sage" only when needed.**

## 1. Ingestion Module (The "Keeper" System)
*Runs on standard university servers or dedicated Raspberry Pi 4/5.*

- **Input Pipeline:**
  - Python scripts monitor designated folders for new cultural artifacts (news, music, data).
  - Automatic validation against `data-schema-draft.md` (JSON-LD).
  - **Format Normalization:** Auto-conversion tools (e.g., `libreoffice --headless` for PDF/A, `ffmpeg` for FLAC audio) ensure long-term readability.
- **Local Database:**
  - SQLite database stores metadata and indexes.
  - Raw files stored in a structured directory (`/YYYY/MM/DD/type/filename`).
- **Sync Mechanism:**
  - Periodic job (cron) verifies integrity (SHA-256) and prepares data for writing to the archival medium.

## 2. Storage Module (The "Capsule" Core)
*Passive storage medium, no power required.*

- **Medium:** 5D Optical Glass (Project Silica) or Archival M-Disc.
- **Structure:**
  - Root directory contains `README_FIRST.txt` (plain text, multiple languages) explaining how to access the data.
  - `/data`: Encrypted? **No.** All data must be plain/open standard.
  - `/schema`: Copy of the JSON-LD schema definition.
  - `/software`: Portable viewers (e.g., a simple PDF reader binary for common OS architectures) just in case.

## 3. Recovery Module: Two-Stage Architecture
*The heart of the Open Capsule. Designed to survive decades of dormancy and provide maximum intelligence upon activation.*

### Stage 1: The Pilot System (Low Power "Portier")
*Always-on standby, minimal energy consumption.*

- **Hardware Spec:**
  - **Microcontroller:** Ultra-low-power RISC-V or ARM Cortex-M (e.g., ESP32-S3, Raspberry Pi Pico W).
  - **Power Source:** Primary Li-SOCl2 Battery (20+ year shelf life) OR Super-capacitor trickle-charged by a small external solar cell (1W).
  - **I/O:** Single microphone, small speaker, physical interrupt pin (from key/switch).
- **Software Stack:**
  - **OS:** Bare-metal RTOS or MicroPython.
  - **AI Model:** Tiny LLM (<100MB, e.g., TinyLlama, Phi-2 quantized to INT4).
  - **Functions:**
    1.  **Wake Detection:** Listens for specific voice patterns or physical switch activation.
    2.  **Language Fingerprinting:** Analyzes phonetic patterns of the opener's speech to identify language family.
    3.  **Basic Dialogue:** Engages in simple conversation ("Hello. I am the Capsule Guardian. Shall I activate the Main Core for detailed assistance?").
    4.  **Handshake:** Sends a hardware signal to release power to Stage 2.
    5.  **Fallback Mode:** If Stage 2 fails, guides users to physical analog backups (engraved metal plates).

### Stage 2: The Main Core (High Power "Sage")
*Deep sleep until activated by Stage 1. Contains the full knowledge of humanity.*

- **Hardware Spec:**
  - **Compute Cluster:** High-efficiency SBC cluster (e.g., 4x Raspberry Pi 5, NVIDIA Jetson Orin Nano) or a single high-end ARM server board.
  - **Power Source:** Secondary Li-Ion/Li-FePO4 Battery Bank (protected by BMS) connected to larger internal solar panels. **Circuit is physically open until Stage 1 closes the relay.**
  - **Storage:** High-speed NVMe SSD cache for the active LLM + Direct access to Archival Medium.
- **Software Stack:**
  - **OS:** Minimal Linux (Alpine/Debian).
  - **AI Model:** Advanced LLM (e.g., Llama-3-70B, Mixtral 8x22B quantized to 4-bit/6-bit).
    - *Requirement:* Must fit in available RAM (e.g., 64GB-128GB unified memory).
  - **Functions:**
    1.  **Deep Translation:** Full neural machine translation for any known language.
    2.  **Technical Tutoring:** Step-by-step guidance on rebuilding infrastructure (medicine, agriculture, energy, engineering).
    3.  **Semantic Search:** Retrieves specific information from the archival database based on complex queries.
    4.  **Contextual Teaching:** Adapts explanations to the technological level of the survivors.

## 4. Power Management Unit (PMU)
*The bridge between Stage 1 and Stage 2.*

- **Logic:**
  - **Default State:** Stage 2 power rail is **DISCONNECTED** (hardware relay open). Zero leakage current for the main core.
  - **Activation:** Stage 1 closes the relay only after user confirmation.
  - **Solar Regulation:** MPPT (Maximum Power Point Tracking) chargers manage input from external solar panels to charge both battery banks independently.
  - **Safety:** Over-discharge protection to prevent battery damage during long periods of darkness.

## 5. Security & Resilience
- **No Encryption:** Knowledge must not be locked.
- **Faraday Shielding:** Entire electronics module enclosed in copper/steel mesh to survive EMP/CME.
- **Redundancy:**
  - Critical metadata duplicated in plain text headers of every file.
  - **Analog Fallback:** Essential survival instructions (water purification, basic first aid) engraved on metal plates inside the capsule, accessible even if all electronics fail.

## Next Steps for Collaborators
- **Embedded Engineers:** Design the PMU relay logic and low-power firmware for Stage 1.
- **AI Researchers:** Optimize Tiny LLMs for microcontrollers and large LLMs for efficient edge inference.
- **Hardware Engineers:** Select specific components (batteries, solar cells, SBCs) for a 20+ year lifespan.
- **Security Experts:** Audit the system for any single points of failure in the power chain.   
