import paho.mqtt.client as mqtt
import json
import time
import random

# This is the Publisher to Mosquitto on topic
topic = 'sensors/johntopic2'
broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port, 60)
print(f"connected on {port}")
for i in range(100):
    data = json.dumps({"temperature": random.randint(0, 100)})
    client.publish(topic, data)
    print(f"published: {data}")
    time.sleep(1)
client.disconnect()
