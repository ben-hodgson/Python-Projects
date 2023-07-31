from pms_a003 import Sensor
import paho.mqtt.client as mqtt
from datetime import datetime
from time import sleep
from smbus import SMBus
import json
from bme280 import BME280


mqtt_broker = '192.168.0.2'
mqtt_port  = 1883
air_mon = Sensor()
air_mon.connect_hat(port="/dev/ttyS0", baudrate=9600)
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

def on_connect(client, userdata, flags,rc):
    print(f"Connected with result {rc}")
    client.subscribe("weather/#")
    
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    

client = mqtt.Client("Little Room")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_broker, mqtt_port)

# Get data and disgard to avoid garbage first reading
values = air_mon.read()
temperature = bme280.get_temperature()
pressure = bme280.get_pressure()
humidity = bme280.get_humidity()
pms1 = values.pm10_cf1
pms25 = values.pm25_cf1
pms10 = values.pm100_cf1
sleep(1)

while True:
    values = air_mon.read()
    now = datetime.now()
    date_string = now.strftime("%m/%d/%Y, %H:%M:%S")
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    pms1 = values.pm10_cf1
    pms25 = values.pm25_cf1
    pms10 = values.pm100_cf1
  
    # Dictionary with sensor data
    data = {
        "temperature" : temperature,
        "humidity" : humidity,
        "pressure" : pressure,
        "pms1" : pms1,
        "pms25" : pms25,
        "pms10" : pms10,
    }
    
    # Convert disctionary to JSON
    json_data = json.dumps(data)
    
    # Publish JSON data to topic 'weather'
    client.publish("weather", json_data)
    
    #print output
    print("Published: Time :" + date_string + " Data: " + json_data)
    print()
    
    #wait for period before next message
    sleep(60)

air_mon.disconnect_hat()
