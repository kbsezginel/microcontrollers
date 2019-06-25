// SWITCH EXAMPLE
const byte SWITCH_PIN = 4;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);

  pinMode(SWITCH_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // read the analog in value:
  String text = "~~~OFF~~~";
  if (digitalRead(SWITCH_PIN) == HIGH) {
    text = "!!!ON!!!";
    digitalWrite(LED_BUILTIN, HIGH);
    }
  else {
    digitalWrite(LED_BUILTIN, LOW);
  }

  Serial.print(text + "\n");
  delay(500);
}
