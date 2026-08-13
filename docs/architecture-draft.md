# Open Capsule Architecture Draft (Phase 2)

## Overview
This document outlines the software and hardware architecture for the Open Capsule prototype. The system is divided into three distinct operational modes: **Ingestion** (Active), **Storage** (Passive), and **Recovery** (Post-Collapse).

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

## 3. Recovery Module (The "Guide" AI)
*Low-power embedded system activated upon capsule opening.*

- **Hardware Spec:**
  - **Microcontroller:** Raspberry Pi Zero 2 W or RISC-V equivalent (low power, high availability).
  - **Power:** Supercapacitor + Li-SOCl2 Battery backup + Small Solar Panel (5V/1W) on capsule exterior.
  - **I/O:** Microphone, Speaker, Optional E-Ink display.
- **Software Stack:**
  - **OS:** Minimal Linux (Alpine) or bare-metal RTOS.
  - **AI Model:** Quantized Small Language Model (SLM) like **Llama-3-8B** or **Phi-3-mini** (4-bit quantization) capable of running on <4GB RAM.
  - **Function:**
    1. **Wake Word/Key:** Activates on sound or physical switch.
    2. **Language Detection:** Analyzes input speech for phonetic patterns.
    3. **Adaptive Translation:** If language is unknown, uses context clues from the database to build a translation map (Rosetta Stone approach).
    4. **Guided Retrieval:** Acts as a conversational interface to help survivors find specific knowledge (e.g., "How to purify water?", "Where are medical manuals?").

## Security & Resilience
- **No Encryption:** Knowledge must not be locked.
- **Faraday Shielding:** Entire electronics module enclosed in copper/steel mesh to survive EMP.
- **Redundancy:** Critical metadata duplicated in plain text headers of every file.

## Next Steps for Collaborators
- **Software Engineers:** Develop the Python ingestion scripts and validation tools.
- **AI Researchers:** Optimize SLM models for low-power hardware and few-shot language learning.
- **Hardware Engineers:** Design the power management system for the Recovery Module.   
