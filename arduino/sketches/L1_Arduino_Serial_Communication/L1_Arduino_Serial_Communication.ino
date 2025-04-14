const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);  // Start the serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char receivedData = Serial.read();  // Read the data sent from the computer

    if (receivedData == '1') {
      digitalWrite(ledPin, HIGH);       // Turn LED on
      Serial.write("LED ON\n");         // Send a message back to the computer
    } 
    else if (receivedData == '0') {
      digitalWrite(ledPin, LOW);        // Turn LED off
      Serial.write("LED OFF\n");        // Send a message back
    } 
    else {
      Serial.write("Invalid Command\n"); // Handle unexpected input
    }
  }
}
