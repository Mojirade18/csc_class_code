#define TRIG 11
#define ECHO 12

long duration;
int distance;
int binHeight = 0;   // Will be measured at startup
int fillLevel = 0;

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  Serial.begin(9600);

  delay(2000); // wait 2s before calibration

  // === CALIBRATE BIN HEIGHT ===
  binHeight = measureDistance();
  Serial.print("Calibrated Bin Height: ");
  Serial.print(binHeight);
  Serial.println(" cm");
}

void loop() {
  distance = measureDistance();

  // Clamp to binHeight
  if (distance > binHeight) distance = binHeight;
  if (distance < 0) distance = 0;

  // Calculate % fill
  fillLevel = ((binHeight - distance) * 100) / binHeight;

  // Print results
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.print(" cm  |  Fill Level: ");
  Serial.print(fillLevel);
  Serial.println("%");

  delay(1000);
}

// Function to get distance from ultrasonic
int measureDistance() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  duration = pulseIn(ECHO, HIGH);
  int d = duration * 0.034 / 2;
  return d;
}
