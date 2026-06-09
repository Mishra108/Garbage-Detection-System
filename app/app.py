# app.py
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile

# ─── PAGE CONFIG ──────────────────────────────────────────
st.set_page_config(page_title="Garbage Detection System", layout="wide")
st.title("🗑️ Garbage Detection System")
st.markdown("Detects and localises garbage in images and video using YOLOv8")

# ─── LOAD MODEL ───────────────────────────────────────────
@st.cache_resource
def load_model():
    return YOLO("models/weights/best.pt")

model = load_model()

# ─── RTC CONFIG (STUN server for network traversal) ───────
RTC_CONFIG = RTCConfiguration({
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
})

# ─── SIDEBAR ──────────────────────────────────────────────
mode = st.sidebar.radio("Select Mode", ["📷 Image Upload", "🎥 Video Upload", "📹 Live Webcam"])

# ─── IMAGE MODE ───────────────────────────────────────────
if mode == "📷 Image Upload":
    st.subheader("Image Detection")
    uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded:
        image = Image.open(uploaded).convert("RGB")
        img_array = np.array(image)

        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Original Image", use_container_width=True)

        results = model(img_array, conf=0.5)[0]
        annotated = results.plot()

        with col2:
            st.image(annotated, caption="Detected Garbage", use_container_width=True)

        st.subheader("Detection Results")
        if results.boxes:
            st.success(f"Total Garbage Detected: **{len(results.boxes)}**")
            for i, box in enumerate(results.boxes):
                cls = model.names[int(box.cls)]
                conf = float(box.conf)
                st.write(f"**Detection {i+1}:** {cls} — Confidence: `{conf:.2%}`")
        else:
            st.info("No garbage detected in this image.")

# ─── VIDEO MODE ───────────────────────────────────────────
elif mode == "🎥 Video Upload":
    st.subheader("Video Detection")
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded_video.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        count_placeholder = st.empty()
        stop = st.button("⏹ Stop")

        st.info("Processing video frame by frame...")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret or stop:
                break

            results = model(frame, conf=0.5)[0]
            annotated = results.plot()
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            stframe.image(annotated_rgb, use_container_width=True)

            count = len(results.boxes)
            count_placeholder.write(f"Garbage detected in this frame: **{count}**")

        cap.release()
        st.success("Video processing complete!")

