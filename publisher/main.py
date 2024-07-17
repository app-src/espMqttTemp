import network
import time
import json
import ubinascii
from machine import Pin
from umqtt.robust import MQTTClient
import dht

# Initialize the DHT22 sensor
sensor = dht.DHT22(Pin(15))

# WiFi settings
WIFI_SSID = ""
WIFI_PASSWORD = ""

# MQTT settings
mqtt_broker = ""
mqtt_port = 0
mqtt_username = ""
mqtt_password = ""
client_id = ""
topic = ""

# Other declerations
DATA_FREQUENCY_IN_SECONDS = 60

# Load MQTT credentials from JSON file
def load_credentials():
    global mqtt_broker, mqtt_port, mqtt_username, mqtt_password, WIFI_SSID,WIFI_PASSWORD,client_id,topic
    try:
        with open("creds.json") as f:
            data = json.load(f)
            mqtt_broker = data["broker"]
            mqtt_port = data["port"]
            client_id = data["client_id"]
            mqtt_username = data["username"]
            mqtt_password = data["password"]
            topic = data["topic"]
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

# Callback for MQTT messages
def mqtt_callback(topic, msg):
    print((topic, msg))
    
def read_sensor_data():
    try:
        # Measure the temperature and humidity
        sensor.measure()
        temperature = sensor.temperature()
        return(temperature)
    except OSError as e:
        print('Failed to read sensor.')
        return(0.0)

# Main function
def main():
    # Load MQTT credentials
    load_credentials()
    
    # Connect to WiFi
    connect_wifi()
    
    print(client_id.encode('utf-8'), mqtt_broker.encode('utf-8'), mqtt_port, mqtt_username.encode('utf-8'), mqtt_password.encode('utf-8'))
    
    # Create MQTT client and connect
    client = MQTTClient(client_id.encode('utf-8'), mqtt_broker.encode('utf-8'), port=mqtt_port, user=mqtt_username.encode('utf-8'), password=mqtt_password.encode('utf-8'))
    client.set_callback(mqtt_callback)
    client.connect()
    print("Connected to MQTT broker")
    
    # Subscribe to a topic
    client.subscribe(topic.encode('utf-8'))
    
    # Start time monitoring
    start_time = time.time()
    
    while True:
        current_time = time.time()
        
        # Check if 60 seconds (1 minute) have passed
        if current_time - start_time >= DATA_FREQUENCY_IN_SECONDS:
            # Publish sensor data
            temperature = read_sensor_data()
            client.publish(topic.encode('utf-8'),str(temperature))
            
            # Reset start time
            start_time = current_time
            
        time.sleep(5)
    

# Run the main function
if __name__ == "__main__":
    main()


