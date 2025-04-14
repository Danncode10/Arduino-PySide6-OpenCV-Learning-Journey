
# **Lesson 2: Python Serial Communication**

## 🧠 Goal:
Learn how to send data from a Python script to the Arduino using pyserial, just like you did using the Serial Monitor.

---

## 🔧 Install pyserial
Open your terminal (or VS Code terminal) and run:

```bash
pip install pyserial
```

This library lets Python talk to the Arduino over USB.

---

## 🧰 First, How Do I Find My Arduino Port?
Before running any Python code, you need to know which USB port your Arduino is connected to.

On Mac, open Terminal and run:

```bash
ls /dev/cu.usb*
```

You'll see something like:

```
/dev/cu.usbserial-140
```

⚠️ **Copy that full path!** That’s what you use in your Python code as the `port=` value.

---

💥 **WARNING: Close Serial Monitor!**

Important: If your Serial Monitor (in the Arduino IDE) is open, Python will **NOT** be able to talk to the Arduino.

❌ **Error you’ll see:**  
`serial.serialutil.SerialException: [Errno 16] Resource busy`

So, before running your Python script, make sure to:  
✅ **Close Serial Monitor**

---

## 🧠 Your Python Code (With Explanations)

**`/python/integration/led_control.py`**

```python
import serial  # Library to talk to the Arduino
import time    # Library to wait/pause

# Connect to the Arduino through the USB port
arduino = serial.Serial(port='/dev/cu.usbserial-140', baudrate=9600, timeout=1)

time.sleep(2)  # Wait 2 seconds for Arduino to reset after opening the connection

# Function to send a command (like '1' or '0') to the Arduino
def send_command(cmd):
    arduino.write(cmd.encode())  # Turn '1' or '0' into bytes and send it
    print(f"Sent: {cmd}")        # Print what we sent for confirmation

# Loop to ask user for input over and over again
while True:
    answer = str(input("Enter Values (1 or 0): "))  # Ask user for input

    send_command(answer)  # Send the value to the Arduino

    if answer == 'stop':  # If user types 'stop', exit the loop
        break

time.sleep(1)  # Wait a bit before the script ends
```

# led_control.py

import serial  # Library to talk to the Arduino
import time    # Library to wait/pause

# Connect to the Arduino through the USB port
arduino = serial.Serial(port='/dev/cu.usbserial-140', baudrate=9600, timeout=1)

time.sleep(2)  # Wait 2 seconds for Arduino to reset after opening the connection

# Function to send a command (like '1' or '0') to the Arduino
def send_command(cmd):
    arduino.write(cmd.encode())  # Turn '1' or '0' into bytes and send it
    print(f"Sent: {cmd}")        # Print what we sent for confirmation

# Loop to ask user for input over and over again
while True:
    answer = str(input("Enter Values (1 or 0): "))  # Ask user for input

    send_command(answer)  # Send the value to the Arduino

    if answer == 'stop':  # If user types 'stop', exit the loop
        break

time.sleep(1)  # Wait a bit before the script ends


---

## 🧃 Simple Explanation (Line by Line)

| Line                                | What It Does (Like You're 5)                          |
|-------------------------------------|--------------------------------------------------------|
| `import serial`                     | Lets Python talk to Arduino over USB                  |
| `import time`                       | Lets us pause/wait a few seconds                      |
| `serial.Serial(...)`               | This opens the USB connection to Arduino              |
| `time.sleep(2)`                     | Arduino resets when you connect—give it 2 sec to wake up |
| `def send_command(cmd):`           | A mini machine that takes your input and sends it to Arduino |
| `arduino.write(cmd.encode())`      | Turns your input ('1' or '0') into bytes Arduino understands |
| `while True:`                       | This loop keeps asking you for new input forever (until you stop it) |
| `input("Enter Values (1 or 0): ")` | Shows a message asking you to type '1', '0', or 'stop' |
| `if answer == 'stop': break`       | If you type 'stop', the program ends nicely           |
| `time.sleep(1)`                     | Wait a bit before closing (totally optional)          |

---

## 🧪 What Should Happen?

Run the script:

```bash
python python/integration/led_control.py
```

- Type `1` → LED turns **ON**  
- Type `0` → LED turns **OFF**  
- Type `stop` → Python exits the program

---

## ✅ Mini Task:
Try running the script and turning your LED on/off using keyboard input. Make sure to:

- Upload the Arduino code from **Lesson 1**
- Close the **Serial Monitor**
- Use the correct **USB port path** in Python

---

Exactly! You've got the core ideas perfectly. Here's a quick summary of what you just said, cleaned up for your notes or PDF:

---

## ✅ **Lesson 2 Summary – Python Serial Communication**

### 💬 What I Learned:

1. **`import serial`**
   - This brings in the tool (library) that lets Python talk to devices like Arduino over USB.

2. **Create an Arduino object**
   ```python
   arduino = serial.Serial(port='your_port_here', baudrate=9600, timeout=1)
   ```
   - This opens the connection to the Arduino. It's like plugging a USB cable into your code.

3. **Send data using `serial.write()`**
   ```python
   arduino.write(b'1')  # sends the byte version of '1'
   ```
   - `serial.write()` only works with **bytes**, not regular strings.
   - That’s why we use `cmd.encode()` to turn a string (like `'1'`) into bytes before sending:
     ```python
     arduino.write(cmd.encode())
     ```

4. **How to find the correct port on Mac**
   - Use this command in the terminal:
     ```bash
     ls /dev/cu.usb*
     ```
   - You'll see something like:
     ```
     /dev/cu.usbserial-140
     ```
   - This is your Arduino's USB address. Use it as the `port=` value in your Python script.

5. **Important Tip**
   - Always **close the Serial Monitor** in the Arduino IDE before running the Python script.
   - Only one program can talk to the Arduino over USB at a time!

---

Let me know when you're ready to tackle **Lesson 3: PySide6 GUI to Control Arduino** — we’ll bring in buttons and make your software feel *real*. 💡