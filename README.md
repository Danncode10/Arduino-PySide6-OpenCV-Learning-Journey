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
