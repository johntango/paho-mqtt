import time
import paho.mqtt.client as mqtt


def on_message(client, userdata, message):
    print(f"message received: {message.payload.decode()}")
    print(f"message topic: {message.topic}")


port = 1883
broker = "localhost"
topic = "sensors/johntopic2"

client = mqtt.Client("A1")
client.on_message = on_message

print('Connect to broker')
client.connect(broker, port)
client.loop_start()
client.subscribe(topic)
print(f'subscribed to {topic}')
client.publish(topic, 'ON')
time.sleep(25)
client.loop_stop()
