#include <Servo.h>          // include servo library

Servo servoLeft;            // declare left servo
Servo servoRight;           // declare right servo

void setup() {
servoLeft.attach(13);
servoRight.attach(12);
}

void loop() {
  
servoLeft.write(5);
delay(2000);
servoRight.write(-5);
delay(2000);
servoLeft.write(180);
servoRight.write(180);

}

void spin() {
servoLeft.write(5);
servoRight.write(-5);
}
void forward() {
servoLeft.write(5);
servoRight.write(0);
}
void reverse() {
  servoLeft.write(0);
  servoRight.write(5);
}

void turnRight() {
  servoLeft.write(180);
  servoRight.write(180);
}
void turnLeft() {
  servoLeft.write(0);
  servoRight.write(0);
}

void stopRobot() {
  servoLeft.write(90);
  servoRight.write(90);
}
