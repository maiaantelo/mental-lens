import librosa
import numpy as np
import os


def extract_vocal_signatures(file_path):
    """
    Turns raw sound into a numerical 'fingerprint' for the AI.
    """
    if not os.path.exists(file_path):
        return "File not found."

    # Load audio (2.5 seconds is enough to catch a panic breath/sob)
    data, sample_rate = librosa.load(file_path, duration=2.5, offset=0.6)

    # Extract MFCCs (The 'DNA' of the voice)
    mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40).T, axis=0)

    # Extract Spectral Rolloff (Helps detect 'breathiness' or gasping)
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=data, sr=sample_rate))

    return {"mfccs": mfccs, "breathiness": rolloff}


# This part lets you test it individually
if __name__ == "__main__":
    # Replace this with an actual path once you download CREMA-D
    test_path = "data/CREMA-D/AudioWAV/1001_DFA_ANG_XX.wav"
    print("Audio engine initialized. Ready to process CREMA-D.")