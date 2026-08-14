# Open Capsule: Pilot System (Offline MVP)

This directory contains the core software for the **Stage 1 Pilot System**, designed to run on a Raspberry Pi (or similar SBC) without internet access.

## 🎯 Function
- **Activation:** Powers on automatically when the capsule is opened (mechanical switch triggers power).
- **Role:** Acts as the "Gatekeeper." It listens to the survivor, attempts to identify the language, and guides them to activate the **Main Core** (Stage 2).
- **Constraint:** Runs 100% offline. No Wi-Fi, no Cloud APIs.

## 📦 Dependencies
- **Python 3.7+**
- **Vosk:** Offline speech recognition engine (supports 20+ languages).
- **PyAudio:** For microphone input.
- **Piper TTS (Optional):** For high-quality offline text-to-speech (fallback: `espeak`).
- **RPi.GPIO:** For controlling the relay that powers the Main Core.

## 🛠️ Installation

### 1. System Requirements (Raspberry Pi OS)
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-pyaudio espeak-ng portaudio19-dev git
```

### 2. Python Dependencies
```bash
pip3 install -r requirements.txt
```

### 3. Download Speech Model (Crucial)

You must download a Vosk language model. For the Pilot System, a "small" model is recommended for speed and lower RAM usage.

English (Small): vosk-model-small-en-us-0.15 [https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip]
Multilingual (Small): vosk-model-small-multilang-0.15 (Recommended for global capsules) [https://alphacephei.com/vosk/models/vosk-model-small-multilang-0.15.zip]

### Steps:

    1. Download and unzip the model.
    2. Rename the folder to model.
    3. Place it inside this directory: code/model/.

_(Optional) Install Piper TTS for better voice quality_: Follow instructions at Piper TTS GitHub [https://github.com/rhasspy/piper].

## 🚀 Usage
### Running the System
```bash
python3 pilot_system.py
```

### How It Works
    1. **Boot**: Upon power-up, the system speaks: "Welcome. I am the Open Capsule Pilot System. Please speak to me. I am learning your language."
    2. **Listening**: It enters a loop, waiting for speech.
    3. **Processing**:
        - It captures audio and uses Vosk to transcribe it locally.
        - If it detects keywords like "help", "core", or "activate", it triggers the GPIO Relay (Pin 18) to power on the Main Core.
        - If the language is unknown, it acknowledges the input and reiterates the need to activate the Main Core for full translation.
    4. **Hardware Trigger**: When activated, GPIO Pin 18 goes HIGH, closing the relay that connects the Main Core's battery.

### ⚙️ Configuration
    - GPIO Pin: Default is 18. Change in pilot_system.py if using a different pin.
    - Model Path: Ensure the model folder is in the same directory as the script.
    - Language: The default fallback is English. Using the multilang Vosk model allows better detection of non-English inputs.

### 🧪 Testing on PC (Simulation Mode)

You can test the logic on your computer without a Raspberry Pi.

    1. Install dependencies (pip install -r requirements.txt). Note: RPi.GPIO will fail on PC, but the script has a try/except block to run in simulation mode.
    2. Run the script. It will simulate the relay activation in the console.

### 📝 Next Steps (v0.2)
    - Implement **Audio Echo** (play back user's voice for imitation learning).
    - Integrate **Vosk Multi-language** detection dynamically.
    - Add **Low-Power Sleep Mode** when the capsule is closed (GPIO interrupt).

_For hardware assembly instructions, see /personal-version/diy-faraday-guide.md._