import paho.mqtt.client as mqtt
import random
import json
import time

# This is the Publisher to Mosquitto on topic
topic = 'sensors/johntopic2'
broker = "localhost"
port = 1883
client = mqtt.Client()
client.connect(broker, port, 60)
print(f"connectd on: {port}")
client.loop_start()
data = {'temperature': 0}
for i in range(10):
    data['temperature'] = random.randint(0, 100)
    dataf = json.dumps(data)
    print(data)
    client.publish(topic, dataf, qos=1)
    time.sleep(1)
client.loop_stop()
client.disconnect()
