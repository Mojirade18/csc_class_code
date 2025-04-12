int leds[] = {2, 3, 4, 5, 6, 7, 8, 9};
int numLeds = 8;
int buttonPin = 10;
int delayTime = 300;

void setup()
{
  for (int i = 0; i < numLeds; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop()
{
  if (digitalRead(buttonPin) == LOW)
  {
    delayTime = 100;
  }
  else
  {
    delayTime = 300;
  }

  for (int i = 0; i < numLeds; i++)
  {
    digitalWrite(leds[i], HIGH);
    delay(delayTime);
    digitalWrite(leds[i], LOW);
  }

  for (int i = numLeds - 1; i >= 0; i--)
  {
    digitalWrite(leds[i], HIGH);
    delay(delayTime);
    digitalWrite(leds[i], LOW);
  }
}