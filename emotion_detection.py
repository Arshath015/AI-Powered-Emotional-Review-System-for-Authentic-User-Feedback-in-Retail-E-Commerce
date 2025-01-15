import cv2
from deepface import DeepFace

def detect_emotion(frame):
    try:
        # Analyze the emotion
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']  # Access emotion from result dictionary
        return emotion
    except Exception as e:
        print(f"Error in emotion detection: {e}")
        return None
