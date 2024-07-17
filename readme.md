# Hardware setup
Choose an ESP-32 for the task, loaded Micropython Firmware to it's flash for running code in python.  
# Software Setup
Created on MQTT Broker that would handle MQTT requests from both the ends, publisher and subscriber.  
Tested a sample print statement code in micropython on ESP32 board.  
Added credentials to wifi and mqtt broker in a JSON file named "creds.json".  
Wrote micropython code to read the JSON, parse it and connect to the WiFi with credentials.  
Added micropython code to connect to MQTT server
Added python code for subscriber to connect to MQTT server and listen for the received temp data from publisher, parse it and save it locally in sensor_data.txt as required in the assignment. It can also raise alarm if the temprature data received is greater than the specified threshhold for a specified time threshhold. These values can be updated through the "data.json" in /subscriber folder. 
Added python code for server that would read the "sensor_data.txt" and return the last recived data and it's timestamp in a JSON fromat on get request on "0.0.0.0:5000"