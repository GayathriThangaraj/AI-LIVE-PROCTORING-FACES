A simple real-time head position and distraction detection system built using Flask and OpenCV. The system checks if the user’s face is visible and whether they are distracted by looking away. Alerts are displayed in real-time via a web interface.

How It Works
   The system detects faces using Haar Cascade.

   If no face is detected, an alert "No face detected" is shown.

   If multiple faces are detected, it shows "Multiple faces detected".

   This is useful for online exams or proctoring environments where only one focused user should be present.

Installation
 1. Clone the Repository
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
 2. Install Dependencies
    Make sure you have Python installed. Then install the required Python libraries:

pip install opencv-python Flask numpy
 3. Download Haar Cascade Model
    Download the file haarcascade_frontalface_default.xml
Place it inside a folder named models/ in your project directory.

Running the Application
   python app.py
   Open your browser and go to: http://127.0.0.1:5000/

