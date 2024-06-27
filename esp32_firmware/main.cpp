#include <Arduino.h>
#include "WiFiManager.h"
#include "RGBController.h"

const char* ssid = "DG1670A89-2.4";
const char* password = "DG1670A89F812";

//Defining the RGB LED strip pin and number of LEDs
#define LED_PIN 5
#define NUM_LEDS 300

WiFiManager wifiManager(ssid, password);
RGBController rgbController(LED_PIN, NUM_LEDS);

void setup(){
  Serial.begin(115200);

  // Connect to WiFi
  Serial.println("Connecting to WiFi...");
  wifiManager.connect();

  if (wifiManager.isConnected()) {
      Serial.print("IP address: ");
      Serial.println(wifiManager.getIPAddress());
  } else {
      Serial.println("Failed to connect to WiFi. Please check your network credentials.");
  }

  // Initialize RGB strip
  rgbController.initialize();
}

void loop(){
  if (wifiManager.isConnected()){
    // Set all to red
    rgbController.setColor(255, 0, 0);
    rgbController.updateLEDs();
    delay(1000);

    // Set all to green
    rgbController.setColor(0, 255, 0);
    rgbController.updateLEDs();
    delay(1000);

    // Set all to blue
    rgbController.setColor(0, 0, 255);
    rgbController.updateLEDs();
    delay(1000);
  }
  else{
    Serial.println("WiFi connection lost. Attempting to reconnect...");
    wifiManager.connect();
  }
}