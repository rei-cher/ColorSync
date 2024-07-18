#include <Arduino.h>
#include <FastLED.h>
#include <rgb_controller.h>

enum Command {
  FILL_RED,
  RAINBOW,
  OFF,
  SCREEN_SYNC,
  INVALID
};

Command getCommand(const String& command) {
    if (command == "fillRed") return FILL_RED;
    if (command == "rainbow") return RAINBOW;
    if (command == "off") return OFF;
    if (command.startsWith("rgb:")) return SCREEN_SYNC;
    return INVALID;
}

void setup() {
    FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, NUM_LEDS);
    FastLED.setBrightness(15);
    Serial.begin(115200); // Initialize serial communication
    rgb_off();
}

void loop() {
  if (Serial.available() > 0) {
      String command = Serial.readStringUntil('\n');
      command.trim();

      running = false;

      switch (getCommand(command)){
        case FILL_RED:
          fillRed();
          break;
        case RAINBOW:
          running = true;
          rainbow();
          break;
        case OFF:
          rgb_off();
          break;
        case SCREEN_SYNC:
          screen_sync(command);
          break;
        case INVALID:
        default:
          rgb_off();
          break;
      }
  }
}
