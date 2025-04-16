const int led = 13; //pin 13
const int r_rgb = 3;
const int g_rgb = 5;
const int b_rgb = 6;
const int buzzer = 9;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  pinMode(r_rgb, OUTPUT);
  pinMode(g_rgb, OUTPUT);
  pinMode(b_rgb, OUTPUT);
  Serial.begin(9600); // Start the serial communication

}

void loop() {
  if (Serial.available() > 0){ //checks if the computer is connected to the arduino
    String data = Serial.readStringUntil('\n');
    delay(50);
    
    Serial.print("Received: ");
    Serial.println(data);

    // LED Control

    if (data == "LED,on") {
      digitalWrite(led, HIGH);
    }
    else if(data == "LED,off"){
      digitalWrite(led, LOW);
    }

    // RGB Control
    int r,g,b;
    if (data.startsWith("RGB")){
      int first_comma = data.indexOf(',');
      int second_comma = data.indexOf(',', first_comma + 1);
      int third_comma = data.indexOf(',', second_comma + 1);

      r = data.substring(first_comma + 1, second_comma).toInt();
      g = data.substring(second_comma + 1, third_comma).toInt();
      b = data.substring(third_comma + 1).toInt();

      analogWrite(r_rgb, r);
      analogWrite(g_rgb, g);
      analogWrite(b_rgb, b);

    }

    if (data.equals("BUZ,off")){
      analogWrite(buzzer, 0);
    }
    else if (data.equals("BUZ,beep")){
      beep();
      
    }
    else if (data.equals("BUZ,alarm")){
      analogWrite(buzzer, 255);
    }

  } 

}

void beep(){
  analogWrite(buzzer, 255);
  delay(1000);
  analogWrite(buzzer, 0);
  delay(1000);
}

void rgb(int r, int g, int b){
  analogWrite(r_rgb, r);
  analogWrite(g_rgb, g);
  analogWrite(b_rgb, b);
}
