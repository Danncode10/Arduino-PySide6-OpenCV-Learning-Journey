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
