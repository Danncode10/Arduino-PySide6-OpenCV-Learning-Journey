from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from my_ui import Ui_MainWindow
import serial
import time

# Setup serial
arduino = serial.Serial('/dev/cu.usbserial-130', 9600, timeout=1)
time.sleep(2)  # Let Arduino reset

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Update every 100ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_distance)
        self.timer.start(100)

    def update_distance(self):
        if arduino.in_waiting:
            line = arduino.readline().decode().strip()
            self.ui.label.setText(f"Distance: {line} cm")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
