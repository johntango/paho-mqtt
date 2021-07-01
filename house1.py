import paho.mqtt.client as mqtt
import time
import json
# This is the Publisher to Mosquitto on topic

client = mqtt.Client()
broker = "192.168.1.42"
port = 1883
topic = "v1/devices/me/telemetry"
accessToken = "6ewdYyKrcOaMvq0CjXhr"
client.username_pw_set(accessToken)
client.connect(broker, port, 60)
client.loop_start()
data = {'temperature': 0}
for i in range(10):
    data['temperature'] = i
    dataf = json.dumps(data)
    print(data)
    client.publish(topic, dataf, 1)
    time.sleep(1)
client.loop_stop()
client.disconnect()
print('End of Publish')
