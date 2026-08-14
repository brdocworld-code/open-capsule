#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open Capsule - Pilot System (Offline MVP)
-----------------------------------------
Role: The "Gatekeeper" & Language Learner
Hardware: Raspberry Pi 4/5 + Mic + Speaker + GPIO (for Relay)
Trigger: Mechanical Power On (No Wake Word)
Logic: 
  1. Boot -> Welcome Message (English).
  2. Listen -> Detect Language (Vosk).
  3. Learn -> Echo/Pattern Match unknown languages.
  4. Handshake -> Instruct user to activate Main Core.

Dependencies: vosk, piper-tts, pyaudio, RPi.GPIO
"""

import os
import sys
import time
import json
import wave
import threading
from datetime import datetime

# Hardware GPIO (Simulado para teste em PC, ativo no Pi)
try:
    import RPi.GPIO as GPIO
    RELAY_PIN = 18  # GPIO pin that triggers Main Core power
    HARDWARE_AVAILABLE = True
except ImportError:
    HARDWARE_AVAILABLE = False
    print("[WARN] RPi.GPIO not found. Running in Simulation Mode.")

# Speech Recognition (Offline)
from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio

# Text-to-Speech (Offline - Piper placeholder)
# In production, this would call the piper binary
def speak_text(text):
    """Synthesizes speech using Piper or system fallback."""
    print(f"[SPEAK]: {text}")
    # Exemplo de comando para Piper (se instalado):
    # os.system(f'echo "{text}" | piper --model models/en_US-lessac-high.onnx --output_file.wav')
    # Fallback para espeak (Linux) ou say (Mac)
    if os.name == 'posix':
        os.system(f'espeak -v en "{text}" 2>/dev/null')
    else:
        print("[AUDIO OUTPUT DISABLED ON THIS SYSTEM]")

class PilotSystem:
    def __init__(self, model_path="models/vosk-model-small"):
        self.audio_rate = 16000
        self.chunk_size = 8000
        
        # Initialize Vosk Model (Offline)
        if not os.path.exists(model_path):
            print(f"[ERROR] Model not found at {model_path}. Please download a Vosk model.")
            sys.exit(1)
        
        self.model = Model(model_path=model_path)
        self.recognizer = KaldiRecognizer(self.model, self.audio_rate)
        
        # State Machine
        self.state = "WELCOME"  # WELCOME, LISTENING, LEARNING, HANDSHAKE
        self.detected_lang = None
        self.audio_buffer = []
        
        # GPIO Setup
        if HARDWARE_AVAILABLE:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(RELAY_PIN, GPIO.OUT)
            GPIO.output(RELAY_PIN, GPIO.LOW) # Keep Main Core OFF initially

    def listen_loop(self):
        """Main listening loop."""
        p = pyaudio.PyAudio()
        stream = p.format=pyaudio.paInt16, channels=1, rate=self.audio_rate, input=True, frames_per_buffer=self.chunk_size)
        stream.start_stream()
        
        print("[SYSTEM] Pilot Online. Listening...")
        
        while True:
            data = stream.read(self.chunk_size, exception_on_overflow=False)
            
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get('text', '')
                
                if text:
                    print(f"[HEARD]: {text}")
                    self.process_input(text)
            
            # Partial results could be used for real-time echo, but keeping it simple for now
            
        stream.stop_stream()
        stream.close()
        p.terminate()

    def process_input(self, text):
        """Processes recognized text based on current state."""
        text_lower = text.lower()
        
        if self.state == "WELCOME":
            # After welcome, any speech moves to learning
            self.state = "LEARNING"
            self.analyze_language(text)
            
        elif self.state == "LEARNING":
            self.analyze_language(text)
            # Simple logic: if we hear "help" or "core", trigger handshake
            if "help" in text_lower or "core" in text_lower or "activate" in text_lower:
                self.trigger_handshake()
            else:
                # Echo mode for unknown languages
                self.speak_echo(text)

    def analyze_language(self, text):
        """Attempts to guess language based on vocabulary (Simplified)."""
        # In a real scenario, Vosk returns language if multi-language model is used
        # Here we simulate detection or default to 'unknown'
        print(f"[ANALYSIS] Processing input for language patterns...")
        # Logic to store patterns for the Main Core later
        self.detected_lang = "unknown" # Placeholder

    def speak_echo(self, text):
        """Imitates the user or gives basic feedback."""
        # In a real 'imitation' mode, we would play back the audio buffer
        # For now, we acknowledge receipt
        self.speak_text("I hear you. Please activate the Main Core for full translation.")

    def trigger_handshake(self):
        """Activates the Main Core Relay."""
        print("[ACTION] Activating Main Core Relay...")
        self.speak_text("Activating Main Core. Please wait.")
        
        if HARDWARE_AVAILABLE:
            GPIO.output(RELAY_PIN, GPIO.HIGH) # Close relay, power on Main Core
        else:
            print("[SIMULATION] Relay CLOSED. Main Core Power ON.")
            
        time.sleep(2)
        self.speak_text("Main Core is now booting. I will stand by.")
        self.state = "STANDBY"

    def run(self):
        """Boot Sequence."""
        # 1. Welcome Message (Automatic on Power On)
        self.speak_text("Welcome. I am the Open Capsule Pilot System.")
        self.speak_text("Please speak to me. I am learning your language.")
        
        self.state = "WELCOME"
        
        # 2. Start Listening
        try:
            self.listen_loop()
        except KeyboardInterrupt:
            print("\n[SYSTEM] Shutting down Pilot System.")
            if HARDWARE_AVAILABLE:
                GPIO.cleanup()

if __name__ == "__main__":
    bot = PilotSystem()
    bot.run()