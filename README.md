A simple real-time head position detection system built using Flask, OpenCV, and dlib. The system checks if the user is facing forward and shows alerts if they look away or get distracted.

How It Works
The system detects faces using Haar Cascade and facial landmarks using dlib.

It estimates the head's position (yaw and pitch).

If the head is turned too far to the side or up/down, it shows a distraction alert.

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Install the dependencies: Install the required libraries using pip:

bash
Copy
Edit
pip install opencv-python dlib numpy Flask
Download the facial landmark model: Download shape_predictor_68_face_landmarks.dat from here, extract it, and place it in the models/ directory.

Run the application:

bash
Copy
Edit
python app.py
Access the application: Open a browser and go to http://127.0.0.1:5000/ to view the video feed and distraction alerts.

How to Use
The video feed will show up in your browser.

If the user's head is not facing forward, an alert will appear.
