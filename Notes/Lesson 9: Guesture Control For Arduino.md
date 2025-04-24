# Lesson 9: Guesture Control For Arduino

### 🧠 **Original Code Recap**
In the original code, you used **MediaPipe** to detect hands and count how many fingers are up using `get_finger_states()`. You displayed the result (`finger_states`) visually on the screen using OpenCV, but **you didn't connect this detection to any physical hardware**.

---

### ⚙️ **What We Learned in Lesson 8**
In **Lesson 8**, you learned how to:
- **Send data from Python to an Arduino** using **serial communication**.
- Use the `pyserial` library to open a communication channel with the Arduino.
- Send specific **bytes** that the Arduino can understand and respond to.

---

### ➕ **What's Added in the Modified Code**

#### ✅ 1. **Serial Connection Setup**
```python
arduino = serial.Serial(port='/dev/cu.usbserial-1140', baudrate=9600, timeout=1)
time.sleep(2)  # Give Arduino time to reset
```
- This line opens a **serial connection** to the Arduino through the USB port (`/dev/cu.usbserial-1140`).
- The `baudrate=9600` must match the baud rate in your Arduino sketch.
- `time.sleep(2)` gives the Arduino enough time to reset after the connection is established. This is important, or the Arduino might miss the first few commands.

#### ✅ 2. **Sending Gestures to Arduino**
```python
arduino.write(b'0')  # example inside detect_gesture()
```
- In the `detect_gesture()` function, you added `arduino.write(b'X')` commands.
- This sends a **byte** (`b'0'`, `b'1'`, ..., `b'5'`) to the Arduino whenever a specific finger gesture is detected.
- These bytes act like **commands** that your Arduino can decode and respond to—like turning on LEDs, playing buzzers, moving servos, etc.

---

### 🧩 **Putting It All Together**
So now, instead of just *seeing* the detected gesture on screen, you're using what you learned from **Lesson 8** to:
- **Send commands** to your Arduino
- **Physically control devices** based on your hand gestures


[lesson9_guesture_control_for_arduino.py](../python/opencv/lesson9_guesture_control_for_arduino.py)

```python
import cv2
import mediapipe as mp
import serial
import time

# Connect to the Arduino through the USB port
arduino = serial.Serial(port='/dev/cu.usbserial-1140', baudrate=9600, timeout=1)
time.sleep(2)  # Give Arduino time to reset

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Gesture utility
def get_finger_states(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb: check x axis
    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers: check y axis
    for tip_id in tips[1:]:
        if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

def detect_gesture(finger_states):
    if finger_states == [0, 0, 0, 0, 0]:
        arduino.write(b'0') # -------------------> Sends '0' to the Arduino
        return "Zero"
    elif finger_states == [0, 0, 0, 0, 1]:
        arduino.write(b'1')
        return "One"
    elif finger_states == [0, 0, 0, 1, 1]:
        arduino.write(b'2')
        return "Two"
    elif finger_states == [0, 0, 1, 1, 1]:
        arduino.write(b'3')
        return "Three"
    elif finger_states == [0, 1, 1, 1, 1]:
        arduino.write(b'4')
        return "Four"
    elif finger_states == [1, 1, 1, 1, 1]:
        arduino.write(b'5')
        return "Five"
    else:
        return "Unknown"

# Open webcam
cap = cv2.VideoCapture(1)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # Flip and convert
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process frame
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Draw landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Detect gesture
                finger_states = get_finger_states(hand_landmarks)
                gesture = detect_gesture(finger_states)

                # Print gesture on screen
                cv2.putText(frame, f'Gesture: {gesture}', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('MediaPipe Gesture', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

```

---

### 📟 Now we move on to the **Arduino side of the project**

Your Python–OpenCV script sends gesture data (`'0'` to `'5'`) through **serial communication**. The Arduino listens for that data and reacts to it.

Let’s break down what’s happening:

---

### 🛑 **Why not use pin 1?**
Pin **1** on the Arduino (along with pin 0) is used for **Serial communication** (`TX/RX`).  
- If you use pin 1 as a regular output while also using `Serial.begin()`, you can cause **conflicts or unexpected behavior**.
- That’s why your LEDs or outputs start from **pin 2** and go to pin 6 instead.

---

### 📥 `Serial.read();`
```cpp
char gesture = Serial.read();
```
- This reads **one character** that was sent over the serial connection (e.g., `'3'` from Python).
- It’s stored in the variable `gesture`, which you then use to decide what to do next.

---

### 🔀 The `if` statements
```cpp
if (gesture == '0') {
  control(0, 0, 0, 0, 0);
}
...
```
- Each `if` checks which gesture was received.
- Based on the gesture (e.g., `'1'`, `'2'`, etc.), it calls the `control()` function with different values.
- These values represent the brightness (0–255) of each LED (or output pin).

So for example:
- `'1'` → Only the first LED (pin 2) turns on at full brightness.
- `'3'` → Pins 2, 3, and 4 are turned on.
- `'5'` → All five pins (2–6) are on.

---

### 🧠 `control()` function
```cpp
void control(int a, int b, int c, int d, int e) {
  analogWrite(2, a);
  analogWrite(3, b);
  analogWrite(4, c);
  analogWrite(5, d);
  analogWrite(6, e);
}
```
- This function receives five values and writes them to pins 2 through 6 using `analogWrite`.
- `analogWrite(pin, value)` controls the **PWM signal**, letting you dim LEDs or control motor speeds.
- By using this function, your code stays **clean and organized** instead of repeating the same `analogWrite()` lines over and over.

[L9_gesture_control_for_arduino.ino](../arduino/sketches/L9_gesture_control_for_arduino/L9_gesture_control_for_arduino.ino)

```cpp
void setup() {
  // Initialize pins 2 to 6 as OUTPUT
  for (int i = 2; i <= 6; i++) {
    pinMode(i, OUTPUT);
  }

  Serial.begin(9600);  // Start the serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char gesture = Serial.read();

    if (gesture == '0') {
      control(0, 0, 0, 0, 0);
    } else if (gesture == '1') {
      control(255, 0, 0, 0, 0);
    } else if (gesture == '2') {
      control(255, 255, 0, 0, 0);
    } else if (gesture == '3') {
      control(255, 255, 255, 0, 0);
    } else if (gesture == '4') {
      control(255, 255, 255, 255, 0);
    } else if (gesture == '5') {
      control(255, 255, 255, 255, 255);
    } else {
      control(0, 0, 0, 0, 0); // default
    }
  }
}

void control(int a, int b, int c, int d, int e) {
  analogWrite(2, a);
  analogWrite(3, b);
  analogWrite(4, c);
  analogWrite(5, d);
  analogWrite(6, e);
}

```

---

