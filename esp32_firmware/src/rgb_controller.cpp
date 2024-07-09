#include <FastLED.h>
#include <rgb_controller.h>
#include <config.h>

CRGB leds[NUM_LEDS];

int snakeL = 10;

void fillRed(){
    fill_solid(leds, NUM_LEDS, CRGB::Red);
    FastLED.show();
}

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
    for (int i=0; i<NUM_LEDS; i++){
        leds[i] = CRGB::Black;
    }
    FastLED.show();
}