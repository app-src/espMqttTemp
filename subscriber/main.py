import time
import paho.mqtt.client as mqtt
import json

# Load MQTT settings from JSON file
with open("subscriber\data.json", "r") as file:
    data = json.load(file)
    MQTT_BROKER = data.get("MQTT_BROKER")
    MQTT_PORT = data.get("MQTT_PORT")
    MQTT_TOPIC = data.get("MQTT_TOPIC")
    TEMPERATURE_THRESHOLD = data.get("TEMPERATURE_THRESHOLD")
    THRESHOLD_DURATION = data.get("THRESHOLD_DURATION")
    CLIENT_ID = data.get("CLIENT_ID")

# Variables to track threshold crossing
threshold_counter = 0

# Callback when a message is received
def on_message(client, userdata, msg):
    global threshold_counter
    print(f"Received message: {msg.topic} - {msg.payload}")

    try: 
        temperature = float(msg.payload.decode())
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        # Save data locally with timestamp
        with open("sensor_data.txt", "a") as f:
            f.write(f"{timestamp} - Temperature: {temperature:.2f}\n")

        # Check if temperature exceeds threshold
        if temperature > TEMPERATURE_THRESHOLD:
            threshold_counter += 1
            if threshold_counter >= THRESHOLD_DURATION:
                print("Temperature threshold exceeded for 5 consecutive minutes! Alarm raised.")
                threshold_counter = 0  # Reset counter after alarm
        else:
            threshold_counter = 0  # Reset counter if threshold not exceeded

    except:
        print("Invalid temperature value received.")

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

# Initialize the MQTT client
client = mqtt.Client(client_id=CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

if __name__ == "__main__":
    client.loop_forever()

