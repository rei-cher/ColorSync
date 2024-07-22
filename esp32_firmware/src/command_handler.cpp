#include "command_handler.h"

Command getCommand(const String& command) {
    if (command.startsWith("fillSolid:")) return FILL_SOLID;
    if (command == "rainbow") return RAINBOW;
    if (command == "off") return OFF;
    if (command.startsWith("rgb:")) return SCREEN_SYNC;
    if (command.startsWith("wifi:")) return SET_WIFI;
    return INVALID;
}
