const int trigPin = 9;
const int echoPin = 10;
const int buzzerPin = 8;

long duration;
int distance;

void setup(){
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  // Send Sound wave for 10us
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW); // Dont send sound waves
  delayMicroseconds(10); 

  duration = pulseIn(echoPin, HIGH); //measures the time how long the sound wave last
  // sound wave hit the wall, then go back to sensor therefore the duration = distance * 2

  //convert duration(us) to cm
  distance = duration * 0.034/2;

  Serial.println(distance);

  if(distance < 10){
    analogWrite(buzzerPin, 255);
  }
  else{
    analogWrite(buzzerPin, 0);
  }

  delay(200); // Recieve the distance every 0.2 seconds.  

}