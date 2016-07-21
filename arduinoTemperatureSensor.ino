int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor
int ctr = 1;
int sensortotal=0;
int maxTemp = 450;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);  
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
   // read the incoming tempsetting
   maxTemp = Serial.read();
  }
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);    
  // turn the ledPin on
  //Serial.println(sensorValue);
  
  sensortotal += sensorValue;
  //Serial.println(sensortotal);
  if( ctr % 10 == 0)
  {
    
  sensorValue = sensortotal/10;
  //Serial.println(sensorValue);
  //the quick way
  // map it to the range of the analog out:
  int outputValue = 0;
  outputValue = map(sensorValue, maxTemp-20, maxTemp, 0, 255);
  // change the analog out value:
  analogWrite(ledPin, outputValue);
  
  //the dumb way
//  if(sensorValue <= maxTemp-20)
//  {
//    analogWrite(ledPin,0);
//  }
//  else if(sensorValue > maxTemp-20 && sensorValue <= maxTemp-17)
//  {
//    analogWrite(ledPin,30);
//  }
//  else if(sensorValue > maxTemp-17 && sensorValue <= maxTemp-14)
//  {
//    analogWrite(ledPin,60);
//  }
//  else if(sensorValue > maxTemp-14 && sensorValue <= maxTemp-11)
//  {
//    analogWrite(ledPin,100);
//  }
//  else if(sensorValue > maxTemp-11 && sensorValue <= maxTemp-8)
//  {
//    analogWrite(ledPin,125);
//  }
//  else if(sensorValue > maxTemp-8 && sensorValue <= maxTemp-5)
//  {
//    analogWrite(ledPin,170);
//  }
//  else if(sensorValue > maxTemp-5 && sensorValue<= maxTemp)
//  {
//    analogWrite(ledPin,205);
//  }
//  else if(sensorValue > maxTemp)
//  {
//    analogWrite(ledPin,250);
//  }
  
  sensortotal = 0;
  ctr = 0;
  }
  ctr += 1;
  delay(20);                  
}
