from PySide6.QtWidgets import QApplication, QMainWindow
from extended_gui import Ui_MainWindow  # Auto-generated from .ui file
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


        # Signals:
        self.ui.btn_led_toggle.toggled.connect(self.led_on)

        self.ui.red_scroll.actionTriggered.connect(self.red)
        self.ui.green_scroll.actionTriggered.connect(self.green)
        self.ui.blue_scroll.actionTriggered.connect(self.blue)

        self.ui.comboBox.currentTextChanged.connect(self.buzzer_command)

        # Custom Variables
        self.red_ = 0
        self.green_ = 0
        self.blue_ = 0

    # LED ########################
    def led_on(self, checked):
        if checked:
            print("LED ON")
            arduino.write(b'LED,on\n')
        else:
            print("LED OFF")
            arduino.write(b'LED,off\n')

    # RGB ########################

    def red(self):
        self.red_ = self.ui.red_scroll.value()
        self.ui.red_value.display(self.red_)
        self.rgb_color(self.red_, self.green_, self.blue_)

    def green(self):
        self.green_ = self.ui.green_scroll.value()
        self.ui.green_value.display(self.green_)
        self.rgb_color(self.red_, self.green_, self.blue_)

    def blue(self):
        self.blue_ = self.ui.blue_scroll.value()
        self.ui.blue_value.display(self.blue_)
        self.rgb_color(self.red_, self.green_, self.blue_)

    def rgb_color(self, r, g, b):
        cmd = f"RGB,{r},{g},{b}"
        arduino.write(cmd.encode())

    # BUZZER #######################

    def buzzer_command(self, text):
        command = f"BUZ,{text.lower()}\n"
        print(f"Sending buzzer command: {command.strip()}")
        arduino.write(command.encode())


# Create the app
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
