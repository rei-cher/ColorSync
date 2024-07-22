#ifndef COMMAND_HANDLER_H
#define COMMAND_HANDLER_H

#include <Arduino.h>

enum Command {
    FILL_SOLID,
    RAINBOW,
    OFF,
    SCREEN_SYNC,
    SET_WIFI,
    INVALID
};

Command getCommand(const String& command);

#endif
