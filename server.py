from flask import Flask
import json, os
import subscriber as mqtt_subscriber

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_sensor_data():
    try:
        path = os.getcwd()
        with open(path+"\\sensor_data.txt", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                return json.dumps(json.loads(last_line.strip())), 200
            else:
                return json.dumps({"error": "No data available"}), 404
    except Exception as e:
        return json.dumps({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    mqtt_subscriber.main()

