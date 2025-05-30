### Lesson 1: Arduino Serial Communication

- `Serial.begin(9600)`: Starts a "talking line" between your Arduino and computer.
- `Serial.read()`: Reads one character from the "talking line" (like grabbing a letter from the inbox).
- `Serial.write()`: Sends a letter back to the computer (writing something to the talking line).
- `Serial.available() > 0`: Checks if there’s a letter in the inbox waiting to be read.

### Lesson 2: Python Serial Communication

- `import serial`: Lets Python talk to Arduino through USB.  
- `serial.Serial(...)`: Connects Python to Arduino using the correct port and baud rate.  
- `serial.write()`: Sends bytes only to Arduino (use `.encode()` to convert string to bytes).  
- `ls /dev/cu.usb*`: Terminal command to find your Arduino's port on Mac*

### Lesson 3: GUI App to Control Arduino

- **PySide6 Designer**: Drag-and-drop tool to design your GUI visually.  
- `.ui` file: Saved design file from PySide6 Designer.  
- `pyside6-uic led_gui.ui -o led_gui.py`: Converts the design to usable Python code.  
- `button.clicked.connect(func)`: Links a button press to a Python function (no parentheses!).  
- `arduino.write(b'1')`: Sends a byte (`'1'` or `'0'`) to control the LED from Python.  
- `time.sleep(2)`: Waits 2 seconds to let the Arduino finish resetting before sending data.

### **Lesson 4: Extend GUI for More Controls**

####  Arduino (Important Commands)
- `Serial.readStringUntil('\n')`: Read full line from Python.
- `data.startsWith("RGB")`: Check if command is for RGB.
- `data.indexOf(',')`: Find comma positions to split values.
- `data.substring(...).toInt()`: Extract RGB values from string.
- `analogWrite(pin, value)`: Set brightness/tone (RGB & buzzer).
- `digitalWrite(pin, HIGH/LOW)`: Turn LED on/off.

####  Python (Important Concepts)
- `slider.value()`: Get RGB value from GUI.
- `cmd = f"RGB,{r},{g},{b}"`: Format RGB command string.
- `arduino.write(cmd.encode())`: Send command to Arduino.
- `.currentTextChanged.connect(...)`: Dropdown signal for buzzer.
- `.actionTriggered.connect(...)`: Slider signal for RGB.

####  Serial Commands to Send
- LED: `LED,on\n` or `LED,off\n`
- RGB: `RGB,255,0,128\n`
- Buzzer: `BUZ,off\n`, `BUZ,beep\n`, `BUZ,alarm\n`

#### Lesosn 4.1 Activity, Servo Motors
- `Serial.parseInt()` reads the full number sent from Python.
- `constrain(angle, 0, 180)` ensures angle stays within safe limits.
- `Serial.println()` is helpful for debugging in the Serial Monitor.


### **Lesson 4 Activity 2: Distance Sensor GUI**

#### 🔧 Arduino Code (Key Parts)

- `trigPin = OUTPUT`, `echoPin = INPUT`: Trig sends sound, Echo listens.  
- `digitalWrite(trigPin, HIGH); delayMicroseconds(10);`: Triggers a 10μs pulse.  
- `pulseIn(echoPin, HIGH)`: Measures time until echo is received.  
- `distance = duration * 0.034 / 2;`: Converts time to cm.  
- `Serial.println(distance);`: Sends distance to Python via USB.

---

#### 🐍 Python Code (PySide6 + Serial)

- `serial.Serial(...)`: Connect to Arduino.  
- `arduino.in_waiting`: Checks if Arduino sent data.  
- `arduino.readline().decode().strip()`: Reads and cleans distance value.

---

#### 🖥 GUI Logic (PySide6)

- `QTimer()`: Repeats an action on a schedule.  
- `timeout.connect(func)`: Runs a function every tick.  
- `timer.start(100)`: Updates distance every 100ms.  
- `label.setText(...)`: Displays live distance in the GUI.

---

### Lesson 5: OpenCV Camera & Drawing

#### 📷 5.1 OpenCV Camera

- **Install OpenCV**:  
  Run `pip install opencv-python` to install the OpenCV library.

- **Open the Camera**:  
  Use `cap = cv2.VideoCapture(1)` to open the camera (use `0` for the default camera).

