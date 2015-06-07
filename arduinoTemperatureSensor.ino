
int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor
int ctr = 1;
int sensortotal=0;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);  
  //Serial.begin(9600); 
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);    
  // turn the ledPin on
  //Serial.println(sensorValue);
  
  sensortotal += sensorValue;
  //Serial.println(sensortotal);
  if( ctr % 7 == 0)
  {
    
  sensorValue = sensortotal/7;
  //Serial.println(sensorValue);
  if(sensorValue <= 480)
  {
    analogWrite(ledPin,0);
  }
  else if(sensorValue > 480 && sensorValue <= 483)
  {
    analogWrite(ledPin,20);
  }
  else if(sensorValue > 483 && sensorValue <= 486)
  {
    analogWrite(ledPin,35);
  }
  else if(sensorValue > 486 && sensorValue <= 489)
  {
    analogWrite(ledPin,60);
  }
  else if(sensorValue > 489 && sensorValue <= 492)
  {
    analogWrite(ledPin,110);
  }
  else if(sensorValue > 492 && sensorValue <= 495)
  {
    analogWrite(ledPin,160);
  }
  else if(sensorValue > 495 && sensorValue<= 500)
  {
    analogWrite(ledPin,205);
  }
  else if(sensorValue > 500)
  {
    analogWrite(ledPin,250);
  }
  
  sensortotal = 0;
  ctr = 0;
  }
  ctr += 1;
  delay(25);                  
}
