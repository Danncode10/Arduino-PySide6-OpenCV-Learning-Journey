# import cv2
#
# cap = cv2.VideoCapture(1)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # Show the frame
#     cv2.imshow("Webcam", frame)
#
#     # Exit on 'q' key
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# Example 2

import cv2

# Start camera
cap = cv2.VideoCapture(1)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Draw a blue rectangle
    cv2.rectangle(frame, (50, 50), (200, 200), (255, 0, 0), 2)

    # Draw a green circle
    cv2.circle(frame, (300, 200), 50, (0, 255, 0), 3)

    # Write some white text
    cv2.putText(frame, 'Hello OpenCV', (50, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the result in a window
    cv2.imshow("Webcam", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Turn off the camera and close the window
cap.release()
cv2.destroyAllWindows()

