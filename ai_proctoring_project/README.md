
# AI Proctoring System

## Description
A simple AI proctoring system that uses Haar Cascade to detect faces in real-time using a webcam. Built with Flask and OpenCV.

## Setup Instructions
1. Create a virtual environment (optional but recommended).
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open `http://127.0.0.1:5000/` in your browser.

## Alerts
- "No face detected!"
- "Multiple faces detected!"

## Note
Make sure to place `haarcascade_frontalface_default.xml` inside the `models/` folder.
