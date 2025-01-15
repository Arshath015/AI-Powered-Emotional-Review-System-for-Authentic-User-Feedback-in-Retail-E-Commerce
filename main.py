import streamlit as st
from ui import start_emotion_detection, stop_emotion_detection, save_feedback, next_question
from emotion_detection import detect_emotion

def main():
    st.set_page_config(page_title="Emotion-Based Review System", layout="wide")

    # Sidebar options
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page", ["Home", "Feedback"])

    if page == "Home":
        st.title("Emotion-Based Review System")
        st.write("This system detects your emotions and provides feedback based on your responses.")
        start_emotion_detection()
    elif page == "Feedback":
        st.title("Feedback Summary")
        save_feedback()

if __name__ == "__main__":
    main()
