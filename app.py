from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Mock function to simulate scanning Wi-Fi networks
def scan_wifi_networks():
    # This should be replaced with actual scanning logic from the ESP32
    return [
        {'ssid': 'Network_1', 'strength': -50},
        {'ssid': 'Network_2', 'strength': -70},
        {'ssid': 'Network_3', 'strength': -60}
    ]

@app.route('/')
def index():
    networks = scan_wifi_networks()
    return render_template('index.html', networks=networks)

@app.route('/connect', methods=['POST'])
def connect():
    ssid = request.form['ssid']
    password = request.form['password']
    # Here, you would typically send this data to the ESP32
    print(f"Received SSID: {ssid}, Password: {password}")
    return "Credentials received!", 200

@app.route('/scan')
def scan():
    networks = scan_wifi_networks()
    return jsonify(networks)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
