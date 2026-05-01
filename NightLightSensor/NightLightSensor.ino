int potPin = A1;
int potVal;
int lastVal = 0;
int br = 9600;
int wt = 100; 

const int sensor_pin = A0;
int sensor;
int sensInt = 0;
const int threshold = 500;
int led = 9;
int buzzer = 6;
String mode = "Daylight Mode";

unsigned long lastLogTime = 0;    // Stores the last time dataLog ran
const long logInterval = 10000;    // Interval at which to log (5 seconds)


void dataLog() {
  sensor = analogRead(sensor_pin);
  potVal = analogRead(potPin);
  float voltage = (potVal / 1023.0) * 5.0;
  
  Serial.println("**Data Log**");
  Serial.print("Current Mode: ");   Serial.println(mode);
  Serial.print("Voltage: ");  Serial.println(voltage);
  Serial.print("Dimmer Value: ");   Serial.println(potVal);
  Serial.print("Light Sensor Value: ");   Serial.println(sensor);
  Serial.println();
}

void setup() {
    pinMode(potPin, INPUT);
    pinMode(led, OUTPUT);
    pinMode(sensor_pin, INPUT);  // set sensor pin as input
    pinMode(buzzer,OUTPUT);
    Serial.begin(br);


}


void loop() {
  // 1. NON-BLOCKING TIMER CHECK
  unsigned long currentMillis = millis(); // Get the current "time"
  
  if (currentMillis - lastLogTime >= logInterval) {
    lastLogTime = currentMillis; // Reset the timer
    dataLog();                   // Run the log
  }

sensor = analogRead(sensor_pin);
  potVal = analogRead(potPin);
  int brightness = map(potVal, 0, 1023, 0, 255);

  if (sensor <= 500 && sensor >= 480) { tone(buzzer, 400, 100); }
  if (sensor >= 540 && sensor <= 560) { tone(buzzer, 700, 100); }

  if (sensor > threshold) {
    mode = "Daylight Mode"; // Update mode string for the logger
    analogWrite(led, 0);
    if (abs(sensor - sensInt) > 15) {
        Serial.println("Action: Daylight Mode Detected");
        sensInt = sensor;
    }
  } else {
    mode = "Night Mode";    // Update mode string for the logger
    analogWrite(led, brightness); // Removed the delay(300) to keep it smooth
    
    if (abs(potVal - lastVal) > 5 || abs(sensor - sensInt) > 15) {
        Serial.println("Action: Night Mode Adjust");
        lastVal = potVal;
        sensInt = sensor;
    }
  }
 
  delay(wt);    // Small delay so the Serial Monitor isn't overwhelmed
}