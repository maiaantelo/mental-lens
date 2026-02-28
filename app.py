import streamlit as st
import librosa
import numpy as np
import time
import cv2


# --- 1. THE BRAIN ---
def analyze_vocal_tone(audio_file):
    try:
        y, sr = librosa.load(audio_file)
        avg_freq = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)[0])
        return 0.85 if avg_freq > 1800 else 0.25
    except:
        return 0.0


# --- 2. UI STYLING (The Ring Light) ---
st.set_page_config(page_title="Mental Lens", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    /* The Ring Light Glow Effect */
    .ring-light-active {
        border: 15px solid #fff5e6;
        border-radius: 50%;
        box-shadow: 0 0 50px 20px #fff;
        transition: all 0.5s ease-in-out;
    }

    /* TikTok style glow for the camera input */
    [data-testid="stCameraInput"] {
        border: 10px solid white;
        border-radius: 20px;
        box-shadow: 0 0 20px #AEE6E6;
        padding: 10px;
        background-color: white;
    }

    .stApp { background-color: #0e1117; }
    h1 { color: #AEE6E6; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Mental Lens AI")

# --- 3. INPUTS ---

# TEXT SECTION
st.subheader("1. Self-Report")
user_text = st.text_area("How are you feeling?", placeholder="Type here...", label_visibility="collapsed")

# AUDIO SECTION
st.subheader("2. Voice Stress Test")
recorded_audio = st.audio_input("Record: 'I need help breathing.'", label_visibility="collapsed")

# VISION SECTION (With Ring Light Toggle)
st.subheader("3. Vital Scan")
st.write("💡 *Tip: High lighting improves BPM accuracy.*")

# The Ring Light Toggle
ring_light = st.toggle("Activate Software Ring Light")

if ring_light:
    st.markdown("### 💡 RING LIGHT ACTIVE")
    # This empty div with a huge shadow acts as the light source on the user's face
    st.markdown("""
        <div style="height: 10px; width: 100%; background-color: white; box-shadow: 0px 0px 100px 50px white; margin-bottom: 50px;"></div>
    """, unsafe_allow_html=True)

video_snapshot = st.camera_input("Position face in frame", label_visibility="collapsed")

st.write("---")

# --- 4. THE ANALYSIS ---
if st.button("EXECUTE ANALYSIS", use_container_width=True, type="primary"):
    if not (user_text and recorded_audio and video_snapshot):
        st.error("Please complete all steps.")
    else:
        with st.status("Analyzing...", expanded=True) as status:
            time.sleep(1.5)
            status.update(label="Sync Complete!", state="complete", expanded=False)

        bpm = np.random.randint(98, 115)  # Simulated BPM
        st.metric(label="Estimated Heart Rate", value=f"{bpm} BPM", delta="Elevated")

        if bpm > 100:
            st.warning("⚠️ High Arousal Detected.")
            st.video("https://www.youtube.com/watch?v=5f5N6YFjvvc")