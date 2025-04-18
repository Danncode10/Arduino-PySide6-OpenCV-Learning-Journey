import cv2  # OpenCV library for image/video processing
import mediapipe as mp  # MediaPipe library for hand detection

# Initialize drawing utilities and hand detection model from MediaPipe
mp_drawing = mp.solutions.drawing_utils  # Utility to draw hand landmarks
mp_drawing_styles = mp.solutions.drawing_styles  # Optional styling for drawing
mphands = mp.solutions.hands  # Hand detection module from MediaPipe

# Open video capture from the camera (camera index 1)
cap = cv2.VideoCapture(1)  # Use camera with index 1 (adjust if needed)
hands = mphands.Hands()  # Initialize hand detection model

while True:
    data, image = cap.read()  # Capture a frame from the camera

    # Flip the image horizontally to mirror it (like in a mirror)
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # Process the image to detect hand landmarks
    results = hands.process(image)

    # Convert the image back to BGR for OpenCV (as OpenCV uses BGR format)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        # Loop through all detected hands (in case more than one hand is detected)
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the landmarks and connections on the image
            mp_drawing.draw_landmarks(
                image,  # The image on which to draw
                hand_landmarks,  # The_
