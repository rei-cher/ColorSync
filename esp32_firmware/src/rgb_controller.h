#ifndef RGB_CONTROLLER_H

#include <FastLED.h>
#include <config.h>

extern CRGB leds[NUM_LEDS];
extern bool running;

void rainbow();
void snake();
void rgb_off();
void fillSolid(CRGB color);
void fillSolidColor(const String& command);
void screen_sync(const String& command);
void set_brightness(uint8_t brightness);

#endif