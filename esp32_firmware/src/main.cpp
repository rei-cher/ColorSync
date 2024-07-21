#include <Arduino.h>
#include <FastLED.h>
#include <rgb_controller.h>
#include <web_server.h>

const char* ssid = "SpectrumSetup-4FDF";
const char* password = "royalcable228";

enum Command {
  FILL_SOLID,
  RAINBOW,
  OFF,
  SCREEN_SYNC,
  SET_WIFI,
  INVALID
};

Command getCommand(const String& command) {
    if (command.startsWith("fillSolid:")) return FILL_SOLID;
    if (command == "rainbow") return RAINBOW;
    if (command == "off") return OFF;
    if (command.startsWith("rgb:")) return SCREEN_SYNC;
    if (command.startsWith("wifi:")) return SET_WIFI;
    return INVALID;
}

void setup() {
    Serial.begin(115200);

    setupWifi(ssid, password);
    setupWebServer();

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
        case FILL_SOLID:
          running = true;
          fillSolidColor(command);
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
        case SET_WIFI:
          connectToWifi(command);
          break;
        case INVALID:
        default:
          rgb_off();
          break;
      }
  }
}
