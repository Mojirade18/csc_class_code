// LED pins
const int redLED = 8;
const int yellowLED = 9;
const int greenLED = 10;

// Button pin
const int buttonPin = 2;

// Button state
int buttonState = 0;

void setup()
{
    pinMode(redLED, OUTPUT);
    pinMode(yellowLED, OUTPUT);
    pinMode(greenLED, OUTPUT);

    pinMode(buttonPin, INPUT);
}

void loop()
{
    buttonState = digitalRead(buttonPin);

    if (buttonState == HIGH)
    {
        // Button is pressed
        digitalWrite(redLED, LOW);
        digitalWrite(greenLED, HIGH);
        delay(3000); // Green for 3 seconds
        digitalWrite(greenLED, LOW);

        digitalWrite(yellowLED, HIGH);
        delay(1000); // Yellow for 1 second
        digitalWrite(yellowLED, LOW);

        digitalWrite(redLED, HIGH); // Return to Red
    }
    else
    {
        // Button NOT pressed
        digitalWrite(redLED, HIGH);
        digitalWrite(greenLED, LOW);
        digitalWrite(yellowLED, LOW);
    }
}
