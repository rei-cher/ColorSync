#include <web_server.h>
#include <rgb_controller.h>
#include <WiFi.h>
#include <ESPmDNS.h>
#include <command_handler.h>

AsyncWebServer server(80);

void setupWifi(const char* ssid, const char* password){
    //conncet to Wifi
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED){
        delay(1000);
        Serial.println("Connecting to Wifi...");
    }
    Serial.println("Connected to Wifi");
    // Print the ESP32 IP address
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
}

void connectToWifi(const String& command) {
    int ssidIndex = command.indexOf(':') + 1;
    int passwordIndex = command.indexOf(':', ssidIndex) + 1;


    String newSsid = command.substring(ssidIndex, passwordIndex - 1);
    String newPassword = command.substring(passwordIndex);

    Serial.println("New wifi ssid: "+newSsid+", and new password is: "+newPassword);

    setupWifi(newSsid.c_str(), newPassword.c_str());
}

void setupWebServer(){
    //Route for root
    server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
        request->send(200, "text/plain", "ESP32 is up and running");
    });

    // Route to handle RGB commands via POST
    server.on("/command", HTTP_POST, [](AsyncWebServerRequest *request) {
        if (request->hasParam("plain", true)) {
            String command = request->getParam("plain", true)->value();
            Serial.println("Received command: " + command);

            running = false;

            switch (getCommand(command)) {
                case FILL_SOLID:
                    running = true;
                    fillSolidColor(command);
                    break;
                case RAINBOW:
                    running = true;
                    rainbow();
                    break;
                case OFF:
                    rgb_off();
                    break;
                case SCREEN_SYNC:
                    screen_sync(command);
                    break;
                case SET_WIFI:
                    connectToWifi(command);
                    break;
                case INVALID:
                default:
                    rgb_off();
                    break;
            }

            request->send(200, "text/plain", "Command received: " + command);
        } else {
            request->send(400, "text/plain", "Bad Request: Missing command parameter");
            Serial.println("Bad Request: Missing command parameter");
        }
    });

    //start server
    server.begin();
    Serial.println("HTTP server started");
}