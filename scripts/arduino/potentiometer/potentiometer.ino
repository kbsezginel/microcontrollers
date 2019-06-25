const byte POT_PIN = 1;
int potRead;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  potRead = analogRead(POT_PIN);
  Serial.print(potRead);
  Serial.print("\n");
  if (potRead > 500) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(500);
}
