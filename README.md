Driver Drowsiness Detection System
Overview

The Driver Drowsiness Detection System is a real-time safety application that detects signs of driver fatigue using Computer Vision and Machine Learning techniques. The system continuously monitors the driver's eyes through a webcam and alerts the driver when drowsiness is detected, helping to prevent accidents caused by fatigue.

Features
Real-time face and eye detection
Eye Aspect Ratio (EAR) based drowsiness detection
Automatic audio alert when fatigue is detected
Live webcam monitoring
High detection accuracy
User-friendly interface
Technologies Used
Python
OpenCV
Dlib
NumPy
SciPy
Imutils
Computer Vision
Project Structure
Driver-Drowsiness-Detection/
│
├── models/
│   └── shape_predictor_68_face_landmarks.dat
│
├── alarm.wav
├── drowsiness_detector.py
├── requirements.txt
├── README.md
└── assets/
How It Works
Captures video frames from the webcam.
Detects the driver's face using Dlib.
Identifies facial landmarks and extracts eye coordinates.
Calculates the Eye Aspect Ratio (EAR).
Monitors eye closure duration.
Triggers an alarm if eyes remain closed beyond a predefined threshold.
Continues monitoring until the application is stopped.
Installation
Clone the Repository
git clone https://github.com/your-username/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection
Install Dependencies
pip install -r requirements.txt
Download Facial Landmark Model

Download shape_predictor_68_face_landmarks.dat and place it inside the models folder.

Usage

Run the application:

python drowsiness_detector.py

Press Q to quit the application.

Results
Detects driver fatigue in real time.
Provides instant audio alerts.
Achieved approximately 95% detection accuracy during testing.
Future Enhancements
Yawning detection
Head pose estimation
Mobile application integration
Night vision support
Cloud-based monitoring and analytics
Applications
Smart vehicles
Driver assistance systems
Fleet management
Public transportation safety
Commercial vehicle monitoring
Author

Ayush Sharma

GitHub: Ayush Sharma GitHub

LinkedIn: Ayush Sharma LinkedIn

License

This project is developed for educational and research purposes.
