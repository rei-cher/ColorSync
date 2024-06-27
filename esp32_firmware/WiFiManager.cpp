#include "WiFiManager.h"

WiFiManager::WiFiManager(const char* ssid, const char* password){
    _ssid = ssid;
    _password = password;
}

void WiFiManager::connect(){
    WiFi.begin(_ssid, _password);
    int maxAttempts = 20; // Maximum number of attempts to connect
    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED && attempts < maxAttempts) {
        delay(500);
        Serial.print(".");
        Serial.print(" Attempt: ");
        Serial.println(attempts);
        attempts++;
    }
    if (WiFi.status() == WL_CONNECTED) {
        Serial.println("\nConnected to WiFi");
        Serial.print("IP Address: ");
        Serial.println(WiFi.localIP());
    } else {
        Serial.println("\nFailed to connect to WiFi");
        Serial.print("WiFi Status: ");
        Serial.println(WiFi.status());
        Serial.print("SSID: ");
        Serial.println(_ssid);
        Serial.print("Password: ");
        Serial.println(_password);
    }
}

bool WiFiManager::isConnected() {
    return WiFi.status() == WL_CONNECTED;
}

IPAddress WiFiManager::getIPAddress() {
    return WiFi.localIP();
}