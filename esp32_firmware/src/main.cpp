#include <Arduino.h>
#include <FastLED.h>
#include <rgb_controller.h>

bool running = false;

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

        if (command == "fillRed") {
          fillRed();
        } 
        // else if (command == "snake"){
        //   running = true;
        //   while(running){
        //     snake();
        //     if (command != "snake"){
        //       running = false;
        //     }
        //   }
        // }
        else if (command == "rainbow") {
          rainbow();
        }
        else if (command == "off") {
          rgb_off();
        }
        else if (command.startsWith("rgb:")) {
          int commaIndex1 = command.indexOf(',');
          int commaIndex2 = command.indexOf(',', commaIndex1 + 1);
          
          if (commaIndex1 > 0 && commaIndex2 > 0) {
            int r = command.substring(4, commaIndex1).toInt();
            int g = command.substring(commaIndex1 + 1, commaIndex2).toInt();
            int b = command.substring(commaIndex2 + 1).toInt();

            fillSolid(CRGB(r, g, b));
          }
        }
    }
}