- **Read Camera Feed**:  
  `ret, frame = cap.read()` reads a single frame from the camera. `ret` is True if successful, `frame` is the captured image.

- **Show the Feed**:  
  Display the captured frame with `cv2.imshow("Webcam", frame)` in a window.

- **Press 'q' to Quit**:  
  Use `if cv2.waitKey(1) & 0xFF == ord('q'): break` to quit the loop when 'q' is pressed.

- **Cleanup**:  
  After exiting, release the camera with `cap.release()` and close all windows with `cv2.destroyAllWindows()`.

---

#### 5.2 OpenCV Drawing

- **Draw a Rectangle**:  
  Use `cv2.rectangle(frame, (50, 50), (200, 200), (255, 0, 0), 2)` to draw a blue rectangle (Note: Color is in BGR format, not RGB) on the camera feed. `(50, 50)` is the top-left corner, `(200, 200)` is the bottom-right corner, and `2` is the line thickness.

- **Draw a Circle**:  
  Use `cv2.circle(frame, (300, 200), 50, (0, 255, 0), 3)` to draw a green circle. `(300, 200)` is the center, `50` is the radius, and `3` is the border thickness.

- **Add Text**:  
  Use `cv2.putText(frame, 'Hello OpenCV', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)` to add the text "Hello OpenCV" at position `(50, 400)` in white color with a size of 1.

- **Show Everything**:  
  Finally, display the updated frame with `cv2.imshow("Webcam", frame)`.
---

### Lesson 6: Color Detection
- `cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`: Convert frame to HSV.
- Define two red ranges using `np.array([H, S, V])`.
- `cv2.inRange(hsv, lower, upper)`: Create masks for red.
- `cv2.bitwise_or(mask1, mask2)`: Combine both masks.
- `cv2.bitwise_and(frame, frame, mask=mask)`: Show only red areas.

---

### **Lesson 7: Contours & Basic Hand Detection**

#### 🧠 MediaPipe Setup

- `import mediapipe as mp`: Brings in the MediaPipe library to use hand tracking tools.
- `mp_drawing = mp.solutions.drawing_utils`: Lets us draw hand points and lines on the screen.
- `mp_drawing_styles = mp.solutions.drawing_styles`: Optional styles to make the hand drawing look nicer.
- `mp_hands = mp.solutions.hands`: Shortcut to access the hand-tracking feature.

---

#### ✋ Start Hand Detection

- `hands = mp_hands.Hands()`: Turns on the hand detector. It will look for hands in each video frame.

---

#### 🔄 Flip + Convert Image

```python
image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
```

- `cv2.flip(image, 1)`: Flips the image left to right — like looking in a mirror.
- `cv2.cvtColor(..., cv2.COLOR_BGR2RGB)`: Changes the color format because MediaPipe needs RGB, but OpenCV uses BGR.

---

#### 🤖 Process the Frame

```python
results = hands.process(image)
```

- Checks the image for hands.
- If a hand is found, it saves the "landmarks" — little points on your fingers and palm.

---

#### 🎨 Draw the Hand

```python
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )
```

- `if results.multi_hand_landmarks`: Checks if any hands were found. Example if 2 hands are there in the camera it returns: [HandLandmark_1, HandLandmark_2]
- `for hand_landmarks in ...`: Loops through each hand (in case you have two).
- `mp_drawing.draw_landmarks(...)`: Draws dots on your hand and connects them with lines — so you can *see* the hand shape on screen.

---

#### 🎨 Convert Image Back

```python
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
```

- Turns the image back to BGR so OpenCV can show it properly in a window.

---

### Lesson 7.1: Contours

| Code | Explanation |
|------|-------------|
| `cv2.VideoCapture(1)` | Opens your webcam (try 0 if 1 doesn't work) |
| `cv2.cvtColor` | Converts image to grayscale |
| `cv2.GaussianBlur` | Smooths image to remove noise |
| `cv2.threshold` | Turns grayscale into black & white shapes |
| `cv2.findContours` | Finds the outlines of the shapes |
| `cv2.drawContours` | Draws the outlines on your image |
| `cv2.imshow` | Shows the camera + contour drawing |
| `cv2.waitKey(1)` | Updates the image every frame |
| `cap.release()` | Closes webcam properly |
| `cv2.destroyAllWindows()` | Closes all windows |

