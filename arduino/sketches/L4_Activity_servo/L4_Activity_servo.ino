#include <Servo.h>
int servo_pin = 9;

Servo myServo;

void setup() {
 Serial.begin(9600);
 myServo.attach(servo_pin); 
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();
    angle = constrain(angle, 0, 180);
    Serial.print("Recieved data: ");
    Serial.println(angle);

    myServo.write(angle);

    // Clear any leftover characters
    while (Serial.available()) Serial.read();
  }
}
