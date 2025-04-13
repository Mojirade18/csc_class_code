#include <LiquidCrystal.h>

// Initialize the LCD with RS, E, D4, D5, D6, D7
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

const int buttonPin = 2;
int buttonState = 0;
int lastButtonState = 0;

const String fortunes[] = {
    "You will succeed!",
    "Happiness is near",
    "Big changes ahead",
    "Future is bright!",
    "Trust your gut."};

void setup()
{
  pinMode(buttonPin, INPUT_PULLUP);
  randomSeed(analogRead(A0));

  lcd.begin(16, 2); // Initialize LCD for 16 columns & 2 rows

  lcd.setCursor(0, 0);
  lcd.print("Welcome to the");
  lcd.setCursor(0, 1);
  lcd.print("Fortune Teller!");
  delay(2000);
  lcd.clear();
}

void loop()
{
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW && lastButtonState == HIGH)
  {
    int fortuneIndex = random(0, 5);
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Fortune:");
    lcd.setCursor(0, 1);
    lcd.print(fortunes[fortuneIndex]);
    delay(200);
  }

  lastButtonState = buttonState;
}
