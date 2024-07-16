# Hardware setup
Choose an ESP-32 for the task, loaded Micropython Firmware to it's flash for running code in python.  
# Software Setup
Created on MQTT Broker that would handle MQTT requests from both the ends, publisher and subscriber.  
Tested a sample print statement code in micropython on ESP32 board.  
Added credentials to wifi and mqtt broker in a JSON file named "creds.json".  
Wrote micropython code to read the JSON, parse it and connect to the WiFi with credentials.  