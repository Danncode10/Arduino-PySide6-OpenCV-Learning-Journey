void setup() {
  // Initialize pins 2 to 6 as OUTPUT
  for (int i = 2; i <= 6; i++) {
    pinMode(i, OUTPUT);
  }

  Serial.begin(9600);  // Start the serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char gesture = Serial.read();

    if (gesture == '0') {
      control(0, 0, 0, 0, 0);
    } else if (gesture == '1') {
      control(255, 0, 0, 0, 0);
    } else if (gesture == '2') {
      control(255, 255, 0, 0, 0);
    } else if (gesture == '3') {
      control(255, 255, 255, 0, 0);
    } else if (gesture == '4') {
      control(255, 255, 255, 255, 0);
    } else if (gesture == '5') {
      control(255, 255, 255, 255, 255);
    } else {
      control(0, 0, 0, 0, 0); // default
    }
  }
}

void control(int a, int b, int c, int d, int e) {
  analogWrite(2, a);
  analogWrite(3, b);
  analogWrite(4, c);
  analogWrite(5, d);
  analogWrite(6, e);
}
