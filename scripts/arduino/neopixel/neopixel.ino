#include <Adafruit_NeoPixel.h>

const byte NEO_PIN = 12;
const byte NUM_PIXELS = 24;
Adafruit_NeoPixel ledRing = Adafruit_NeoPixel(NUM_PIXELS, NEO_PIN, NEO_GRB + NEO_KHZ800);

byte ledCounter = 0;
byte gLedStep = 3;
byte gColorStep = 9;
byte gColorIdx = 0;

void setup() {
  ledRing.begin();
  ledRing.setBrightness(50);  // btw 0 - 127
}


void loop() {
  lightLedRing(0, ledCounter, gColorIdx);

  delay(500);
  ledCounter += gLedStep;
  gColorIdx += gColorStep * gLedStep;
  if (ledCounter > NUM_PIXELS) {
    clearLedRing();
    ledCounter = gLedStep;
    gColorIdx = 0;
  }
}

void clearLedRing() {
  for(int i = 0; i<NUM_PIXELS; i++){
    ledRing.setPixelColor(i, 0x000000);
    ledRing.show();
  }
}

void lightLedRing(int startIndex, int nPixels, int colorIdx) {
  for(int i=startIndex;i<startIndex+nPixels;i++){
    ledRing.setPixelColor(i, colorWheel(colorIdx));
    ledRing.show();
  }
}

uint32_t colorWheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return ledRing.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return ledRing.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return ledRing.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}

uint32_t dimColor(uint32_t color, uint8_t width) {
   return (((color&0xFF0000)/width)&0xFF0000) + (((color&0x00FF00)/width)&0x00FF00) + (((color&0x0000FF)/width)&0x0000FF);
}
