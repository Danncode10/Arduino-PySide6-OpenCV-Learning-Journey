from PySide6.QtWidgets import QApplication, QMainWindow
from led_gui import Ui_MainWindow  # Auto-generated from .ui file
import serial
import time

# Connect to the Arduino through the USB port
arduino = serial.Serial(port='/dev/cu.usbserial-140', baudrate=9600, timeout=1)
time.sleep(2)  # Give Arduino time to reset

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the signals (no parentheses here!)
        self.ui.on_button.clicked.connect(self.turn_on)
        self.ui.off_button.clicked.connect(self.turn_off)

    def turn_on(self):
        word = 'ON'
        self.ui.label_2.setText(f"The LED is {word}")
        arduino.write(b'1')  # Send 1 to turn on

    def turn_off(self):
        word = 'OFF'
        self.ui.label_2.setText(f"The LED is {word}")
        arduino.write(b'0')  # Send 0 to turn off

# Create the app
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
