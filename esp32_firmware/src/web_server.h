#ifndef WEB_SERVER_H
#define WEB_SERVER_H

#include <ESPAsyncWebServer.h>

extern AsyncWebServer server;

void setupWifi(const char* ssid, const char* password);
void connectToWifi(const String& command);
void setupWebServer();


#endif