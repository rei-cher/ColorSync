#include "RGBController.h"

RGBController::RGBController(int pin, int numLEDs){
    _pin = pin;
    _numLEDs = numLEDs;
    leds = new RGB[numLEDs];
}

void RGBController::initialize(){
    pinMode(_pin, OUTPUT);
    for (int i=0; i < _numLEDs; i++){
        leds[i] = {0, 0, 0};
    }

    updateLEDs();
}

void RGBController::setColor(uint8_t r, uint8_t g, uint8_t b){
    for (int i=0; i < _numLEDs; i++){
        leds[i] = {r,g,b};
    }
}

void RGBController::updateLEDs(){
    for (int i=0; i < _numLEDs; i++){
        sendByte(leds[i].g);
        sendByte(leds[i].r);
        sendByte(leds[i].b);
    }
}

void RGBController::sendByte(uint8_t b){
    for (int i=0; i < 8; i++){
        if (b & 0x80){
            digitalWrite(_pin, HIGH);
            delayMicroseconds(800);
            digitalWrite(_pin, LOW);
            delayMicroseconds(450);
        }
        else {
            digitalWrite(_pin, HIGH);
            delayMicroseconds(400);
            digitalWrite(_pin, LOW);
            delayMicroseconds(850);
        }
        b <<= 1;
    }
}