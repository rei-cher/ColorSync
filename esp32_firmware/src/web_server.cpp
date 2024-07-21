#include <web_server.h>
#include <WiFi.h>
#include <ESPmDNS.h>

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

    //Route to handle RGB commands
    server.on("/rgb", HTTP_GET, [](AsyncWebServerRequest *request){
        if(request->hasParam("color")){
            String color = request->getParam("color")->value();
            //Parse and set rgb color
            request->send(200, "text/plain", "Color set to "+color);
            Serial.print("Color set to: ");
      Serial.println(color);
        }
        else{
            request->send(400, "text/palin", "Bad Request");
            Serial.println("Bad Request: Missing 'color' parameter");
        }
    });

    //start server
    server.begin();
    Serial.println("HTTP server started");
}