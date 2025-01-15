# Emotion Based Feedback System
# AI Powered Emotional Review System for Authentic User Feedback in Retail and E-Commerce
Developed an **AI-powered system to generate real-time  emotional reviews** by analyzing user sentiment, addressing the issue of fake feedback in retail and e-commerce. The  system improves user engagement by ensuring authentic, emotion-driven reviews, helping businesses better understand  customer experiences and refine their services.

---

## Features
- **Real-Time Emotion Detection**: Analyze user emotions using a live video feed.
- **Emotion-Based Feedback**: Map detected emotions to ratings and save feedback.
- **Interactive Questionnaires**: Engage users with shuffled questions to gather detailed feedback.
- **Data Visualization**: View and analyze saved feedback in a tabular format.
- **Custom Emotion Model**: Train and integrate a custom emotion detection model.

---

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: TensorFlow, DeepFace
- **Programming Language**: Python
- **Data Processing**: Pandas, NumPy
- **Computer Vision**: OpenCV

---

## Installation

### Prerequisites
- Python 3.8 or later

### Steps
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd emotion-based-feedback-system
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate    # Windows
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

### Running the Application
1. Start the Streamlit app:
    ```bash
    streamlit run main.py
    ```
2. Navigate to the web app at `http://localhost:8501`.

### Modules
- **Feedback**: View saved feedback data.
- **Emotion Detector**: Detect and capture emotions in real time using a webcam.

---

## File Structure
```
.
├── main.py                # Main application file
├── ui.py                  # User interface and logic
├── emotion_detection.py   # Emotion detection using DeepFace
├── model_training.py      # Custom emotion model training script
├── requirements.txt       # Python dependencies
├── data/
│   ├── questions.txt      # Question bank for feedback
│   └── feedback.csv       # Saved feedback data
└── README.md              # Project documentation
```

---

## Custom Model Training
1. Prepare your dataset and organize it into training folders (`data/train`).
2. Adjust the model configuration in `model_training.py` if needed.
3. Train the model:
    ```bash
    python model_training.py
    ```

---

## Key Mappings
- Emotion-to-Rating Mapping:
    | Emotion | Rating |
    |---------|--------|
    | Happy   | 5      |
    | Neutral | 4      |
    | Sad     | 3      |
    | Fear    | 2      |
    | Angry   | 1      |

---

## Troubleshooting
- **Camera Access Issue**: Ensure your webcam is connected and accessible.
- **Missing Feedback File**: Create an empty `feedback.csv` in the `data/` folder.
- **Emotion Detection Error**: Check the DeepFace library setup and dependencies.

---

## Future Enhancements
- Add support for multiple users.
- Integrate additional emotion categories.
- Provide data analytics dashboards for visualizing trends.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Contributors
- **Your Name**: Developer & Project Lead

Feel free to contribute to this project by submitting issues or pull requests.
