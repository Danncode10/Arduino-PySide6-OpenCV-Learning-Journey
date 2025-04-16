from PySide6.QtWidgets import QApplication, QMainWindow
from my_gui import Ui_MainWindow  # Auto-generated from .ui file
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
        self.ui.spinBox.editingFinished.connect(self.servo_control)

    def servo_control(self):
        angle = self.ui.spinBox.value()
        self.ui.label_3.setText(f"The Angle is: {angle}")
        arduino.write(f"{angle}\n".encode())

# Create the app
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
