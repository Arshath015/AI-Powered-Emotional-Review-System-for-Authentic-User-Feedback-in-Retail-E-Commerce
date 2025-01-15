import streamlit as st
from PIL import Image
import cv2
from emotion_detection import detect_emotion
import pandas as pd
import random

# Load questions
with open("data/questions.txt", "r") as file:
    questions = file.readlines()

# Initialize data storage
feedback_data = []

def start_emotion_detection():
    st.header("Live Emotion Detection")

    # Load the video feed
    cap = cv2.VideoCapture(0)

    if st.button("Start Detection"):
        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("Unable to access webcam.")
                break

            # Emotion detection
            emotion = detect_emotion(frame)
            if emotion:
                st.write(f"Detected Emotion: {emotion}")
            else:
                st.write("Emotion: None")

            # Show video feed
            st.image(frame, channels="BGR")

    if st.button("Stop Detection"):
        stop_emotion_detection(cap)

def stop_emotion_detection(cap):
    if cap:
        cap.release()
        cv2.destroyAllWindows()
    st.info("Stopped emotion detection.")

def save_feedback():
    if st.button("Save Feedback"):
        question = random.choice(questions).strip()
        emotion = st.text_input("Detected Emotion", placeholder="Emotion detected will appear here.")
        rating_map = {"happy": 5, "neutral": 3, "sad": 1}
        feedback_data.append([question, emotion, rating_map.get(emotion.lower(), 2)])
        df = pd.DataFrame(feedback_data, columns=["Question", "Emotion", "Rating"])
        df.to_csv("data/feedback.csv", index=False)
        st.success("Feedback saved successfully!")

def next_question():
    return random.choice(questions).strip()
