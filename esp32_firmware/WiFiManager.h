#ifndef WiFiManager_h
#define WiFiManager_h

#include <WiFi.h>

class WiFiManager {
    public:
        WiFiManager(const char* ssid, const char* password);
        void connect();
        bool isConnected();
        IPAddress getIPAddress();
    
    private:
        const char* _ssid;
        const char* _password;
};

#endif