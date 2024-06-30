#ifndef RGBController_h
#define RGBController_h

#include <Arduino.h>

class RGBController{
    public:
        RGBController(int pin, int numLEDs);
        void initialize();
        void setColor(uint8_t r, uint8_t g, uint8_t b);
        void updateLEDs();

    private:
        void sendByte(uint8_t b);
        int _pin;
        int _numLEDs;
        struct RGB
        {
            uint8_t r;
            uint8_t g;
            uint8_t b;
        };

        RGB* leds;
        
};

#endif