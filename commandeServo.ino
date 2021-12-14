#include <Wire.h>
#include "Servo.h"

volatile int Val; // variable used by the master to sent data to the slave
char t[7]={};

Servo servo1;
Servo servo2;
int inUse = 0;

void setup() {
  Wire.begin(11);                

  Wire.onReceive(receiveEvent); // what to do when receiving data
  Serial.begin(9600);  // serial for displaying data on your screen
  servo1.attach(9);
  servo2.attach(10);
  servo1.write(0);
  servo2.write(0);
}

void loop() {
//convers the float or integer to a string. (floatVar, minStringWidthIncDecimalPoint, numVarsAfterDecimal, empty array);
          // print the character
 
//gathers data comming from slave
int i=0; //counter for each bite as it arrives

  while (Wire.available()) { 
    t[i] = Wire.read(); // every character that arrives it put in order in the empty array "t"  
    i++;
  }
  if(strcmp(t, "servo1") == 0 && inUse==0){
    Serial.println("oui 1");
    useServo(servo1);
    inUse = 1;
  }
  else if(strcmp(t, "servo2") == 0 && inUse==0){
    Serial.println("oui 2");
    useServo(servo2);
    inUse = 1;
  }
  else{
    Serial.print("t = ");
    Serial.println(t);
  }

   //shows the data in the array t
delay(500); //give some time to relax
}

// function: what to do when asked for data


// what to do when receiving data from master
void receiveEvent(int howMany)
{Wire.read();
  Serial.print("new");
  inUse = 0;}

void useServo(Servo servo){
  servo.write(90);
  delay(5000);
  servo.write(0);
}
