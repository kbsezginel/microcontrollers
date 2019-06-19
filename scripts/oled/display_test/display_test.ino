/*********
  Rui Santos
  Complete project details at https://randomnerdtutorials.com  
*********/

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

const byte POT_PIN = 3;
const byte LED_PIN = 9;
int bpm = 120;
int gPotVal = 500;
float delayTime = 60.0 / bpm * 1000.0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  
  Serial.begin(115200);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3D for 128x64
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  
  display.clearDisplay();

  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(20, 20);
  // Display static text
  display.println("MODULED!");
  display.display();
  delay(2000);
}

void loop() {
  setBPM();
  
  display.clearDisplay();
  display.setCursor(10, 10);
  display.println(bpm);
  display.println(" - ");
  display.println(delayTime);
  display.display();
  
  digitalWrite(LED_PIN, HIGH);
  delay(delayTime);
  digitalWrite(LED_PIN, LOW);
}

void setBPM() {
  int potRead = analogRead(POT_PIN);
  // Change value only if current read is different than previous set value
  if (abs(gPotVal - potRead) > 20) {
    bpm = map(potRead, 0, 1023, 10, 300);
    delayTime = 60.0 / bpm * 1000.0;
  }
}
