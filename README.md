# Arduino + PySide6 + OpenCV Learning Journey

This repository documents my personal learning journey as I integrate **Arduino**, **PySide6 (Qt Designer)**, and **OpenCV** to build gesture-controlled hardware projects.

I started with basic Arduino knowledge and some GUI development experience using PySide6. My goal is to use **hand gesture detection via OpenCV** to control real-world devices like LEDs, buzzers, and RGB lights connected to an Arduino board.

---

## 🚀 Project Goal

- Build a system where a Python application detects hand gestures using OpenCV (and MediaPipe) and sends commands to Arduino to control components.
- Combine GUI control with computer vision in a single Python interface using PySide6.

---

## ✅ Prerequisites

Before starting, make sure you have:

### 🧠 Knowledge
- Arduino basics (pinMode, analogWrite, Serial, sensors, LED, RGB, buzzer, etc.)
- Python basics
- Some experience with PySide6 and Qt Designer

### 🛠️ Tools & Software
- **Arduino IDE** (or equivalent)
- **Python 3.8+**
- **Libraries:**
  - `pyserial`
  - `PySide6`
  - `opencv-python`
  - `mediapipe` (for advanced gesture detection)

Install them via pip:

```bash
pip install pyserial PySide6 opencv-python mediapipe
```
### 🔧 Part 1: Arduino + Python Serial Communication

#### **Lesson 1: Arduino Serial Communication Refresher**
- Review `Serial.begin()`, `Serial.read()`, `Serial.write()`
- Understand how Arduino receives and processes serial commands  
- **Mini Task**: Send `1` and `0` from Serial Monitor to turn LED on/off

#### **Lesson 2: Python Serial Communication**
- Install and use `pyserial` in Python
- Send serial data from Python to Arduino
- Handle serial reading/writing in Python  
- **Mini Task**: Python script to turn LED on/off via serial

---

### 🖼️ Part 2: PySide6 + Arduino GUI

#### **Lesson 3: GUI App to Control Arduino**
- Create a basic PySide6 GUI with buttons
- Use Qt Designer to design UI layout
- Connect buttons to serial functions in Python  
- **Mini Task**: Click button in GUI to toggle LED on Arduino

#### **Lesson 4: Extend GUI for More Controls**
- Add sliders for RGB control
- Add buzzer toggle or dropdown for modes
- Use signal-slot system to connect UI elements to Arduino commands  
- **Mini Task**: GUI with LED toggle, RGB sliders, and buzzer control

---

### 🎥 Part 3: OpenCV Computer Vision

#### **Lesson 5: OpenCV Camera & Drawing**
- Open webcam using OpenCV
- Learn basic drawing: rectangles, circles, text  
- **Mini Task**: Draw a shape on the live webcam feed

#### **Lesson 6: Color Detection**
- Convert BGR to HSV color space
- Use `cv2.inRange()` for color masking
- Track colored objects in real-time  
- **Mini Task**: Detect and follow a red object

#### **Lesson 7: Contours & Basic Hand Detection**
- Detect hand using contours and convex hull
- Calculate finger count using defects  
- **Mini Task**: Show number of fingers on screen

#### **Lesson 8: MediaPipe Hands (Advanced Hand Tracking)**
- Use MediaPipe’s Hand module for easy and accurate tracking
- Detect hand landmarks and gestures (fist, palm, peace sign, etc.)  
- **Mini Task**: Print gesture name on screen

---

### 🤝 Part 4: Connecting CV to Arduino

#### **Lesson 9: Gesture Control for Arduino**
- Map gestures to commands (e.g., open palm = LED on)
- Send commands via serial to Arduino
- Combine OpenCV + MediaPipe + PySerial  
- **Mini Task**: Control LED with hand gestures

#### **Lesson 10: Full Integration - GUI + OpenCV + Arduino**
- Embed OpenCV webcam feed inside PySide6 GUI
- Add controls for switching modes (manual / gesture)
- Combine everything into one polished app  
- **Mini Task**: Build a full software that controls Arduino using gestures and GUI


## 🧑‍💻 Author

Made  by **Lester Dann G. Lopez**  
Follow me on my Arduino, GUI, and Computer Vision journey!

