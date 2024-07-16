import network
import time
import json
import ubinascii
from machine import Pin
from umqtt.robust import MQTTClient

# WiFi settings
WIFI_SSID = ""
WIFI_PASSWORD = ""

# MQTT settings
mqtt_broker = ""
mqtt_port = 0
mqtt_username = ""
mqtt_password = ""

# Load MQTT credentials from JSON file
def load_credentials():
    global mqtt_broker, mqtt_port, mqtt_username, mqtt_password, WIFI_SSID,WIFI_PASSWORD
    try:
        with open("creds.json") as f:
            data = json.load(f)
            mqtt_broker = data["broker"]
            mqtt_port = data["port"]
            mqtt_username = data["username"]
            mqtt_password = data["password"]
            WIFI_SSID  = data["ssid"]
            WIFI_PASSWORD = data["wifi_password"]
    except Exception as e:
        print("Failed to load credentials:", e)

# Connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    
    while not wlan.isconnected():
        print("Waiting for connection...")
        time.sleep(1)
    
    print("WiFi connected")
    print("IP:", wlan.ifconfig()[0])

# Main function
def main():
    # Load MQTT credentials
    load_credentials()
    print(WIFI_SSID)
    
    # Connect to WiFi
    connect_wifi()
    
# Run the main function
if __name__ == "__main__":
    main()
