#include <FastLED.h>
#include <rgb_controller.h>
#include <config.h>

bool running = false;

CRGB leds[NUM_LEDS];

int snakeL = 10;

void rainbow(){
    leds[0] = CHSV(random(0,255), 255, 255);
    
    for (int i = NUM_LEDS - 1; i>0; i--){
        leds[i] = leds[i-1];
    }
    FastLED.show();
    delay(50);

}

void snake(){
    for (int i=0; i<NUM_LEDS; i++){
        for (int j=0; j<snakeL; j++){
            int pos = (i+j) % NUM_LEDS;
            leds[pos] = CHSV(random(0,255), 255, 255);
        }
        FastLED.show();
        delay(100);

        for (int j=0; j<snakeL; j++){
            int pos = (i+j) % NUM_LEDS;
            leds[pos] = CRGB::Black;
        }
    }
}

void rgb_off(){
    running = false;
    fill_solid(leds, NUM_LEDS, CRGB::Black);
    FastLED.show();
}

void fillSolid(CRGB color) {
    fill_solid(leds, NUM_LEDS, color);
    FastLED.show();
}

void fillSolidColor(const String& command) {
    if (command.startsWith("fillSolid:")) {
        int startIdx = command.indexOf(':') + 1;
        int commaIndex1 = command.indexOf(',', startIdx);
        int commaIndex2 = command.indexOf(',', commaIndex1 + 1);
        int bIndex = command.indexOf("b:");
        if (commaIndex1 > 0 && commaIndex2 > 0) {
            int r = command.substring(startIdx, commaIndex1).toInt();
            int g = command.substring(commaIndex1 + 1, commaIndex2).toInt();
            int b = command.substring(commaIndex2 + 1).toInt();
            int brightness = command.substring(bIndex + 2).toInt();
            fillSolid(CRGB(r, g, b));
            set_brightness(brightness);
        }
    }
}

void screen_sync(const String& command){
    int commaIndex1 = command.indexOf(',');
    int commaIndex2 = command.indexOf(',', commaIndex1 + 1);
    int bIndex = command.indexOf("b:");
    if (commaIndex1 > 0 && commaIndex2 > 0 && bIndex > 0) {
        int r = command.substring(4, commaIndex1).toInt();
        int g = command.substring(commaIndex1 + 1, commaIndex2).toInt();
        int b = command.substring(commaIndex2 + 1).toInt();
        int brightness = command.substring(bIndex + 2).toInt();
        fillSolid(CRGB(r, g, b));
        set_brightness(brightness);
    }
}

void set_brightness(uint8_t brightness) {
    FastLED.setBrightness(map(brightness, 0, 100, 0, 255));
    FastLED.show();
}