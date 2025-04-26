import cv2
import serial
import mediapipe as mp
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6 import uic
from PySide6.QtGui import QImage, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI (generated from Qt Designer)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up Arduino
        self.arduino = serial.Serial(port='/dev/cu.usbserial-1140', baudrate=9600, timeout=1)

        # Set up OpenCV and MediaPipe
        self.cap = cv2.VideoCapture(1)
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

        # Set up QTimer to update the webcam feed
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30ms

        # Connect signals to methods
        self.ui.comboBox_mode.currentIndexChanged.connect(self.change_mode)
        self.ui.button_led_off.clicked.connect(self.turn_led_off)
        self.ui.button_led_on.clicked.connect(self.turn_led_on)

    def change_mode(self, index):
        if index == 0:  # Manual Mode
            print("Manual Mode")
            self.manual_mode()
        else:  # Gesture Mode
            print("Gesture Mode")
            self.gesture_mode()

    def manual_mode(self):
        # Here, manual controls for the LED will work
        pass

    def gesture_mode(self):
        # In this mode, gestures will control the LED
        pass

    def turn_led_on(self):
        self.arduino.write(b'1')  # Sends '1' to turn the LED ON
        print("LED ON")

    def turn_led_off(self):
        self.arduino.write(b'0')  # Sends '0' to turn the LED OFF
        print("LED OFF")

    def update_frame(self):
        # Capture frame-by-frame from webcam
        success, frame = self.cap.read()
        if not success:
            return

        # Flip frame, convert to RGB for MediaPipe
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe
        result = self.hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        # Convert OpenCV frame to QImage
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_BGR888)

        # Update the Label to show the webcam frame
        self.ui.webcam.setPixmap(QPixmap.fromImage(q_image))

# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
