# 🧭 Lesson 4 Activity: Servo Motor Control via PySide6 GUI

## 🧠 Objective:
Control a servo motor connected to Arduino by sending angle values (0–180°) from a PySide6 GUI.

---

## 🛠️ Hardware Used:
- Arduino board
- Servo motor (connected to pin 9)
- USB connection for serial communication

---

## 🖥️ Software Overview

### ✅ Python GUI (`python/gui/Lesson 4 Activity/activity.py`)

```python
from PySide6.QtWidgets import QApplication, QMainWindow
from my_gui import Ui_MainWindow  # Generated from Qt Designer
import serial
import time

arduino = serial.Serial(port='/dev/cu.usbserial-140', baudrate=9600, timeout=1)
time.sleep(2)  # Let Arduino reset

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Trigger when the user finishes typing an angle
        self.ui.spinBox.editingFinished.connect(self.servo_control)

    def servo_control(self):
        angle = self.ui.spinBox.value()  # Get value from spin box
        self.ui.label_3.setText(f"The Angle is: {angle}")  # Update label
        arduino.write(f"{angle}\n".encode())  # Send angle as text

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
```

### 💡 Notes:
- `spinBox.editingFinished` triggers only after typing is done.
- `f"{angle}\n".encode()` sends the number with a newline, perfect for `Serial.parseInt()` on Arduino.

---

### ✅ Arduino Sketch (`/arduino/sketches/L4_Activity_servo/L4_Activity_servo.ino`)

```cpp
#include <Servo.h>

int servo_pin = 9;
Servo myServo;

void setup() {
  Serial.begin(9600);  // Start serial communication
  myServo.attach(servo_pin);  // Attach servo to pin
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();              // Read angle as integer
    angle = constrain(angle, 0, 180);           // Clamp value to servo range
    Serial.print("Received data: ");
    Serial.println(angle);                      // Debug print
    myServo.write(angle);                       // Move servo

    while (Serial.available()) Serial.read();   // Clear leftover data
  }
}
```

### 💡 Notes:
- `Serial.parseInt()` reads the full number sent from Python.
- `constrain(angle, 0, 180)` ensures angle stays within safe limits.
- `Serial.println()` is helpful for debugging in the Serial Monitor.


