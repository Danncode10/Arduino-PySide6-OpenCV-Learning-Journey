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



# while True:
#     num = '1'
#     send_command(num)
#     time.sleep(1)
#     num = '0'
#     send_command(num)
#     time.sleep(1)

time.sleep(1)  # Wait a bit before the script ends
