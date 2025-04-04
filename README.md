# Witness Vision Wonders (WvW) - Interactive Computer Vision Playground

![image](https://github.com/user-attachments/assets/50bea47c-7720-48c7-b07b-8ad1fb549c08)


---

## 🚀 Project Overview

Welcome to **Witness Vision Wonders (WvW)**, a multi-functional application I built as a secondary school student passionate about computer vision and Python. This project integrates real-time hand tracking with OpenCV, Graphical User Interface (GUI) development with Tkinter, showcasing my ability to create engaging, user-centric tech solutions. From gesture-controlled Ping-Pong to a virtual painter and educational quizzes, WvW is a testament to my skills in coding, problem-solving, and innovation.

### Key Features
- **Ping-Pong**: Play a classic game using your hands as paddles, powered by hand tracking.
- **Rock Paper Scissors**: Challenge an AI with gesture recognition.
- **Virtual Painter**: Draw in the air with color selection via hand gestures.
- **Volume Gesture Control**: Adjust system volume with thumb-index distance.
- **Press Game**: Test reflexes by pressing virtual buttons with hand proximity.
- **Air Quiz**: Answer multiple-choice questions with hand gestures.
- **Personalized Greeting**: Enter your name and get a time-based audio welcome.

## 🛠️ Tech Stack

| Technology         | Purpose                          |
|--------------------|----------------------------------|
| **Python**         | Core programming language        |
| **OpenCV (cv2)**   | Computer vision and image processing |
| **cvzone**         | Hand tracking and overlays       |
| **Tkinter**        | GUI for user interaction         |
| **gTTS**           | Text-to-speech for greetings     |
| **pygame.mixer**   | Audio playback                   |
| **pycaw**          | System volume control            |
| **NumPy**          | Mathematical computations        |
| **CSV**            | Quiz data management             |

## ⚙️ Installation

Follow these steps to run WvW on your machine:

### Prerequisites
- **Operating System**: Windows (for `pycaw` volume control; adaptable for other OS with tweaks).
- **Hardware**: Webcam (for hand tracking), speakers (for audio features).
- **Python Version**: 3.7.9 

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/nyatihinesh/Witness_Vision_Wonders.git
   cd Witness_Vision_Wonders
2. **Install Libraries**
   Run the commands above one-by-one in your terminal or command prompt to install all dependencies.

   ```bash
   pip install opencv-python
   pip install cvzone
   pip install mediapipe
   pip install gtts
   pip install pygame
   pip install pycaw
   pip install numpy
3. **Run the Application**
   Ensure your webcam is connected and speakers are on.
   
   Execute the main script:
   ```bash
   python WvW.py

4. **Controls**
General: Press q to exit most modules.

Ping-Pong: Use r to restart after game over.

Press Game: Use r to restart after time’s up.

Follow on-screen prompts or hand gestures (e.g., thumb-index distance for volume).

5. **Troubleshooting**
Webcam Issues: Check cv.VideoCapture(0)—change to 1 if using an external camera.

Audio Errors: Ensure speakers are active; pycaw works only on Windows.



