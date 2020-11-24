import smbus2
import bme280
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'ec2-18-156-208-13.eu-central-1.compute.amazonaws.com'
ACCESS_TOKEN = 'zbwdc6FbMo4hsCblUvXP'

INTERVAL = 2

sensor_data = {'temperature': 0, 'humidity': 0, 'pressure': 0}

client = mqtt.Client()
# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

# port = 1
# address = 0x76
# bus = smbus2.SMBus(port)

while True:
    # calibration_params = bme280.load_calibration_params(bus, address)
    # data = bme280.sample(bus, address, calibration_params)
    # temperature = data.temperature
    # print (temperature)
    # pressure = data.pressure
    # humidity = data.humidity
    # Sending humidity and temperature data to ThingsBoard
    sensor_data['temperature'] = temperature
    sensor_data['pressure'] = pressure
    sensor_data['humidity'] = humidity
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

client.loop_stop()
client.disconnect()

