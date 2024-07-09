#ifndef RGB_CONTROLLER_H

#include <FastLED.h>
#include <config.h>

extern CRGB leds[NUM_LEDS];

void fillRed();
void rainbow();
void snake();
void rgb_off();
void fillSolid(CRGB color);

#endif