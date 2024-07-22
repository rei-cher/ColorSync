#include <Arduino.h>
#include <FastLED.h>
#include <rgb_controller.h>
#include <web_server.h>
#include <command_handler.h>

const char* ssid = "SpectrumSetup-4FDF";
const char* password = "royalcable228";


void setup() {
    Serial.begin(115200);

    setupWifi(ssid, password);
    setupWebServer();

    FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, NUM_LEDS);
    // FastLED.setBrightness(15);
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
