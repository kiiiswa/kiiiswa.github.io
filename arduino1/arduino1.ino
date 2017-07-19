void setup() {
 pinMode(7, OUTPUT);
 pinMode(6, OUTPUT);
 pinMode(5, OUTPUT);
 pinMode(4, OUTPUT);
}

void loop() {
 delay(5000);
 digitalWrite(7, LOW);
 digitalWrite(6, LOW);
 digitalWrite(5, LOW);
 digitalWrite(4, LOW);
 delay(50);              
 digitalWrite(7, HIGH);
 
 delay(3000);
 
 digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
 digitalWrite(5, HIGH);
 digitalWrite(4, HIGH);
 delay(50);
 digitalWrite(7, LOW);
 digitalWrite(6, LOW);
 digitalWrite(5, LOW);
 digitalWrite(4, LOW);
 delay(50);
 digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
 digitalWrite(5, HIGH);
 digitalWrite(4, HIGH);  
 delay(50);
 digitalWrite(7, LOW);
 digitalWrite(6, LOW);
 digitalWrite(5, LOW);
 digitalWrite(4, LOW);
 delay(50);
 digitalWrite(7, HIGH);
 digitalWrite(6, HIGH);
 digitalWrite(5, HIGH);
 digitalWrite(4, HIGH);  
 delay(6000);
 

 

 digitalWrite(6, HIGH);  
 delay(50);              
 digitalWrite(6, LOW);
 delay(50);

 digitalWrite(7, HIGH);  
 delay(100);              
 digitalWrite(7, LOW);
 delay(100);

 digitalWrite(6, HIGH);  
 delay(100);              
 digitalWrite(6, LOW);
 delay(100);

 digitalWrite(5, HIGH);  
 delay(100);              
 digitalWrite(5, LOW);
 delay(100);

 digitalWrite(4, HIGH);  
 delay(100);              
 digitalWrite(4, LOW);
 delay(100);

 
}
