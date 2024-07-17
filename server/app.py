from flask import Flask, jsonify
import subscriber.main as mqtt_subscriber

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_sensor_data():
    try:
        with open("sensor_data.txt", "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                return jsonify({"last_data_point": last_line.strip()}), 200
            else:
                return jsonify({"error": "No data available"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    mqtt_subscriber.main()

