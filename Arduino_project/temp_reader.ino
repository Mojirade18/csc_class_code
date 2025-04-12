// Define pins
const int tempPin = A0;  // TMP36 temperature sensor connected to A0
const int redPin = 9;    // Red pin of RGB LED
const int greenPin = 10; // Green pin of RGB LED
const int bluePin = 11;  // Blue pin of RGB LED

void setup()
{
    Serial.begin(9600); // Start serial communication
    pinMode(redPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
    pinMode(bluePin, OUTPUT);
}

void loop()
{
    int reading = analogRead(tempPin);          // Read analog value from sensor
    float voltage = reading * (5.0 / 1023.0);   // Convert to voltage
    float temperatureC = (voltage - 0.5) * 100; // Convert to Celsius

    Serial.print("Temperature: ");
    Serial.print(temperatureC);
    Serial.println(" °C");

    // Change LED color based on temperature
    if (temperatureC < 20)
    {
        setColor(0, 0, 255); // Blue for cold
    }
    else if (temperatureC >= 20 && temperatureC <= 30)
    {
        setColor(0, 255, 0); // Green for normal
    }
    else
    {
        setColor(255, 0, 0); // Red for hot
    }

    delay(1000); // Update every 1 second
}

// Function to set RGB LED color
void setColor(int red, int green, int blue)
{
    analogWrite(redPin, red);
    analogWrite(greenPin, green);
    analogWrite(bluePin, blue);
}
