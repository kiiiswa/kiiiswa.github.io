int photoTran = 9;
int reading = 0;

void setup() {
  // put your setup code here, to run once:
pinMode(photoTran, INPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
reading = analogRead(photoTran);
Serial.println(reading);
delay(100);
}
