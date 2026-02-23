from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

PI_URL = "http://192.168.1.42:5000/sensor"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/sensor")
def sensor_proxy():
    try:
        r = requests.get(PI_URL)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
