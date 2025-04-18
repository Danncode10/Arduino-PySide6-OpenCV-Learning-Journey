### **Lesson 4: Extend GUI for More Controls + Distance Sensor**

---

#### 🟧 Arduino: Serial Communication + Logic

- `Serial.begin(9600)`: Start communication with Python.
- `Serial.readStringUntil('\n')`: Read full command sent by Python until a newline (`\n`) is received.
- `data.startsWith("RGB")`: Check if the incoming string is an RGB command.
- `data.indexOf(',')`: Find the position of commas (used to split RGB values).
- `data.substring(...).toInt()`: Extract numbers from the string and convert to integer.
- `analogWrite(pin, value)`: Set brightness for RGB LEDs or buzzer strength (PWM).
- `digitalWrite(pin, HIGH/LOW)`: Turn components ON or OFF.
- `pulseIn(echoPin, HIGH)`: Measure how long it takes for an ultrasonic wave to bounce back.
- `distance = duration * 0.034 / 2`: Convert time (in microseconds) to distance in **centimeters**.
- `Serial.println(distance)`: Send the distance value to Python for display.

---

#### 🟦 Python: GUI + Serial Communication

- `import serial`: Let Python talk to Arduino over USB.
- `arduino = serial.Serial(...)`: Connect to Arduino on the right port with the correct speed.
- `time.sleep(2)`: Wait for Arduino to reset before sending/receiving data.
- `cmd = f"RGB,{r},{g},{b}"`: Format the RGB command string.
- `arduino.write(cmd.encode())`: Send the command (must be bytes).
- `.decode().strip()`: Clean the message received from Arduino (remove `\n`, spaces).
- `.in_waiting`: Check if Arduino has sent new data.
- `.readline()`: Read one full line of data from Arduino (until `\n`).
- `slider.value()`: Get the current value from a GUI slider.
- `.valueChanged.connect(...)`: Trigger function when the slider changes.
- `QTimer()`: Used to repeat tasks (like updating sensor data).
- `.timeout.connect(func)`: Call a function every few milliseconds.
- `.start(100)`: Start the timer with an interval of 100 ms (0.1 seconds).

---

#### 🧪 Serial Commands from Python to Arduino

- **LED**:  
  `LED,on\n` → Turn LED on  
  `LED,off\n` → Turn LED off

- **RGB LED**:  
  `RGB,255,0,128\n` → Set Red to 255, Green to 0, Blue to 128

- **Buzzer**:  
  `BUZ,off\n` → Turn buzzer off  
  `BUZ,beep\n` → Short beep  
  `BUZ,alarm\n` → Continuous sound

---

#### ⚙️ Lesson 4.1 Activity: Servo Motor

- `Serial.parseInt()`: Reads full number like an angle (e.g., 90).
- `constrain(angle, 0, 180)`: Make sure the servo doesn’t go too far.
- `myServo.write(angle)`: Move servo to specific angle.
- `Serial.println(...)`: Useful to check what data is received.

---

#### 📏 Lesson 4.2 Activity: Distance Sensor + Buzzer + GUI

- **Ultrasonic Sensor**:  
  Sends a sound wave and listens for it to bounce back.
- **Distance Calculation**:  
  `distance = duration * 0.034 / 2`  
  0.034 cm/us is the speed of sound. Divide by 2 because sound travels back and forth.
- **Serial Output**:  
  `Serial.println(distance)` sends the distance to Python.
- **Python GUI**:  
  Uses a `QTimer` to check for new distance values every 100 ms.
- **Display in GUI**:  
  `.setText(f"Distance: {line} cm")` shows the value on a label.

---

### ✅ Summary (TL;DR)

| Topic | Key Concepts |
|-------|--------------|
| **Arduino Serial** | `Serial.begin()`, `Serial.println()`, `pulseIn()`, `analogWrite()`, `substring().toInt()` |
| **Distance Formula** | `distance = duration * 0.034 / 2` |
| **Python Serial** | `arduino.readline().decode().strip()`, `arduino.in_waiting`, `QTimer()` |
| **PySide6 GUI** | `slider.value()`, `.connect()`, `.setText()` |

