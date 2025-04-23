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
