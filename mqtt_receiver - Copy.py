import random

from paho.mqtt import client as mqtt_client


broker = 'public.cloud.shiftr.io'
port = 443

broker = 'public.cloud.shiftr.io'
port = 1883
topic = "notes/test"

#broker = 'broker.emqx.io'
#port = 1883
#topic = "python/mqtt"


# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'public'
password = 'public'


def connect_mqtt() -> mqtt_client:
    print("connect_mqtt() -> mqtt_client:")
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    print("subscribe(client: mqtt_client):")

    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        print(len(msg.payload.decode()))

    client.subscribe(topic)
    client.on_message = on_message

import time
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()



if __name__ == '__main__':
    run()

