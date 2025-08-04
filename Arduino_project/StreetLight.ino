int ldrPin = A0;
int potPin = A1;
int pirPin = 2;
int ledPin = 6;

int lightThreshold = 200;

void setup()
{
    pinMode(pirPin, INPUT);
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    int lightLevel = analogRead(ldrPin);
    int motion = digitalRead(pirPin);
    int potValue = analogRead(potPin); // 0 to 1023
    int ledBrightness = map(potValue, 0, 1023, 0, 255);

    Serial.print("Light: ");
    Serial.print(lightLevel);
    Serial.print(" | Motion: ");
    Serial.print(motion);
    Serial.print(" | Brightness: ");
    Serial.println(ledBrightness);

    if (lightLevel < lightThreshold && motion == HIGH)
    {
        analogWrite(ledPin, ledBrightness);
    }
    else
    {
        analogWrite(ledPin, 0);
    }

    delay(200);
}
