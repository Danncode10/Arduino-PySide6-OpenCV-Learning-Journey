import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and Drawing utilities
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Set up video capture
cap = cv2.VideoCapture(0)

# Initialize Hands detector
hands = mp_hands.Hands()

while True:
    # Read a frame from the webcam
    ret, image = cap.read()

    if not ret:
        break

    # Flip the image horizontally for a mirror effect
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # Process the frame and get hand landmarks
    results = hands.process(image)

    # Convert the image color back to BGR for OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # If hand landmarks are detected, draw them on the image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Display the image with landmarks
    cv2.imshow('Handtracker', image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
