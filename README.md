# 🔥 Naruto VFX using Computer Vision

A real-time **Naruto-style visual effects (VFX)** system built using **Python**, **OpenCV**, and **MediaPipe**.  
The application detects hand gestures through a webcam and overlays animated effects like **Rasengan** and **Chidori** onto the user's hand in real time.

---

## 🚀 Features

- Real-time hand tracking using MediaPipe
- Gesture-based VFX activation
- Animated frame-based visual effects
- Dynamic scaling (growing effect)
- Multi-hand detection (Left & Right)
- Alpha blending for transparent overlays
- Lightweight and modular design

---

## 🧠 How It Works

1. Webcam captures live video frames  
2. Frames are flipped for mirror view  
3. MediaPipe detects hand landmarks  
4. Custom logic checks if the hand is open  
5. Animation frames are loaded from folders  
6. Visual effect is positioned on the wrist  
7. Effect scales dynamically while the hand remains open  
8. Frames are rendered continuously in real time  

---

## 🛠 Tech Stack

- **Python**
- **OpenCV (cv2)**
- **MediaPipe**
- **NumPy**
- **Math / OS / Sys (Built-in modules)**

---

## 🐍 Python Version

```bash
Python 3.9
```

## 📦 Installation
```bash
pip install opencv-python mediapipe numpy
```


## ▶️ Run the Project
python main.py
Press:"ESC" to exit the application.

## 📁 Project Structure
Naruto-VFX/
│
├── main.py
├── Utility.py
│
├── Effects/
│   ├── Effect1/        # Rasengan animation frames
│   └── Effect2/        # Chidori animation frames
│
└── README.md

## This project is intended for educational purposes, portfolio demonstration, and computer vision experimentation.

