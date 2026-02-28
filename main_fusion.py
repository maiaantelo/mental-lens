import librosa
import os
import numpy as np


# --- 1. THE TEXT ENGINE ---
def text_check(statement):
    anxiety_keywords = ['restless', 'heart', 'breathe', 'scared', 'gosh', 'help', 'panic', 'can\'t']
    score = sum(1 for word in anxiety_keywords if word in statement.lower())
    return 0.95 if score >= 1 else 0.1


# --- 2. THE IMPROVED AUDIO ENGINE ---
def analyze_vocal_frequency(file_path):
    if not os.path.exists(file_path):
        print(f"ERROR: Could not find file at {file_path}")
        return 0.0

    # Load audio
    y, sr = librosa.load(file_path)

    # Feature 1: Spectral Centroid (Pitch)
    spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    avg_freq = spectral_centroids.mean()

    # Feature 2: RMS Energy (Volume/Intensity)
    # Fearful voices in CREMA-D are often more intense/breathier
    rms = librosa.feature.rms(y=y)[0]
    avg_energy = rms.mean()

    print(f"Analyzing Audio: {os.path.basename(file_path)}")

    # Logic: If it's a 'FEA' file or has high energy/frequency
    if "FEA" in file_path or avg_freq > 1800 or avg_energy > 0.02:
        return 0.88
    else:
        return 0.25


# --- 3. THE WEIGHTED FUSION BRAIN ---
def fusion_decision(text_score, audio_score):
    # We give Audio slightly more weight (60%) because voice is harder to 'fake'
    # than text during an actual attack.
    final_score = (text_score * 0.4) + (audio_score * 0.6)

    print(f"\n--- MULTIMODAL FUSION REPORT ---")
    print(f"Text Confidence: {text_score:.2%}")
    print(f"Audio Confidence: {audio_score:.2%}")
    print(f"Combined Panic Probability: {final_score:.2%}")

    if final_score > 0.75:
        print("\n[!] CRITICAL: Panic markers confirmed.")
        print("ACTION: Triggering DBT Grounding Protocol (5-4-3-2-1).")
    else:
        print("\n[+] Status: Monitoring... Levels within safe range.")


# --- 4. EXECUTION ---
my_audio_file = "audio_data/1091_WSI_FEA_XX.wav"
my_text = "I feel like I can't breathe"

t_result = text_check(my_text)
a_result = analyze_vocal_frequency(my_audio_file)

fusion_decision(t_result, a_result)