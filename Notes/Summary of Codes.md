### Lesson 1: Arduino Serial Communication

- `Serial.begin(9600)`: Starts a "talking line" between your Arduino and computer.
- `Serial.read()`: Reads one character from the "talking line" (like grabbing a letter from the inbox).
- `Serial.write()`: Sends a letter back to the computer (writing something to the talking line).
- `Serial.available() > 0`: Checks if there’s a letter in the inbox waiting to be read.

### Lesson 2: Python Serial Communication

- `import serial`: Lets Python talk to Arduino through USB.  
- `serial.Serial(...)`: Connects Python to Arduino using the correct port and baud rate.  
- `serial.write()`: Sends bytes only to Arduino (use `.encode()` to convert string to bytes).  
- `ls /dev/cu.usb*`: Terminal command to find your Arduino's port on Mac*

### Lesson 3: GUI App to Control Arduino

- **PySide6 Designer**: Drag-and-drop tool to design your GUI visually.  
- `.ui` file: Saved design file from PySide6 Designer.  
- `pyside6-uic led_gui.ui -o led_gui.py`: Converts the design to usable Python code.  
- `button.clicked.connect(func)`: Links a button press to a Python function (no parentheses!).  
- `arduino.write(b'1')`: Sends a byte (`'1'` or `'0'`) to control the LED from Python.  
- `time.sleep(2)`: Waits 2 seconds to let the Arduino finish resetting before sending data.

