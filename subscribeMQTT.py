#!/usr/bin/env python3
#  Check first - It seems a bit flaky
import paho.mqtt.client as mqtt
import time

# This is the Subscriber to Mosquitto Server
port = 1883
broker = 'localhost'
topic = "sensors/johntopic2"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned rc code=", rc)
        client.connected_flag = True
    else:
        print("Bad connection Returned code=", rc)


def on_message(client, userdata, msg):
    print(f"Got MQTT: {msg.payload.decode()}")


def on_subscribe(client, userdata, msg):
    print("On_Subscribe Success")


def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")
    if rc != 0:
        print('Unexpected MQTT disconnection. Will auto-reconnect')
        client.connected_flag = False
    else:
        print('rc value:' + str(rc))
    try:
        print("Trying to Reconnect")
        client.connect(broker, port)
        client.subscribe(topic, qos=0)
    except:
        print("Error in Retrying to Connect with Broker")


def wait_for(client, msgType, period=0.25):
    if msgType == "SUBACK":
        if client.on_subscribe:
            while not client.suback_flag:
                logging.info("waiting suback")
                client.loop()  # check for messages
                time.sleep(period)


mqtt.Client.connected_flag = False
topic_ack = []
client = mqtt.Client()
client.on_connect = on_connect   # callback function
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe


client.loop_start()
client.connect("localhost", port, 60)
while not client.connected_flag:
    print("in wait loop")
    time.sleep(1)
print("in MAIN loop")
try:
    r = client.subscribe(topic, qos=0)
    if r[0] == 0:
        topic_ack.append(r[1])
        print(f"QoS: {r[1]}")
    else:
        print('Stop Client Loop')
        client.loop_stop()
except Exception as e:
    print("Exception")
    client.disconnect()
    client.loop_stop()
    sys.exit(1)
client.loop_forever()
print('End')
