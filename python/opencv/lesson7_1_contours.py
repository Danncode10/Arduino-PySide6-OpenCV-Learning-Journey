import cv2

# Open webcam (0 or 1 depending on your camera index)
cap = cv2.VideoCapture(0)  # You can try 0 if 1 doesn't work

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (black & white version)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur the image to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply threshold to get binary image (black & white shapes)
    ret, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)

    # Find contours on the threshold image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw all contours in green
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Show the result
    cv2.imshow("Contours", frame)
    cv2.imshow("Threshold", thresh)

    # Break on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
