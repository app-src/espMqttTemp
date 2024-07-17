# Hardware setup
* Chose an ESP-32 for the task, loaded Micropython Firmware to it's flash for running code in python.  
* Used DHT22 for temprature data and conneted it on pin 15 of ESP32 and attach after program uploading.
# Software Setup
* Created on MQTT Broker that would handle MQTT requests from both the ends, publisher and subscriber.  
* Tested a sample print statement code in micropython on ESP32 board.  
* Added credentials to wifi and mqtt broker in a JSON file named "creds.json".  
* Wrote micropython code to read the JSON, parse it and connect to the WiFi with credentials.  
* Added micropython code to connect to MQTT server
* Added python code for subscriber to connect to MQTT server and listen for the received temp data from publisher, parse it and save it locally in sensor_data.txt as required in the assignment. It can also raise alarm if the temprature data received is greater than the specified threshhold for a specified time threshhold. These values can be updated through the "data.json" in /subscriber folder. 
* Added python code for server that would read the "sensor_data.txt" and return the last recived data and it's timestamp in a JSON fromat on get request on "0.0.0.0:5000".
# Project Structure
```bash
│   readme.md
│   requirements.txt
│   sensor_data.txt
│   server.py
│
├───publisher
│       creds.json
│       main.py
│
└───subscriber
        data.json
        main.py
```
# How to run
## Server
- In the root directory run the server.py file to activate Flask based server it would start and you can go to the link flashed in the terminal to check the data.
## Subscriber 
- In the subscriber directory in root run "main.py" to activate the subscriber it would connect to MQTT server and listen to any updated sent by the publisher.
- If the recived data is consistently above the threshold value for the minimum required perid that is 5 times(5 minutes)  the Alarm would be raised.
- Subscriber also saved the data to a text file in the root directory "sensor_data.text".
## Publisher
- Here we have to upload code to the ESP32, for that we need tools like thonny.
- First flash the firmware to ESP32 using thonny.
- After flashing open the file contents and transfer the two files (creds.json and main.py) in the flash of the ESP23 from the publisher directory.
- Just edit the Wifi credentials in the creds.json so ESP32 can connect to MQTT server and save to flash.
- Run the "main.py" by either clicking run button or reseting the ESP32.


# So here's how I completed my assignment
# Please feel free to contact me for any further discussion or issue related to code.
## Ashish 
## 8368242921
## ashish.adgitm@gmail.com
